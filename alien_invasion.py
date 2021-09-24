import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
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

        # Utworzenie egzemplarza danych statystycznych dotyczących gry
        self.stats = GameStats(self)

        self.scoreboard = Scoreboard(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Utworzenie przycisku Gra
        self.play_button = Button(self, "Gra")


    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Rozpoczęcie nowej gry po kliknięciu przez użytkownika przycisku Gra"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

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
        elif event.key == pygame.K_g and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        # Wyzerowanie ustawień dotyczących gry
        self.stats.reset_stats()
        self.settings.initialize_dynamic_settings()
        self.stats.game_active = True
        # Usunięcie zawartości list aliens i bullets
        self.aliens.empty()
        self.bullets.empty()
        # Utworzenie nowej floty i wyśrodkowanie statku
        self._create_fleet()
        self.ship.center_ship()
        # Ukrycie kursora myszy
        pygame.mouse.set_visible(False)

    def _ship_hit(self):
        """Reakcja na uderzenie obcego w statek"""
        if self.stats.ships_left > 0:
            # Zmniejszenie liczby pozostałych do wykorzystania statków
            self.stats.ships_left -= 1

            # Usunięcie pozostałych obcych i pocisków
            self.aliens.empty()
            self.bullets.empty()

            # Utworzenie nowej floty i wyśrodkowanie statku
            self._create_fleet()
            self.ship.center_ship()

            # Wstrzymanie czasu
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom_screen(self):
        """Sprawdzenie czy obcy dotarł do dolnej krawędzi ekranu"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def fire_bullet(self):
        """Utworzenie nowego pocisku i wyświetlenie go na ekranie"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych"""
        self.bullets.update()
        # Usunięcie pocisków które znajdują się poza ekranem
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Reakcja na kolizję między pociskiem a obcym"""
        # Sprawdzanie kolizji pocisków i obcych
        # W przypadku trafienia usuwane są zarówno pocisk jak i obcy
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Pozbycie się istniejących pocisków, przyśpieszenie gry i odtworzenie floty obcych
            self.bullets.empty()
            self.settings.increase_speed()
            self._create_fleet()

    def _update_aliens(self):
        """Sprawdzanie czy flota obcych znajduje się przy krawędzi ekranu i uaktualnienie położenia obcych"""
        self._check_fleet_edges()
        self.aliens.update()

        # Wykrywanie kolizji między statkiem a obcym
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Wykrywanie obcych docierających do dolnej krawędzi ekranu
        self._check_aliens_bottom_screen()

    def _create_fleet(self):
        """Utworzenie floty obcych"""
        # Utworzenie obcego i obliczenie liczby obcych, którzy zmieszczą się w jednym rzędzie
        # Odległość między obcymi przyjęto równą szerokości obcego
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        # Obliczenie liczby rzędów obcych mieszczących się na ekranie
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - 3 * alien_height - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # Utworzenie floty obcych
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Utworzenie obcego i umieszczenie go w rzędzie"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Reakcja na dotarcie obcego do krawędzi ekranu"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Przesunięcie całej floty obcych w dół i zmiana jej kierunku"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Uaktualnianie obrazów na ekranie i przejścia do nowego ekranu"""
        # Wypełnienie tła utworzonym kolorem
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Wyświetlanie punktacji
        self.scoreboard.show_score()

        # Wyświetlanie przycisku uruchamiającego grę, wtedy gdy jest nieaktywna
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Wyświetlanie ostatnio zmodyfikowanego ekranu
        pygame.display.flip()


if __name__ == '__main__':
    # Utworzenie egemplarza gry i jej uruchomienie
    ai = AlienInvasion()
    ai.run_game()
