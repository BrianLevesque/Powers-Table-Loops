cont = True
print("Learn your squares and cubes!")

while cont:
    num = int(input("Please enter an integer:"))
    underline = "======="
    print('Number\t\tSquared\t\tCubed')
    print('=======\t\t=======\t\t=======')

    for i in range(num):
        k = i + 1
        print(f'{k}\t\t\t{k * k}\t\t\t{k * k * k}')




    printstr = "\n\t\t"




    # creating multiplaction table
    for i in range(num):     # creating the top row of numbers
        printstr += f'{i + 1}\t'
    print(printstr)
    printstr = "\t\t"
    for i in range(num):  # creating line between first and second row
        printstr += f'=\t'
    print(printstr)
    printstr = " "
    for i in range(num):
        printstr += f'{i + 1} |\t'
        for j in range(num):
            printstr += f'{(i + 1) * (j + 1)}\t'
        print(printstr)
        printstr = " "
    print(printstr)

    con = input("continue?(y/n)")
    if con == "n":
        break