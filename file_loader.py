from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_file(file_path: str):
    """
    Load a text, markdown or pdf file and split it into chunks.
    """

    file_type_support = [".txt", ".md", ".pdf"]

    if file_path not in file_type_support:
        print("File type not supported")
        return None
    # 1. Choose the right loader based on the file extension
    if file_path.endswith(".txt"):
        loader = TextLoader(file_path)
        docs = loader.load()
    elif file_path.endswith(".md"):
        loader = TextLoader(file_path)
        docs = loader.load()
    elif file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        docs = loader.load()
    else:
        print("File type not supported")
        return None


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    # 3. Split the document into chunks
    chunks = text_splitter.split_documents(docs)
    
    return chunks