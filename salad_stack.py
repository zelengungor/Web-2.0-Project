class SaladStack:
    def __init__(self):
        self.layers = []
    
    def push(self, ingredient):
        print(f"→ Adding {ingredient} layer")
        self.layers.append(ingredient)
    
    def pop(self):
        if not self.layers:
            return "✗ Bowl empty!"
        return self.layers.pop()
    
    def peek(self):
        return f"Top layer: {self.layers[-1]}" if self.layers else "Bowl empty"

# Example usage:
salad = SaladStack()
salad.push("Lettuce")    # Base frame
salad.push("Cucumber")   # New stack frame
salad.push("Tomatoes")   # Another frame
salad.push("Onions")     # Growing the stack
salad.push("Carrots")    # Current top frame

# Popping off ingredients (last in, first out)
print(salad.pop())  # Carrots
print(salad.pop())  # Onions
print(salad.pop())  # Tomatoes
print(salad.pop())  # Cucumber
print(salad.pop())  # Lettuce

# Stack overflow example (do NOT run this without a base case!)
# def infinite_salad(stack):
#     stack.push("More Salad!")
#     infinite_salad(stack)

# infinite_salad(salad)

# Base case recursion example
def base_case_example(ingredients):
    if not ingredients:
        print("Base case reached. No more ingredients.")
        return
    print(f"Processing {ingredients[0]}")
    base_case_example(ingredients[1:])

base_case_example(["Lettuce"])
