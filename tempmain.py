from engine import (
    read_syllabus,
    extract_syllabus_window,
    generate_question_paper
)

def main():
    # 1. Read raw syllabus
    raw = read_syllabus("syllabus.docx")

    print("\n================ RAW SYLLABUS (first 1500 chars) ================\n")
    print(raw[:1500])
    print("\n=================================================================\n")

    # 2. Extract syllabus window
    window = extract_syllabus_window(raw)

    print("\n=========== SYLLABUS WINDOW SENT TO LLM (FULL) ==================\n")
    print(window)
    print("\n=================================================================\n")

    print("\n=========== SYLLABUS WINDOW LENGTH ==============================\n")
    print(len(window), "characters")
    print("\n=================================================================\n")

    # 3. DIRECT generation (no retries, no validation)
    print("\n=========== RAW LLM OUTPUT ======================================\n")
    paper = generate_question_paper(window)
    print(paper)
    print("\n=================================================================\n")


if __name__ == "__main__":
    main()
