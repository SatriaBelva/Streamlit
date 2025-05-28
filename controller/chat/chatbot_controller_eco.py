# import os
# from langchain.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# import streamlit as st

# #blabla
# @st.cache_resource
# def load_chatbot_eco():
#     os.environ["OPENAI_API_KEY"] = "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"

#     embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#     vectorstore = FAISS.load_local(r"controller/chat/vector_index_eco/eco_index",embeddings,allow_dangerous_deserialization=True)


#     llm = ChatOpenAI(
#         model_name="meta-llama/llama-4-scout:free",
#         openai_api_base="https://openrouter.ai/api/v1"
#     )

#     prompt_template = """Anda adalah asisten digital Telkomsel...
# Jawablah pertanyaan pengguna *hanya* berdasarkan informasi berikut:

# {context}   

# Pertanyaan: {question}
# Jawaban akurat dan lengkap berdasarkan data di atas:"""

#     prompt = PromptTemplate(
#         input_variables=["context", "question"],
#         template=prompt_template,
#     )

#     qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=vectorstore.as_retriever(search_kwargs={"k": 50}),
#         chain_type="stuff",
#         chain_type_kwargs={"prompt": prompt},
#         return_source_documents=True
#     )

#     return qa_chain

# def get_chatbot_response_eco(qa, query):
#     return qa(query)


import os
import requests
import streamlit as st

def get_chatbot_response_eco(query):
    try:
        response = requests.post("https://bagusilman-fastapibotrlo.hf.space/chat/eco", json={"question": query})

        # Log respons mentah
        print("Status:", response.status_code)
        print("Response:", response.text)

        # Pastikan response adalah JSON valid
        return response.json().get("result", "Tidak ada hasil dari server.")
    except requests.exceptions.RequestException as e:
        return f"⚠️ Gagal terhubung ke server: {e}"
    except ValueError as e:
        return f"⚠️ Response bukan JSON valid: {e}"