import pygame
import pygame.camera
import pygame.image
import cv2
import time
# initialize game
pygame.init()

# screen option setting
size = [1920, 1080]
icon = pygame.image.load('gui_imgs/SADA_logo.png')
screen = pygame.display.set_mode(size)
pygame.display.set_icon(icon)
pygame.display.set_caption('사다네컷')

# game setting
clock = pygame.time.Clock()

class Obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sx = 0
        self.sy = 0

    def put_img(self, img_path):
        if img_path[-3:] == 'png':
            self.img = pygame.image.load(img_path).convert_alpha()
        else:
            self.img = pygame.image.load(img_path)
        self.sx, self.sy = self.img.get_size()

    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img, (self.x, self.y))


# object setting

slide1 = Obj()
slide1.put_img('gui_imgs/슬라이드1.png')
slide1.change_size(1920, 1080)
slide1.x, slide1.y = 0, 0

slide2 = Obj()
slide2.put_img('gui_imgs/슬라이드2.png')
slide2.change_size(1920, 1080)
slide2.x, slide2.y = 0, 0

slide3 = Obj()
slide3.put_img('gui_imgs/슬라이드3.png')
slide3.change_size(1920, 1080)
slide3.x, slide3.y = 0, 0

slide4 = Obj()
slide4.put_img('gui_imgs/슬라이드4.png')
slide4.change_size(1920, 1080)
slide4.x, slide4.y = 0, 0

slide5 = Obj()
slide5.put_img('gui_imgs/슬라이드5.png')
slide5.change_size(1920, 1080)
slide5.x, slide5.y = 0, 0

slide6 = Obj()
slide6.put_img('gui_imgs/슬라이드6.png')
slide6.change_size(1920, 1080)
slide6.x, slide6.y = 0, 0

# check img
check1 = Obj()
check1.put_img('gui_imgs/check.png')
check1.change_size(250, 250)

check2 = Obj()
check2.put_img('gui_imgs/check.png')
check2.change_size(250, 250)

bool1, bool2 = False, False

# slide event, frame
SB = 0
SN = 1
slide1.show()
FRAME_NUM = 0
PEOPLE_NUM = 0
mx, my = 0, 0

# camera setting
pygame.camera.init()
cameras = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cameras[0])
webcam.start()

while SB == 0:
    # FPS setting
    pygame.time.delay(10)
    # update
    #pygame.display.flip()
    pygame.display.update()
    # sense inputs
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx,my)
    if SN == 1:
        slide1.show()
        if 768 < mx < 1153 and 641 < my < 760:
            SN = 2
    elif SN == 2:
        slide2.show()
        # check1
        if bool1 == False:
            if 189 < mx < 453 and 178 < my < 577:
                FRAME_NUM = 1
                check1.x, check1.y = 194, 263
                bool1 = True
            elif 348 < mx < 768 and 178 < my < 577:
                FRAME_NUM = 2
                check1.x, check1.y = 505, 263
                bool1 = True
            elif 807 < mx < 1077 and 178 < my < 577:
                FRAME_NUM = 3
                check1.x, check1.y = 830, 263
                bool1 = True
            elif 1118 < mx < 1387 and 178 < my < 577:
                FRAME_NUM = 4
                check1.x, check1.y = 1130, 263
                bool1 = True
            elif 1432 < mx < 1697 and 178 < my < 577:
                FRAME_NUM = 5
                check1.x, check1.y = 1440, 263
                bool1 = True
        # check2
        if bool2 == False:
            if 605 < mx < 814 and 752 < my < 964:
                PEOPLE_NUM = 2
                check2.x, check2.y = 610,724
                bool2 = True
            elif 1104 < mx < 1316 and 753 < my < 963:
                PEOPLE_NUM = 4
                check2.x, check2.y = 1100,724
                bool2 = True
        if bool1: check1.show()
        if bool2: check2.show()
        if bool1 and bool2:
            SN = 3
            #pygame.time.delay(500)
    elif SN==3:
        slide3.show()
        pygame.time.delay(3000)
        SN = 4

    elif SN==4:
        # opencv로 이미지 찍게 하자 이거는 pygame 이용
        slide4.show()
        img = webcam.get_image()
        img = pygame.transform.flip(img, True, False)
        # draw frame
        screen.blit(pygame.transform.scale(img, (640*1.8, 480*1.8)), (381, 190))
        # screen.blit(overlay, (258, 178))
        pygame.display.flip()
        # grab next frame

pygame.quit()
