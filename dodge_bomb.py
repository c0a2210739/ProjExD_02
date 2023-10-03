import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900


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
    kk_dic = {pg.K_UP:(0,-5),pg.K_DOWN:(0,5),pg.K_LEFT:(-5,0),pg.K_RIGHT:(5,0)}
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
        kk_rct.move_ip(sum_mv[0],sum_mv[1])
        screen.blit(kk_img, kk_rct)
        screen.blit(enn,bc_rct)
        bc_rct.move_ip(vx,vy)        
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()