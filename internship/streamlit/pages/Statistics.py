import streamlit as st
import matplotlib.pyplot as plt
import json

#need to hide before game finishes. and appear after. 
#still testing

with open('saved_guess_data.json', 'r') as openfile:
    st.session_state.count_dict = json.load(openfile)

x = st.session_state.count_dict["guess_num"]
y = st.session_state.count_dict["population"]
colors=st.session_state.count_dict["colors"]

fig, ax = plt.subplots()

ax.bar(x, y, 
    width=1, 
    edgecolor="white", 
    linewidth=0.7,
    color=colors,
    )

ax.set_title("Guessing Performance by Person")
ax.set_xlabel("Number of Guesses Taken")
ax.set_ylabel("People")
st.pyplot(fig)