import pygame as pg
import sys
import random
import time


def check_bound(obj_rct, scr_rct):
    # 第1引数；こうかとんrectまたは爆弾ect
    # 第2引数：スクリーンrect
    # 範囲内：+1/範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock = pg.time.Clock()

    #練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    
    #練習3
    tori_sfc = pg.image.load("fig/4.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    #scrn_sfcにtori_rctに従って,tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct)

    #練習5
    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)
    vx, vy = +1, +1
    st = time.time() # ゲームのスタート時間    


    #練習2
    while True:
        ed = time.time() 
        gt = ed-st # ゲームの経過時間を計る
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習4
        key_dct = pg.key.get_pressed() #　辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            #どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        scrn_sfc.blit(tori_sfc, tori_rct)     

        # 練習8
        if tori_rct.colliderect(bomb_rct) :  # こうかとんと爆弾がぶつかったら
            tori_sfc = pg.image.load("fig/8.png") #泣いているこうかとんに変える
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
            bomb_rct.move_ip(vx, vy)
            scrn_sfc.blit(bomb_sfc, bomb_rct)
            scrn_sfc.blit(tori_sfc, tori_rct)
            vx, vy = 0, 0 # 爆弾の移動が止まる
        else:
            if gt >= 30: # ゲームの経過時間が30秒経ったら
                tori_sfc = pg.image.load("fig/6.png") #楽しいこうかとんに変える
                tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
                bomb_rct.move_ip(vx, vy)
                scrn_sfc.blit(tori_sfc, tori_rct)
                vx, vy = 0, 0 # 爆弾の移動速度が0になる
            if gt >= 35: # 35秒に経ったらゲーム終了
                return
            else:
                bomb_rct.move_ip(vx, vy)
                scrn_sfc.blit(bomb_sfc, bomb_rct)
                yoko, tate = check_bound(bomb_rct, scrn_rct)
                vx *= yoko
                vy *= tate
                if gt%5==0: # 経過時間が五秒ごと経ったら爆弾の移動速度が早くなる
                    vx += 1
                    vy += 1
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
