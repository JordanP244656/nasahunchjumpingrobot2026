import subprocess
from datetime import datetime
import os
 
DEVICE_MAC = "28:95:29:8E:F6:6A"
IMAGES_DIR = "images"
 
os.makedirs(IMAGES_DIR, exist_ok=True)
 
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
path = f"{IMAGES_DIR}/photo_{timestamp}.jpg"
 
subprocess.run(
    ["rpicam-still", "-o", path, "--nopreview"],
    check=True
)
 
subprocess.run(
    ["blueman-sendto", "--device", DEVICE_MAC, path],
    check=True
)
 
print("Photo captured and sent via Blueman:", path)
 