class Settings(object):
    def __init__(self):
        self.block_size = 40

        self.screen_size = (self.block_size * 15, self.block_size * 20)
        self.background = (0, 0, 0)

        self.split_line_size = 3
        self.split_line_color = (255, 255, 255)

        self.font_size = 48
