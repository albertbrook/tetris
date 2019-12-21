import pygame


class Information(object):
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.data = None
        self.score = 0
        self.high_score = 0
        self.reset_data()

        self.font = pygame.font.SysFont(None, self.settings.font_size)

    def draw(self):
        pygame.draw.line(self.screen, self.settings.split_line_color,
                         (10 * self.settings.block_size + self.settings.split_line_size // 2, 0),
                         (10 * self.settings.block_size + self.settings.split_line_size // 2,
                          20 * self.settings.block_size),
                         self.settings.split_line_size)
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j]:
                    pygame.draw.rect(self.screen, self.data[i][j],
                                     ((11 + j) * self.settings.block_size + self.settings.split_line_size,
                                      (1 + i) * self.settings.block_size,
                                      self.settings.block_size, self.settings.block_size))
        self.draw_text("score", 0)
        self.draw_text(str(self.score), 1)
        self.draw_text("high score", 2)
        self.draw_text(str(self.high_score), 3)

    def draw_text(self, text, y):
        font_image = self.font.render(text, True, self.settings.split_line_color)
        font_rect = font_image.get_rect()
        font_rect.x = 12.5 * self.settings.block_size + self.settings.split_line_size - font_rect.width / 2
        font_rect.y = (6.5 + y) * self.settings.block_size - font_rect.height / 2
        self.screen.blit(font_image, font_rect)

    def reset_data(self):
        self.data = [[0] * 4 for _ in range(4)]
