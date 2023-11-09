from limpieza_model import LimpiezaModel
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

model = LimpiezaModel(10, 10, 30, 30)
for i in range(100):
    model.step()
