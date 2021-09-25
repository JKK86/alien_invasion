import pygame.font


class Scoreboard:
    """Klasa przeznaczona do przedstawianie informacji o punktacji"""
    def __init__(self, ai_game):
        """Inicjalizacja atrybutów dotyczących punktacji"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Ustawienia czcionki dla informacji dotyczącej punktacji
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Przygotowanie początkowch obrazów z punktacją
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Wyświetlanie punktacji w prawym górnym rogu ekranu
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Przekształcenie najlepszego wyniku w grze na wygenerowany obraz"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Wyświetlanie najlepszego wyniku na środku, przy górnej krawędzi ekranu
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Wyświetlanie punktacji na ekranie"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
