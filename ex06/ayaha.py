import pygame as pg
import sys
import time, random


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

    color_red = pg.Color(255, 0, 0)
    color_white = pg.Color(255, 255, 255)
    color_green = pg.Color(0, 255, 0)
    color_yello = pg.Color(255, 212, 0)
    scrn_sfc = pg.display.set_mode((600, 400))
    scrn_rct = scrn_sfc.get_rect()
    scrn_sfc.fill(color_white)
    pg.display.set_caption("蛇")
    arr = [([0] * 41) for i in range(61)]  
    x = 10  # 蛇の初期x座標
    y = 10  # 蛇の初期y座標
    foodx = random.randint(1, 60)  # 食べ物のx座標
    foody = random.randint(1, 40)  # 食べ物のy座標
    arr[foodx][foody] = -1
    snake_lon = 3  # 蛇の長さ
    way = 1  # 蛇の運動方向

    tekix = random.randint(1, 60)  # 敵のx座標
    tekiy = random.randint(1, 40)  # 敵のy座標
    arr[tekix][tekiy] = -2

    teki_sfc = pg.Surface((10, 10)) # 正方形の空のSurface
    pg.draw.rect(teki_sfc, color_yello, (0, 0, 10, 10))
    teki_rct = teki_sfc.get_rect()
    teki_rct.centerx = tekix*10
    teki_rct.centery = tekiy*10

    xy = [+3,-3, 0]        #敵の移動と方向    
    vx = random.choice(xy)
    vy = random.choice(xy)

    font = pg.font.Font(None, 30) #スコアの文字列
    scor = 0 #スコアの初期値

    st = time.time()



    while True:
        scrn_sfc.fill(color_white)
        text = font.render(f"Score {scor}", True, (0,0,0))   # 描画する文字列の設定
        scrn_sfc.blit(text, [20, 1])# 文字列の表示位置

        ed = time.time()
        gt = ed-st
        
        time.sleep(0.1)
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN:
                if (event.key == pg.K_RIGHT) and (way != 2):  # 右
                    way = 1
                if (event.key == pg.K_LEFT) and (way != 1):  # 左
                    way = 2
                if (event.key == pg.K_UP) and (way != 4):  # 上
                    way = 3
                if (event.key == pg.K_DOWN) and (way != 3):  # 下に移動
                    way = 4
        if way == 1:
            x += 1
        if way == 2:
            x -= 1
        if way == 3:
            y -= 1
        if way == 4:
            y += 1
        if (x > 60) or (y > 40) or (x < 1) or (y < 1) or (arr[x][y] > 0):  # 死亡(壁、自分の体をぶつかったら)
            font1 = pg.font.Font(None, 100) 
            text1 = font1.render("Game Over!", True, color_red)
            text2 = font1.render(f"Score {scor}", True, color_red)   # 描画する文字列の設定
            scrn_sfc.blit(text1, [100, 100])# 文字列の表示位置
            scrn_sfc.blit(text2, [150, 200])
        
            
        arr[x][y] = snake_lon
        for a, b in enumerate(arr, 1):
            for c, d in enumerate(b, 1):
                # 食べ物は-1，空地は0，蛇の位置は正数
                if (d > 0):
                    # print(a,c) #蛇の座標を表示
                    arr[a - 1][c - 1] = arr[a - 1][c - 1] - 1
                    pg.draw.rect(scrn_sfc, color_green, ((a - 1) * 10, (c - 1) * 10, 10, 10))
                if (d == -1):
                    pg.draw.rect(scrn_sfc, color_red, ((a - 1) * 10, (c - 1) * 10, 10, 10))
                if (d == -2):
                    teki_rct.move_ip(vx, vy)
                    scrn_sfc.blit(teki_sfc, teki_rct)
                    yoko,tate = check_bound(teki_rct, scrn_rct)
                    vx *= yoko
                    vy *= tate
                    
                
        if (x == tekix*10) and (y == tekiy*10): #敵をぶつかったら、ゲームオーバー
            font1 = pg.font.Font(None, 100) 
            text1 = font1.render("Game Over!", True, color_red)
            text2 = font1.render(f"Score {scor}", True, color_red)   # 描画する文字列の設定
            scrn_sfc.blit(text1, [100, 100])# 文字列の表示位置
            scrn_sfc.blit(text2, [150, 200])
        else:
            if (x == foodx) and (y == foody):   #蛇が食べ物を食べったら
                snake_lon += 1    #長さ+1
                while (arr[foodx][foody] != 0):    #新しい食べ物を表示
                    foodx = random.randint(1, 60)
                    foody = random.randint(1, 40)
                arr[foodx][foody] = -1
                scor += 1 #スコアが+1
            if round(gt%5) == 0: #五秒ごと経つと敵動く方向が変わる
                print(gt)
                vx = random.choice(xy)
                vy = random.choice(xy)
                teki_rct.move_ip(vx, vy)
                scrn_sfc.blit(teki_sfc, teki_rct)            

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    
    

      
