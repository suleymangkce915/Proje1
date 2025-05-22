import pygame
import random


pygame.init()


SIYAH = (0, 0, 0)
YESIL = (0, 255, 0)
KIRMIZI = (255, 0, 0)
BEYAZ = (255, 255, 255)


genislik = 600
yukseklik = 400
ekran = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Yılan Oyunu")


saat = pygame.time.Clock()
hiz = 8  


blok_boyutu = 20
font = pygame.font.SysFont(None, 35)


def skor_goster(skor):
    yazi = font.render("Skor: " + str(skor), True, BEYAZ)
    ekran.blit(yazi, (10, 10))


def yilan_ciz(blok_boyutu, yilan_listesi):
    for x in yilan_listesi:
        pygame.draw.rect(ekran, YESIL, [x[0], x[1], blok_boyutu, blok_boyutu])


def oyun():
    oyun_durum = True
    oyun_bitti = False

    x = genislik / 2
    y = yukseklik / 2

    x_degisim = 0
    y_degisim = 0

    yilan_listesi = []
    yilan_uzunluk = 1

    
    yem_x = round(random.randrange(0, genislik - blok_boyutu) / 20.0) * 20.0
    yem_y = round(random.randrange(0, yukseklik - blok_boyutu) / 20.0) * 20.0

    while oyun_durum:

        while oyun_bitti:
            ekran.fill(SIYAH)
            yazi = font.render("Oyun Bitti! 1 = Restart, Q = Çık", True, KIRMIZI)
            ekran.blit(yazi, (genislik / 6, yukseklik / 3))
            skor_goster(yilan_uzunluk - 1)
            pygame.display.update()

            for etkinlik in pygame.event.get():
                if etkinlik.type == pygame.KEYDOWN:
                    if etkinlik.key == pygame.K_q:
                        oyun_durum = False
                        oyun_bitti = False
                    if etkinlik.key == pygame.K_r:
                        oyun()

        for etkinlik in pygame.event.get():
            if etkinlik.type == pygame.QUIT:
                oyun_durum = False
            if etkinlik.type == pygame.KEYDOWN:
                if etkinlik.key == pygame.K_LEFT:
                    x_degisim = -blok_boyutu
                    y_degisim = 0
                elif etkinlik.key == pygame.K_RIGHT:
                    x_degisim = blok_boyutu
                    y_degisim = 0
                elif etkinlik.key == pygame.K_UP:
                    y_degisim = -blok_boyutu
                    x_degisim = 0
                elif etkinlik.key == pygame.K_DOWN:
                    y_degisim = blok_boyutu
                    x_degisim = 0

        x += x_degisim
        y += y_degisim

        
        if x >= genislik or x < 0 or y >= yukseklik or y < 0:
            oyun_bitti = True

        ekran.fill(SIYAH)
        pygame.draw.rect(ekran, KIRMIZI, [yem_x, yem_y, blok_boyutu, blok_boyutu])

        yilan_bas = []
        yilan_bas.append(x)
        yilan_bas.append(y)
        yilan_listesi.append(yilan_bas)

        if len(yilan_listesi) > yilan_uzunluk:
            del yilan_listesi[0]

        
        for segment in yilan_listesi[:-1]:
            if segment == yilan_bas:
                oyun_bitti = True

        yilan_ciz(blok_boyutu, yilan_listesi)
        skor_goster(yilan_uzunluk - 1)

        pygame.display.update()

        
        if x == yem_x and y == yem_y:
            yem_x = round(random.randrange(0, genislik - blok_boyutu) / 20.0) * 20.0
            yem_y = round(random.randrange(0, yukseklik - blok_boyutu) / 20.0) * 20.0
            yilan_uzunluk += 1

        saat.tick(hiz)

    pygame.quit()
    quit()

oyun()
