import pygame


class Ship:
    def __init__(self, ai_game):
        """Inicjalizacja statku i jego położenie początkowe"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytywanie obrazu statku i przypisanie jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Określenie początkowej lokalizacji statku
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Wyświetlanie statku kosmicznego"""
        self.screen.blit(self.image, self.rect)
