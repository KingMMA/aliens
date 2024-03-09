import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Клас для управління снарядами, якими стріляє корабель"""

    def __init__(self, ai_game):
        """Створює об'єкт снаряду в поточній позиції корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Створюємо снаряд в позиції (0, 0) і призначаємо правильну позицію
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиція снаряду зберішається у float
        self.y = float(self.rect.y)
        self.shoot_channel = pygame.mixer.Channel(self.settings.music_channel["shoot"])
        self.shoot_sound = pygame.mixer.Sound(self.settings.music_path["shoot"])

    def update(self):
        """Переміщує снаряд угору по екрану"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Виводе снаряд на екран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
