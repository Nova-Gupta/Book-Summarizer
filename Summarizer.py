import streamlit as st
import google.generativeai as genai
import PyPDF2

# Set your API key
genai.configure(api_key="api key")

# Gemini summary function
def summarize_with_gemini(text):
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    response = model.generate_content(f"Summarize the following text:\n\n{text}")
    return response.text

# Extract text from uploaded PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    extracted_text = ""
    for page in pdf_reader.pages:
        extracted_text += page.extract_text()
    return extracted_text

# Streamlit UI
st.set_page_config(page_title="Book Summarizer Chatbot")
st.title("📚 Book Summarizer Chatbot")

uploaded_file = st.file_uploader("📄 Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    with open("temp_uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.info("⏳ Extracting text from PDF...")
    extracted_text = extract_text_from_pdf("temp_uploaded.pdf")

    st.success("✅ Text extracted! Generating summary...")
    summary = summarize_with_gemini(extracted_text)

    st.subheader("📘 Book Summary")
    st.write(summary)
