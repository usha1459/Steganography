import streamlit as st
from encrypt_and_encode import app as encrypt_app
from decode_and_decrypt import app as decrypt_app

st.set_page_config(page_title="Steganography App", page_icon="🔐", layout="wide")

tabs = st.tabs(["Encrypt and Encode", "Decode and Decrypt"])

with tabs[0]:
    encrypt_app()

with tabs[1]:
    decrypt_app()
