import os
from langchain.document_loaders import UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def build_vector_index(doc_path, save_dir):
    print("🔄 Memuat dokumen...")
    loader = UnstructuredWordDocumentLoader(doc_path)
    documents = loader.load()

    print("🔗 Membagi dokumen jadi chunk...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=700)
    chunks = splitter.split_documents(documents)

    print("📌 Membuat embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("📦 Membuat FAISS vectorstore...")
    vectorstore = FAISS.from_documents(chunks, embedding=embeddings)

    print(f"💾 Menyimpan index ke '{save_dir}' ...")
    vectorstore.save_local(save_dir)

    print("✅ Index selesai dibuat dan disimpan.")

if __name__ == "__main__":
    DOC_PATH = "D:\magang telkom 2\Streamlit\controller\chat\data product telkomsel new.docx"
    SAVE_DIR = "vector_index/chatllm"
    
    os.makedirs(SAVE_DIR, exist_ok=True)
    build_vector_index(DOC_PATH, SAVE_DIR)
