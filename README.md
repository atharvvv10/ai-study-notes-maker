```bash
# 🧠 AI Study Notes Maker

# 📌 Internship Context
# Built as part of the Prodigal AI Internship – Day 16 to 30.
# Objective: Learn AI agents using LangChain, CrewAI, HuggingFace, and Pydantic.
# Goal: Build a simple, modular tool that summarizes .txt files using open-source LLMs.

# ✅ Highlights:
# - Agent-based architecture
# - LLM-powered summarization
# - No API keys required
# - Offline, CPU-compatible
# - Practical real-world automation

# 📦 Installation

# Clone the repository
git clone https://github.com/atharvvv10/ai-study-notes-maker.git
cd ai-study-notes-maker

# Install dependencies
pip install -r requirements.txt

# 🚀 Usage

# 1. Place any .txt file into the input_files/ directory
# 2. Run the summarizer
python agent.py

# Output will be stored inside output_notes/ with filename: <original>_summary.txt

# 📂 Project Structure

# ai-study-notes-maker/
# ├── agent.py                 # Main summarizer logic
# ├── input_files/             # Input folder for raw .txt files
# ├── output_notes/            # Folder for summarized output
# ├── requirements.txt         # Dependencies
# ├── README.md                # You’re reading this
# ├── crewai_agents/           # Optional: CrewAI-based architecture
# │   └── summarizer_crew.py   # Agents, tasks, crew logic
# └── langchain_agents/        # Optional: LangChain-based pipeline
#     └── summarizer_chain.py  # LLMChain with prompt logic

# 📖 Example

# Input (input_files/topic.txt):
# Artificial Intelligence (AI) is the simulation of human intelligence processes by machines...

# Output (output_notes/topic_summary.txt):
# AI refers to machines mimicking human intelligence such as learning, reasoning, and decision making.

# 🧪 Model Used

# Model: google/flan-t5-base OR flan-t5-large
# Inference: HuggingFace pipeline("text2text-generation")
# No API key, runs on CPU

# ✨ Features

# ✅ Simple text-to-summary AI agent
# ✅ Accepts flexible input (.txt)
# ✅ Outputs clean, simplified notes
# ✅ Works offline (no API)
# ✅ Supports CrewAI and LangChain agent systems

# 🧩 Agent Architectures (Optional)

# CrewAI Version:
# crewai_agents/summarizer_crew.py
# → Modular agents: File Loader, Preprocessor, Summarizer
# → CrewAI orchestrates flow of tasks

# LangChain Version:
# langchain_agents/summarizer_chain.py
# → LLMChain + prompt template
# → Simple linear summarization pipeline

# 🔮 Future Enhancements

# - Add PDF and Word document support
# - Streamlit/Gradio UI
# - Extractive summaries with highlights
# - Adjustable summary length

# 🤝 Contributing

# Fork the repo
# Add new agent pipelines or UI
# Commit with docs
# Submit a PR

# 📄 License

# MIT License © 2025 — Atharv

```
