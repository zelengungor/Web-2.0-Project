# oop_cookies.py

"""
Object-Oriented Programming with Cookies 🍪

This script demonstrates inheritance, encapsulation, and polymorphism
through a baking-themed analogy with a Cookie base class and three subclasses.
"""

class Cookie:  
    def __init__(self, bake_time, ingredients):  
        self.bake_time = bake_time  
        self.ingredients = ingredients  

    def bake(self):  
        print(f"Baking for {self.bake_time} minutes with: {', '.join(self.ingredients)}")  


class ChocolateChip(Cookie):
    def __init__(self):
        super().__init__(bake_time=12, ingredients=["flour", "sugar", "butter", "chocolate chips"])

    def bake(self):
        print("Baking a gooey chocolate chip cookie… 🍫")


class Raisin(Cookie):
    def __init__(self):
        super().__init__(bake_time=15, ingredients=["flour", "sugar", "raisins", "butter"])

    def bake(self):
        print("Baking a hearty raisin cookie… 🥣")


class HeartSprinkle(Cookie):
    def __init__(self):
        super().__init__(bake_time=10, ingredients=["flour", "sugar", "butter", "heart sprinkles"])

    def bake(self):
        print("Baking a sweet heart-sprinkle cookie… ❤️")


def bake_all(cookies):
    for cookie in cookies:
        cookie.bake()  # Single interface, multiple behaviors


# Example usage
if __name__ == "__main__":
    cookies = [ChocolateChip(), Raisin(), HeartSprinkle()]
    bake_all(cookies)
