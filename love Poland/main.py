import pygame
from objekty import obekt
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((1280, 720))
Icon = pygame.image.load('Icon_cow.jpg')
pygame.display.set_icon(Icon)
pygame.display.set_caption("Cow walk")
Polish_Right = [pygame.image.load('polish cow_right.png'), pygame.image.load('polish cow_right2.png')]
Polish_Left = [pygame.image.load('polish cow_left.png'), pygame.image.load('polish cow_left2.png')]
BG = pygame.image.load('BG.jpg')
BG2 = pygame.image.load('BG_lvl2.jpg')
BG3 = pygame.image.load('BG_lvl3.jpg')
BG4 = pygame.image.load('BG_Milk.jpg')
Dead = pygame.image.load('prohra.png')
Shot = [pygame.image.load('PVZ_shot1.png'), pygame.image.load('PVZ_shot2.png'), pygame.image.load('PVZ_shot3.png'), pygame.image.load('PVZ_shot4.png')]
Plot1 = obekt(180, 60, 500, 520, True, pygame.image.load('Plot.png'))
Plot2 = obekt(180, 60, 1300, 520, True, pygame.image.load('Plot.png'))
Plot3 = obekt(180, 60, 1360, 520, True, pygame.image.load('Plot.png'))
Zem1 = obekt(64, 384, 850, 450, False, pygame.image.load('zem.jpg'))
Zem2 = obekt(64, 384, 1600, 450, False, pygame.image.load('zem.jpg'))
Zem3 = obekt(64, 384, 1984, 450, False, pygame.image.load('zem.jpg'))
Boom1 = obekt(64, 64, 2270, 390, False, pygame.image.load('PVZ.png'))
Boom2 = obekt(64, 64, 2400, 390, False, pygame.image.load('PVZ_Right.png'))
Boom3 = obekt(64, 64, 3400, 390, False, pygame.image.load('PVZ.png'))
Klic = obekt(64, 64, 2200, 396, False, pygame.image.load('Klíč.png'))
Zem4 = obekt(384, 64, 2340, 50, False, pygame.image.load('Zem2.jpg'))
Zem5 = obekt(64, 384, 2368, 450, False, pygame.image.load('zem.jpg'))
Zem6 = obekt(64, 384, 3050, 450, False, pygame.image.load('zem.jpg'))
Zem7 = obekt(384, 64, 3200, 450, False, pygame.image.load('Zem2.jpg'))
Zem1_lvl2 = obekt(64, 384, 750, 565, False, pygame.image.load('zem.jpg'))
Zem2_lvl2 = obekt(64, 384, 2550, 565, False, pygame.image.load('zem.jpg'))
Zem3_lvl2 = obekt(64, 384, 3500, 565, False, pygame.image.load('zem.jpg'))
Plot1_lvl2 = obekt(180, 60, 2712, 385, True, pygame.image.load('Plot.png'))
Boom1_lvl2 = obekt(64, 64, 3500, 511, False, pygame.image.load('PVZ.png'))
Dvere = obekt(200, 80, 2340, 514, False, pygame.image.load('Dveře_zavřené.png'))
Zem1_lvl3 = obekt(64, 384, 600, 450, False, pygame.image.load('zem.jpg'))
Zem2_lvl3 = obekt(64, 384, 984, 450, False, pygame.image.load('zem.jpg'))
Zem3_lvl3 = obekt(64, 384, 1368, 450, False, pygame.image.load('zem.jpg'))
Zem4_lvl3 = obekt(384, 64, 1650, 50, False, pygame.image.load('Zem2.jpg'))
Zem5_lvl3 = obekt(64, 384, 1850, 450, False, pygame.image.load('zem.jpg'))
Zem6_lvl3 = obekt(64, 384, 2234, 450, False, pygame.image.load('zem.jpg'))
Zem7_lvl3 = obekt(64, 384, 2900, 450, False, pygame.image.load('zem.jpg'))
tlacitko = obekt(16, 64, 1560, 434, pygame.image.load('čudlik_2.png'), pygame.image.load('čudlik_1.png'))
tlacitko2 = obekt(16, 64, 1950, 434, pygame.image.load('čudlik_2.png'), pygame.image.load('čudlik_1.png'))
Boom1_lvl3 = obekt(64, 64, 1500, 390, False, pygame.image.load('PVZ.png'))
Vlk1 = obekt(64, 120, 1000, 620, True, pygame.image.load('Vlk_prava.png'))
Vlk = [pygame.image.load('Vlk_leva.png'), pygame.image.load('Vlk_prava.png'), pygame.image.load('Vlk_ded.png')]
Past = obekt(384, 64, 1780, 50, False, pygame.image.load('Past.png'))
Kamen = obekt(64,64, 1780, 50, True, pygame.image.load('šutr.png'))
Plot1_lvl3 = obekt(180, 60, 800, 280, True, pygame.image.load('Plot.png'))
Milk = obekt(300, 150, 3500, 390, pygame.image.load('Milk_ded.png'), pygame.image.load('Milk.png'))
Menu = [pygame.image.load('Menu_01.jpg'), pygame.image.load('Menu_02.jpg'), pygame.image.load('Menu_lvl_2.jpg'),
        pygame.image.load('Menu_LVL_2_2.jpg'), pygame.image.load('Menu_lvl_2_3.jpg'), pygame.image.load('Menu_lvl_3_1.jpg'),
        pygame.image.load('Menu_lvl_3_2.jpg'), pygame.image.load('Menu_lvl_3_3.jpg'), pygame.image.load('Menu_lvl_3_4.jpg')]

music = pygame.mixer.music.load('Polish Cow.mp3')
Otevrene_Dvere = pygame.image.load('Dveře_otevřené.jpg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
Fly = False
Prohra = False
Cow_Vysoko = 12
Cow_Jump = False
Cow_Fall = False
Go_Right = True
Go_Left = False
BG_x = 0
Cow_Timer = 0
Cow_Dance1 = True
Cow_Dance2 = False
Cow_x = 150
Cow_y = 640
On_Fall = False
Fall = 0
Klic_take = False
Spin = 0
B1 = True
B2 = False
B3 = False
B4 = False
Shot_delka = 0
Shot_Tam = True
Shot_Zpadky = False
Menu_timer = 0
Menu_timer_Nahoru = True
Menu_timer_Dolu = False
No_jump = False
zem1_lvl2_rychlost = 3
zem1_lvl_prava = True
zem1_lvl_leva = False
vlk_leva = True
tlacitko_push = False
Vlk_ded = False
Zem1_fake = False
Zem2_fake = False
Milk_ded = False

Lvl1 = False
Lvl2_unlock = False
Lvl2 = False
Lvl3_unlock = False
Lvl3 = False
Menu_lvl = 0

#menu
def menu():
    if Menu_timer_Nahoru:
        if Lvl3_unlock:
            win.blit(Menu[5], (0, 0))
        elif Lvl2_unlock:
            win.blit(Menu[2], (0, 0))
        else:
            win.blit(Menu[0], (0, 0))
    elif Menu_timer_Dolu:
        if Lvl3_unlock:
            if Menu_lvl == 2:
                win.blit(Menu[6], (0, 0))
            elif Menu_lvl == 1:
                win.blit(Menu[7], (0, 0))
            else:
                win.blit(Menu[8], (0, 0))

        elif Lvl2_unlock:
            if Menu_lvl == 1:
                win.blit(Menu[3], (0, 0))
            else:
                win.blit(Menu[4], (0, 0))
        else:
           win.blit(Menu[1], (0, 0))


#pozadí
def BACK():
    win.blit(BG, (BG_x, 0))

#Cow
def COW():
    if Go_Right:
        if Cow_Dance1:
            win.blit(Polish_Right[0], (Cow_x, Cow_y))
        elif Cow_Dance2:
            win.blit(Polish_Right[1], (Cow_x, Cow_y))
    elif Go_Left:
        if Cow_Dance1:
            win.blit(Polish_Left[0], (Cow_x, Cow_y))
        elif Cow_Dance2:
            win.blit(Polish_Left[1], (Cow_x, Cow_y))
def objekty():
    win.blit(Plot1.obraz, (Plot1.x + BG_x, Plot1.y))
    win.blit(Plot2.obraz, (Plot2.x + BG_x, Plot2.y))
    win.blit(Plot3.obraz, (Plot3.x + BG_x, Plot3.y))
    win.blit(Zem1.obraz, (Zem1.x + BG_x, Zem1.y))
    win.blit(Zem2.obraz, (Zem2.x + BG_x, Zem2.y))
    win.blit(Zem3.obraz, (Zem3.x + BG_x, Zem3.y))
    win.blit(Zem4.obraz, (Zem4.x + BG_x, Zem4.y))
    win.blit(Zem5.obraz, (Zem5.x + BG_x, Zem5.y))
    win.blit(Zem6.obraz, (Zem6.x + BG_x, Zem6.y))
    win.blit(Zem7.obraz, (Zem7.x + BG_x, Zem7.y))
    win.blit(Boom1.obraz, (Boom1.x + BG_x, Boom1.y))
    win.blit(Boom2.obraz, (Boom2.x + BG_x, Boom2.y))
    win.blit(Boom3.obraz, (Boom3.x + BG_x, Boom3.y))
    if Klic_take:
        win.blit(Otevrene_Dvere, (Dvere.x + BG_x, Dvere.y))
    else:
        win.blit(Dvere.obraz, (Dvere.x + BG_x, Dvere.y))
    if B1:
        win.blit(Shot[0], (Boom1.x + BG_x - Shot_delka, Boom1.y))
    elif B2:
        win.blit(Shot[1], (Boom1.x + BG_x - Shot_delka, Boom1.y))
    elif B3:
        win.blit(Shot[2], (Boom1.x + BG_x - Shot_delka, Boom1.y))
    elif B4:
        win.blit(Shot[3], (Boom1.x + BG_x - Shot_delka, Boom1.y))

    if B1:
        win.blit(Shot[0], (Boom2.x + BG_x + Shot_delka, Boom2.y))
    elif B2:
        win.blit(Shot[1], (Boom2.x + BG_x + Shot_delka, Boom2.y))
    elif B3:
        win.blit(Shot[2], (Boom2.x + BG_x + Shot_delka, Boom2.y))
    elif B4:
        win.blit(Shot[3], (Boom2.x + BG_x + Shot_delka, Boom2.y))

    if B1:
        win.blit(Shot[0], (Boom3.x + BG_x - Shot_delka, Boom3.y))
    elif B2:
        win.blit(Shot[1], (Boom3.x + BG_x - Shot_delka, Boom3.y))
    elif B3:
        win.blit(Shot[2], (Boom3.x + BG_x - Shot_delka, Boom3.y))
    elif B4:
        win.blit(Shot[3], (Boom3.x + BG_x - Shot_delka, Boom3.y))

    if not Klic_take:
        win.blit(Klic.obraz, (Klic.x + BG_x, Klic.y))

#smrt
def smrt():
    win.blit(Dead, (0, 0))

#Lvl2
def BACK2():
    win.blit(BG2, (BG_x, 0))
def obekty2():
    win.blit(Zem1_lvl2.obraz, (Zem1_lvl2.x + BG_x, Zem1_lvl2.y))
    win.blit(Zem2_lvl2.obraz, (Zem2_lvl2.x + BG_x, Zem2_lvl2.y))
    win.blit(Zem3_lvl2.obraz, (Zem3_lvl2.x + BG_x, Zem3_lvl2.y))
    win.blit(Plot1_lvl2.obraz, (Plot1_lvl2.x + BG_x, Plot1_lvl2.y))
    win.blit(Boom1_lvl2.obraz, (Boom1_lvl2.x + BG_x, Boom1_lvl2.y))

    if B1:
        win.blit(Shot[0], (Boom1_lvl2.x + BG_x - Shot_delka, Boom1_lvl2.y))
    elif B2:
        win.blit(Shot[1], (Boom1_lvl2.x + BG_x - Shot_delka, Boom1_lvl2.y))
    elif B3:
        win.blit(Shot[2], (Boom1_lvl2.x + BG_x - Shot_delka, Boom1_lvl2.y))
    elif B4:
        win.blit(Shot[3], (Boom1_lvl2.x + BG_x - Shot_delka, Boom1_lvl2.y))

#lvl3
def obekty3():
    if not Vlk_ded:
        if vlk_leva:
            win.blit(Vlk[0], (Vlk1.x + BG_x, Vlk1.y))
        else:
            win.blit(Vlk[1], (Vlk1.x + BG_x, Vlk1.y))
    else:
        win.blit(Vlk[2], (Vlk1.x + BG_x, Vlk1.y))
    win.blit(Zem1_lvl3.obraz, (Zem1_lvl3.x + BG_x, Zem1_lvl3.y))
    if not Zem1_fake:
        win.blit(Zem2_lvl3.obraz, (Zem2_lvl3.x + BG_x, Zem2_lvl3.y))
    if not Zem2_fake:
        win.blit(Zem7_lvl3.obraz, (Zem7_lvl3.x + BG_x, Zem7_lvl3.y))
    win.blit(Zem3_lvl3.obraz, (Zem3_lvl3.x + BG_x, Zem3_lvl3.y))
    win.blit(Zem4_lvl3.obraz, (Zem4_lvl3.x + BG_x, Zem4_lvl3.y))
    win.blit(Zem5_lvl3.obraz, (Zem5_lvl3.x + BG_x, Zem5_lvl3.y))
    win.blit(Zem6_lvl3.obraz, (Zem6_lvl3.x + BG_x, Zem6_lvl3.y))
    win.blit(Boom1_lvl3.obraz, (Boom1_lvl3.x + BG_x, Boom1_lvl3.y))
    win.blit(Plot1_lvl3.obraz, (Plot1_lvl3.x + BG_x, Plot1_lvl3.y))
    win.blit(Past.obraz, (Past.x + BG_x, Past.y))
    win.blit(Kamen.obraz, (Kamen.x + BG_x, Kamen.y))
    if B1:
        win.blit(Shot[0], (Boom1_lvl3.x + BG_x - Shot_delka, Boom1_lvl3.y))
    elif B2:
        win.blit(Shot[1], (Boom1_lvl3.x + BG_x - Shot_delka, Boom1_lvl3.y))
    elif B3:
        win.blit(Shot[2], (Boom1_lvl3.x + BG_x - Shot_delka, Boom1_lvl3.y))
    elif B4:
        win.blit(Shot[3], (Boom1_lvl3.x + BG_x - Shot_delka, Boom1_lvl3.y))
    if not tlacitko_push:
        win.blit(tlacitko.obraz, (tlacitko.x + BG_x, tlacitko.y))
    else:
        win.blit(tlacitko.killing, (tlacitko.x + BG_x, tlacitko.y))
    if not Milk_ded:
        win.blit(tlacitko2.obraz, (tlacitko2.x + BG_x, tlacitko2.y))
    else:
        win.blit(tlacitko2.killing, (tlacitko2.x + BG_x, tlacitko2.y))
    if Milk_ded:
        win.blit(Milk.killing, (Milk.x + BG_x - 50, Milk.y + 150))
    else:
        win.blit(Milk.obraz, (Milk.x + BG_x, Milk.y))



#pozadí3
def BACK3():
    if Milk_ded:
        win.blit(BG4, (BG_x, 0))
    else:
        win.blit(BG3, (BG_x, 0))

#main run
run = True
while run:
    pygame.time.delay(20)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not Lvl1 and not Lvl2 and not Lvl3:

        if keys[pygame.K_RIGHT]:
            Menu_lvl += 1
        elif keys[pygame.K_LEFT]:
            Menu_lvl -= 1
        if Lvl3_unlock:
            if Menu_lvl > 2:
                Menu_lvl = 2
        elif Lvl2_unlock:
            if Menu_lvl > 1:
                Menu_lvl = 1
        else:
            if Menu_lvl > 0:
                Menu_lvl = 0

        if Menu_lvl == 0 and keys[pygame.K_SPACE]:
            Lvl1 = True
        elif Menu_lvl == 1 and keys[pygame.K_SPACE]:
            Lvl2 = True
        elif Menu_lvl == 2 and keys[pygame.K_SPACE]:
            Lvl3 = True

        if Menu_timer_Nahoru:
            Menu_timer += 1
            if Menu_timer >= 5:
                Menu_timer_Nahoru = False
                Menu_timer_Dolu = True
        elif Menu_timer_Dolu:
            Menu_timer -= 1
            if Menu_timer <= 0:
                Menu_timer_Nahoru = True
                Menu_timer_Dolu = False
        menu()
        pygame.display.update()
        pygame.time.delay(100)
    if Lvl1:
        if Prohra:
            if keys[pygame.K_z]:
                Fly = False
                Prohra = False
                Cow_Vysoko = 12
                Cow_Jump = False
                Cow_Fall = False
                Go_Right = True
                Go_Left = False
                BG_x = 0
                Cow_Timer = 0
                Cow_Dance1 = True
                Cow_Dance2 = False
                Cow_x = 150
                Cow_y = 640
                On_Fall = False
                Fall = 0
                Klic_take = False
                Spin = 0
                B1 = True
                B2 = False
                B3 = False
                B4 = False
                Shot_delka = 0
                Shot_Tam = True
                Shot_Zpadky = False
        else:

# bomerank otocky
            if B1:
                Spin += 1
                if Spin == 9:
                    B1 = False
                    B2 = True
            elif B2:
                Spin += 1
                if Spin == 19:
                    B2 = False
                    B3 = True
            elif B3:
                Spin += 1
                if Spin == 29:
                    B3 = False
                    B4 = True
            elif B4:
                Spin += 1
                if Spin == 39:
                    B4 = False
                    B1 = True
                    Spin = 0

            if Shot_Tam:
                Shot_delka += 15
                if Shot_delka >= 720:
                    Shot_Zpadky = True
                    Shot_Tam = False
            elif Shot_Zpadky:
                Shot_delka -= 15
                if Shot_delka <= 0:
                    Shot_Tam = True
                    Shot_Zpadky = False



# Cow_Dance
            if Cow_Dance1:
                if Cow_Timer >= 35:
                    Cow_Dance1 = False
                    Cow_Dance2 = True
                else:
                    Cow_Timer += 1
            elif Cow_Dance2:
                if Cow_Timer <= 0:
                    Cow_Dance1 = True
                    Cow_Dance2 = False
                else:
                    Cow_Timer -= 1
#Cow_Movemant
            if BG_x > -4096:
                if keys[pygame.K_d]:
                    BG_x -= 5
                    Go_Right = True
                    Go_Left = False
            if BG_x < 0:
                if keys[pygame.K_a]:
                    BG_x += 5
                    Go_Left = True
                    Go_Right = False
#Cow_Jump
            if Cow_Fall and not No_jump:
                Cow_Vysoko += 0.25
                Cow_y += Cow_Vysoko
                if Cow_Vysoko == 12:
                    Cow_Fall = False
            elif not Cow_Jump:
                if keys[pygame.K_w]:
                    Cow_Jump = True
            elif Cow_Jump:
                Cow_y -= Cow_Vysoko
                Cow_Vysoko -= 0.25
                if Cow_Vysoko == 0:
                    Cow_Jump = False
                    Cow_Fall = True

            if Cow_Fall:
                Fly = True
                Cow_Vysoko += 0.25
                Cow_y += Cow_Vysoko
                if Cow_y >= 640:
                    Cow_y = 640
                    Cow_Vysoko = 12
                    Cow_Fall = False


            if Cow_y > 640:
                Cow_y = 640

            if Cow_y + 51 >= Plot1.y and Cow_x + 60 >= Plot1.x + BG_x and Cow_y >= Plot1.y - Plot1.Vyska and Cow_x - BG_x <= Plot1.x + Plot1.Sirka:
                Prohra = True
            if Cow_y + 51 >= Plot2.y and Cow_x + 60 >= Plot2.x + BG_x and Cow_y >= Plot2.y - Plot2.Vyska and Cow_x - BG_x <= Plot2.x + Plot2.Sirka:
                Prohra = True
            if Cow_y + 51 >= Plot3.y and Cow_x + 60 >= Plot3.x + BG_x and Cow_y >= Plot3.y - Plot3.Vyska and Cow_x - BG_x <= Plot3.x + Plot3.Sirka:
                Prohra = True
            if Cow_y + 51 >= Boom1.y and Cow_x +60 >= Boom1.x + BG_x - Shot_delka and Cow_y <= Boom1.y + 16 and Cow_x <= Boom1.x + BG_x - Shot_delka + 16:
                Prohra = True
            if Cow_y + 51 >= Boom2.y and Cow_x +60 >= Boom2.x + BG_x + Shot_delka and Cow_y <= Boom2.y + 16 and Cow_x <= Boom2.x + BG_x + Shot_delka + 16:
                Prohra = True
            if Cow_y + 51 >= Boom3.y and Cow_x + 60 >= Boom3.x + BG_x - Shot_delka and Cow_y <= Boom3.y + 16 and Cow_x <= Boom3.x + BG_x - Shot_delka + 16:
                Prohra = True
#Zem1
            if Cow_x + 60 >= Zem1.x + BG_x and Cow_x - BG_x <= Zem1.x + Zem1.Sirka and Cow_y >= Zem1.y -20 and Cow_y <= Zem1.y + Zem1.Vyska:
                On_Fall = True
                No_jump = True

                Cow_y = Zem1.y + Zem1.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem1.y and Cow_x + 60 >= Zem1.x + BG_x and Cow_y >= Zem1.y - Zem1.Vyska -40 and Cow_x - BG_x <= Zem1.x + Zem1.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
                On_Fall = False

#Zem2
            if Cow_x + 60 >= Zem2.x + BG_x and Cow_x - BG_x <= Zem2.x + Zem2.Sirka and Cow_y >= Zem2.y -20 and Cow_y <= Zem2.y + Zem2.Vyska:
                On_Fall = True
                No_jump = True
                Cow_y = Zem2.y + Zem2.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem2.y and Cow_x + 60 >= Zem2.x + BG_x and Cow_y >= Zem2.y - Zem2.Vyska -40 and Cow_x - BG_x <= Zem2.x + Zem2.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
                On_Fall = False
#Zem3
            if Cow_x + 60 >= Zem3.x + BG_x and Cow_x - BG_x <= Zem3.x + Zem3.Sirka and Cow_y >= Zem3.y -20 and Cow_y <= Zem3.y + Zem3.Vyska:
                On_Fall = True
                No_jump = True
                Cow_y = Zem3.y + Zem3.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem3.y and Cow_x + 60 >= Zem3.x + BG_x and Cow_y >= Zem3.y - Zem3.Vyska -40 and Cow_x - BG_x <= Zem3.x + Zem3.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
                On_Fall = False
#Zem4
            if Cow_y <= Zem4.y + Zem4.Vyska and Cow_x + 40 >= Zem4.x + BG_x and Cow_x <= Zem4.x + BG_x + Zem4.Sirka - 30:
                BG_x += 20
            if Cow_y <= Zem4.y + Zem4.Vyska and Cow_x >= Zem4.x +40 + BG_x and Cow_x <= Zem4.x + BG_x + Zem4.Sirka:
                BG_x -= 20
#zem5
            if Cow_x + 60 >= Zem5.x + BG_x and Cow_x - BG_x <= Zem5.x + Zem5.Sirka and Cow_y >= Zem5.y -20 and Cow_y <= Zem5.y + Zem5.Vyska:
                On_Fall = True
                No_jump = True
                Cow_y = Zem5.y + Zem5.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem5.y and Cow_x + 60 >= Zem5.x + BG_x and Cow_y >= Zem5.y - Zem5.Vyska -40 and Cow_x - BG_x <= Zem5.x + Zem5.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
                On_Fall = False
#Zem6
            if Cow_x + 60 >= Zem6.x + BG_x and Cow_x - BG_x <= Zem6.x + Zem6.Sirka and Cow_y >= Zem6.y -20 and Cow_y <= Zem6.y + Zem6.Vyska:
                On_Fall = True
                No_jump = True
                Cow_y = Zem6.y + Zem6.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem6.y and Cow_x + 60 >= Zem6.x + BG_x and Cow_y >= Zem6.y - Zem6.Vyska -40 and Cow_x - BG_x <= Zem6.x + Zem6.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
                On_Fall = False
#Zem7
            if Cow_y >= Zem7.y and Cow_x + 40 >= Zem7.x + BG_x and Cow_x <= Zem7.x + BG_x + Zem7.Sirka - 30:
                BG_x += 20
            if Cow_y >= Zem7.y and Cow_x >= Zem7.x +40 + BG_x and Cow_x <= Zem7.x + BG_x + Zem7.Sirka:
                BG_x -= 20


#Dvere
            if not Klic_take:
                if Cow_y <= Dvere.y + Dvere.Vyska and Cow_x + 40 >= Dvere.x + BG_x and Cow_x <= Dvere.x + BG_x + Dvere.Sirka - 30:
                    BG_x += 20



#zpadnutí
            if Fly:
                if Cow_x + 60 <= Zem1.x + BG_x or Cow_x - BG_x >= Zem1.x + Zem1.Sirka and Cow_x + 60 <= Zem2.x + BG_x or Cow_x - BG_x >= Zem2.x + Zem2.Sirka and Cow_x + 60 <= Zem3.x + BG_x or Cow_x - BG_x >= Zem3.x + Zem3.Sirka and Cow_x + 60 <= Zem5.x + BG_x or Cow_x - BG_x >= Zem5.x + Zem5.Sirka and Cow_x + 60 <= Zem6.x + BG_x or Cow_x - BG_x >= Zem6.x + Zem6.Sirka:
                    On_Fall = True
                    Fly = False
            if Cow_y > 550 and not Cow_Jump:
                On_Fall = True
                Fly = False
#pád
            if On_Fall:
                Cow_y += Fall
                if keys[pygame.K_w] and not No_jump:
                    On_Fall = False
                if Cow_y >= 640:
                    Fall = 0
                    On_Fall = False
                    No_jump = False
                    Cow_y = 640
                else:
                    Fall += 1

            if not Klic_take:
                if Cow_x + 60 >= Klic.x + BG_x and Cow_x - BG_x <= Klic.x + Klic.Sirka and Cow_y >= Klic.y -20 and Cow_y <= Klic.y + Klic.Vyska:
                    Klic_take = True


            if BG_x <= -3850:
                Lvl2_unlock = True
                Lvl1 = False
                Fly = False
                Prohra = False
                Cow_Vysoko = 12
                Cow_Jump = False
                Cow_Fall = False
                Go_Right = True
                Go_Left = False
                BG_x = 0
                Cow_Timer = 0
                Cow_Dance1 = True
                Cow_Dance2 = False
                Cow_x = 150
                Cow_y = 640
                On_Fall = False
                Fall = 0
                Klic_take = False
                Spin = 0
                B1 = True
                B2 = False
                B3 = False
                B4 = False
                Shot_delka = 0
                Shot_Tam = True
                Shot_Zpadky = False


        BACK()
        objekty()
        COW()
        if Prohra:
            smrt()
        pygame.display.update()


    elif Lvl2:
        if Prohra:
            smrt()
            if keys[pygame.K_z]:
                Fly = False
                Prohra = False
                Cow_Vysoko = 12
                Cow_Jump = False
                Cow_Fall = False
                Go_Right = True
                Go_Left = False
                BG_x = 0
                Cow_Timer = 0
                Cow_Dance1 = True
                Cow_Dance2 = False
                Cow_x = 150
                Cow_y = 640
                On_Fall = False
                Fall = 0
                Klic_take = False
                Spin = 0
                B1 = True
                B2 = False
                B3 = False
                B4 = False
                Shot_delka = 0
                Shot_Tam = True
                Shot_Zpadky = False






        else:
# bomerank otocky
            if B1:
                Spin += 1
                if Spin == 9:
                    B1 = False
                    B2 = True
            elif B2:
                Spin += 1
                if Spin == 19:
                    B2 = False
                    B3 = True
            elif B3:
                Spin += 1
                if Spin == 29:
                    B3 = False
                    B4 = True
            elif B4:
                Spin += 1
                if Spin == 39:
                    B4 = False
                    B1 = True
                    Spin = 0

            if Shot_Tam:
                Shot_delka += 15
                if Shot_delka >= 2500:
                    Shot_Zpadky = True
                    Shot_Tam = False
            elif Shot_Zpadky:
                Shot_delka -= 15
                if Shot_delka <= 0:
                    Shot_Tam = True
                    Shot_Zpadky = False

# Cow_Dance
            if Cow_Dance1:
                if Cow_Timer >= 35:
                    Cow_Dance1 = False
                    Cow_Dance2 = True
                else:
                    Cow_Timer += 1
            elif Cow_Dance2:
                if Cow_Timer <= 0:
                    Cow_Dance1 = True
                    Cow_Dance2 = False
                else:
                    Cow_Timer -= 1
# Cow_Movemant
            if BG_x > -4096:
                if keys[pygame.K_d]:
                    BG_x -= 5
                    Go_Right = True
                    Go_Left = False
            if BG_x < 0:
                if keys[pygame.K_a]:
                    BG_x += 5
                    Go_Left = True
                    Go_Right = False
# Cow_Jump
            if Cow_Fall and not No_jump:
                Cow_Vysoko += 0.25
                Cow_y += Cow_Vysoko
                if Cow_Vysoko == 12:
                    Cow_Fall = False
            elif not Cow_Jump:
                if keys[pygame.K_w]:
                    Cow_Jump = True
            elif Cow_Jump:
                Cow_y -= Cow_Vysoko
                Cow_Vysoko -= 0.25
                if Cow_Vysoko == 0:
                    Cow_Jump = False
                    Cow_Fall = True

            if Cow_Fall:
                Fly = True
                Cow_Vysoko += 0.25
                Cow_y += Cow_Vysoko
                if Cow_y >= 640:
                    Cow_y = 640
                    Cow_Vysoko = 12
                    Cow_Fall = False
# lava
            if Cow_y == 640 and BG_x <= -450 and BG_x >= -2960:
                Prohra = True

            if Cow_y > 640:
                Cow_y = 640

# plot
            if Cow_y + 51 >= Plot1_lvl2.y and Cow_x + 60 >= Plot1_lvl2.x + BG_x and Cow_y >= Plot1_lvl2.y - Plot1_lvl2.Vyska and Cow_x - BG_x <= Plot1_lvl2.x + Plot1_lvl2.Sirka:
                Prohra = True
# boom
            if Cow_y + 51 >= Boom1_lvl2.y and Cow_x +60 >= Boom1_lvl2.x + BG_x - Shot_delka and Cow_y <= Boom1_lvl2.y + 16 and Cow_x <= Boom1_lvl2.x + BG_x - Shot_delka + 16:
                Prohra = True

# Zem_lvl2 move

            if Zem1_lvl2.x <= 750:
                zem1_lvl_prava = True
                zem1_lvl_leva = False
            elif Zem1_lvl2.x >= 1420:
                zem1_lvl_prava = False
                zem1_lvl_leva = True
            if zem1_lvl_prava:
                Zem1_lvl2.x += zem1_lvl2_rychlost
                Zem2_lvl2.x -= zem1_lvl2_rychlost
                Plot1_lvl2.x -= zem1_lvl2_rychlost
            elif zem1_lvl_leva:
                Zem1_lvl2.x -= zem1_lvl2_rychlost
                Zem2_lvl2.x += zem1_lvl2_rychlost
                Plot1_lvl2.x += zem1_lvl2_rychlost


# Zem1_lvl2
            if Cow_x + 60 >= Zem1_lvl2.x + BG_x and Cow_x - BG_x <= Zem1_lvl2.x + Zem1_lvl2.Sirka and Cow_y >= Zem1_lvl2.y - 20 and Cow_y <= Zem1_lvl2.y + Zem1_lvl2.Vyska:
                On_Fall = True
                No_jump = True

                Cow_y = Zem1_lvl2.y + Zem1_lvl2.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem1_lvl2.y and Cow_x + 60 >= Zem1_lvl2.x + BG_x and Cow_y >= Zem1_lvl2.y - Zem1_lvl2.Vyska - 40 and Cow_x - BG_x <= Zem1_lvl2.x + Zem1_lvl2.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
                On_Fall = False


# Zem2_lvl2
            if Cow_x + 60 >= Zem2_lvl2.x + BG_x and Cow_x - BG_x <= Zem2_lvl2.x + Zem2_lvl2.Sirka and Cow_y >= Zem2_lvl2.y - 20 and Cow_y <= Zem2_lvl2.y + Zem2_lvl2.Vyska:
                On_Fall = True
                No_jump = True

                Cow_y = Zem2_lvl2.y + Zem2_lvl2.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem2_lvl2.y and Cow_x + 60 >= Zem2_lvl2.x + BG_x and Cow_y >= Zem2_lvl2.y - Zem2_lvl2.Vyska - 40 and Cow_x - BG_x <= Zem2_lvl2.x + Zem2_lvl2.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
                On_Fall = False
# Zem3_lvl2
            if Cow_x + 60 >= Zem3_lvl2.x + BG_x and Cow_x - BG_x <= Zem3_lvl2.x + Zem3_lvl2.Sirka and Cow_y >= Zem3_lvl2.y - 20 and Cow_y <= Zem3_lvl2.y + Zem3_lvl2.Vyska:
                On_Fall = True
                No_jump = True

                Cow_y = Zem3_lvl2.y + Zem3_lvl2.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem3_lvl2.y and Cow_x + 60 >= Zem3_lvl2.x + BG_x and Cow_y >= Zem3_lvl2.y - Zem3_lvl2.Vyska - 40 and Cow_x - BG_x <= Zem3_lvl2.x + Zem3_lvl2.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
                On_Fall = False


            if Fly:
                if Cow_x + 60 <= Zem1_lvl2.x + BG_x or Cow_x - BG_x >= Zem1_lvl2.x + Zem1_lvl2.Sirka and Cow_x + 60 <= Zem2_lvl2.x + BG_x or Cow_x - BG_x >= Zem2_lvl2.x + Zem2_lvl2.Sirka and Cow_x + 60 <= Zem3_lvl2.x + BG_x or Cow_x - BG_x >= Zem3_lvl2.x + Zem3_lvl2.Sirka:
                    On_Fall = True
                    Fly = False
            if Cow_y > 550 and not Cow_Jump:
                On_Fall = True
                Fly = False

            if On_Fall:
                Cow_y += Fall
                if keys[pygame.K_w] and not No_jump:
                    On_Fall = False
                if Cow_y >= 640:
                    Fall = 0
                    On_Fall = False
                    No_jump = False
                    Cow_y = 640
                else:
                    Fall += 1
            if BG_x <= -3900:
                Lvl3_unlock = True
                Fly = False
                Prohra = False
                Cow_Vysoko = 12
                Cow_Jump = False
                Cow_Fall = False
                Go_Right = True
                Go_Left = False
                BG_x = 0
                Cow_Timer = 0
                Cow_Dance1 = True
                Cow_Dance2 = False
                Cow_x = 150
                Cow_y = 640
                On_Fall = False
                Fall = 0
                Klic_take = False
                Spin = 0
                B1 = True
                B2 = False
                B3 = False
                B4 = False
                Shot_delka = 0
                Shot_Tam = True
                Shot_Zpadky = False
                Menu_timer = 0
                Menu_timer_Nahoru = True
                Menu_timer_Dolu = False
                No_jump = False
                zem1_lvl2_rychlost = 3
                zem1_lvl_prava = True
                zem1_lvl_leva = False
                Lvl2 = False


        BACK2()
        COW()
        obekty2()
        if Prohra:
            smrt()
        pygame.display.update()
    if Lvl3:
        if Prohra:
            smrt()
            if keys[pygame.K_z]:
                Fly = False
                Prohra = False
                Cow_Vysoko = 12
                Cow_Jump = False
                Cow_Fall = False
                Go_Right = True
                Go_Left = False
                BG_x = 0
                Cow_Timer = 0
                Cow_Dance1 = True
                Cow_Dance2 = False
                Cow_x = 150
                Cow_y = 640
                On_Fall = False
                Fall = 0
                Klic_take = False
                Spin = 0
                B1 = True
                B2 = False
                B3 = False
                B4 = False
                Shot_delka = 0
                Shot_Tam = True
                Shot_Zpadky = False
                Menu_timer = 0
                Menu_timer_Nahoru = True
                Menu_timer_Dolu = False
                No_jump = False
                zem1_lvl2_rychlost = 3
                zem1_lvl_prava = True
                zem1_lvl_leva = False
                vlk_leva = True
                tlacitko_push = False
                Vlk_ded = False
                Kamen.y = 50
                Kamen.x = 1780
                Vlk1.x = 1000
                Zem1_fake = False

        else:
# bomerank otocky
            if B1:
                Spin += 1
                if Spin == 9:
                    B1 = False
                    B2 = True
            elif B2:
                Spin += 1
                if Spin == 19:
                    B2 = False
                    B3 = True
            elif B3:
                Spin += 1
                if Spin == 29:
                    B3 = False
                    B4 = True
            elif B4:
                Spin += 1
                if Spin == 39:
                    B4 = False
                    B1 = True
                    Spin = 0

            if Shot_Tam:
                Shot_delka += 15
                if Shot_delka >= 900:
                    Shot_Zpadky = True
                    Shot_Tam = False
            elif Shot_Zpadky:
                Shot_delka -= 15
                if Shot_delka <= 0:
                    Shot_Tam = True
                    Shot_Zpadky = False

# Cow_Dance
            if Cow_Dance1:
                if Cow_Timer >= 35:
                    Cow_Dance1 = False
                    Cow_Dance2 = True
                else:
                    Cow_Timer += 1
            elif Cow_Dance2:
                if Cow_Timer <= 0:
                    Cow_Dance1 = True
                    Cow_Dance2 = False
                else:
                    Cow_Timer -= 1
# Cow_Movemant
            if BG_x > -4096:
                if keys[pygame.K_d]:
                    BG_x -= 5
                    Go_Right = True
                    Go_Left = False
            if BG_x < 0:
                if keys[pygame.K_a]:
                    BG_x += 5
                    Go_Left = True
                    Go_Right = False
# Cow_Jump
            if Cow_Fall and not No_jump:
                Cow_Vysoko += 0.25
                Cow_y += Cow_Vysoko
                if Cow_Vysoko == 12:
                    Cow_Fall = False
            elif not Cow_Jump:
                if keys[pygame.K_w]:
                    Cow_Jump = True
            elif Cow_Jump:
                Cow_y -= Cow_Vysoko
                Cow_Vysoko -= 0.25
                if Cow_Vysoko == 0:
                    Cow_Jump = False
                    Cow_Fall = True

            if Cow_Fall:
                Fly = True
                Cow_Vysoko += 0.25
                Cow_y += Cow_Vysoko
                if Cow_y >= 640:
                    Cow_y = 640
                    Cow_Vysoko = 12
                    Cow_Fall = False

#kamen
            if tlacitko_push:
                if Kamen.y <= 640:
                    Kamen.y += 10
                else:
                    Kamen.x -= 10
# lava

            if Cow_y == 640 and BG_x <= -2500 and BG_x >= -3300 and not Milk_ded:
                Prohra = True

# vlk
            if Vlk1.y + 51 >= Kamen.y and Vlk1.x + 60 >= Kamen.x and Vlk1.y >= Kamen.y - Kamen.Vyska and Vlk1.x <= Kamen.x + Kamen.Sirka:
                Vlk_ded = True
            if not Vlk_ded:
                if Cow_x - BG_x <= Vlk1.x:
                    Vlk1.x -= 6
                    vlk_leva = True
                else:
                    Vlk1.x += 6
                    vlk_leva = False

                if Cow_y + 51 >= Vlk1.y and Cow_x + 60 >= Vlk1.x + BG_x and Cow_y >= Vlk1.y - Vlk1.Vyska and Cow_x - BG_x <= Vlk1.x + Vlk1.Sirka:
                    Prohra = True


            if Cow_y + 51 >= Kamen.y and Cow_x + 60 >= Kamen.x + BG_x and Cow_y >= Kamen.y - Kamen.Vyska and Cow_x - BG_x <= Kamen.x + Kamen.Sirka:
                Prohra = True

# tlacitko
            if Cow_y + 51 >= tlacitko.y and Cow_x + 60 >= tlacitko.x + BG_x and Cow_y <= tlacitko.y + tlacitko.Vyska and Cow_x <= tlacitko.x + BG_x + tlacitko.Sirka:
                tlacitko_push = True
#tlacitko2
            if Cow_y + 51 >= tlacitko2.y and Cow_x + 60 >= tlacitko2.x + BG_x and Cow_y <= tlacitko2.y + tlacitko2.Vyska and Cow_x <= tlacitko2.x + BG_x + tlacitko2.Sirka:
                Milk_ded= True
# boom
            if Cow_y + 51 >= Boom1_lvl3.y and Cow_x +60 >= Boom1_lvl3.x + BG_x - Shot_delka and Cow_y <= Boom1_lvl3.y + 16 and Cow_x <= Boom1_lvl3.x + BG_x - Shot_delka + 16:
                Prohra = True
            if Cow_y + 51 >= Plot1_lvl3.y and Cow_x + 60 >= Plot1_lvl3.x + BG_x and Cow_y >= Plot1_lvl3.y - Plot1_lvl3.Vyska and Cow_x - BG_x <= Plot1_lvl3.x + Plot1_lvl3.Sirka:
                Prohra = True

# zem1_lvl3
            if Cow_x + 60 >= Zem1_lvl3.x + BG_x and Cow_x - BG_x <= Zem1_lvl3.x + Zem1_lvl3.Sirka and Cow_y >= Zem1_lvl3.y -20 and Cow_y <= Zem1_lvl3.y + Zem1_lvl3.Vyska:
                On_Fall = True
                No_jump = True

                Cow_y = Zem1_lvl3.y + Zem1_lvl3.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem1_lvl3.y and Cow_x + 60 >= Zem1_lvl3.x + BG_x and Cow_y >= Zem1_lvl3.y - Zem1_lvl3.Vyska -40 and Cow_x - BG_x <= Zem1_lvl3.x + Zem1_lvl3.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
                On_Fall = False
# zem2_lvl3
            if Cow_x + 60 >= Zem2_lvl3.x + BG_x and Cow_x - BG_x <= Zem2_lvl3.x + Zem2_lvl3.Sirka and Cow_y >= Zem2_lvl3.y -20 and Cow_y <= Zem2_lvl3.y + Zem2_lvl3.Vyska:
                Zem1_fake = True

            if Cow_Fall and Cow_y + 50 >= Zem2_lvl3.y and Cow_x + 60 >= Zem2_lvl3.x + BG_x and Cow_y >= Zem2_lvl3.y - Zem2_lvl3.Vyska -40 and Cow_x - BG_x <= Zem2_lvl3.x + Zem2_lvl3.Sirka:
                On_Fall = True
                No_jump = True
# Zem3_lvl3
            if Cow_x + 60 >= Zem3_lvl3.x + BG_x and Cow_x - BG_x <= Zem3_lvl3.x + Zem3_lvl3.Sirka and Cow_y >= Zem3_lvl3.y -20 and Cow_y <= Zem3_lvl3.y + Zem3_lvl3.Vyska:
                On_Fall = True
                No_jump = True

                Cow_y = Zem3_lvl3.y + Zem3_lvl3.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem3_lvl3.y and Cow_x + 60 >= Zem3_lvl3.x + BG_x and Cow_y >= Zem3_lvl3.y - Zem3_lvl3.Vyska -40 and Cow_x - BG_x <= Zem3_lvl3.x + Zem3_lvl3.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
                On_Fall = False
# Zem4_lvl3
            if Cow_y <= Zem4_lvl3.y + Zem4_lvl3.Vyska and Cow_x + 40 >= Zem4_lvl3.x + BG_x and Cow_x <= Zem4_lvl3.x + BG_x + Zem4_lvl3.Sirka - 30:
                BG_x += 20
            if Cow_y <= Zem4_lvl3.y + Zem4_lvl3.Vyska and Cow_x >= Zem4_lvl3.x +40 + BG_x and Cow_x <= Zem4_lvl3.x + BG_x + Zem4_lvl3.Sirka:
                BG_x -= 20
#Zem5_lvl3
            if Cow_x + 60 >= Zem5_lvl3.x + BG_x and Cow_x - BG_x <= Zem5_lvl3.x + Zem5_lvl3.Sirka and Cow_y >= Zem5_lvl3.y - 20 and Cow_y <= Zem5_lvl3.y + Zem5_lvl3.Vyska:
                On_Fall = True
                No_jump = True

                Cow_y = Zem5_lvl3.y + Zem5_lvl3.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem5_lvl3.y and Cow_x + 60 >= Zem5_lvl3.x + BG_x and Cow_y >= Zem5_lvl3.y - Zem5_lvl3.Vyska - 40 and Cow_x - BG_x <= Zem5_lvl3.x + Zem5_lvl3.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
                On_Fall = False
# Zem6_lvl3
            if Cow_x + 60 >= Zem6_lvl3.x + BG_x and Cow_x - BG_x <= Zem6_lvl3.x + Zem6_lvl3.Sirka and Cow_y >= Zem6_lvl3.y -20 and Cow_y <= Zem6_lvl3.y + Zem6_lvl3.Vyska:
                On_Fall = True
                No_jump = True

                Cow_y = Zem6_lvl3.y + Zem6_lvl3.Vyska

            if Cow_Fall and Cow_y + 50 >= Zem6_lvl3.y and Cow_x + 60 >= Zem6_lvl3.x + BG_x and Cow_y >= Zem6_lvl3.y - Zem6_lvl3.Vyska -40 and Cow_x - BG_x <= Zem6_lvl3.x + Zem6_lvl3.Sirka:
                Cow_Vysoko = 12
                Cow_Fall = False
                Fly = True
# zem7_lvl3
                if Cow_x + 60 >= Zem7_lvl3.x + BG_x and Cow_x - BG_x <= Zem7_lvl3.x + Zem7_lvl3.Sirka and Cow_y >= Zem7_lvl3.y - 20 and Cow_y <= Zem7_lvl3.y + Zem7_lvl3.Vyska:
                    Zem2_fake = True

                if Cow_Fall and Cow_y + 50 >= Zem7_lvl3.y and Cow_x + 60 >= Zem7_lvl3.x + BG_x and Cow_y >= Zem7_lvl3.y - Zem7_lvl3.Vyska - 40 and Cow_x - BG_x <= Zem7_lvl3.x + Zem7_lvl3.Sirka:
                    On_Fall = True
                    No_jump = True

            if Fly:
                if Cow_x + 60 <= Zem1_lvl3.x + BG_x or Cow_x - BG_x >= Zem1_lvl3.x + Zem1_lvl3.Sirka and Cow_x + 60 <= Zem3_lvl3.x + BG_x or Cow_x - BG_x >= Zem3_lvl3.x + Zem3_lvl3.Sirka and Cow_x + 60 <= Zem5_lvl3.x + BG_x or Cow_x - BG_x >= Zem5_lvl3.x + Zem5_lvl3.Sirka and Cow_x + 60 <= Zem6_lvl3.x + BG_x or Cow_x - BG_x >= Zem6_lvl3.x + Zem6_lvl3.Sirka:
                    On_Fall = True
                    Fly = False
            if Cow_y > 550 and not Cow_Jump:
                On_Fall = True
                Fly = False

            if On_Fall:
                Cow_y += Fall
                if keys[pygame.K_w] and not No_jump:
                    On_Fall = False
                if Cow_y >= 640:
                    Fall = 0
                    On_Fall = False
                    No_jump = False
                    Cow_y = 640
                else:
                    Fall += 1
            if BG_x <= -3900:
                Fly = False
                Prohra = False
                Cow_Vysoko = 12
                Cow_Jump = False
                Cow_Fall = False
                Go_Right = True
                Go_Left = False
                BG_x = 0
                Cow_Timer = 0
                Cow_Dance1 = True
                Cow_Dance2 = False
                Cow_x = 150
                Cow_y = 640
                On_Fall = False
                Fall = 0
                Klic_take = False
                Spin = 0
                B1 = True
                B2 = False
                B3 = False
                B4 = False
                Shot_delka = 0
                Shot_Tam = True
                Shot_Zpadky = False
                Menu_timer = 0
                Menu_timer_Nahoru = True
                Menu_timer_Dolu = False
                No_jump = False
                zem1_lvl2_rychlost = 3
                zem1_lvl_prava = True
                zem1_lvl_leva = False
                vlk_leva = True
                tlacitko_push = False
                Vlk_ded = False
                Kamen.y = 50
                Kamen.x = 1780
                Vlk1.x = 1000
                Lvl3 = False


            BACK3()
            obekty3()
            COW()
            if Prohra:
                smrt()
            pygame.display.update()
