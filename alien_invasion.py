import sys

import pygame


class AlienInvasion:
    """ Ogólna klasa do zarządzania sposobem działania gry"""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (106, 90, 205)

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Wypełnienie tła utworzonym kolorem
            self.screen.fill(self.bg_color)

            # Wyświetlanie ostatnio zmodyfikowanego ekranu
            pygame.display.flip()


if __name__ == '__main__':
    # Utworzenie egemplarza gry i jej uruchomienie
    ai = AlienInvasion()
    ai.run_game()
