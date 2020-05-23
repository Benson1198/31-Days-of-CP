english, eng_roll_numbers = (int(input()), set(map(int, input().split())))
french, french_roll_numbers = (int(input()), set(map(int, input().split())))
difference = eng_roll_numbers.symmetric_difference(french_roll_numbers)
print(len(difference))