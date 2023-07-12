import matplotlib.pyplot as plt

categories = ["Category A", "Category B", "Category C", "Category D", "Category E"]
percentages = [25, 30, 15, 10, 20]

explode = [0, 0.1, 0, 0, 0.2]
colors = ["red", "blue", "orange", "green", "purple"]

plt.pie(percentages, explode = explode, labels = categories, colors = colors, shadow = True)
plt.title("Percentage Distribution")
plt.legend(categories)
plt.show()
