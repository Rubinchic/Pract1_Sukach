import json
import os
from threading import Lock

class Assistant:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.lock = Lock()
        self.notes = []
        self._load_notes()

    def _load_notes(self):
        if not os.path.exists(self.filename):
            self.notes = []
            self._save_notes()
            return
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.notes = json.load(f)
        except Exception:
            self.notes = []
            self._save_notes()

    def _save_notes(self):
        with self.lock:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.notes, f, ensure_ascii=False, indent=2)

    def add_note(self, note: str, tags=None):
        tags = tags or []
        self.notes.append({"note": note, "tags": tags})
        self._save_notes()

    def list_notes(self):
        return self.notes

    def search_notes(self, keyword: str):
        result = [n for n in self.notes if keyword.lower() in n["note"].lower()]
        return result

    def search_by_tag(self, tag: str):
        return [n for n in self.notes if tag.lower() in [t.lower() for t in n["tags"]]]

