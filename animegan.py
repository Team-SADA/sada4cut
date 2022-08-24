import torch
from PIL import Image

model = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="face_paint_512_v2")
model = model.to(torch.device('mps')) # Change to your device!
face2paint = torch.hub.load("bryandlee/animegan2-pytorch:main", "face2paint", size=1080)
img = Image.open(r"asdf.jpg").crop((848, 0, 2542, 1694)).resize((1080, 1080)).convert("RGB")
out = face2paint(model, img)
out.show()
