import sqlite3

DB_PATH = "kitcad.db"

def get_lengths(gost: str, thread: str) -> list:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT length FROM bolts
        WHERE gost = ? AND thread = ?
        ORDER BY length
    """, (gost, thread))
    rows = cursor.fetchall()
    conn.close()
    return [r[0] for r in rows]

def get_all_gosts() -> list:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT gost FROM bolts")
    rows = cursor.fetchall()
    conn.close()
    return [r[0] for r in rows]

def get_threads_by_gost(gost: str) -> list:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT thread FROM bolts WHERE gost = ?", (gost,))
    rows = cursor.fetchall()
    conn.close()
    return [r[0] for r in rows]

# Пример использования:
if __name__ == "__main__":
    print("Все ГОСТы:", get_all_gosts())
    print("Резьбы для ГОСТ 7798-70:", get_threads_by_gost("7798-70"))
    print("Длины для М8 по ГОСТ 7798-70:", get_lengths("7798-70", "M8"))
