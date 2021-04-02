from random import randint

class Die():
    """Simulating a die"""
    def __init__(self, num_sides = 6):
        """The regular die is a D6"""
        self.num_sides = num_sides
        

    def roll(self):
        """Simulating a die roll"""
        return randint(1, self.num_sides)



            

