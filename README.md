# YOLO-RPS-Detector  🪨✂️📄
Practice to create a real-time hand gesture detection for the classic Rock-Paper-Scissors game using a fine-tuned YOLO model.

## 🚀 Features
- Fine-tuned YOLOv8 model for detecting rock / paper / scissors hand poses
- Real-time inference from webcam or video input
- Game logic to determine winner against computer
- Clean, modular codebase with Pydantic config & Poetry-managed dependencies

## 🛠️ Tech Stack
- Python `>=3.13,<3.14`
- [Ultralytics](https://github.com/ultralytics/ultralytics) (YOLOv8)
- PyTorch
- Pydantic (v2)
- Poetry (dependency & virtual env management)

## ▶️ Quick Start
```bash
# Clone & enter repo
git clone https://github.com/yourname/YOLO-RPS-Detector.git
cd YOLO-RPS-Detector

# Install deps
poetry install

# Run inference on webcam
poetry run python src/play.py
```

> 💡 Requires a pre-trained YOLO model (`best.pt`) trained on a custom RPS hand gesture dataset.

## 📂 Project Structure
```
.
├── data/               # Dataset & labels
├── models/             # Trained weights
├── src/
│   ├── detect.py       # Hand pose detection
│   ├── game.py         # Game logic
│   └── play.py         # Main entry (video/webcam)
├── pyproject.toml      # Poetry config
└── README.md
```
## 📜 License
MIT
