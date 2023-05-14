def main():
    initial = input("Enter numbers, seperated by space: ")
    value_a = initial.split(" ")[0]
    value_b = initial.split(" ")[1]
    print(value_b, value_a)
    
if __name__ == "__main__":
    main()
