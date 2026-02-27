from PIL import Image, ImageDraw
from datetime import datetime
import os
import subprocess
 
DEVICE_MAC = "28:95:29:8E:F6:6A"
IMAGES_DIR = "images"
 
os.makedirs(IMAGES_DIR, exist_ok=True)
 
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
path = f"{IMAGES_DIR}/generated_{timestamp}.png"
 
img = Image.new("RGB", (800, 600), (40, 40, 40))
draw = ImageDraw.Draw(img)
draw.text(
    (50, 260),
    "NO CAMERA ATTACHED\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    fill=(255, 255, 255)
)
img.save(path)
 
subprocess.run(
    ["blueman-sendto", "--device", DEVICE_MAC, path],
    check=True
)
 
print("Generated image sent:", path)
 
