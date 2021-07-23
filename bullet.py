import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Klasa do zarządzania pociskami"""

    def __init__(self, ai_game):
        """Utworzenie obiektu pocisku w aktualnym położeniu statku"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Utworzenie prostokąta pocisku w punkcie (0,0), a następnie zdefiniowaniedla niego odpowiedniego położenia
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Położenie pocisku zdefiniowane za pomocą wartości zmiennoprzecinkowej
        self.y = float(self.rect.y)
