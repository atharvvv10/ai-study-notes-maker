# main.py

from agents.note_agents import split_content, summarize_section, format_notes

def read_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    path = input("📄 Enter path to your .txt study chapter: ").strip()
    content = read_content(path)

    print("\n🔍 Splitting content into logical topics...\n")
    split_output = split_content(content)
    print("🧩 Split Topics:\n", split_output)

    print("\n📝 Summarizing each topic...\n")
    summarized_output = summarize_section(split_output)
    print("🧠 Summarized Points:\n", summarized_output)

    print("\n🗂 Formatting into study notes...\n")
    final_notes = format_notes(summarized_output)

    print("\n✅ Final Study Notes:\n")
    print(final_notes)
