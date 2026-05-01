from prompts import BASE_INSTRUCTIONS, SIMPLE_PROMPT, DETAILED_PROMPT, EXAM_PROMPT
from langchain_ollama import ChatOllama
from file_loader import load_file
from note_engine import save_note

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
    temperature=0
)

file_path = input("Enter the path to the file you want to summarize: ").strip()
chunks = load_file(f"./data/{file_path}")

if chunks is None:
    print("Could not load file. Please check the file path and type, then try again.")
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

print(response.content)

save_choice = input("Do you want to save this note? (yes/no): ").lower()

if save_choice == "yes":
    save_note(response.content)
    print("\nNote saved successfully!")
    print("\nNote saved in 'notes.txt' file which is in 'data' folder.")
elif save_choice == "no":
    print("\nNote not saved.")
else:
    print("\nInvalid input. Note not saved.")