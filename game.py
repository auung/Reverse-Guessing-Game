import random

min_num = int(input("Enter minimum number: "))
max_num = int(input("Enter maximum number: "))
guessed = False

print(f"Pick a number between {min_num} and {max_num}.\nIs this your number?")
answer = random.randint(min_num, max_num)
print(answer)

while not guessed:
    user_input = input("Yes/Over/Under: ").lower()
    diff = (max_num - min_num)
    if user_input == "yes":
        print("Yay!")
        guessed = True
    elif user_input == "under":
        min_num = int(answer)
        if diff >= 3:
            answer += diff // 3
        else:
            answer += diff // 2
        print(answer)
    elif user_input == "over":
        max_num = int(answer)
        if diff >= 3:
            answer -= diff // 3
        else:
            answer -= diff // 2
        print(answer)
    else:
        print("Invalid Keyword")
