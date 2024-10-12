import random
import tkinter as tk
from tkinter import messagebox
import os

# Function to load words and hints from the wordlist.txt
def load_words(file_path):
    word_hint_dict = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                word, hint = line.strip().split(': ')
                word_hint_dict[word.strip()] = hint.strip()
        return word_hint_dict
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return {}

# Function to select a random word from the word list
def select_random_word(word_dict):
    word = random.choice(list(word_dict.keys()))
    hint = word_dict[word]
    return word, hint

# Function to update the displayed word
def display_word(word, correct_guesses):
    return ''.join([letter if letter in correct_guesses else '_' for letter in word])

# Function to check if the player won
def check_win(word, correct_guesses):
    return all(letter in correct_guesses for letter in word)

# Hangman game logic
def play_hangman():
    global word, hint, correct_guesses, incorrect_guesses, word_hint_dict

    word, hint = select_random_word(word_hint_dict)
    correct_guesses = []
    incorrect_guesses = 0
    update_display()

# Update the display after each guess
def update_display():
    word_display.config(text=display_word(word, correct_guesses))
    hint_display.config(text=f"Hint: {hint}")
    incorrect_display.config(text=f"Incorrect guesses: {incorrect_guesses}")

# Function to handle the player's guess
def handle_guess(event=None):  # Added 'event' parameter to handle key binding
    global incorrect_guesses

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if guess in word and guess not in correct_guesses:
        correct_guesses.append(guess)
        if check_win(word, correct_guesses):
            messagebox.showinfo("Hangman", "Congratulations, you won!")
            play_hangman()  # Start the next word
    else:
        incorrect_guesses += 1
        if incorrect_guesses >= 6:  # You can set the incorrect limit here
            messagebox.showinfo("Hangman", f"You lost! The word was: {word}")
            play_hangman()  # Start the next word
    update_display()

# Set up the GUI
root = tk.Tk()
root.title("Hangman Game")

# Word display
word_display = tk.Label(root, text="_" * 10, font=("Helvetica", 24))
word_display.pack(pady=10)

# Hint display
hint_display = tk.Label(root, text="Hint: ", font=("Helvetica", 14))
hint_display.pack(pady=10)

# Incorrect guesses display
incorrect_display = tk.Label(root, text="Incorrect guesses: 0", font=("Helvetica", 14))
incorrect_display.pack(pady=10)

# Guess entry field
guess_entry = tk.Entry(root, font=("Helvetica", 14))
guess_entry.pack(pady=10)

# Guess button
guess_button = tk.Button(root, text="Guess", command=handle_guess)
guess_button.pack(pady=10)

# Bind the Enter key to the guess entry (works as Guess button)
root.bind('<Return>', handle_guess)  # Bind the Enter key to submit guess

# Next word button
next_word_button = tk.Button(root, text="Next Word", command=play_hangman)
next_word_button.pack(pady=10)

# Load words from the wordlist.txt file
base_dir = os.path.dirname(__file__)
word_file_path = os.path.join(base_dir, 'wordlist.txt')  # Relative path
word_hint_dict = load_words(word_file_path)

print(f"Loaded words: {word_hint_dict}")  # Debug information to check if words are loaded

# Start the game
play_hangman()

# Run the GUI loop
root.mainloop()
