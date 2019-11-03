def printSum(a, b):
	print(a + b)
	return None


def add(num1, num2):
	return num1 + num2

gst = 1.05

def calcTotalPrice(price):
	return price*gst

def buildHeader():
	header = "****************\n*    Welcome   *\n****************"
	return header

def buildNumberedList(maxNumber):
	numberedList = []
	for i in range(maxNumber):
		numberedList.append(i)
		print(numberedList)
		numberedTuple = tuple(numberedList)
		print(numberedTuple)
	return numberedTuple

def getDaysOfWeek():
	return "Sunday","Monday","Tuesday"

def worsePrint(*text):
	print(*text)

def average(*args):
	average = 0
	for num in args:
		average += num
	average /= len(args)
	return average

print(average(5,4,5,4))
worsePrint("Hello my name is Jordan","Test")
print("Hello","my","name","is","Jordan")
day1, day2, day3 = getDaysOfWeek()
print(day2)
a,b = buildNumberedList(2)
print(b)
print(add(5,3))
printSum(2,3)
print(calcTotalPrice(5))
print(gst)
print(buildHeader())