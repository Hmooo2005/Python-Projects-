def max_num(n1 , n2 , n3):
	if n1 >= n2 and n1 >= n3:
		return n1
	if n2 >= n1 and n2 >= n3:
		return n2
	if n3 >= n1 and n3 >= n2:
		return n3
		
		
result = max_num(23 , 45 , 13)
print(result)


print("#" * 60)

def match_str(str1 , str2):
	if str1 == str2:
		return "strings are matching"
	elif str1 != str2:
		return "string are not matching"
		
result2 = match_str("mohammed" , "mohammed")
print(result2)


print("#" * 60)


#operator = input("Choose The Operator: ")
#num1 = float(input("Enter The first number: "))
#num2 = float(input("Enter The Second number: "))

#if operator =="+":
	#print(num1 + num2)
#elif operator =="*":
	#print(num1 * num2)
#elif operator =="/":
#	print(num1 / num2)
#elif operator =="-":
#	print(num1 - num2)
#else:
#	print("Wrong choice")
	

print("#" * 60)


monthes = {
	1 : "January",
	2 : "February",
	3 : "March",
	4 : "April",
	5 : "May",
	6 : "June",
	7 : "July",
	8 : "August",
	9 : "September",
	10 : "October",
	11 : "November",
	12 : "December"
}
print(monthes[1])
print(monthes.get(4))
print(monthes.get(16))
print(monthes.get(20, "Value do not Exist"))














































