Student_Info = {}

Student_Info["Name "] = input("Enter the name of the Student ")
Student_Info["Roll_no. "] = int(input("Enter your roll no. : "))
Student_Info["Percentage "] = float(input("Enter your Percentage: "))
Student_Info["Family_Income"] = float(input("ENter your family income "))

rural = input("Do student belong fromm the rural area ? ")
Student_Info["Rural "] = rural.lower() == "true"

eligible = (Student_Info["Percentage "] > 90) or (Student_Info["Percentage "] > 85 and Student_Info["Family_Income"] < 300000 )
print("\nStudent Info:", Student_Info)

if eligible:
    print("Student is Eligible")
else:
    print("Student is Not Eligible")





