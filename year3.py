import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from load_data import load_data

N = 365

if __name__ == "__main__":
    _, dates, data = load_data()
    temperature = data[:, 0]

    first_year, last_year = (
        dates[0].year,
        dates[-1].year,
    )

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
            T[y_i, x_i] = (
                1 if t > avg else -1
            )  # row (i.e. y) is first index

    fig, ax = plt.subplots()
    im = ax.imshow(
        T,
        origin="lower",
        interpolation="none",
        cmap=cm.jet,
        vmin=np.min(T),
        vmax=np.max(T),
        extent=[first_year, last_year, 1, 365],
        aspect="auto",
    )

    plt.show()
