from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx",
    ".java", ".cpp", ".c", ".cs", ".go",
    ".md", ".json", ".yaml", ".yml"
}

class FileScannerService:
    def __init__(self, root: str):
        self.root = Path(root)

    def scan(self):
        files = []
        for path in self.root.rglob("*"):
            if path.suffix in SUPPORTED_EXTENSIONS and path.is_file():
                files.append(path)
        return files
