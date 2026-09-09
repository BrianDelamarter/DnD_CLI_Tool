import random
from print_effects import printer

class dice:
    def __init__(self, faces, modifier=0):
        self.faces = faces
        self.modifier = modifier
        if not self.check():
            print(f"A D{self.faces} is not a real dice.")

    def roll(self):
        roll = random.randint(1,self.faces)
        return (roll+self.modifier)

    def check(self):
        common_dice = [4,6,8,10,12,20,100]
        if self.faces in common_dice:
            return True
        else:
            return False

class D20(dice):
    def __init__(self, faces=20, modifier=0):
        super().__init__(faces, modifier)

    def roll(self):
        roll = random.randint(1,self.faces)
        if roll == 1:
            printer(f"You rolled a nat {roll}! That's a critical failure.")
        if roll == 20:
            printer(f"You rolled a nat {roll}! That's a critical Success/Hit")
        modified = roll + self.modifier
        return (modified)


class D100(dice):
    def __init__(self, faces=100, modifier=0):
        if modifier != 0:
            printer("Modifiers are not allowed for D100 rolls. Setting modifier to 0.")
        super().__init__(faces, 0)

    def roll(self):
        roll = random.randint(1,self.faces)
        return (roll)