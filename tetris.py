import pygame
import random

pygame.init()

# Oyun ekranı ayarları
genislik = 300  # 10 blok
yukseklik = 600  # 20 blok
blok_boyutu = 30

ekran = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Tetris")

# Renkler
RENKLER = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# Taş şekilleri
SEKILLER = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0],
     [1, 1, 1]],     # J
    [[0, 0, 1],
     [1, 1, 1]],     # L
    [[1, 1],
     [1, 1]],        # O
    [[0, 1, 1],
     [1, 1, 0]],     # S
    [[0, 1, 0],
     [1, 1, 1]],     # T
    [[1, 1, 0],
     [0, 1, 1]]      # Z
]

# Taş sınıfı
class TetrisTasi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sekil = random.choice(SEKILLER)
        self.renk = RENKLER[SEKILLER.index(self.sekil)]

    def döndür(self):
        self.sekil = [list(row) for row in zip(*self.sekil[::-1])]

# Oyun tahtası
def tablo_olustur():
    return [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

def cizim(ekran, tablo):
    ekran.fill((0, 0, 0))
    for y in range(len(tablo)):
        for x in range(len(tablo[y])):
            pygame.draw.rect(ekran, tablo[y][x],
                             (x * blok_boyutu, y * blok_boyutu, blok_boyutu, blok_boyutu), 0)

def sekil_ciz(ekran, sekil):
    for i, satir in enumerate(sekil.sekil):
        for j, deger in enumerate(satir):
            if deger:
                pygame.draw.rect(ekran, sekil.renk,
                                 ((sekil.x + j) * blok_boyutu, (sekil.y + i) * blok_boyutu, blok_boyutu, blok_boyutu), 0)

# Ana oyun fonksiyonu
def oyun():
    saat = pygame.time.Clock()
    tablo = tablo_olustur()
    sekil = TetrisTasi(3, 0)
    düsme_zamani = 0
    hiz = 500  # ms

    calisiyor = True
    while calisiyor:
        düsme_zamani += saat.get_rawtime()
        saat.tick()

        for etkinlik in pygame.event.get():
            if etkinlik.type == pygame.QUIT:
                calisiyor = False
            elif etkinlik.type == pygame.KEYDOWN:
                if etkinlik.key == pygame.K_LEFT:
                    sekil.x -= 1
                elif etkinlik.key == pygame.K_RIGHT:
                    sekil.x += 1
                elif etkinlik.key == pygame.K_UP:
                    sekil.döndür()
                elif etkinlik.key == pygame.K_DOWN:
                    sekil.y += 1

        if düsme_zamani > hiz:
            sekil.y += 1
            düsme_zamani = 0

        # Çizim
        cizim(ekran, tablo)
        sekil_ciz(ekran, sekil)
        pygame.display.update()

    pygame.quit()

def oyun():
    saat = pygame.time.Clock()
    tablo = tablo_olustur()
    sekil = TetrisTasi(3, 0)
    sonraki_sekil = TetrisTasi(3, 0)
    düsme_zamani = 0
    hiz = 500  # ms

    def geçerli_hamle(sekil, tablo):
        for i, satir in enumerate(sekil.sekil):
            for j, deger in enumerate(satir):
                if deger:
                    x = sekil.x + j
                    y = sekil.y + i
                    if x < 0 or x >= 10 or y >= 20:
                        return False
                    if y >= 0 and tablo[y][x] != (0, 0, 0):
                        return False
        return True

    def sabitle(sekil, tablo):
        for i, satir in enumerate(sekil.sekil):
            for j, deger in enumerate(satir):
                if deger:
                    x = sekil.x + j
                    y = sekil.y + i
                    if y >= 0:
                        tablo[y][x] = sekil.renk

    def satir_temizle(tablo):
        yeni_tablo = [satir for satir in tablo if any(kare == (0, 0, 0) for kare in satir)]
        silinen_satir_sayisi = 20 - len(yeni_tablo)
        for _ in range(silinen_satir_sayisi):
            yeni_tablo.insert(0, [(0, 0, 0) for _ in range(10)])
        return yeni_tablo

    calisiyor = True
    while calisiyor:
        düsme_zamani += saat.get_rawtime()
        saat.tick()

        for etkinlik in pygame.event.get():
            if etkinlik.type == pygame.QUIT:
                calisiyor = False
            elif etkinlik.type == pygame.KEYDOWN:
                eski_x = sekil.x
                eski_y = sekil.y
                eski_sekil = sekil.sekil

                if etkinlik.key == pygame.K_LEFT:
                    sekil.x -= 1
                elif etkinlik.key == pygame.K_RIGHT:
                    sekil.x += 1
                elif etkinlik.key == pygame.K_DOWN:
                    sekil.y += 1
                elif etkinlik.key == pygame.K_UP:
                    sekil.döndür()

                if not geçerli_hamle(sekil, tablo):
                    sekil.x = eski_x
                    sekil.y = eski_y
                    sekil.sekil = eski_sekil

        if düsme_zamani > hiz:
            sekil.y += 1
            if not geçerli_hamle(sekil, tablo):
                sekil.y -= 1
                sabitle(sekil, tablo)
                tablo = satir_temizle(tablo)
                sekil = sonraki_sekil
                sonraki_sekil = TetrisTasi(3, 0)
                if not geçerli_hamle(sekil, tablo):
                    print("Oyun Bitti!")
                    calisiyor = False
            düsme_zamani = 0

        # Çizim
        cizim(ekran, tablo)
        sekil_ciz(ekran, sekil)
        pygame.display.update()

    pygame.quit()

oyun()
