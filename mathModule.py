PI = 3.14159

def add(num1, num2):
	return num1+num2

#subtract
#divide
#multiply
def fib(n):
	assert (n >= 0), "Fibonacci only works for positive integers"

	num1 = 0;
	num2 = 1;
	for i in range(1,n):
		if(i%2==0):
			num1 = num1 + num2
		else:
			num2 = num1 + num2
	if(n%2==0):
		return num2
	else:
		return num1

def fact(n):
	if n < 0:
		raise ArithmeticError
	if n==0:
		return 1
	else:
		return n*fact(n-1)


if __name__ == '__main__':
	try:
		print(fact(-4))
	except ArithmeticError:
		print("Invalid input")

	try:
		print(fib(-8))
	except AssertionError as e:
		print("Invalid input")
		print(e)