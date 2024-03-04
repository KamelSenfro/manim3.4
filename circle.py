from manim import *

from manim_data_structures import *

class ArrayScene(Scene):
    def construct(self):
        arr = MArray(self, [1, 2, 3], label='Arr')
        self.add(arr)