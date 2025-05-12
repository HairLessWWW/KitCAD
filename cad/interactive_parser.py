import re

def ask_missing_parameters(text: str, type_: str) -> dict:
    prompts = []

    if type_ == "bolt":
        if not re.search(r"м\d+", text.lower()):
            prompts.append("Укажи, пожалуйста, диаметр болта (например, М6, М8)")
        if not re.search(r"(длина|l=|h=)\s*\d+", text.lower()):
            prompts.append("Какова длина болта?")
        if "шестигран" not in text.lower() and "потайн" not in text.lower():
            prompts.append("Какой тип головки — шестигранная, потайная или другая?")
    elif type_ == "gearbox":
        if not re.search(r"передаточ", text.lower()):
            prompts.append("Какое передаточное число редуктора?")
        if not re.search(r"(размер|габарит|ширин|высот|длин)", text.lower()):
            prompts.append("Укажи габариты редуктора или ограничения по размерам")
        if "момент" not in text.lower():
            prompts.append("Какой крутящий момент нужен на выходе?")

    return prompts
