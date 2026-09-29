# AI Car Dashboard - Camera Proximity Alerter 🚗💨

An AI-powered computer vision safety system designed for car dashboards. The application tracks surrounding obstacles using real-time object detection and dynamically calculates relative distance based on shape size geometry to sound an emergency alert during close-range threats.

## 🛠️ Project Components
* **`CarDashboard.ipynb`**: The cloud training notebook used to train the machine learning weights on a Tesla T4 GPU.
* **`dashboard_app.py`**: The local application script that hooks into desktop camera hardware, processes video streams at 30+ FPS, and controls the audio buzzer warning loop.

## ⚙️ How it Works
1. **Real-Time Detection:** Streams live video frames and feeds them directly into a lightweight **YOLOv8 Nano** machine learning model.
2. **Proximity Tracking:** Constantly evaluates the geometric pixel area footprint of target obstacles.
3. **Emergency Alerts:** If any tracking rectangle crosses the safety threshold size boundary, the system flips the UI boundary to **Red** and commands the local motherboard sound drivers to emit rapid **1200 Hz alert beep pulses**.
