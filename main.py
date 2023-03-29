# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import matplotlib.pyplot as plt


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    squares = [1, 4, 9, 16, 25]

    fig, ax = plt.subplots()
    ax.plot(squares, linewidth=3)

    #Set chart title and label axes.
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    #Set size of tick labels.
    ax.tick_params(axis='both', labelsize=14)

    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
