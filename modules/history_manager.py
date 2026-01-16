import os

# On remonte d'un dossier pour trouver history.txt à la racine
HISTORY_FILE = "history.txt"

def save_to_history(expression, result):
    """Sauvegarde l'opération et son résultat."""
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as file:
            file.write(f"{expression} = {result}\n")
    except Exception as e:
        print(f"Error saving history: {e}")

def get_history():
    """Récupère le contenu de l'historique."""
    if not os.path.exists(HISTORY_FILE):
        return "History is empty."
    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
        return "".join(lines) if lines else "History is empty."

def clear_history():
    """Efface l'historique."""
    if os.path.exists(HISTORY_FILE):
        open(HISTORY_FILE, "w").close()
        return "History cleared."
    return "No history to clear."