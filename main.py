from covid import Covid
import matplotlib.pyplot as pyplot
import numpy as np

# Taking input from the user
countries = input("Enter your Country Name (seperated by ',')")
covid = Covid(source="worldometers")
countries = countries.split(',')
# GUI using Matplotlib
pyplot.figure("Covid Tracker by Swapnil")
pyplot.title(" ".join(countries))

n = ["confirmed", "active","deaths", "recovered"]
bar_width = 1/len(countries) - 0.1

# Go over all countries
for idx, country in enumerate(countries):
# Fetching the data from worldometers.info and storing it.
    data = covid.get_status_by_country_name(country)
    a = {
        key:data[key]
        for key in data.keys() & {"confirmed", "active","deaths", "recovered"}
        }
    v = list(a.values())
    pyplot.bar(np.arange(len(n))+idx*bar_width, v, tick_label=n, width=bar_width, label=country)

pyplot.ylabel("Total number")
pyplot.legend()
pyplot.show()
