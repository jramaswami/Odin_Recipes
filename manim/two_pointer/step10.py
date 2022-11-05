from manim import *


class Step10(Scene):

    def construct(self):
        self.camera.background_color = WHITE
        odinproject = Tex("edonprijoct", fill_color=BLACK).scale(2)
        self.add(odinproject)
