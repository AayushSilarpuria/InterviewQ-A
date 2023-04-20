import pandas as pd
import matplotlib.pyplot as plt

#df =pd.DataFrame()

#print(df.to_string())

ff =pd.read_json("data.json")
print(ff.to_string())


csv = pd.read_csv("data.csv")
print(csv)

csv.plot()
plt.show()