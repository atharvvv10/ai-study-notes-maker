# agents/note_agents.py

from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage, SystemMessage

llm = ChatOllama(model="llama3")

def split_content(text: str) -> str:
    prompt = [
        SystemMessage(content="Split the text into 3–5 logical topics."),
        HumanMessage(content=text)
    ]
    return llm.invoke(prompt).content

def summarize_section(section: str) -> str:
    prompt = [
        SystemMessage(content="Summarize this section into 3–5 key bullet points."),
        HumanMessage(content=section)
    ]
    return llm.invoke(prompt).content

def format_notes(summaries: str) -> str:
    prompt = [
        SystemMessage(content="Convert the summaries into clean, bullet-style study notes."),
        HumanMessage(content=summaries)
    ]
    return llm.invoke(prompt).content
