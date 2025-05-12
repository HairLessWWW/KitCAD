from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Literal, Optional

app = FastAPI()

class EngineeringQuery(BaseModel):
    message: str

@app.post("/ask")
async def handle_engineering_query(query: EngineeringQuery):
    response = process_engineering_query(query.message)
    return response

# chat_handler.py
def process_engineering_query(message: str) -> dict:
    message_lower = message.lower()

    if "гост" in message_lower:
        return {
            "type": "gost_info",
            "response": f"🔍 Ищу информацию по: {message} (пока заглушка)"
        }
    elif any(kw in message_lower for kw in ["болт", "гайка", "шайба", "фланец", "узел"]):
        return {
            "type": "generate_model",
            "input_text": message,
            "message": "✅ Запрос на генерацию модели принят. Сохрани в input.txt и запусти генератор."
        }
    else:
        return {
            "type": "unknown",
            "message": "⚠️ Не удалось распознать запрос. Попробуй уточнить или использовать слово 'ГОСТ', 'болт', 'модель' и т.д."
        }
from fastapi.staticfiles import StaticFiles
import os

app.mount("/", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "../static"), html=True), name="static")
