import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def draw_pic():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    # save the figure to a my_test

    plt.savefig('my_test/my_test.png')
    plt.show()
draw_pic()