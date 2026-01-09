from typing import Tuple, List, Set
from pathlib import Path

def find_missing_pairs(
    images_paths: List[Path],
    label_paths: List[Path]
) -> Tuple[List[Path], List[Path]]:
    """
    Checks whether image files and labels match.

    Args:
        images_paths (List[Path]): List of paths to image files.
        label_paths (List[Path]):  List of paths to label files.

    Returns:
        Tuple(List[Path], List[Path]): A tuple of two lists:
                - images without labels,
                - labels without images.
    """
    image_stems: Set[str] = {p.stem for p in images_paths}
    label_stems: Set[str] = {p.stem for p in label_paths}
    # Найдем изображения без разметки
    missing_labels: List[Path] =[
        img 
        for img in images_paths 
        if img.stem not in label_stems]
    # Найдем разметки без изображений
    missing_images: List[Path] =[
        label 
        for label in label_paths 
        if label.stem not in image_stems]
    return missing_images, missing_labels