import matplotlib.pyplot as plt
import streamecg


data = streamecg.readFromBinary("./data.txt")

fig,axes = plt.subplots(1,1,figsize=(10,5))
axes.plot(data, 'b', linewidth=0.5)
plt.show()

