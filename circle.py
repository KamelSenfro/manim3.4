from manim import *

class CircleExplanation(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=1, color=BLUE)

        # Add the circle to the scene
        self.add(circle)

        # Create text using LaTeX
        explanation_text = MathTex(r"\text{Why does it have } 360^\circ").next_to(circle, UP)

        # Add the text to the scene
        self.add(explanation_text)

        # Display the scene
        self.wait(2)  # Wait for 2 seconds before ending the scene
