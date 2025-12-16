import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100,101):
   x = x + [n]

# create y values
for n in x:
   y = y + [pow(n,2)-3]
   #y = n**2 - 3

# print chart
plt.plot(x,y)
plt.show()





#plt.title("Wykres funkcji f(x) = x\u00b2 - 3")
#plt.xlabel("Oś X")
#plt.ylabel("Oś Y")
#plt.grid(True)
#plt.savefig("wykres_funkcji_x2_minus_3.png")