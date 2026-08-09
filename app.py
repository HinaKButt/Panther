import os
import tempfile

import streamlit as st
from langchain_community.document_lloaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from lanchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from lanchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecuriveCharacterTextSplitter


st.set_page_config(
    page_title="PDF RAG Agent",
    page_icon= "📃",
    layout="wide"
    )

st.title("PDF RAG Agent 📃")

st.caption(
    "Upload a PDF file and ask questions about its content"
)

with st.sidebar:

    st.header("settings")

    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        Value=os.environ.get("OPENAI_API_KEY", "")
    )

    model_name = st.selectbox(
        "Model",
        ["gpt-4o-mini", "gpt-4o"]
        index=0
    )

    chunk_size = st.slider(
        "Chunk Size",
        min_values=100,
        max_value=1000,
        value=500,
        step=50
    )

    chunk_overlap = st.slider(
        "Chunk Overlap",
        min_value=0,
        max_value=chunk_size,
        value=50,
        step=10
    )

    top_k = st.slider(
        "Retrieved Chunks (k)",
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )

    if not api_key:
        st.info("please enter your OpenAI API kay in the sidebar to continue.")
        st.stop()

        os.environ["OPENAI_API_KEY"] = api_key

        uploaded_pdf = st.file_uploader(
            "Upload a PDF file",
            type="pdf"
        )

        def build_vectorstore(pdf_fle: bytes, chunk_size: int, chunk_overlap: int) -> FAISS:
            with tempfile.NamedTemporaryFile(delete=False, suffix=" .pdf") as temp_pdf:
                temp_pdf .write(pdf_file.read())
                temp_pdf_path = temp_pdf.Name

                




                
