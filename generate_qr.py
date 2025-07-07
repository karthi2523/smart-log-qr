import qrcode
import os

prototypes = ['PROT-A', 'PROT-B', 'PROT-C', 'PROT-D']
os.makedirs('prototype_qrs', exist_ok=True)

for pid in prototypes:
    img = qrcode.make(pid)
    img.save(f'prototype_qrs/{pid}.png')

print("✅ QR codes generated in 'prototype_qrs' folder.")
