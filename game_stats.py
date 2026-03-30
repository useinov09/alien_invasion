import json

class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""
    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False

        # Рекорд не должен сбрасываться.
        try:
            with open('record.json') as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0
        except json.decoder.JSONDecodeError:
            self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1