attempts = 0
while attempts < 3:
    name = input("Enter your name: ")
    if name == "":
        print("Blank input! Try again.")
        continue
    attempts += 1
    print("Hello", name)
print("Total valid attempts:", attempts)

for i in range(1, 4):
    number = int(input("Enter a number: "))
    if number < 0:
        print("Negative number skipped")
        continue
    if number == 0:
        print("Zero found")
        break
    print("Number:", number)
else:
    print("Loop completed")
