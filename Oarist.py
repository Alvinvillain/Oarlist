import itertools
import os
import time
from pyfiglet import Figlet

# Function to generate wordlists
def generate_wordlists(characters, min_length, max_length):
    wordlists = []
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            wordlists.append(''.join(combination))
    return wordlists

# Function to print ASCII art
def print_ascii_art(text):
    figlet = Figlet(font='slant')
    ascii_art = figlet.renderText(text)
    print(ascii_art)

# Function to estimate the size of the wordlist
def estimate_wordlist_size(characters, min_length, max_length):
    total_combinations = 0
    for length in range(min_length, max_length + 1):
        total_combinations += len(characters) ** length
    average_word_size = (min_length + max_length) / 2
    estimated_size_bytes = total_combinations * (average_word_size + 1)  # +1 for newline character
    return estimated_size_bytes, total_combinations

# Function to estimate the time required to generate the wordlist
def estimate_time(total_combinations):
    start_time = time.time()
    # Generate a small portion of the combinations to estimate time
    sample_combinations = min(total_combinations, 10000)
    for _ in itertools.islice(itertools.product('abc', repeat=3), sample_combinations):
        pass
    end_time = time.time()
    time_per_combination = (end_time - start_time) / sample_combinations
    estimated_time = time_per_combination * total_combinations
    return estimated_time

# Main function
def main():
    print_ascii_art("OAR")
    
    print("Enter characters to include in the wordlist:")
    print("1. Letters only")
    print("2. Letters and numbers")
    print("3. Letters, numbers, and special characters")
    print("4. Custom set of characters")
    choice = input("Choose an option (1-4): ").strip()

    if choice == '1':
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif choice == '2':
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    elif choice == '3':
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:",.<>?'
    elif choice == '4':
        characters = input("Enter your custom set of characters: ")
    else:
        print("Invalid choice. Exiting.")
        return
    
    min_length = int(input("Enter minimum length of words: "))
    max_length = int(input("Enter maximum length of words: "))
    filename = input("Enter the filename for the wordlist: ")

    estimated_size_bytes, total_combinations = estimate_wordlist_size(characters, min_length, max_length)
    estimated_size_mb = estimated_size_bytes / (1024 ** 2)
    estimated_time = estimate_time(total_combinations) / 60  # Convert to minutes

    print(f"Estimated size of the wordlist: {estimated_size_mb:.2f} MB")
    print(f"Estimated time to generate the wordlist: {estimated_time:.2f} minutes")
    confirm = input("Are you sure you want to generate the wordlist? (yes/no): ").strip().lower()

    if confirm != 'yes':
        print("Operation cancelled.")
        return

    wordlists = generate_wordlists(characters, min_length, max_length)
    
    # Save to a file
    with open(filename, "w") as f:
        for word in wordlists:
            f.write(word + "\n")
    
    print(f"Wordlist generated and saved to {filename}. Total words: {len(wordlists)}")

if __name__ == "__main__":
    main()
