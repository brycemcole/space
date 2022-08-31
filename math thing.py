def main():
    global expression
    global total
    global operations
    global curr
    global prev
expression = str(input("expression: ")).split(" ")
total = 0
operations = []
curr = None
prev = None

for idx, val in enumerate(expression):
    if val in ("+", "-", "*", "/"):
        operations.append([idx, val])

for idx, set in enumerate(operations):
    curr = set
    if set[1] == "+": 
        if prev == None or expression[curr[0] - 1] != expression[prev[0] + 1]:
            total += int(expression[set[0] - 1]) + int(expression[set[0] + 1]) 
        else: 
            total += int(expression[set[0] + 1])
    elif set[1] == "-":
        if prev == None or expression[curr[0] - 1] != expression[prev[0] + 1]:
            total += int(expression[set[0] - 1]) - int(expression[set[0] + 1])
        else:
            total -= int(expression[set[0] + 1])
    prev = set

print(total)
