import pygame


class Ship:
    def __init__(self, ai_game):
        """Inicjalizacja statku i jego położenie początkowe"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytywanie obrazu statku i przypisanie jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Określenie początkowej lokalizacji statku
        self.rect.midbottom = self.screen_rect.midbottom

        # Położenie poziome statku w postaci liczby zmiennoprzecinkowej
        self.x = float(self.rect.x)

        # Opcje wskazujące na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Uaktualnienie położenia statku na podstawie opcji wskazującej na jego ruch"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Uaktualnienie obiektu rect
        self.rect.x = self.x

    def blitme(self):
        """Wyświetlanie statku kosmicznego"""
        self.screen.blit(self.image, self.rect)
