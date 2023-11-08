from money_model import MoneyModel
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# # Create the model
# starter_model = MoneyModel(10)
# # Step pver the model 10 times
# for i in range(10):
#     starter_model.step()

# agent_wealth = [a.wealth for a in starter_model.schedule.agents]
# # Create a histogram with seaborn
# g = sns.histplot(agent_wealth, discrete=True)
# g.set(title="Wealth distribution", xlabel="Wealth", ylabel="Number of agents");  # The semicolon is just to avoid printing the object representation

# all_wealth = []
# # This runs the model 100 times, each model executing 10 steps.
# for j in range(100):
#     # Run the model
#     model = MoneyModel(10)
#     for i in range(10):
#         model.step()

#     # Store the results
#     for agent in model.schedule.agents:
#         all_wealth.append(agent.wealth)

# # Use seaborn
# g = sns.histplot(all_wealth, discrete=True)
# g.set(title="Wealth distribution", xlabel="Wealth", ylabel="Number of agents");

# plt.show()


model = MoneyModel(100, 10, 10)
for i in range(100):
    model.step()

# agent_counts = np.zeros((model.grid.width, model.grid.height))
# for cell_content, (x, y) in model.grid.coord_iter():
#     agent_count = len(cell_content)
#     agent_counts[x][y] = agent_count
# # Plot using seaborn, with a size of 5x5
# g = sns.heatmap(agent_counts, cmap="viridis",
#                 annot=True, cbar=False, square=True)
# g.figure.set_size_inches(4, 4)
# g.set(title="Number of agents on each cell of the grid")

gini = model.datacollector.get_model_vars_dataframe()
# Plot the Gini coefficient over time
g = sns.lineplot(data=gini)
g.set(title="Gini Coefficient over Time", ylabel="Gini Coefficient");

agent_wealth = model.datacollector.get_agent_vars_dataframe()
agent_wealth.head()

plt.show()
