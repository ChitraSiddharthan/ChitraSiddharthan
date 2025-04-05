class ChitraSiddharthan:
    def __init__(self):
        self.name = "Chitra Siddharthan"
        self.education = ["MSc in Computer Science", "BE in Computer Science and Engineering"]
        self.interests = ["Software Engineering", "Embedded Systems", "IoT", "Data Visualization"]
        self.currently_learning = ["Advanced ML", "Cloud Infrastructure", "Advanced Data Viz"]
    
    def say_hi(self):
        print(f"Hi, I'm {self.name}! Thanks for dropping by! Let's build something amazing together!")
    
    def show_details(self):
        print("\n📚 Education:")
        for degree in self.education:
            print(f"  - {degree}")
        
        print("\n💡 Interests:")
        for interest in self.interests:
            print(f"  - {interest}")
        
        print("\n🚀 Currently Learning:")
        for topic in self.currently_learning:
            print(f"  - {topic}")

# Create an instance and interact
me = ChitraSiddharthan()
me.say_hi()
me.show_details()
