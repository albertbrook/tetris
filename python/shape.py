import pygame
import random


class Shape(pygame.sprite.Sprite):
    def __init__(self, settings, screen, display, information, flag=True):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.display = display
        self.information = information

        self.flag = flag

        self.data = [
            [[1, 1], [1, 1]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
            [[1, 1, 0], [0, 1, 1], [0, 0, 0]],
            [[0, 1, 1], [1, 1, 0], [0, 0, 0]],
            [[0, 1, 0], [1, 1, 1], [0, 0, 0]],
            [[1, 0, 0], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 1], [1, 1, 1], [0, 0, 0]]
        ]
        self.z = random.randint(0, len(self.data) - 1)
        self.size = None
        self.place = None
        for _ in range(random.randint(1, 4)):
            self.rotate()
        self.x = (self.place[0] - self.size[0] + 10) // 2
        self.y = self.place[1] - self.size[1]
        self.color = tuple([random.randint(0, 255) for _ in range(3)])
        self.display_shape()
        pygame.time.set_timer(pygame.USEREVENT, 500)

    def update(self):
        self.y += 1
        if self.collide():
            self.y -= 1
            self.print_shape()
            return not self.kill()

    def draw(self):
        for i in range(len(self.data[self.z])):
            for j in range(len(self.data[self.z][i])):
                if self.data[self.z][i][j]:
                    pygame.draw.rect(self.screen, self.color,
                                     ((self.x + j) * self.settings.block_size,
                                      (self.y + i) * self.settings.block_size,
                                      self.settings.block_size, self.settings.block_size))

    def rotate(self):
        size = len(self.data[self.z]) - 1
        for i in range((size + 1) // 2):
            for j in range(i, size - i):
                self.exchange([i, j], [size - j, i], [size - i, size - j], [j, size - i])
        self.size = self.get_size()
        self.place = [self.get_x(), self.get_y()]

    def exchange(self, *args):
        for i in range(len(args) - 1):
            (self.data[self.z][args[i][0]][args[i][1]],
             self.data[self.z][args[i + 1][0]][args[i + 1][1]]) = \
                (self.data[self.z][args[i + 1][0]][args[i + 1][1]],
                 self.data[self.z][args[i][0]][args[i][1]])

    def get_size(self):
        width = []
        height = 0
        for i in self.data[self.z]:
            flag = False
            for j in range(len(i)):
                if i[j]:
                    width.append(j)
                    flag = True
            if flag:
                height += 1
        width = len(set(width))
        return width, height

    def get_x(self):
        for x in range(len(self.data[self.z][0])):
            for i in range(len(self.data[self.z])):
                if self.data[self.z][i][x]:
                    return -x

    def get_y(self):
        for y in range(len(self.data[self.z])):
            for i in self.data[self.z][y]:
                if i:
                    return -y

    def move_left(self):
        self.x -= 1
        if self.collide():
            self.x += 1

    def move_right(self):
        self.x += 1
        if self.collide():
            self.x -= 1

    def collide(self):
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                if (not 0 <= self.x - self.place[0] + j <= 9 or self.y - self.place[1] + i > 19 or
                        self.data[self.z][i - self.place[1]][j - self.place[0]] and
                        self.y - self.place[1] + i >= 0 and
                        self.display.data[self.y - self.place[1] + i][self.x - self.place[0] + j]):
                    return True

    def display_shape(self):
        self.information.reset_data()
        for i in range(len(self.data[self.z])):
            for j in range(len(self.data[self.z][i])):
                if self.data[self.z][i][j]:
                    self.information.data[i][j] = self.color
        self.information.legend_score[self.z] += 1

    def print_shape(self):
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                if self.data[self.z][i - self.place[1]][j - self.place[0]] and self.y - self.place[1] + i >= 0:
                    self.display.data[self.y - self.place[1] + i][self.x - self.place[0] + j] = self.color
