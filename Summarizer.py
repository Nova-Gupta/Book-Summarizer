import streamlit as st
import google.generativeai as genai
import PyPDF2

# Set your API key
api_Key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_Key)

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
st.markdown("""
    <style>
        .top-left-text {
            position: fixed;
            top: 60px;
            left: 10px;
            color: white;
            font-size: 16px;
            font-weight: bold;
            z-index: 9999;
        }
    </style>
    <div class="top-left-text">
        👋 Nova - 12326332<br>
        Ankureet - 12327118
    </div>
""", unsafe_allow_html=True)
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
