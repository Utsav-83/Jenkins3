import sys

if len(sys.argv) == 7:  
    file_name = sys.argv[0]
    name = sys.argv[1]
    mark1 = int(sys.argv[2])
    mark2 = int(sys.argv[3])
    mark3 = int(sys.argv[4])
    mark4 = int(sys.argv[5])
    mark5 = int(sys.argv[6])     
    print("User provided input values:")
else:
    name = "xyz"
    mark1 = 00
    mark2 = 00
    mark3 = 00
    mark4 = 00
    mark5 = 00
    print("No input given - using default values:")

average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5

print("Student Name:", name)
print("Marks Entered:", mark1, mark2, mark3, mark4, mark5)
print("Average Marks:", average)
