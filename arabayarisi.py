import pygame
import random

# Pygame'i başlat
pygame.init()

# Ekran boyutları
genislik = 500
yukseklik = 600
ekran = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Araba Yarışı")

# Renkler
BEYAZ = (255, 255, 255)
SIYAH = (0, 0, 0)
KIRMIZI = (255, 0, 0)

# Araba boyutu
araba_gen = 50
araba_yuk = 80

# Oyuncu arabası
araba = pygame.image.load("araba.png")  # 50x80 boyutlarında bir görsel ekle
araba = pygame.transform.scale(araba, (araba_gen, araba_yuk))
araba_x = genislik // 2 - araba_gen // 2
araba_y = yukseklik - araba_yuk - 10

# Düşman arabaları
dusman_gen = 50
dusman_yuk = 80
dusman_hiz = 5
dusmanlar = []

def dusman_uret():
    x = random.randint(0, genislik - dusman_gen)
    dusmanlar.append([x, -dusman_yuk])

# Saat
saat = pygame.time.Clock()

# Ana döngü
calisiyor = True
puan = 0
while calisiyor:
    saat.tick(60)
    ekran.fill(SIYAH)

    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            calisiyor = False

    # Tuş kontrol
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT] and araba_x > 0:
        araba_x -= 5
    if tuslar[pygame.K_RIGHT] and araba_x < genislik - araba_gen:
        araba_x += 5

    # Düşman üretimi
    if random.randint(1, 20) == 1:
        dusman_uret()

    # Düşman hareketi ve çarpışma kontrolü
    for d in dusmanlar[:]:
        d[1] += dusman_hiz
        pygame.draw.rect(ekran, KIRMIZI, (d[0], d[1], dusman_gen, dusman_yuk))
        if d[1] > yukseklik:
            dusmanlar.remove(d)
            puan += 1
        # Çarpışma
        if (araba_x < d[0] + dusman_gen and araba_x + araba_gen > d[0] and
                araba_y < d[1] + dusman_yuk and araba_y + araba_yuk > d[1]):
            print("Çarpışma! Puan:", puan)
            calisiyor = False

    # Oyuncu arabası
    ekran.blit(araba, (araba_x, araba_y))

    # Puan göster
    font = pygame.font.SysFont(None, 30)
    yazi = font.render("Puan: " + str(puan), True, BEYAZ)
    ekran.blit(yazi, (10, 10))

    pygame.display.flip()

pygame.quit()
