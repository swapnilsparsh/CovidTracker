from covid import Covid
import matplotlib.pyplot as pyplot

# Taking input from the user
country = input("Enter your Country Name")
covid = Covid(source="worldometers")

# Fetching the data from worldometers.info and storing it.
data = covid.get_status_by_country_name(country)
a = {
    key:data[key]
    for key in data.keys() & {"confirmed", "active","deaths", "recovered"}        
    }
n = list(a.keys())
v = list(a.values())

# GUI using Matplotlib
pyplot.figure("Covid Tracker by Swapnil")
pyplot.title(country)
pyplot.bar(range(len(a)), v, tick_label=n)
pyplot.ylabel("Cases per 10 lakh")
pyplot.show()
