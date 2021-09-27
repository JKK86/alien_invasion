class GameStats:
    """Monitorowanie danych statystycznych w grze"""

    def __init__(self, ai_game):
        """Inicjalizacja danych statystycznych"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Uruchomienie gry w stanie nieaktywnym
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Inicjalizacja danych statystycznych zmieniających się w czasie gry"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
