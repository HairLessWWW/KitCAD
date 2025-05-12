import re

def parse_description(text):
    result = {}

    if match := re.search(r"м(\d+)", text.lower()):
        result["thread"] = f"M{match.group(1)}"
        result["diameter"] = int(match.group(1))

    if match := re.search(r"(длина|длин[аы]|l=|h=)\s*(\d+)", text.lower()):
        result["length"] = int(match.group(2))
    else:
        result["length"] = 30  # по умолчанию

    if "лева" in text.lower():
        result["direction"] = "left"
    else:
        result["direction"] = "right"

    if "шестигран" in text.lower() or "hex" in text.lower():
        result["head"] = "hex"
    else:
        result["head"] = "none"

    return result
