students = {}

n = int(input("How Many Students You want to add : "))

for i in range(n):
    name = input("Enter Names : ")
    marks = int(input("Enter Marks : "))

    students[name] = marks 
    print(students)

sum = 0

for i in students:
    print(i , students[i])

avg = sum / len(students)
print(avg)

search_name = input("Enter Name you want to search : ")

if search_name in students:
    print("Found|" , search_name , students[search_name])
else:
    print("Not Found")

if "Ravi" in students:
    del students["Ravi"]
    print(students)

if "Devansh" in students:
    students["Devansh"] = 98
    print(students)

count = 0

for i in students:
    if students[i] > 80:
        count += 1
print(students,count)

highest_name = ""
highest_marks = 0

for i in students:
    if students[i] > highest_marks:
        highest_marks = students[i]
        highest_name = i

print("Highest Name And Marks of Student is : " , highest_name , highest_marks)

lowest_name = ""
lowest_marks = 999

for i in students:
    if students[i] < lowest_marks:
        lowest_marks = students[i]
        lowest_name = i

print("Lowest Name And Marks of Student is : " , lowest_name , lowest_marks)

