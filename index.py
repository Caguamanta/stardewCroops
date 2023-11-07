combs = []

while True:
    try:
        x = int(input("Seeds: "))
        break
    except ValueError:
        print("Please enter an integer value.")

for i in range(1, x + 1):
    if x % i == 0:
        a = (i, x // i)
        combs.append(a)
        
print("You can seed in the following ways:")
for a in combs:
    print(a)

input("Press Enter to exit")
