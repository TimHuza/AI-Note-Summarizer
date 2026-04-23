from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_file(file_path):
    """
    Load a text file and split it into chunks.
    """

    loader = TextLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chuunk_size=1000,
        chunk_overlap=200,
    )

    chunks = text_splitter.split_text(docs)

    return chunks