# Steganography App

This Streamlit-based application allows you to securely hide and retrieve messages within images using steganography and encryption techniques. The app has two main functionalities:

1. **Encrypt and Encode**: Encrypts a message and encodes it into an image. It outputs an encoded image and a key.
2. **Decode and Decrypt**: Decodes an encrypted message from an image and decrypts it.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Encrypt and Encode](#encrypt-and-encode)
  - [Decode and Decrypt](#decode-and-decrypt)
- [Concepts](#concepts)
  - [Encoding](#encoding)
  - [Encryption](#encryption)
  - [Key](#key)
  - [LSB](#lsb)
  - [Decoding](#decoding)
  - [Decryption](#decryption)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/steganography-app.git
    cd steganography-app
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```
# Installation
## Encoding
Encoding is the process of converting data into a specific format. In this application, encoding refers to hiding an encrypted message within an image using the Least Significant Bit (LSB) method.

## Encryption
Encryption is the process of converting plaintext into ciphertext using an algorithm and a key. This ensures that the message can only be read by someone who has the corresponding decryption key. The app uses the Fernet encryption from the cryptography library.

## Key
A key is a piece of information used in encryption and decryption processes. In this app, a key is generated for encryption and must be used for the decryption process. Without the correct key, the encrypted message cannot be decrypted.

## LSB
LSB stands for Least Significant Bit. In image steganography, the LSB method involves altering the least significant bits of the image pixels to encode the message. This slight modification is generally imperceptible to the human eye.

## Decoding
Decoding is the process of extracting the hidden message from the encoded image. This involves reversing the encoding process to retrieve the encoded message.

## Decryption
Decryption is the process of converting the encrypted message (ciphertext) back into its original form (plaintext) using the correct decryption key. This ensures that only authorized parties can read the message.
