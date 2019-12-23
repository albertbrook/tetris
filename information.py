import pygame


class Information(object):
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.data = None
        self.reset_data()
        self.score = None
        self.high_score = 0
        self.legend = [
            [[1, 1], [1, 1]],
            [[1, 1, 1, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1, 0]],
            [[0, 1, 0], [1, 1, 1]],
            [[1, 0, 0], [1, 1, 1]],
            [[0, 0, 1], [1, 1, 1]]
        ]
        self.legend_score = None
        self.reset_info()

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
        for z in range(len(self.legend)):
            for i in range(len(self.legend[z])):
                for j in range(len(self.legend[z][i])):
                    if self.legend[z][i][j]:
                        pygame.draw.rect(self.screen, self.settings.split_line_color,
                                         ((11 + j / 2) * self.settings.block_size + self.settings.split_line_size,
                                          (9.5 + z / 2 * (3 if z != 1 else 3.5) + i / 2) * self.settings.block_size,
                                          self.settings.block_size / 2, self.settings.block_size / 2))
        info_list = ["score", str(self.score), "high score", str(self.high_score)]
        for score in self.legend_score:
            info_list.append(str(score))
        info_list_len = len(info_list) - len(self.legend_score)
        for i in range(len(info_list)):
            self.draw_text(info_list[i], i, info_list_len if i >= info_list_len else False)

    def draw_text(self, text, y, move):
        font_image = self.font.render(text, True, self.settings.split_line_color)
        font_rect = font_image.get_rect()
        font_rect.x = 12.5 * self.settings.block_size + self.settings.split_line_size - font_rect.width / 2
        font_rect.y = (5.5 + y) * self.settings.block_size - font_rect.height / 2
        if move:
            font_rect.x += 1.5 * self.settings.block_size
            font_rect.y += (y - move + 1) * self.settings.block_size / 2
        self.screen.blit(font_image, font_rect)

    def reset_data(self):
        self.data = [[0] * 4 for _ in range(4)]

    def reset_info(self):
        self.score = 0
        self.legend_score = [0] * len(self.legend)
