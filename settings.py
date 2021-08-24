class Settings:
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczące statku
        self.ship_speed = 1.5

        # Ustawienia dotyczące pocisków
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Ustawienia dotyczące obcego
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction wynoszące 1 oznacza ruch w prawo, a -1 w lewo
        self.fleet_direction = 1