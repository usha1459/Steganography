from cryptography.fernet import Fernet
from PIL import Image
import streamlit as st
import base64
import io
import zipfile

# Function to generate a key and write it to a file
def write_key():
    key = Fernet.generate_key()
    return key

# Function to encrypt the contents of a text file
def encrypt_message(message: str, key: bytes) -> bytes:
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# Function to convert text to bits
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

# Function to encode the encrypted message into an image
def encode_image(image, message):
    img = Image.open(image)
    pixels = img.load()
    
    bits = text_to_bits(message)
    bits += '1111111111111110'  # End of message delimiter
    
    width, height = img.size
    if len(bits) > width * height * 3:
        raise ValueError("The message is too large to hide in this image.")
    
    bit_idx = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if bit_idx < len(bits):
                r = (r & 0xFE) | int(bits[bit_idx])
                bit_idx += 1
            if bit_idx < len(bits):
                g = (g & 0xFE) | int(bits[bit_idx])
                bit_idx += 1
            if bit_idx < len(bits):
                b = (b & 0xFE) | int(bits[bit_idx])
                bit_idx += 1
            pixels[x, y] = (r, g, b)
    
    return img

# Streamlit UI for encryption and encoding
def app():
    st.title("Encrypt and Encode Text into Image")
    
    # Input text box for secret message
    message = st.text_area("Enter the message you want to hide:")
    
    # File uploader for the image
    image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
    if image is not None:
        st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button("Encrypt and Encode"):
        if message and image:
            key = write_key()
            encrypted_message = encrypt_message(message, key)
            encoded_image = encode_image(image, encrypted_message.decode())
            
            # Prepare key file in memory
            key_file = io.BytesIO()
            key_file.write(key)
            key_file.seek(0)
            
            # Prepare encrypted message file in memory
            encrypted_message_file = io.BytesIO()
            encrypted_message_file.write(encrypted_message)
            encrypted_message_file.seek(0)
            
            # Prepare encoded image file in memory
            encoded_image_file = io.BytesIO()
            encoded_image.save(encoded_image_file, format='PNG')
            encoded_image_file.seek(0)
            
            # Create a ZIP file containing the key, encrypted message, and encoded image
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                zip_file.writestr("key.key", key_file.getvalue())
                zip_file.writestr("encrypted_message.txt", encrypted_message_file.getvalue())
                zip_file.writestr("encoded_image.png", encoded_image_file.getvalue())
            zip_buffer.seek(0)
            
            st.success("Message encoded into image successfully!")
            st.download_button(label="Download Encoded Image, Key, and Encrypted Message", data=zip_buffer, file_name="encoded_image_and_key.zip", mime="application/zip")
        else:
            st.error("Please provide both a message and an image.")

if __name__ == "__main__":
    app()
