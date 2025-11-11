import sys

if len(sys.argv) == 6:  
    name = sys.argv[0]
    mark1 = float(sys.argv[1])
    mark2 = float(sys.argv[2])
    mark3 = float(sys.argv[3])
    mark4 = float(sys.argv[4])
    mark5 = float(sys.argv[5])     
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

print("Script Name:", name)
print("Marks Entered:", mark1, mark2, mark3, mark4, mark5)
print("Average Marks:", average)
