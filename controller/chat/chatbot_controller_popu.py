from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import streamlit as st

@st.cache_resource
def get_chatbot(chat_type="eco"):
    # Konfigurasi per chatbot
    config = {
        "eco": {
            "api_key": "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",
            "index_path": "controller/chat/vector_index_eco/eco_index"
        },
        "popu": {
            "api_key": "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",
            "index_path": "controller/chat/vector_index_popu/popu_index"
        }
    }

    if chat_type not in config:
        raise ValueError(f"Unknown chatbot type: {chat_type}")

    # Load konfigurasi
    api_key = config[chat_type]["api_key"]
    index_path = config[chat_type]["index_path"]

    # Embedding dan FAISS vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

    # Load LLM
    llm = ChatOpenAI(
        model_name="google/gemini-2.0-flash-exp:free",
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=api_key
    )

    # Prompt template
    prompt_template = """Anda adalah asisten digital Telkomsel...
Jawablah pertanyaan pengguna *hanya* berdasarkan informasi berikut:

{context}

Pertanyaan: {question}
Jawaban akurat dan lengkap berdasarkan data di atas:"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template,
    )

    # QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 50}),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

    return qa_chain

def get_chatbot_response_popu(qa, query):
    return qa(query)

