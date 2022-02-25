import matplotlib
import numpy as np
import matplotlib.pyplot as plt





def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    p_coeff = np.polyfit(x - x[0], y, p)     
    poly = np.poly1d(p_coeff)   
    return poly, x[0]


    
def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    poly, d0 = polyfit(dates, levels, p)

    

    # Plot original data points
    plt.plot(x - x[0], y, '.')

    #label
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1 - x1[0], poly(x1 - x[0]), label = "polynomial of best fit")


    # Display plot
    plt.show()
    plt.tight_layout()

def get_gradient(dates, levels, p):
    if len(dates) != 0:
        p_coeff = np.polyfit(dates - dates[-1], levels, p)     
        poly = np.poly1d(p_coeff)   
        derivative = np.polyder(poly)
        today = dates[0] - dates[-1]
        gradient = derivative(today)
        return gradient
    else:
        return None
    