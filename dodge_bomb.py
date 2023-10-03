import sys
import pygame as pg
import random
import math


WIDTH, HEIGHT = 1600, 900

def check_bou(obj_rct):
    """
    引数:こうかとんRect,爆弾Rect
    戻り値：タプル（横方向判定結果，縦方向判定結果）
    画面内ならTrue,画面外ならFalse
    """
    yoko,tate = True,True
    if obj_rct.left <= 0 or WIDTH <= obj_rct.right:
        yoko = False
    if obj_rct.top <= 0 or HEIGHT <= obj_rct.bottom:
        tate = False
    return yoko,tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900,400)  #こうかとん初期座標
    enn = pg.Surface((20,20))
    pg.draw.circle(enn,(255,0,0),(10,10),10)
    enn.set_colorkey((0,0,0))
    ran_x = random.randint(0,1600)
    ran_y = random.randint(0,900)
    bc_rct = enn.get_rect()
    bc_rct.center = ran_x,ran_y
    vx = 5
    vy = 5
    
    clock = pg.time.Clock()
    tmr = 0

    accs = [a for a in range(1, 11)] # 加速度のリスト
    enn_imgs = []
    for r in range(1, 11):
        enn_img = pg.Surface((20*r, 20*r), pg.SRCALPHA)
        pg.draw.circle(enn_img, (255, 0, 0), (10*r, 10*r), 10*r)
        enn_imgs.append(enn_img)

    kk_dic = {
        pg.K_UP:(0,-5),
        pg.K_DOWN:(0,5),
        pg.K_LEFT:(-5,0),
        pg.K_RIGHT:(5,0)
        }
    
    kk2_dic = {
        (0, 5): (pg.transform.flip(kk_img, True, False), -90),
        (5, 5): (pg.transform.flip(kk_img, True, False), -45),
        (5, 0): (pg.transform.flip(kk_img, True, False), 0),
        (5, -5): (pg.transform.flip(kk_img, True, False), 45),
        (0, -5): (pg.transform.flip(kk_img, True, False), 90),
        (-5, 5): (kk_img, 45),
        (-5, -5): (kk_img, -45),
        (-5, 0): (kk_img, 0)
    }

    key_lst = pg.key.get_pressed()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        
        screen.blit(bg_img, [0, 0])

        key_lst = pg.key.get_pressed()
        sum_mv = [0,0]
        for key,mv in kk_dic.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]   #横合計移動量
                sum_mv[1] += mv[1]   #縦   
        #こうかとんの向きを変える
        for kk, mm in kk2_dic.items():
            if sum_mv[0] == kk[0] and sum_mv[1] == kk[1]:
                kk_img= pg.transform.rotozoom(mm[0], mm[1], 1.0)
        screen.blit(kk_img, [kk_rct.x, kk_rct.y])

        kk_rct.move_ip(sum_mv[0],sum_mv[1])

        if check_bou(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])  #元の位置に
        
        
        
        bc_rct.move_ip(vx,vy)
        yoko,tate = check_bou(bc_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        

        enn_img = enn_imgs[min(tmr//500, 9)] # 時間とともに爆弾を拡大
        screen.blit(enn_img, [bc_rct.x, bc_rct.y])
        
        if kk_rct.colliderect(bc_rct):
            print("ゲームオーバー")
            return
        
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()