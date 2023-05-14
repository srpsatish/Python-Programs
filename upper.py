def main():
    print(
"""
\nSelect mode:
    1. Any -> Full uppercase
    2. Any -> Full lowercase""")
    mode = int(input("Enter mode: "))
    text = str(input("Enter text: "))
    if mode == 1:
        print(text.upper())
    elif mode == 2:
        print(text.lower())
    else:
        print("Invalid input")
        
if __name__ == "__main__":
    while True:
        main()
