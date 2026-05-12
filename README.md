# 📝 AI Note Summarizer Documentation

> An intelligent, offline-first **web UI tool** that reads your notes and produces clean, structured summaries — powered by **LangChain**, **Ollama** (Llama 3.1), and **Streamlit**.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Placing Your Files](#placing-your-files)
- [Summary Styles](#summary-styles)
- [Supported File Types](#supported-file-types)
- [Saving Your Summary](#saving-your-summary)
- [Module Breakdown](#module-breakdown)
- [Example Walkthrough](#example-walkthrough)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)

---

## Overview

**AI Note Summarizer** is a **Streamlit web application** that takes your text notes — whether they're plain `.txt` files, Markdown `.md` documents, or PDF files — and uses a locally running large language model (LLM) to produce a concise, readable summary.

Because it runs entirely **on your own machine** using Ollama, no data is ever sent to an external server. Your notes stay private.

The tool was built using:

| Library | Purpose |
|---|---|
| [`LangChain`](https://python.langchain.com/) | Orchestrating the LLM pipeline and prompt management |
| [`langchain-ollama`](https://pypi.org/project/langchain-ollama/) | Connecting LangChain to a locally running Ollama model |
| [`langchain-community`](https://pypi.org/project/langchain-community/) | Document loaders for `.txt`, `.md`, and `.pdf` files |
| [`langchain-text-splitters`](https://pypi.org/project/langchain-text-splitters/) | Splitting large documents into manageable chunks |
| [`Ollama`](https://ollama.com/) | Running the Llama 3.1 8B model locally on your machine |
| [`Streamlit`](https://streamlit.io/) | Powering the interactive web UI |

---

## Features

- 🔒 **100% offline** — your notes never leave your computer
- 🖥️ **Streamlit web UI** — no terminal commands needed after launch
- 📄 Supports `.txt`, `.md`, and `.pdf` file formats
- 🎯 Three distinct **summary styles**: Simple, Detailed, and Exam-focused
- 💾 Option to **save** the generated summary to a `notes.txt` file
- 🧩 Clean modular architecture — easy to extend and modify
- ⚡ Handles large files via intelligent **text chunking**

---

## Project Structure

```
AI-Note-Summarizer/
│
├── data/                   # ← Place your input files HERE
│   └── notes.txt           # Auto-created when you save a summary
│
├── ui.py                   # Entry point — launches the Streamlit web UI
├── file_loader.py          # Loads and chunks the input document
├── note_engine.py          # Handles saving summaries to disk
├── prompts.py              # Defines the 3 summarization prompt templates
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## Prerequisites

**Before running** the project, make sure you have the following installed on your machine:

### 1. Python 3.10+

Download from [python.org](https://www.python.org/downloads/).

Verify installation:
```bash
python --version
```

### 2. Ollama

Ollama is the local model runner. Download it from [ollama.com](https://ollama.com/).

After installing, pull the required model:
```bash
ollama pull llama3.1:8b
```

> **Note:** The `llama3.1:8b` model is approximately 4.7 GB. Make sure you have enough disk space and a stable internet connection for the initial download. After that, it runs fully offline.

Verify Ollama is running:
```bash
ollama list
```

You should see `llama3.1:8b` in the list.

---

## Installation

### Step 1 — Clone the repository

```bash
git clone https://github.com/TimHuza/AI-Note-Summarizer.git
cd AI-Note-Summarizer
```

### Step 2 — Create a virtual environment

It is strongly recommended to use a virtual environment to avoid dependency conflicts.

```bash
# Create the virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS / Linux)
source venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages:

```
langchain
langchain-community
langchain-core
langchain-ollama
langchain-text-splitters
streamlit
```

---

## How to Run

Once your environment is set up and Ollama is running, launch the web UI with:

```bash
streamlit run ui.py
```

Streamlit will open the app automatically in your default browser (usually at `http://localhost:8501`). The interface guides you through three simple steps:

### Step 1 — Enter the filename

Type **only the filename** (e.g., `cucumbers.txt`) into the text input field. The app automatically looks inside the `data/` folder — do not include the folder prefix.

### Step 2 — Choose a summary style

Use the **dropdown selector** to pick one of:
- `simple` — quick bullet-point overview
- `detailed` — comprehensive full-sentence bullets
- `exam` — dense, fact-focused study bullets

### Step 3 — Summarize and optionally save

Click the **"Summarize"** button. The summary will appear on the page. You'll then see a dropdown asking:

> Do you want to save this note? (yes/no)

Select `yes` to append the summary to `data/notes.txt`, or `no` to continue without saving.

---

## Placing Your Files

> ⚠️ **Important:** All files you want to summarize **must be placed in the `data/` folder** before running the program.

For example, if you have a file called `history_notes.txt`, move it here:

```
AI-Note-Summarizer/
└── data/
    └── cucumbers.txt   ← place it here
```

Then, when the program asks for the filename, simply type:

```
cucumbers.txt
```

Do **not** include the `data/` prefix — the application adds that automatically.

> 💾 **Don't delete `data/notes.txt`!** If you delete it, the app will recreate an empty file — but all your previously saved summaries will be permanently lost. Keep it around as your personal summary history.

---

## Summary Styles

The tool offers three prompt modes, each tailored to a different use case:

### 🟢 `simple`
Best for a quick overview. Produces **3–5 short bullet points** using easy-to-understand language. Ideal when you just need the key takeaways fast.

**Example output:**
```
- Cucumbers are botanically a fruit with ~95% water content.
- They thrive in warm climates and need consistent moisture.
- Harvesting typically occurs 50–70 days after planting.
```

---

### 🔵 `detailed`
Best for thorough understanding. Produces **comprehensive bullet points** with full sentences and important context included. Ideal for study sessions or deep review.

**Example output:**
```
- Cucumbers (Cucumis sativus) are members of the gourd family and are
  classified as fruits because they develop from flowers and contain seeds.
- They have a water content of approximately 95%, making them a key
  ingredient for hydration in global cuisines.
- They require warm climates, consistent moisture, and proper spacing to
  prevent fungal diseases, and are harvested 50–70 days after planting.
```

---

### 🟣 `exam`
Best for exam preparation. Extracts **key facts, definitions, and concepts** in a dense, information-rich format. Each bullet is short and easy to memorize.

**Example output:**
```
- Cucumbers: botanically a fruit (Cucumis sativus), member of gourd family
- Water content: ~95%
- Growing: warm climate, annual plant, consistent moisture needed
- Harvest window: 50–70 days after planting
```

---

## Supported File Types

| Extension | Description |
|---|---|
| `.txt` | Plain text files |
| `.md` | Markdown documents |
| `.pdf` | PDF files (text-based, not scanned images) |

> **Note on PDFs:** Only text-based PDFs are supported. Scanned PDFs (image-only) will not extract readable text and may produce empty or poor results.

---

## Saving Your Summary

When you choose to save, the summary is **appended** to `data/notes.txt`. This means:

- If `notes.txt` doesn't exist yet, it will be created automatically.
- Each new summary is added to the **end** of the file, so you never lose a previous summary.
- You can open `data/notes.txt` at any time to review all saved summaries.

---

## Module Breakdown

### `ui.py`
The application's entry point. Renders the Streamlit web interface and orchestrates the entire pipeline:
1. Renders a text input for the filename and a dropdown for summary style selection
2. Loads the model via `ChatOllama`
3. On button click, loads the file via `file_loader` and joins chunks into a single text block
4. Formats the chosen prompt and invokes the LLM
5. Displays the response in the browser and offers a save dropdown

### `file_loader.py`
Handles document ingestion. The `load_file(file_path)` function:
- Detects the file extension (`.txt`, `.md`, `.pdf`)
- Selects the appropriate LangChain loader (`TextLoader` or `PyPDFLoader`)
- Splits the loaded document into overlapping chunks using `RecursiveCharacterTextSplitter` (chunk size: 1000 chars, overlap: 200 chars)
- Returns the list of chunks, or `None` if the file type is unsupported

### `prompts.py`
Defines the AI's behavior through prompt templates:
- `BASE_INSTRUCTIONS` — A system-level instruction that tells the model to only use the provided text and respond in the same language as the input
- `SIMPLE_PROMPT` — 3–5 short bullet points
- `DETAILED_PROMPT` — Full-sentence, comprehensive bullet points
- `EXAM_PROMPT` — Concise, fact-dense study bullets

### `note_engine.py`
Handles persistence. The `save_note(note)` function:
- Creates `data/notes.txt` if it doesn't already exist
- Appends the summary to the file in append mode, so previous notes are never overwritten

---

## Example Walkthrough

Here's a full end-to-end example using the included `cucumbers.txt` file:

**1. Launch the app:**
```bash
streamlit run ui.py
```
Your browser will open at `http://localhost:8501`.

**2. Enter the filename:**
In the text input field, type:
```
cucumbers.txt
```

**3. Choose exam style:**
Use the dropdown to select `exam`.

**4. Click "Summarize"** and wait for the model to respond (may take 10–60 seconds depending on your hardware):
```
- Cucumbers: botanically a fruit (Cucumis sativus), member of gourd family
- Water content: ~95%
- Thrive in warm climates, annual plants
- Proper spacing prevents fungal diseases
- Harvest: 50–70 days after planting
```

**5. Save the result:**
In the save dropdown, select `yes`. The page will confirm:
```
Note saved successfully!
Note saved in 'notes.txt' file which is in 'data' folder.
```

---

## Troubleshooting

### ❌ `ModuleNotFoundError: No module named 'langchain'` or `No module named 'streamlit'`
You are likely running Python outside of the virtual environment.

**Fix:** Activate the virtual environment first:
```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```
Then run `streamlit run ui.py` again.

---

### ❌ `Connection refused` or Ollama-related error
Ollama is not running, or the model hasn't been downloaded yet.

**Fix:**
1. Open a new terminal and run: `ollama serve`
2. In another terminal, pull the model: `ollama pull llama3.1:8b`
3. Then try running the app again.

---

### ❌ `File type not supported`
You entered a file with an extension other than `.txt`, `.md`, or `.pdf`.

**Fix:** Convert your file to one of the supported formats, or check the filename for typos.

---

### ❌ `Could not load file. Please check the file path and type.`
The file you entered was not found in the `data/` folder.

**Fix:** Make sure:
- The file is placed inside the `data/` directory
- You typed the filename correctly, including the extension (e.g., `notes.md`, not just `notes`)

---

### ⏱️ The model is very slow
Response times depend on your CPU/GPU. On slower machines, a response may take 30 seconds to 2 minutes.

**Tips to speed things up:**
- Use a lighter model: `ollama pull llama3.2:3b` and update `ui.py` to use `"llama3.2:3b"`
- Close other applications to free up RAM
- If you have an NVIDIA GPU, make sure Ollama is using it (it does so automatically on supported systems)

---

## Roadmap

Features planned for future versions:

- [x] ~~GUI / web interface~~ ✅ Released in UI Release
- [ ] Batch summarization (process an entire folder at once)
- [ ] Support for scanned PDFs via OCR
- [ ] Export summaries to `.md` or `.pdf`
- [ ] Multiple language support for the prompt modes
- [ ] Support for additional models (Mistral, Gemma, Phi)
- [ ] Streamlit file uploader (drag-and-drop instead of manual `data/` placement)

---

## License

This project is open source and available for personal and educational use.
