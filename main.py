import cv2
import glob
from qr import *

def makeframe(frame_path):
    # 프레임 이미지 불러오기
    frame = cv2.imread(frame_path)
    frame = cv2.resize(frame, dsize=(756,1134), interpolation=cv2.INTER_AREA)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 프레임 박스 정보
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

    # 프레임 위에 이미지 넣기
    for (filename, left_box, right_box) in zip(glob.iglob('photos/*.jpg', recursive=True), left_boxes.values(), right_boxes.values()):
        img = cv2.imread(filename)
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        lp1, lp2 = left_box
        rp1, rp2 = right_box
        roi = cv2.resize(img, dsize=(lp2[0] - lp1[0], lp2[1] - lp1[1]), interpolation=cv2.INTER_AREA)
        frame[lp1[1]+3:lp2[1]+3, lp1[0]+3:lp2[0]+3] = roi
        roi = cv2.resize(img, dsize=(rp2[0] - rp1[0], rp2[1] - rp1[1]), interpolation=cv2.INTER_AREA)
        frame[rp1[1]+3:rp2[1]+3, rp1[0]+3:rp2[0]+3] = roi

    # QR 코드 생성
    eigen = getMD5(str(time.time()))[:10]
    urltoQR('qrqr.png','http://sada.dothome.co.kr/photo/'+eigen+'.png')
    qrimg = cv2.imread('qrqr.png')
    w,h,_ = qrimg.shape
    qrimg = qrimg[35:w-35,35:h-35]

    # 프레임에 QR코드 넣기
    lp1,lp2 = [(289, 1045), (356, 1113)]
    rp1,rp2 = [(669, 1047), (735, 1113)]
    roi = cv2.resize(qrimg, dsize=(lp2[0] - lp1[0], lp2[1] - lp1[1]), interpolation=cv2.INTER_AREA)
    frame[lp1[1]+2:lp2[1]+2, lp1[0]+1:lp2[0]+1] = roi
    roi = cv2.resize(qrimg, dsize=(rp2[0] - rp1[0], rp2[1] - rp1[1]), interpolation=cv2.INTER_AREA)
    frame[rp1[1]+1:rp2[1]+1, rp1[0]:rp2[0]] = roi

    return frame

# 모든 프레임에 대해 이미지 넣고 결과 저장하기
i=1
for frame in glob.iglob('frames/*.png', recursive=True):
    result = makeframe(frame)
    cv2.imwrite('results/result'+str(i)+'.png', result)
    i += 1