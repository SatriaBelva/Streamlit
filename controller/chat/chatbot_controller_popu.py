import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import streamlit as st

#blabla
@st.cache_resource
def load_chatbot_popu():
    os.environ["OPENAI_API_KEY"] = "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"

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(r"controller/chat/vector_index/popu_index",embeddings,allow_dangerous_deserialization=True)


    llm = ChatOpenAI(
        model_name="google/gemini-2.0-flash-exp:free",
        openai_api_base="https://openrouter.ai/api/v1"
    )

    prompt_template = """Anda adalah asisten digital Telkomsel...
Jawablah pertanyaan pengguna *hanya* berdasarkan informasi berikut:

{context}

Pertanyaan: {question}
Jawaban akurat dan lengkap berdasarkan data di atas:"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template,
    )

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