from prompts import BASE_INSTRUCTIONS, SIMPLE_PROMPT, DETAILED_PROMPT, EXAM_PROMPT
from langchain_ollama import ChatOllama
from file_loader import load_file
from note_engine import save_note
import streamlit as st
import base64

llm = ChatOllama(model="llama3.1:8b", temperature=0)

st.title("🧠✨AI Note-Summarizer")

file_name = st.text_input("Enter a file name: ")

answer_style = st.selectbox("Choose the answer style: ", ["simple", "detailed", "exam"])

if answer_style == "simple":
    prompt = SIMPLE_PROMPT
elif answer_style == "detailed":
    prompt = DETAILED_PROMPT
elif answer_style == "exam":
    prompt = EXAM_PROMPT

if st.button("Summarize"):
    chunks = load_file(f"./data/{file_name}")
    if chunks is None:
        st.error("Could not load file. Please check the file path and type, then try again.")
        exit(1)
        
    text = "\n".join([chunk.page_content for chunk in chunks])
    formated_prompt = prompt.format(text=text)

    messages = [
        {
            "role": "system",
            "content": BASE_INSTRUCTIONS
        },
        {
            "role": "user",
            "content": formated_prompt
        }
    ]
    response = llm.invoke(messages)
    
    st.write(response.content)

    save_choice = st.selectbox("Do you want to save this note? (yes/no): ", ["yes", "no"])
    if save_choice == "yes":
        save_note(response.content)
        st.write("\nNote saved successfully!")
        st.write("\nNote saved in 'notes.txt' file which is in 'data' folder.")
    else:
        st.write("\nNote not saved.")