import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
#make randomwalk and plot the points

    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.figure(figsize=(12,8))
    plt.plot(rw.x_values, rw.y_values, linewidth=0.5)
    plt.plot(0, 0, c='green', linewidth=0.5)
    plt.plot(rw.x_values[-1], rw.y_values[-1], linewidth=0.5)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
