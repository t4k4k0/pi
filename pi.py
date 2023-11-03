precision = int(input("how pwecise you want :3 :"))
pi = 0
i = 0
while (i < 1000 * precision):
    pi = pi + 4/(2*i+1)
    i=i+1
    pi = pi - 4/(2*i+1)
    i=i+1
print(pi)
