# Smart QR Code Log Automation 📋🔍

This project is a Python-based smart logging system that uses QR codes and a webcam to track prototype testing in an R&D lab. It automatically records tester ID, prototype ID, timestamp, and remarks into an Excel file.

## 💡 Features
- QR code scanning using OpenCV and Pyzbar
- Logs saved to `log_data.xlsx`
- Tkinter popups for tester inputs
- Excel-ready data for Power BI dashboards

## 📦 Technologies Used
- Python
- OpenCV
- Pandas
- Pyzbar
- Pillow
- Tkinter

## 🔧 How to Run
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python generate_qr.py
python main.py
