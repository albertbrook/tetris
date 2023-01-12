import pygame


class Display(object):
    def __init__(self, settings, screen, information):
        self.settings = settings
        self.screen = screen
        self.information = information

        self.data = None
        self.reset_data()

    def draw(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j]:
                    pygame.draw.rect(self.screen, self.data[i][j],
                                     (j * self.settings.block_size, i * self.settings.block_size,
                                      self.settings.block_size, self.settings.block_size))

    def eliminate(self):
        n = 0
        for i in range(len(self.data)):
            for j in self.data[i]:
                if not j:
                    break
            else:
                n += 1
                self.data[i] = [0] * 10
                for l in range(i, 0, -1):
                    self.data[l], self.data[l - 1] = self.data[l - 1], self.data[l]
        n = 5 if n == 4 else n
        self.information.score += n
        if self.information.score > self.information.high_score:
            self.information.high_score = self.information.score

    def reset_data(self):
        self.data = [[0] * 10 for _ in range(20)]
