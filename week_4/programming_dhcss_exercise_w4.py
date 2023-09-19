# -*- coding: utf-8 -*-
"""programming_dhcss_exercise_w4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ld7UV8IzcjNtezXDzbPjL78hSHGvXfKo

Programming for DHCSS Exercises: Week 4. Functions, Modules, Exceptions
"""

### Problem 1 ###

### Problem 1a: write a function to print the power of a number.

### Write your code

### Problem 1b: write the same function that prints out error for an erroneous input (e.g., a string as input)

### Problem 1c: write a function to print a list of all the powers of a number "x", up to and including "y"th power (from 0th power)
### E.g., for x = 2 and y = 3, the function should print the follwing: [1, 2, 4, 8]

### Write your code

### Problem 2 ###

### Here is some data on the results of tennis matches.

### For instance, the first item indicates that Federer beat Rafael Nadal by winning 6 games (Nadal winning 4).

matches = [
    ("Roger Federer", "Rafael Nadal", 6, 4),
    ("Serena Williams", "Maria Sharapova", 4, 6),
    ("Andy Murray", "Novak Djokovic", 6, 6),
    ("Venus Williams", "Naomi Osaka", 5, 7),
    ("Dominic Thiem", "Alexander Zverev", 4, 6),
    ("Stan Wawrinka", "Grigor Dimitrov", 6, 5),
    ("Simona Halep", "Karolina Pliskova", 6, 3),
    ("Angelique Kerber", "Sloane Stephens", 5, 5)
]

### Problem 2a: define a function accepts a pair of players and their respecctive acores in a match and prints a match result in the following format: "Federer beat Nadal by 2 games."
### You can start with the following code: def match_summary(player1, player2, score1, score2):
### If the match ended in a tie, just pint "tie".
### Hint: the abs() function returns the absolute value of a given number (abs(-2) -> 2).

### Write your code

### Problem 2b: use the function in a for loop and pass the list (the "matches" list).

### Write your code

### Problem 3 ###

### First, create the following two lists. One is for novel titles, and the other is for reviews.

titles = [
    "Dune by Frank Herbert",
    "Neuromancer by William Gibson",
    "Foundation by Isaac Asimov",
    "Brave New World by Aldous Huxley",
    "The Left Hand of Darkness by Ursula K. Le Guin",
    "Snow Crash by Neal Stephenson",
    "The Stars My Destination by Alfred Bester",
    "Hyperion by Dan Simmons",
    "The Moon is a Harsh Mistress by Robert A. Heinlein",
    "A Canticle for Leibowitz by Walter M. Miller Jr.",
    "The Windup Girl by Paolo Bacigalupi",
    "Altered Carbon by Richard K. Morgan",
    "The Three-Body Problem by Liu Cixin",
    "Red Mars by Kim Stanley Robinson",
    "The Space Merchants by Frederik Pohl and C.M. Kornbluth"
]

reviews = [
    "Dune is an absolute masterpiece. Loved every bit of it.",
    "Neuromancer was a bit hard to get into, but a classic!",
    None,
    "Brave New World presents a startling view of the future which on the surface appears almost comical.",
    "Le Guin's masterpiece manages to transcend both space and gender.",
    "Snow Crash is a mind-altering romp through a future America.",
    "A roller-coaster ride of a story. Bester's prose is powerful.",
    342,
    "Heinlein's tale is both a tribute to the resilience of the human spirit and a harsh criticism of societal structures.",
    "A Canticle for Leibowitz is a gripping tale of the cyclical nature of history.",
    "Bacigalupi's vision of a future Thailand is both captivating and horrifying.",
    "Altered Carbon blends cyberpunk and detective genres in a thrilling way.",
    "Liu Cixin presents a first-contact story with a unique twist. Thought-provoking.",
    "Red Mars is a detailed and realistic portrayal of the colonization of Mars.",
    "The Space Merchants satirizes consumerism and advertising in a future overpopulated world."
]

### Problem 3a: write a function that, given a novel title from our list, extracts and returns the author(s).
### Hint: use the string method "split()".

### Write your code


### Problem 3b: use the function to create a nested list that contains sub-lists of author(s) from each book.

### Write your code


### Problem 3c: define a function that counts the number of words in a review (record np.nan for cases where counting is not available). Use a if-else statement inside the function.
### Hint I: NumPy's nan is a special constant in the NumPy library in Python that represents "Not a Number." It is often used to denote missing values or undefined operations.
### Hint II: Use the "isinstance" function, a built-in function in Python. It is used to check if an object is an instance of a particular class.

### Write your code

### Problem 3d: do the same as Problem 3c, but this time, use a try-except statement.

### Write your code


### Problem 3e. Use the two fucntions to create lists containig the number of words. See if the two lists are identical.

### Write your code


### Problem 3f. Repeat Problem 3d-e, but, instead of recording "non_applicable", record the actual error message or type.
### Hint: use "try" to count the number of words, and use "except Exception as e" to access the error object

### Write your code