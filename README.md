# 🧠 AI Study Notes Maker

# 📌 Internship Context
# This project was built as part of the Prodigal AI Internship – Day 16 to 30.
# Focus was on learning agent-based systems using LangChain, CrewAI, and HuggingFace.
# Not a large product — just a clean demo of agent-based summarization using open-source LLMs.

# ✅ Goals:
# - Understand agent-based architecture
# - Use HuggingFace + LLMs for real-world utilities
# - Build a text summarization agent
# - Maintain clean, modular code for learning and reuse

# 📦 Installation

# Clone the repository
git clone https://github.com/atharvvv10/ai-study-notes-maker.git
cd ai-study-notes-maker

# Install required dependencies
pip install -r requirements.txt

# 🚀 Usage

# Step 1: Place your .txt file inside the input_files/ folder
# Step 2: Run the summarizer
python agent.py

# Output: Summarized notes will be saved inside output_notes/ with '_summary.txt' suffix

# 📂 Project Structure

# ai-study-notes-maker/
# ├── agent.py               # Core AI logic (file reading, summarization, output writing)
# ├── input_files/           # Input folder for raw .txt files
# ├── output_notes/          # Output folder for summarized notes
# ├── requirements.txt       # Python dependency list
# ├── crewai_agents/         # CrewAI-based agent architecture (optional)
# │   └── summarizer_crew.py # Defines agents, tasks, and workflows using CrewAI
# ├── langchain_agents/      # LangChain-based summarization pipeline (optional)
# │   └── summarizer_chain.py# Uses LLMChain for lightweight summarization
# └── README.md              # This file

# 🧪 Model Used

# Uses HuggingFace Transformers: google/flan-t5-base or flan-t5-large
# Model loaded via: pipeline("text2text-generation")
# Offline, CPU-friendly — no API key needed

# 📖 Example

# Input (input_files/topic.txt):
# Artificial Intelligence (AI) is the simulation of human intelligence by machines...

# Output (output_notes/topic_summary.txt):
# AI is machines imitating human intelligence such as learning, reasoning, and problem-solving.

# ✨ Features

# ✅ Accepts .txt input
# ✅ Outputs structured, summarized study notes
# ✅ No external API calls — fully offline
# ✅ Uses HuggingFace model via pipeline
# ✅ Optional use of CrewAI / LangChain agents
# ✅ Minimal, easy to understand and extend

# 🔮 Future Enhancements

# - Add support for PDF and DOCX input
# - Add UI using Streamlit or Gradio
# - Add highlight-based summarization
# - Allow user-defined summarization length (short/medium/long)

# 🤝 Contributing

# Fork the repository
# Make your changes / improvements
# Push and create a pull request with proper documentation

# 📄 License

# MIT License © 2025 — Atharv & Nikhil
