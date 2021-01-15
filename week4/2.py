import matplotlib.pyplot as plt
x = range(100)

s0 = 0; s1 = 1
y = [s0, s1]
for i in x[2:]:
    y.append(0.5*y[i-1]+y[i-2])

plt.plot(x, y)
plt.show()
print(y)

