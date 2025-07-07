import cv2
from pyzbar.pyzbar import decode
from datetime import datetime
import pandas as pd
import os
import tkinter as tk
from tkinter import simpledialog, messagebox


log_file = 'log_data.xlsx'
if not os.path.exists(log_file):
    df = pd.DataFrame(columns=['Timestamp', 'Prototype_ID', 'Tester_ID', 'Remarks'])
    df.to_excel(log_file, index=False)


def get_user_inputs(prototype_id):
    root = tk.Tk()
    root.withdraw()
    tester = simpledialog.askstring("Tester ID", f"Scanned: {prototype_id}\n\nEnter your Tester ID:")
    remarks = simpledialog.askstring("Remarks", "Optional Remarks:")
    return tester, remarks

def log_entry(prototype_id, tester_id, remarks):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df = pd.read_excel(log_file)
    df.loc[len(df)] = [timestamp, prototype_id, tester_id, remarks]
    df.to_excel(log_file, index=False)
    print(f"[Logged] {timestamp} | {prototype_id} | {tester_id} | {remarks}")


cap = cv2.VideoCapture(0)
print("🟢 Scanner active. Show a QR code to log...")

while True:
    _, frame = cap.read()
    for code in decode(frame):
        qr_data = code.data.decode('utf-8')
        print(f"📷 Detected QR: {qr_data}")
        tester_id, remarks = get_user_inputs(qr_data)
        if tester_id:
            log_entry(qr_data, tester_id, remarks)
            messagebox.showinfo("✅ Log Saved", f"Prototype {qr_data} logged successfully.")
            cv2.waitKey(1000)

    cv2.imshow('QR Log Scanner - Press Q to Quit', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
