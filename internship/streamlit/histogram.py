#import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [4, 9, 2]
y = [2, 5, 12]
colors=["xkcd:baby blue", "xkcd:baby blue", "xkcd:dark blue"]

fig, ax = plt.subplots()

ax.bar(x, y, 
       width=1, 
       edgecolor="white", 
       linewidth=0.7,
       color=colors,
       )

"""
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
"""

fig.canvas.manager.set_window_title("Guessing Performance by Person")
ax.set_title("Guessing Performance by Person")
ax.set_xlabel("Number of Guesses Taken")
ax.set_ylabel("People")
plt.show()

"""
chart_data = {
    4: 3,
    5: 2,
    9: 7}

st.bar_chart(
    data=chart_data,
    x_label="Number of Guesses Taken",
    y_label="People",
)
"""