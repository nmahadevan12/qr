import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.title("QR Code Generator")

url = st.text_input("Enter a URL to generate QR Code:")

if st.button("Generate QR Code"):
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill="black", back_color="white")
        
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.image(byte_im)
        
        st.download_button("Download QR Code", byte_im, "qrcode.png", "image/png")
    else:
        st.warning("Please enter a valid URL.")
