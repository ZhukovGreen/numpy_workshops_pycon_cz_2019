import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

from load_data import load_data
from moving_average import moving_average

N = 365

if __name__ == "__main__":
    _, dates, data = load_data()
    temperature = data[:,0]

    first_year, last_year = dates[0].year, dates[-1].year

    x = range(first_year, last_year + 1)
    y = range(1, 365 + 1)
    X, Y = np.meshgrid(x, y)

    avg = temperature.mean()
    dt2day_of_year = lambda dt: dt.timetuple().tm_yday
    T = np.zeros_like(X)
    for i, t in enumerate(temperature):
        dt = dates[i]
        x_i = dt.year - first_year
        y_i = dt2day_of_year(dt)
        if y_i < 365:
            T[y_i,x_i] = t  # row (i.e. y) is first index


    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, T, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    fig.colorbar(surf)
    plt.show()
