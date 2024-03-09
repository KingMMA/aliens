class Settings:
    """Клас для збереження всін налаштувань гри"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        # Параметри екрану
        self.screen_width = 1200
        self.screen_height = 800
        self.dark_mode = True
        self.bg_color = (0, 0, 0) if self.dark_mode else (230, 230, 230)

        # Параметри корабля
        self.ship_limit = 3

        # Параметри снаряду
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0) if self.dark_mode else (60, 60, 60)
        self.bulets_allowed = 5

        # Параметри прибульців
        self.fleet_drop_speed = 10

        # Параметри зірок
        self.star_limit = 100
        self.star_speed = 0.09
        self.star_start_color = 200
        self.star_color_limit = 256
        self.star_color_step = 0.15
        self.star_radius = 3

        # Темпи прискорення гри
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.music_path = {
            "shoot": "./music/shoot.mp3",
            "background": "./music/background.mp3",
            "kill": "./music/kill.mp3",
            "score": "./music/score.mp3",
        }
        self.music_channel = {"background": 0, "shoot": 1, "kill": 2, "score": 3}
        self.include_background_music = True
        self.record_file = "./config/max_record.txt"
        self.initialyze_dynamic_settings()

    def initialyze_dynamic_settings(self):
        """Ініціалізує налаштування, що змінюються по ходу гри"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        # fleet_direction = 1 якщо флот рухається праворуч, -1 - ліворуч
        self.fleet_direction = 1

        # Підрахунок очок
        self.alien_points = 50

    def increase_speed(self):
        """Збільшує налаштування швидкості"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
