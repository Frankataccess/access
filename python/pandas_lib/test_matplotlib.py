import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("python\pandas\correlation.csv")

df.plot(kind = 'hist', x = 'Duration', y = 'Maxpulse')

plt.show()