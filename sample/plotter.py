from datetime import datetime
import matplotlib.pyplot as plt

def plot_graph(x, y):
    plt.figure(figsize=(20, 10))
    plt.plot(x, y)
    plt.ylim(ymin=0)
    plt.show()
