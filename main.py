
# ******************************
# Make your Code
# ******************************

strval = input('Enter numbers: ')
numbers = list(map(int,strval.split()))

target = int(input('Enter a target number: '))
for i in range(len(numbers)):
	amount = numbers.count(target)

print(amount)	
# the below llin 11 are same as the lines from 5 to 8
# numbers = list(map(int, strval))
# print (numbers)
