import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        """Inicjalizacja statku obcych i jego położenie początkowe"""
        super().__init__()
        self.screen = ai_game.screen

        # Wczytywanie obrazu statku obcych i przypisanie jego prostokąta
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Określenie początkowej lokalizacji statku obcych
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)