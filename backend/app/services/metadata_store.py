import json
from pathlib import Path


class MetadataStore:
    def __init__(self):
        # Resolve path relative to this file → backend/data/metadata.json
        base_dir = Path(__file__).resolve().parents[2]
        self.path = base_dir / "data" / "metadata.json"
        self.path.parent.mkdir(parents=True, exist_ok=True)

        if self.path.exists():
            with open(self.path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = []

    def add(self, meta: dict):
        meta["id"] = len(self.data)
        self.data.append(meta)
        self._save()

    def get(self, idx: int):
        if idx < len(self.data):
            return self.data[idx]
        return None

    def _save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)
