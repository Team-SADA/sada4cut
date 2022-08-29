import pygame

# initialize game
pygame.init()

# screen option setting
size = [1600,900]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('사다네컷')

# game setting
clock = pygame.time.Clock()

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sx = 0
        self.sy = 0
    def put_img(self,img_path):
        if img_path[-3:] == 'png':
            self.img = pygame.image.load(img_path).convert_alpha()
        else:
            self.img = pygame.image.load(img_path)
        self.sx, self.sy = self.img.get_size()
    def change_size(self,sx,sy):
        self.img = pygame.transform.scale(self.img,(sx,sy))
        self.sx,self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img,(self.x,self.y))

# test object
test = obj()
test.put_img('gui_imgs/test.jpg')
test.change_size(200,200)
test.x,test.y = 0,0

# phhot1 object
img1 = obj()
img1.put_img('gui_imgs/test.jpg')
img1.x,img1.y = 500,0

# main event
SB = 0

while SB == 0:
    # FPS setting
    clock.tick(1)
    #screen.fill((255, 255, 255))

    # update
    pygame.display.flip()

    # sense inputs()
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            SB = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx,my)

    test.show()
    pygame.display.flip()
pygame.quit()