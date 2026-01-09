from pathlib import Path
from typing import List

from detector.src.modules import get_supported_files
from detector.src.modules import find_missing_pairs

def check_dataset(base_dir: Path) -> str | None:
    """Основная функция проверки соответствия файлов"""
    images_dir: Path = base_dir / 'images'
    labels_dir: Path = base_dir / 'labels'
    
    # Проверяем существование директорий
    if not images_dir.exists():
        print(f"Папка изображений не найдена: {images_dir}")
        return
    if not labels_dir.exists():
        print(f"Папка меток не найдена: {labels_dir}")
        return
    
    # Получаем файлы с поддерживаемыми расширениями
    img_ext: str = '.jpg'
    lbl_ext: str = '.txt'
    
    image_files: List[Path] = get_supported_files(images_dir, img_ext)
    label_files: List[Path] = get_supported_files(labels_dir, lbl_ext)
    
    # Проверяем соответствия
    missing_img, missing_lbl = find_missing_pairs(image_files, label_files)
    
    # Формируем отчёт
    report: List = []
    total_images = len(image_files)
    total_labels = len(label_files)
    
    if not missing_img and not missing_lbl:
        report.append("Все файлы имеют соответствующие пары:")
        report.append(f"  Изображений: {total_images}")
        report.append(f"  Меток: {total_labels}")
    else:
        if missing_img:
            report.append("Изображения без соответствующих меток:")
            for img in missing_img:
                report.append(f"  - {img.name}")
            report.append(f"Всего: {len(missing_img)} изображений")
        
        if missing_lbl:
            report.append("\nМетки без соответствующих изображений:")
            for lbl in missing_lbl:
                report.append(f"  - {lbl.name}")
            report.append(f"Всего: {len(missing_lbl)} меток")
        
        report.append("\nИтоговая статистика:")
        report.append(f"  Всего изображений: {total_images}")
        report.append(f"  Всего меток: {total_labels}")
        report.append(f"  Полных пар: {min(total_images, total_labels) - max(len(missing_img), len(missing_lbl))}")
    
    return "\n".join(report)