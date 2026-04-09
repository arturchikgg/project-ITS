import random

# Word lists
adjectives = ["Fast", "Lazy", "Happy", "Sleepy", "Clever"]
nouns = ["Tiger", "Eagle", "Shark", "Lion", "Panda"]
animals = ["Cat", "Dog", "Mouse", "Elephant", "Kangaroo"]

# Function to generate nicknames

def generate_nickname(style='simple'):
    if style == 'simple':
        return f"{random.choice(adjectives)}{random.choice(nouns)}"  
    elif style == 'numbers':
        return f"{random.choice(adjectives)}{random.choice(nouns)}{random.randint(1, 100)}"
    elif style == 'underscores':
        return f"{random.choice(adjectives)}_{random.choice(nouns)}"
    else:
        return "Invalid style selected. Choose 'simple', 'numbers', or 'underscores'."

# Example usage
if __name__ == '__main__':
    print(generate_nickname('simple'))
    print(generate_nickname('numbers'))
    print(generate_nickname('underscores'))
