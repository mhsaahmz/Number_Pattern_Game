import random

def inc_pattern() -> list:
    n = random.randint(2, 10)
    lst = [n]
    inc = random.randint(2, 5)

    for i in range(4):
        n += inc
        lst.append(n)

    return lst

question = inc_pattern()
last_item = question.pop()

print(question)

counter = 0

while True:
    try:
        guess_num = int(input("Enter the last item of the list: "))
    except ValueError:
        print("Error: please enter a number!")
        continue

    counter += 1

    if guess_num == last_item:
        print("Well done! You won 🎉")
        print("Number of attempts:", counter)
        break
    else:
        print("Wrong answer, try again!")
