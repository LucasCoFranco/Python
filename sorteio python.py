from random import randint
A=set()
while len(A)<10:
    A.add(randint(1,20))
B=set(range(1,21))-A
print("Conjunto A : {}".format(A))
print("Conjunto B : {}".format(B))
if A&B==set():
    print("\nInterseção vazia de A e B")
