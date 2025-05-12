from classifier import classify_prompt
from interactive_parser import ask_missing_parameters

def process_user_input(text: str) -> str:
    classification = classify_prompt(text)
    type_ = classification.get("type", "unknown")

    if type_ == "unknown":
        return "⚠️ Не удалось распознать тип объекта. Попробуй уточнить: болт, гайка, уголок, редуктор и т.д."

    questions = ask_missing_parameters(text, type_)
    if questions:
        return f"🔍 Распознан тип: {type_}\n" + "\n".join(f"❓ {q}" for q in questions)
    else:
        return f"✅ Распознан тип: {type_}. Все необходимые параметры указаны. Можно генерировать модель."

# Пример работы:
if __name__ == "__main__":
    user_text = input("Введите запрос: ")
    print(process_user_input(user_text))
