import random
import string
import os

# Define the dimensions of the word search grid
x = 20
y = 15

# Initialize the word search grid with empty strings
Wlist = [['' for _ in range(y)] for _ in range(x)]

# List of words to be placed in the word search grid
wordPool = ["hello", "world", "python", "code", "random", "list", "example", "function", "variable", "string","algorithm", "data", "structure", "search", "grid", "place", "word", "game", "challenge", "fun", "puzzle","solution", "test", "case", "input", "output", "logic", "debug", "error", "exception", "handle"]

# Debug flag to make successfully inserted words all caps
debug_flag = True

# List to keep track of successfully placed words
placed_words = []

# Specify where to save the text file
filePath = None  # Default to the same directory as the Python file

def can_place_word(Wlist, word, row, col, direction):
    # Check if the word can be placed at the specified location and direction
    if direction == 'horizontal':
        if col + len(word) > len(Wlist[0]):
            return False
        for i in range(len(word)):
            if Wlist[row][col + i] not in ('', word[i]):
                return False
    elif direction == 'vertical':
        if row + len(word) > len(Wlist):
            return False
        for i in range(len(word)):
            if Wlist[row + i][col] not in ('', word[i]):
                return False
    elif direction == 'diagonal':
        if row + len(word) > len(Wlist) or col + len(word) > len(Wlist[0]):
            return False
        for i in range(len(word)):
            if Wlist[row + i][col + i] not in ('', word[i]):
                return False
    return True

def place_word(Wlist, word, row, col, direction):
    # Place the word at the specified location and direction
    if debug_flag:
        word = word.upper()
    if direction == 'horizontal':
        for i in range(len(word)):
            Wlist[row][col + i] = word[i]
    elif direction == 'vertical':
        for i in range(len(word)):
            Wlist[row + i][col] = word[i]
    elif direction == 'diagonal':
        for i in range(len(word)):
            Wlist[row + i][col + i] = word[i]

def fill_random_letters(Wlist):
    # Fill the remaining empty cells with random lowercase letters
    for i in range(len(Wlist)):
        for j in range(len(Wlist[0])):
            if Wlist[i][j] == '':
                Wlist[i][j] = random.choice(string.ascii_lowercase)

def place_words_randomly(Wlist, wordPool, directions, max_attempts=100):
    # Shuffle the word pool to ensure random selection without duplicates
    random.shuffle(wordPool)
    # Attempt to place each word from the shuffled word pool into the grid
    for word in wordPool:
        placed = False
        attempts = 0
        while not placed and attempts < max_attempts:
            random.shuffle(directions)  # Shuffle directions before each attempt
            for direction in directions:
                row = random.randint(0, len(Wlist) - 1)
                col = random.randint(0, len(Wlist[0]) - 1)
                if can_place_word(Wlist, word, row, col, direction):
                    place_word(Wlist, word, row, col, direction)
                    placed_words.append(word)
                    placed = True
                    break
            attempts += 1

def printAll(lst):
    # Print the word search grid to the console
    for row in lst:
        print(" | ".join(row))

def toTextFile(lst, filepath=None):
    # Save the word search grid and placed words to a text file
    if filepath is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, "output.txt")
    max_length = max(len(" | ".join(row)) for row in lst)
    try:
        with open(filepath, 'w') as file:
            for row in lst:
                line = " | ".join(row)
                padding = (max_length - len(line)) // 2
                file.write(" " * padding + line + "\n")
            file.write("\nWords placed:\n")
            words_line = ", ".join(placed_words)
            padding = (max_length - len(words_line)) // 2
            file.write(" " * padding + words_line + "\n")
        print(f"File successfully exported to {filepath}")
    except Exception as e:
        print(f"Failed to export file. Please revise the file path: {filepath}")
        print(f"Error: {e}")

# List of possible directions for placing words
directions = ['horizontal', 'vertical', 'diagonal']

# Place words randomly in the grid
place_words_randomly(Wlist, wordPool, directions)

# Fill remaining empty cells with random letters
fill_random_letters(Wlist)

# Print the word search grid to the console (optional)
# printAll(Wlist)

# Save the word search grid and placed words to a text file
toTextFile(Wlist)