import pygame
from shape import Shape


class Functions(object):
    def __init__(self, settings, screen, information, display, shapes):
        self.settings = settings
        self.screen = screen
        self.information = information
        self.display = display
        self.shapes = shapes

        self.initial_shape()

        self.u1 = False
        self.u2 = False
        self.u3 = False

    def check_event(self):
        shape = self.find_shape()
        self.lay_event(shape)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_k]:
                    shape.rotate()
                    if shape.collide():
                        for _ in range(3):
                            shape.rotate()
                elif event.key == pygame.K_j:
                    for _ in range(3):
                        shape.rotate()
                    if shape.collide():
                        shape.rotate()
                elif event.key == pygame.K_SPACE:
                    while True:
                        if shape.update():
                            self.create_shape()
                            break
                elif event.key == pygame.K_r:
                    self.restart_game()
            elif event.type == pygame.USEREVENT:
                if shape.update():
                    self.create_shape()
            elif event.type == pygame.USEREVENT + 1:
                if shape.update():
                    self.create_shape()
            elif event.type == pygame.USEREVENT + 2:
                shape.move_left()
            elif event.type == pygame.USEREVENT + 3:
                shape.move_right()

    def update_screen(self):
        self.display.eliminate()

    def draw_screen(self):
        self.screen.fill(self.settings.background)
        self.display.draw()
        self.information.draw()
        for shape in self.shapes:
            shape.draw()
        pygame.display.flip()

    def initial_shape(self):
        shape1 = Shape(self.settings, self.screen, self.display, self.information)
        shape1.update()
        shape2 = Shape(self.settings, self.screen, self.display, self.information, False)
        self.shapes.add(shape1, shape2)

    def find_shape(self):
        for shape in self.shapes:
            if shape.flag:
                return shape

    def lay_event(self, shape):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            if not self.u1:
                if shape.update():
                    self.create_shape()
                pygame.time.set_timer(pygame.USEREVENT + 1, 150)
                self.u1 = True
        else:
            pygame.time.set_timer(pygame.USEREVENT + 1, 0)
            self.u1 = False
        if keys[pygame.K_a]:
            if not self.u2:
                shape.move_left()
                pygame.time.set_timer(pygame.USEREVENT + 2, 150)
                self.u2 = True
        else:
            pygame.time.set_timer(pygame.USEREVENT + 2, 0)
            self.u2 = False
        if keys[pygame.K_d]:
            if not self.u3:
                shape.move_right()
                pygame.time.set_timer(pygame.USEREVENT + 3, 150)
                self.u3 = True
        else:
            pygame.time.set_timer(pygame.USEREVENT + 3, 0)
            self.u3 = False

    def create_shape(self):
        shape = Shape(self.settings, self.screen, self.display, self.information)
        shape.add(self.shapes)
        for shape in self.shapes:
            shape.flag = not shape.flag
            if shape.flag:
                if shape.update():
                    self.restart_game()

    def restart_game(self):
        self.display.reset_data()
        self.information.reset_data()
        self.information.reset_info()
        self.shapes.empty()
        self.initial_shape()
