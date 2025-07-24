from PIL import Image
from cryptography.fernet import Fernet
import streamlit as st

def bits_to_text(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def decode_image(image):
    img = Image.open(image)
    pixels = img.load()
    
    bits = ""
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            bits += str(r & 1)
            bits += str(g & 1)
            bits += str(b & 1)
    
    delimiter = '1111111111111110'
    if delimiter not in bits:
        raise ValueError("End of message delimiter not found in the image.")
    
    bits = bits.split(delimiter)[0]
    
    try:
        return bits_to_text(bits)
    except UnicodeDecodeError:
        raise ValueError("Failed to decode the hidden message. The message may be corrupted or improperly encoded.")

def decrypt_message(encrypted_message: str, key: bytes) -> str:
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message.encode()).decode()
    return decrypted_message

# Streamlit UI for decoding and decryption
def app():
    st.title("Decode and Decrypt Message from Image")
    
    # File uploader for the encoded image
    image = st.file_uploader("Choose an encoded image...", type=["png", "jpg", "jpeg"])
    
    # File uploader for the key file
    key_file = st.file_uploader("Choose the key file...", type=["key"])
    
    if st.button("Decode and Decrypt"):
        if image and key_file:
            # Decode the encrypted message from the image
            encrypted_message = decode_image(image)
            
            # Read the key
            key = key_file.read()
            
            # Decrypt the message
            decrypted_message = decrypt_message(encrypted_message, key)
            
            # Provide download link for the decrypted message
            st.success("Message decoded and decrypted successfully!")
            
            st.download_button(label="Download Decrypted Message", data=decrypted_message, file_name="decrypted_message.txt", mime="text/plain")
        else:
            st.error("Please provide both an encoded image and a key file.")

if __name__ == "__main__":
    app()
