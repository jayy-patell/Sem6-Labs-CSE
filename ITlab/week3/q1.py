n1 = int(input("Enter num1 "))
n2 = int(input("Enter num2 "))
op = input("Enter operation ")
out = 0

if op == '+':
    out = n1 + n2
elif op == '-':
    out = n1 - n2
elif op == '*':
    out = n1 * n2
elif op == '/':
    out = n1 / n2
print(f"Output: {n1} {op} {n2} = {out}")