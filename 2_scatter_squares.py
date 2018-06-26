import matplotlib.pyplot as plt

x_values=[value for value in range(1,1001)]
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.jet, edgecolor='none', s=4)

#set chart title and axes labels
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=10)
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plt.png')
plt.show()
