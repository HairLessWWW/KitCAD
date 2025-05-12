from classifier import classify_prompt
from interactive_parser import ask_missing_parameters

def complete_dialog():
    print("👋 Привет! Я KitCAD ассистент. Опиши, что хочешь построить.")
    user_text = input("🧾 Ввод: ").strip()

    classification = classify_prompt(user_text)
    type_ = classification.get("type", "unknown")

    if type_ == "unknown":
        print("⚠️ Не понял, что именно ты хочешь построить (болт, гайка, редуктор, уголок...). Попробуй переформулировать.")
        return

    params_text = user_text
    unanswered = ask_missing_parameters(user_text, type_)

    while unanswered:
        print(f"🔍 Распознан тип: {type_}")
        for question in unanswered:
            print("❓", question)
            answer = input("✏️  Ответ: ").strip()
            params_text += " " + answer

        # повторная проверка после добавления новых ответов
        unanswered = ask_missing_parameters(params_text, type_)

    print("✅ Все параметры собраны. Сохраняю input.txt и запускай генерацию!")
    with open("input.txt", "w", encoding="utf-8") as f:
        f.write(params_text)
    print(f"\n Итоговая строка запроса: \"{params_text}\"")


if __name__ == "__main__":
    complete_dialog()
