import sys

class animal:
    def print(self):
        print("This is my favorite animal:")
        print(f"Its arms are {self.arms_length} length.")
        print(f"Its legs are {self.legs_length} length.")
        print(f"It has {self.eyes_num} eyes.")
        print(f"Its {self.tail} that the animal has a tail.")
        print(f"Its {self.furry} that the animal is furry.")
        
    def __init__(self, larms=4.0, llegs=4.0, neyes=2, btail=True, bfurry=True):
        self.arms_length = larms
        self.legs_length = llegs
        self.eyes_num = neyes
        self.tail = btail
        self.furry = bfurry
        
def main():
    my_animal = animal()
    my_animal.print()
    
if __name__ == "__main__":
    main()