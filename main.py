from langchain.chains.summarize import load_summarize_chain
from prompts import SIMPLE_PROMPT, DETAILED_PROMPT, EXAM_PROMPT
from langchain_core.documents import Document
from langchain_ollama import ChatOllama
from file_loader import load_file

user_answer_style = input("Enter your desired answer style (simple, detailed, exam): ").lower()

if user_answer_style == "simple":
    prompt = SIMPLE_PROMPT
elif user_answer_style == "detailed":
    prompt = DETAILED_PROMPT
elif user_answer_style == "exam":
    prompt = EXAM_PROMPT
else:
    print("Invalid answer style. Defaulting to simple.")
    prompt = SIMPLE_PROMPT

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0,
    system_prompt=prompt
)

text = load_file("./data/notes.txt")
docs = [Document(page_content=text)]

chain = load_summarize_chain(llm, chain_type="map_reduce")
result = chain.run(docs)

print(result["output_text"])
