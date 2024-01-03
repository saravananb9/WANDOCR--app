pip install pytesseract
pip install pillow
pip install pandas
pip install streamlit
import streamlit as st
import pytesseract
from PIL import Image
import pandas as pd

# Configure PyTesseract path
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path if needed

# Function to extract text from image using PyTesseract
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

# Streamlit app layout
st.title("Text Extractor using PyTesseract OCR")

uploaded_file = st.file_uploader("Upload an image containing text", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    text = extract_text_from_image(image)

    st.header("Extracted Text:")
    st.write(text)

    # Optional: Display extracted text in a table (if structure allows)
    try:
        table = pd.DataFrame(text.splitlines(), columns=["Text"])  # Assuming simple table structure
        st.header("Extracted Text Dataframe:")
        st.dataframe(table)
    except:
        st.write("Table display not available for this text format.")
