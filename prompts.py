from langchain_core.prompts import PromptTemplate


BASE_INSTRUCTIONS = """
You are an expert at summarizing text.

Rules:
- Only use information from the provided text
- Do NOT add new information
- Keep the summary clear and accurate
- Return the summary in the SAME language as the input text
"""

SIMPLE_PROMPT = PromptTemplate.from_template(
    BASE_INSTRUCTIONS + """
    
Summarize the following text into 3-5 short bullet points.
Use simple and easy-to-understand language.

Formatting rules:
- Each bullet must start with "- "
- Keep each bullet concise (1 sentence max)

Text:
{text}
"""
)

DETAILED_PROMPT = PromptTemplate.from_template(
    BASE_INSTRUCTIONS + """
    
Summarize the following text into clear and detailed bullet points.
Include important details and explanations.

Formatting rules:
- Each bullet must start with "- "
- Use full sentences

Text:
{text}
"""
)

EXAM_PROMPT = PromptTemplate.from_template(
    BASE_INSTRUCTIONS + """
    
Extract the most important facts and key concepts from the text.
Make the summary concise and useful for studying.

Formatting rules:
- Each bullet must start with "- "
- Keep bullets short and information-dense
- Focus on definitions, concepts, and key points

Text:
{text}
"""
)