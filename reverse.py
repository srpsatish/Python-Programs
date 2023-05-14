def main(initial):
    if initial.isdigit():
        flag = True
    else:
        flag = False
    output = initial[::-1]
    if flag == True:
        return int(output)
    else:
        return output

if __name__ == '__main__':
    inital = input("Enter a number, or a string: ")
    output = main(inital)
    print(output)
