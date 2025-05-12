def classify_prompt(text: str) -> dict:
    text = text.lower()

    if "болт" in text or "винт" in text:
        return {"type": "bolt"}
    if "гайка" in text:
        return {"type": "nut"}
    if "шайба" in text:
        return {"type": "washer"}
    if "уголок" in text:
        return {"type": "angle"}
    if "редуктор" in text:
        return {"type": "gearbox"}
    if "фланец" in text:
        return {"type": "flange"}
    if "сборка" in text or "узел" in text:
        return {"type": "assembly"}

    return {"type": "unknown"}
