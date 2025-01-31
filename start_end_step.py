a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))
c = int(input("Enter the step (c): "))

# we need to make sure the step is positive
if a > b and c > 0:
    # then reverse the step if counting down
    c = -c  
elif a < b and c < 0:
    # ensure step is positive if counting up
    c = -c  

for i in range(a, b + (1 if a < b else -1), c):
    print(i)