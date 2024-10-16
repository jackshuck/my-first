import math
from datetime import datetime
a="run "
b="the python"
print ("{a}{b}")
print("------2nd output------")
print(f"{a}{b}")

# ex2

a=45
b=50
print (a,"+",b"=",a+b)
print("------2nd output------")
print(f"a+b={a+b}")
print("------3rd output------")
print(f"{a+b}={a+b}")
print("------4th output------")
print(f"{a}+{b}={a+b}")
# ex3number

a=125000100
print(f"{a:d}")
print("------2nd output------")
print(f"{a:d}")
print("------3rd output------")
print(f"{a:10d}")
print("------4th output------")
print(f"{a:012}")

#ex4 float

a=450.21
print(f"{a:f}")
print("------2nd output------")
print(f"{a:1}")

#ex5 import math

print(f"{math.pi:f}")
print("------2nd output------")
print(f"{math.pi:2f}")
print("------3rd output------")
print(f"{math.pi:.3f}")
print("------4th output------")
print(f"{math.pi:03.3f}")

#ex6 datatime
print("-----output for dates------")

current_date =datetime.now ()
format_date=current_date.strftime("%y-%d-%m")
print("today is :",format_date)