print("Wpisz pierwsza liczbe:")
a = float(input())

print("Wpisz znak operacji: [+ - / // * ** %]")
op = input()

print("Wpisz druga liczbe:")
b = float(input())

r = 0.0

if op == "+":
    r = a + b
elif op == "-":
    r = a - b
elif op == "*":
    r = a*b
elif op == "**":
    r = a**b
elif op == "/":
    r = a/b
elif op == "//":
    r = a//b
elif op == "%":
    r = a%b
    
print(r)