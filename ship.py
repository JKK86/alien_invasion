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

        # Opcje wskazujące na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Uaktualnienie położenia statku na podstawie opcji wskazującej na jego ruch"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Wyświetlanie statku kosmicznego"""
        self.screen.blit(self.image, self.rect)
