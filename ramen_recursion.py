# Collection of recursion-themed Python examples from "Recursive Ramen" blog post.

import sys

def print_recursion_limit():
    """Prints the system recursion limit (the 'bowl size')."""
    print(f"Your system's recursion limit: {sys.getrecursionlimit()}")

def untangle_noodles(noodle_bowl):
    """
    Recursively removes items from a list, simulating untangling ramen ingredients.
    """
    if not noodle_bowl:
        return "Bowl empty!"
    current_noodle = noodle_bowl.pop()
    print(f"Untangling noodle: {current_noodle}")
    return untangle_noodles(noodle_bowl)

def follow_noodle_strand(strand_length):
    """
    Recursively 'slurps' a noodle by decreasing its length in steps.
    """
    if strand_length <= 0:
        print("Reached noodle end!")
        return
    print(f"Slurping... {strand_length}cm remaining")
    follow_noodle_strand(strand_length - 5)

def count_noodle_layers(bowl_depth, current_layer=1):
    """
    Recursively counts noodle layers up to a given depth.
    """
    if current_layer > bowl_depth:
        print("Reached bowl base!")
        return
    print(f"Layer {current_layer}: Adding more noodles")
    count_noodle_layers(bowl_depth, current_layer + 1)

def infinite_slurp(bite_count=1):
    """
    Demonstrates infinite recursion (stack overflow) by never defining a base case.
    WARNING: will crash when executed!
    """
    print(f"Slurp #{bite_count}")
    infinite_slurp(bite_count + 1)

def perfect_bite(noodles_left, broth_level):
    """
    Proper recursion with two parameters, stopping when resources are depleted.
    """
    if noodles_left <= 0 or broth_level <= 0:
        print("Bowl empty—delicious!")
        return
    noodles_taken = min(5, noodles_left)
    broth_taken = noodles_taken * 2
    print(f"Eating {noodles_taken} noodles with {broth_taken}ml broth")
    perfect_bite(noodles_left - noodles_taken, broth_level - broth_taken)

if __name__ == "__main__":
    print_recursion_limit()
    print(untangle_noodles(["shiitake", "chashu", "menma", "nori"]))
    follow_noodle_strand(30)
    count_noodle_layers(5)
    # infinite_slurp()  # Uncomment to see a stack overflow!
    perfect_bite(20, 100)
