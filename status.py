from covid import Covid
import matplotlib.pyplot as pyplot

class Status:
    def __init__(self):
        self.covid = Covid(source="worldometers")
        self.active = self.covid.get_total_active_cases()
        self.confirmed = self.covid.get_total_confirmed_cases()
        self.recovered = self.covid.get_total_recovered()
        self.deaths = self.covid.get_total_deaths()

    # Plots the status of all the countries in the word
    def get_world_status(self, event):
        # Clear current graph
        pyplot.clf()
        # Get world data:
        world_data = [self.confirmed, self.active, self.deaths, self.recovered]
        x = ["Confirmed", "Active", "Deaths", "Recovered"]
        x_pos = [i for i, _ in enumerate(x)]
        # Plot new:
        pyplot.bar(x_pos, world_data, color="orange")
        pyplot.ylabel("World Total")
        pyplot.title("World Status")
        pyplot.xticks(x_pos, x)
