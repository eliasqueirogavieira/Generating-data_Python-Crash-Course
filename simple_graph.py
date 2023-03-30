# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import matplotlib.pyplot as plt
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x_values = range(1,5001)
    y_values = [x**3 for x in x_values]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

    #Set chart title and label axes.
    ax.set_title("Square numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    #Set the range for each axis.
    ax.axis([0, 5100, 0, 5100**3])
    ax.ticklabel_format(style='plain')

    plt.savefig('new_scatter.png', bbox_inches='tight')
    plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
