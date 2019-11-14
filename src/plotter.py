from datetime import datetime
import matplotlib.pyplot as plt

def plot_with_date(date, value):
    plt.figure(figsize=(20, 10))
    plt.plot(date, value)
    plt.ylim(ymin=0)
    plt.show()
