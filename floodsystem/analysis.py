import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta




def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    poly = np.polyfit(x - x[0], y, p)
    return (poly, x[0])
    
    
def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(x, y, '.')

    #label
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))


    # Display plot
    plt.show()
    plt.tight_layout()
