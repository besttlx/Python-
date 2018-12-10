#!/usr/bin/env python3
n = int(input("Enter the number of students: "))
data = {}	#jihe
Subjects = ('Physics', 'Maths', 'History')	#kemu
for i in range(0, n):
	name = input('Enter the name of the students {}: '.format(i + 1))
	marks = []
	for x in Subjects:
	data[name] = marks

for x, y in data.items():
	total = sum(y)
	print("{}'s total marks".format(x, total))
	if total < 120:
		print(x, "failed:(")
	else:
		print(x, "passed:)")
