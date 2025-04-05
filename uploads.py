from manim import *

class PythonClass(Scene):
    def construct(self):
        code = Code(
            code="""class ChitraSiddharthan:
    def __init__(self):
        self.name = "Chitra Siddharthan"
        self.education = ["MSc in Computer Science", "BE in Computer Science and Engineering"]
        self.interests = ["Software Engineering", "Embedded Systems", "IoT", "Data Visualization"]
        self.currently_learning = ["Advanced ML", "Cloud Infrastructure", "Advanced Data Viz"]
        
    def say_hi(self):
        print("Thanks for dropping by! Let's build something amazing together!")""",
            language="Python",
            font="Monospace",
            style="colorful",
            scale_factor=0.6
        )
        self.play(Write(code))
