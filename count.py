import string

def main():
    counts = {}  # Engaging a dictionary
    text = input("Enter a string: ")
    for character in text:  # Loop thru each character in the provided string
        if character in counts:  # Checks if the character is already in the dictionary
            counts[character] += 1  # If it is, increment the count
        else:
            counts[character] = 1  # Else add it and set the count to 1

    for character, count in counts.items(): # Print the results to the console
        print(f"'{character}' appears {count} times.")


if __name__ == '__main__':
    main() # This if __name__ == '__main__' check will prevent the script from running if imported thru another file
