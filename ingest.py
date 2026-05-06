import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DOCS_FOLDER = "./docs"

def ingest():
    if not os.path.exists(DOCS_FOLDER):
        os.makedirs(DOCS_FOLDER)
        print(f"'{DOCS_FOLDER}' folder bana diya.")
        print("Isme apni .py / .txt / .md files daalo, phir dobara run karo.")
        return

    files = os.listdir(DOCS_FOLDER)
    if not files:
        print(f"'{DOCS_FOLDER}' folder khali hai! Kuch files daalo pehle.")
        return

    print(f"Loading files from '{DOCS_FOLDER}'...")
    loader = DirectoryLoader(
        DOCS_FOLDER,
        glob="**/*.*",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        silent_errors=True,
    )
    docs = loader.load()

    if not docs:
        print("Koi file load nahi hui.")
        return

    print(f"{len(docs)} files mili.")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    print(f"{len(chunks)} chunks bane.")

    print("Embeddings bana raha hoon...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")
    print("✅ Knowledge base ready! Ab app.py chalao.")

if __name__ == "__main__":
    ingest()