import cv2
img1 = cv2.imread('frame.png')
img2 = cv2.imread('naver.png')
print(img1.shape), print(img2.shape)

# 왼쪽 위 구석에 이미지를 넣을 것이다. ROI를 만들자
rows, cols, channels = img2.shape
roi = img1[0:rows,0:cols]

# 사진의 마스크를 만들고 인버스 마스크도 만든다.
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# ROI의 사진의 지역을 블랙아웃해준다.
img1_bg = cv2.bitwise_and(roi, roi,mask = mask_inv)

# 사진으로 부터 인물만 가져온다
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

# 인물사진을 ROI에 넣고 메인 이미지를 수정한다.
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('res' ,img1)
cv2.waitKey(0)
cv2.destroyAllWindows()