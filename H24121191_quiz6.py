import random
print("Guess my number between 1 and 100.")
my_num = random.randint(1, 100)
guess_num = int(input("Enter your guess (1-100):"))
guess_list = []
upper = 100
lower = 1
while guess_num != my_num:
	if guess_num < lower or guess_num > upper:
		guess_num = int(input("Invalid input. Guess again:"))
	elif guess_num < my_num:
		lower = guess_num
		guess_list.append(guess_num)
		guess_num = int(input("Too low. Guess again:"))
	elif guess_num > my_num:
		upper = guess_num
		guess_list.append(guess_num)
		guess_num = int(input("Too high. Guess again:"))
guess_list.append(guess_num)
print("Congratulations! You guessed the number in %d tries." % len(guess_list))
print("Previous guess:", guess_list)
print("Histogram:")
for i in range(1,11):
	time = 0
	for num in guess_list:
		if num >= i * 10 - 9 and num <= i * 10:
			time += 1
	if i != 10:
		print("0%d1-0%d0:" % (i-1, i), "*" * time)
	elif i == 10:
		print("0%d1-%d0:" % (i-1, i), "*" * time)

