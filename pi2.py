pi = 3
pr = int(input("how pwecise you want :3\n")) 
for i in range(2, pr*1000, 5):
    pi = pi + (4 / (i*(i+1)*(i+2))) - (4 / ((i+2)*(i+3)*(i+4)))
print(pi)
