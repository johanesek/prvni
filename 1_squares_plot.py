import matplotlib.pyplot as plt

input_values=[value for value in range(1,6)]
squares = [1,4,9,16,25]

plt.plot(input_values, squares, linewidth=5)

#set chart title and axes labels
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#set size of tick labels
plt.tick_params(axis='both', labelsize=10)

plt.show()