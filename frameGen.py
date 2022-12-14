import cv2
import glob
from qr import *

def makeframe(frame_path):
    # 프레임 이미지 불러오기
    frame = cv2.imread(frame_path)
    frame = cv2.resize(frame, dsize=(2000,3000),interpolation=cv2.INTER_AREA)

    # 프레임 박스 정보
    left_boxes = {
        'box1': [(45, 35), (952, 642)],
        'box2': [(45, 680), (952, 1287)],
        'box3': [(45, 1325), (952, 642 + 645 * 2)],
        'box4': [(45, 1970), (952, 642 + 645 * 3)]
    }

    right_boxes = {
        'box5': [(1045, 35), (1952, 642)],
        'box6': [(1045, 680), (1952, 1287)],
        'box7': [(1045, 1325), (1952, 642 + 645 * 2)],
        'box8': [(1045, 1970), (1952, 642 + 645 * 3)]
    }

    # 프레임 위에 이미지 넣기
    # photos/anim/*.jpg
    for (filename, left_box, right_box) in zip(glob.iglob('photos/*.jpg', recursive=True), left_boxes.values(), right_boxes.values()):
        img = cv2.imread(filename)
        h = len(img)
        w = len(img[0])

        if w * 2 / 3 > h:
            h_f = h - h % 6
            w_f = int(h_f * 3 / 2)
            img = img[:h_f, ((w - w_f) // 2):((w - w_f) // 2 + w_f)]

        else:
            w_f = w - w % 6
            h_f = int(w_f * 2 / 3)
            img = img[((h - h_f) // 2):((h - h_f) // 2 + h_f), :w_f]
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
    k0, k1 = [762,2766], [949,2954]
    sk = 18
    lp1 = (k0[0]+sk,k0[1]+sk)
    lp2 = (k1[0]-sk,k1[1]-sk)
    rp1 = (k0[0]+sk+1000,k0[1]+sk)
    rp2 = (k1[0]-sk+1000,k1[1]-sk)

    roi = cv2.resize(qrimg, dsize=(lp2[0] - lp1[0], lp2[1] - lp1[1]), interpolation=cv2.INTER_AREA)
    frame[lp1[1]+2:lp2[1]+2, lp1[0]+1:lp2[0]+1] = roi
    roi = cv2.resize(qrimg, dsize=(rp2[0] - rp1[0], rp2[1] - rp1[1]), interpolation=cv2.INTER_AREA)
    frame[rp1[1]+1:rp2[1]+1, rp1[0]:rp2[0]] = roi

    return frame,eigen

def animate():
    pass
    '''
    for i in range(1,5):
        name = 'img' + str(i) +'.jpg'
        animateoneImage('photos/'+name,'photos/'+'anim/'+name) #save at 'photos/'+name'''


def generateImage(frameNum):
    frame = 'frames/'+str(frameNum)+'.jpg'
    animate()
    result, eigen = makeframe(frame)
    cv2.imwrite('results/' + eigen + '.png', result)
    uploadtoServer('results/' + eigen + '.png', eigen)
    return frame



# 모든 프레임에 대해 이미지 넣고 결과 저장하기
'''i=1
for frame in glob.iglob('frames/*.jpg', recursive=True):
    result,eigen = makeframe(frame)
    cv2.imwrite('results/'+eigen+'.png', result)
    uploadtoServer('results/'+eigen+'.png',eigen)
    i += 1'''

