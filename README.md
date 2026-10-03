# AI Car Dashboard — Camera Proximity Demo 🚗

A small computer-vision demo that watches a live webcam feed, detects objects, and highlights large detections with a visual warning. Train the model in Google Colab, download its weights, and run the camera app on your computer.

> **Safety first:** This is an educational demo, not a driving aid or a safety-certified system. It does not measure real-world distance, control a vehicle, or sound an audio alarm. Never use it to make driving decisions.

## What's in the project?

| File | Purpose |
| --- | --- |
| [`CarDashboard.ipynb`](./CarDashboard.ipynb) | Google Colab notebook that trains a YOLOv8 Nano model and creates training outputs. |
| [`dashboard_app.py`](./dashboard_app.py) | Local webcam demo that loads `best.pt`, draws detection boxes, and marks large boxes as critical. |

## How it works

1. The notebook trains Ultralytics YOLOv8 Nano (`yolov8n.pt`) for 10 epochs on the built-in **COCO8** sample dataset.
2. Training creates `best.pt` in `runs/detect/train/weights/`.
3. The local app reads frames from camera `0`, runs object detection, and draws a box around each detection.
4. A detection with a bounding-box area above `60,000` pixels is marked **CRITICAL HAZARD - EVADE!** in red. Smaller detections are shown in yellow.

**Important:** COCO8 is a tiny general-purpose sample dataset, not a custom road-hazard dataset. The box-area threshold is only a rough image-space heuristic; it does not calculate physical distance. Expect this demo's predictions to be limited.

## Quick start: run the camera demo

### 1. Get the project files

Clone the repository, or download the project files and open a terminal in the project folder:

```bash
git clone https://github.com/yashrajchavan2311-alt/Car-Dashboard-AI.git
cd Car-Dashboard-AI
```

### 2. Create and activate a virtual environment

Python 3.10 or newer is recommended.

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead:

```bat
.\.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
python -m pip install --upgrade pip
python -m pip install ultralytics opencv-python
```

### 4. Train or obtain the model weights

The app needs a trained weights file named **`best.pt`** in the same folder as `dashboard_app.py`. To create it with the included notebook, follow the [training instructions](#train-the-model-in-google-colab) below and download the weights from Colab.

Your project folder should look like this before running the app:

```text
Car-Dashboard-AI/
├── dashboard_app.py
├── best.pt                 # Downloaded from the Colab training run
├── CarDashboard.ipynb
└── README.md
```

### 5. Start the app

Connect a webcam, then run:

```bash
python dashboard_app.py
```

A window will show the live camera feed with detection boxes. Press **`q`** while the video window is focused to close it.

## Train the model in Google Colab

1. Open [`CarDashboard.ipynb`](https://colab.research.google.com/github/yashrajchavan2311-alt/Car-Dashboard-AI/blob/main/CarDashboard.ipynb) in Google Colab.
2. In Colab, choose **Runtime → Change runtime type**. A GPU is optional, but can speed up training.
3. Run the notebook cells from top to bottom and wait for training to finish.
4. In the Colab file browser, open `runs/detect/train/weights/` and download **`best.pt`**.
   - The notebook's `training_proof.zip` download contains training charts and metrics; it deliberately excludes the weights. Download `best.pt` separately from the `weights` folder.
5. Move `best.pt` into the same local folder as `dashboard_app.py`.
6. Follow the [local setup steps](#quick-start-run-the-camera-demo) to install dependencies and launch the app.

## Troubleshooting

| Problem | What to try |
| --- | --- |
| `Could not find 'best.pt'` | Download `best.pt` from `runs/detect/train/weights/` in Colab and place it beside `dashboard_app.py`. Check that the filename is exactly `best.pt`, not `best.pt.pt`. |
| Camera feed does not open | Close other apps using the camera, check OS camera permissions, and confirm your webcam works. The app currently uses camera index `0`; if your webcam is another device, change `cv2.VideoCapture(0)` in `dashboard_app.py` to its index. |
| `No module named ...` | Activate the virtual environment used for setup, then run `python -m pip install ultralytics opencv-python` again. |
| PowerShell won't activate `.venv` | Use the Command Prompt activation command above, or consult your organization's PowerShell policy before changing it. |
| Boxes appear too early or too late | The demo uses a fixed box-area threshold of `60,000` pixels in `dashboard_app.py`. Changing it affects the visual alert only; it will not make the estimate a real distance measurement. |

## Limitations

- The included training flow uses COCO8, a very small sample dataset; it is not trained specifically for vehicles or road hazards.
- Bounding-box pixel area depends on camera resolution, framing, and object orientation. It is not a reliable distance sensor.
- The app currently provides visual labels only. It does not include the audio buzzer described in some earlier project notes.
- Model accuracy, camera access, and performance vary by machine and lighting.

## Author

**Yashraj Chavan** — [@yashrajchavan2311-alt](https://github.com/yashrajchavan2311-alt)

---

Have fun experimenting, and keep the demo safely off the road! 🛠️✨
