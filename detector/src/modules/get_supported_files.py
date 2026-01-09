from typing import List
from pathlib import Path

def get_supported_files(directory: Path, extensions: list[str] | str) -> List[Path]:
    """Возвращает список файлов с поддерживаемыми расширениями в директории"""
    supported: List[Path] = []
    for file in directory.iterdir():
        if isinstance(extensions, str):
            if file.suffix == extensions:
                supported.append((directory / file).resolve())
        else:
            if file.suffix in extensions:
                supported.append((directory / file).resolve())
    return supported