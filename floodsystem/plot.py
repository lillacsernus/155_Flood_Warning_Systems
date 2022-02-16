import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .datafetcher import fetch_measure_levels


def plot_water_levels(station, dates, levels):

    
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    
    for n in station.typical_range:
        return plt.plot(dates, y = n)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()



