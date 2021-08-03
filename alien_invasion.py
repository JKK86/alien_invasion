import sys

import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    """ Ogólna klasa do zarządzania sposobem działania gry"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # Uruchomienie gry w oknie
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Uruchomienie gry w trybie pełnoekranowym
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
        pygame.display.toggle_fullscreen()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Usunięcie pocisków które znajdują się poza ekranem
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            self._update_screen()

    def _check_events(self):
        """Reakcje na zdarzenia generowane przez użytkownika"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def fire_bullet(self):
        """Utworzenie nowego pocisku i wyświetlenie go na ekranie"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Uaktualnianie obrazów na ekranie i przejścia do nowego ekranu"""
        # Wypełnienie tła utworzonym kolorem
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Wyświetlanie ostatnio zmodyfikowanego ekranu
        pygame.display.flip()


if __name__ == '__main__':
    # Utworzenie egemplarza gry i jej uruchomienie
    ai = AlienInvasion()
    ai.run_game()
