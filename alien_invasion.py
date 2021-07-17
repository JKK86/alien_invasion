import sys

import pygame

from settings import Settings


class AlienInvasion:
    """ Ogólna klasa do zarządzania sposobem działania gry"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Wypełnienie tła utworzonym kolorem
            self.screen.fill(self.settings.bg_color)

            # Wyświetlanie ostatnio zmodyfikowanego ekranu
            pygame.display.flip()


if __name__ == '__main__':
    # Utworzenie egemplarza gry i jej uruchomienie
    ai = AlienInvasion()
    ai.run_game()
