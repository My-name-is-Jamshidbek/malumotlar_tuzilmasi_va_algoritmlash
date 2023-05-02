def getFirstDigit(x) :
	while (x >= 10) :
		x //= 10
	return x
def getCountWithSameStartAndEndFrom1(x) :
	if (x < 10):
		return x

	tens = x // 10

	res = tens + 9

	firstDigit = getFirstDigit(x)
	lastDigit = x % 10

	if (lastDigit < firstDigit) :
		res = res - 1

	return res
def getCountWithSameStartAndEnd(start, end) :
	return (getCountWithSameStartAndEndFrom1(end) -
		getCountWithSameStartAndEndFrom1(start - 1))

start, end = list(map(int, input().split()))
print(getCountWithSameStartAndEnd(start, end))

