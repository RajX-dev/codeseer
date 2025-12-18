from pathlib import Path


class FileScannerService:
    def __init__(self, base_dir: str):
        # Resolve path relative to backend directory
        backend_dir = Path(__file__).resolve().parents[2]
        self.base_dir = backend_dir / base_dir

    def scan(self):
        if not self.base_dir.exists():
            print(f"⚠️ Scan directory does not exist: {self.base_dir}")
            return []

        files = []
        for ext in ("*.py", "*.js", "*.ts", "*.cpp", "*.java"):
            files.extend(self.base_dir.rglob(ext))

        return files
