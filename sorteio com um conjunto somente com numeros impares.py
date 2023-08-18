
from random import randint
A=set()
num=0
while len(A)<10:
    num=randint(1,20)
    if num%2!=0:
        A.add(num)
B=set(range(1,21))-A
print("Conjunto A : {}".format(A))
print("Conjunto B : {}".format(B))
if A&B==set():
    print("\nInterseção vazia de A e B")
