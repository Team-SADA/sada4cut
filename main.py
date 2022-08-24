import cv2
import matplotlib.pyplot as plt
import glob

tframe = cv2.imread('testframe.png')
print(tframe.shape)
frame = cv2.imread('pink.png')
frame = cv2.resize(frame, dsize=tframe.shape[:2][::-1], interpolation=cv2.INTER_AREA)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

left_boxes = {
    'box1': [(16, 10), (356, 239)],
    'box2': [(16, 257), (356, 484)],
    'box3': [(16, 498), (356, 727)],
    'box4': [(16, 744), (356, 972)]
}

right_boxes = {
    'box5': [(393, 10), (735, 239)],
    'box6': [(393, 257), (735, 484)],
    'box7': [(393, 498), (735, 727)],
    'box8': [(393, 744), (735, 972)]
}

for (filename, left_box, right_box) in zip(glob.iglob('imgs/*.jpg', recursive=True), left_boxes.values(), right_boxes.values()):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    lp1, lp2 = left_box
    rp1, rp2 = right_box

    roi = cv2.resize(img, dsize=(lp2[0] - lp1[0], lp2[1] - lp1[1]), interpolation=cv2.INTER_AREA)
    frame[lp1[1]:lp2[1], lp1[0]:lp2[0]] = roi

    roi = cv2.resize(img, dsize=(rp2[0] - rp1[0], rp2[1] - rp1[1]), interpolation=cv2.INTER_AREA)
    frame[rp1[1]:rp2[1], rp1[0]:rp2[0]] = roi

    plt.imshow(frame)
    plt.show()
