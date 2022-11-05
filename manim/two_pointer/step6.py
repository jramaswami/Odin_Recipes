from manim import *


class Step6(Scene):

    def construct(self):
        self.camera.background_color = WHITE
        odinproject = Tex("edinprojoct", fill_color=BLACK).scale(2)
        left_arrow = Arrow(start=UP, end=DOWN, color=RED).next_to(odinproject, UP).shift(LEFT * (odinproject.width * 0.28))
        right_arrow = Arrow(start=UP, end=DOWN, color=GREEN).next_to(odinproject, UP).shift(RIGHT * (odinproject.width * 0.12))
        self.add(odinproject, left_arrow, right_arrow)
