import random
import sys
import os

import pygame as pg

main_dir = os.path.split(os.path.abspath(__file__))[0]

class Screen:
    def __init__(self, title, wh, img_path):
        # 練習１
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path) 
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 

    
class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path) #"fig/6.png"
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio) #2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy #900, 400


    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)


class Brids:
    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio) #2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)



class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):

        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        self.color = color
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy
        
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) 
        
    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) 


class Shield:
    def __init__(self, color, x, y, hw, scr:Screen):
        self.sfc = pg.Surface((hw+50, hw+50))
        pg.draw.rect(self.sfc, color, (x, y, hw, hw))
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) 


    
def load_sound(file):
    """because pygame can be be compiled without mixer."""
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()

    # 練習１
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg" )

    if pg.mixer:
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    hogo = Shield("green", 300, 300, 100, scr)
    hogo.blit(scr)

    # 練習３
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    kkt_friend = Bird("fig/8.png", 1.0, (1400, 100))
    kkt_friend.blit(scr)
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    kkt.update(scr)



    # 練習５
    bkd_lst = []
    colors = ["red", "green", "blue", "yellow", "magenta"]
    for i in range(0, 10):
        color = colors[i%5]
        vx = random.choice([-1, +1])
        vy = random.choice([-1, +1])
        bkd = Bomb(color, 10, (vx, vy), scr)
        bkd_lst.append(bkd)

    
    #bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    #bkd.update(scr)

    # 練習２
    while True:
        scr.blit()   # scrn_sfc.blit(pgbg_sfc, pgbg_rct) 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        hogo.blit(scr)
        kkt.update(scr)
        kkt.blit(scr)
        for i in range(10):
            bkd_lst[i].update(scr)    
            if kkt.rct.colliderect(bkd_lst[i].rct):
                if kkt.rct in hogo.rct:
                    pass
                else:
                    return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
