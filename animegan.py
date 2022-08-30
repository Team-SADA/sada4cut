import torch
from PIL import Image

# 사진기에 따라 바꿀 것
n = None

model = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="face_paint_512_v2")
model = model.to(torch.device('gpu')) # Change to your device!
face2paint = torch.hub.load("bryandlee/animegan2-pytorch:main", "face2paint", size=720)
img = Image.open(r".photos/img1.jpg").crop((0, 0, n, n)).resize((720, 720)).convert("RGB")
out = face2paint(model, img)
out.show()
