from classifier import classify_prompt
from interactive_parser import ask_missing_parameters

def complete_dialog():
    print("👋 Привет! Я KitCAD ассистент. Опиши, что хочешь построить.")
    user_text = input("🧾 Ввод: ").strip()

    classification = classify_prompt(user_text)
    type_ = classification.get("type", "unknown")

    if type_ == "unknown":
        print("⚠️ Не понял, что именно ты хочешь построить (например, болт, гайка, уголок, редуктор...).")
        return

    params_text = user_text
    previous_questions = set()
    loop_counter = 0
    MAX_LOOPS = 5

    while True:
        unanswered = ask_missing_parameters(params_text, type_)
        unanswered_set = set(unanswered)

        if not unanswered:
            print(f"✅ Все параметры собраны. Сохраняю input.txt")
            with open("input.txt", "w", encoding="utf-8") as f:
                f.write(params_text)
            print(f" Итоговая строка запроса: {params_text}")
            break

        if unanswered_set == previous_questions:
            loop_counter += 1
            if loop_counter >= MAX_LOOPS:
                print("❗ Похоже, ответы не помогают. Проверь формулировки и попробуй начать заново.")
                break
        else:
            loop_counter = 0

        previous_questions = unanswered_set
        print(f"
🔍 Распознан тип: {type_}")
        for question in unanswered:
            print("❓", question)
            answer = input("✏️  Ответ: ").strip()
            params_text += " " + answer

if __name__ == "__main__":
    complete_dialog()
