class GameStats:
    """Відслідковування статистики гри"""

    def __init__(self, ai_game):
        """Ініціалізує статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Гра запускається в неактивному стані
        self.game_active = False
        self.game_paused = False
        self.high_score = 0

        with open(self.settings.record_file, "r") as f:
            self.max_score = int(f.read())

    def reset_stats(self):
        """Ініціалізує статистику, що змінюється під час гри"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
