from limpieza_model import LimpiezaModel
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

model = LimpiezaModel(10, 10, 30, 30)
for i in range(100):
    model.step()

# -----------------------------------------------------------------ARCHIVO VISUALIZACIÓN-----------------------------------------------------------------
# import matplotlib.pyplot as plt
# import seaborn as sns

# time = model.datacollector.get_model_vars_dataframe()
# t = sns.lineplot(data=time)
# t.set(title="Time it takes to clean all cells", ylabel="Percentage of cleaned cells")
# plt.show()

time = model.datacollector.get_agent_vars_dataframe()
last_step = time.index.get_level_values("Step").max()
final_trash = time.xs(last_step, level="Step")["Time"]
# Create a histogram of wealth at the last step
t = sns.histplot(final_trash, discrete=True)
t.set(
    title="Distribution of trash at the end of simulation",
    xlabel="Time",
    ylabel="Number of trashes",
);
plt.show()

# -----------------------------------------------------------------ARCHIVO MODEL-----------------------------------------------------------------
# def compute_time(model):
#  M = model.num_agents 


# DENTRO DE MODEL __init__
# self.datacollector = mesa.DataColletor(
#    model_reporters={"Tiempo": compute_time}, agent_reporters={"Time": "time"}
# )

# DENTRO DE MODEL step
# self.datacollector.collect(self)