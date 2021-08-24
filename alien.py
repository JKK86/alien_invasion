import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        """Inicjalizacja statku obcych i jego położenie początkowe"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Wczytywanie obrazu statku obcych i przypisanie jego prostokąta
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Określenie początkowej lokalizacji statku obcych
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Zwraca True jeśli obcy znajduje się przy krawędzi"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Ruch obcego w prawo lub lewo"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
