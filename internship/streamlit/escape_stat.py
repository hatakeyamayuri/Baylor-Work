import streamlit as st
import json
import os

st.title("40X ESCAPE")

#dictionary of the pill values. dashes are stylistic
map_escape_keys = { 
    0: "---E---",
    1: "---S---",
    2: "---C---",
    3: "---A---",
    4: "---P---",
    5: "---E---",
}

#initializing session variables if 1st run
if 'before_selection' not in st.session_state: 
    st.session_state.before_selection = [] #the un-updated list for the specfic run
    st.session_state.escape = [] #updated list
    st.session_state.counter = 0 #number of guesses taken

    if not os.path.isfile("saved_guess_data.json"): #if file doesn't exist
        st.session_state.count_dict = { #creates empty dict
            "guess_num" : [],
            "population" : [],
            "colors" : [],
        }
    else:
        #reads and sets dict
        with open('saved_guess_data.json', 'r') as openfile:
            st.session_state.count_dict = json.load(openfile)

#changes the state of the pill at index inputted, thru presence in list
def toggle(i):
    global escape
    if i in set(st.session_state.escape):
        st.session_state.escape.remove(i)
    else:
        st.session_state.escape.append(i)

#runs when a pill state is changed
def alter_pill():
    global before_selection
    global counter

    to_change = [] #to hold the indexs of pills to change state
    st.session_state.counter += 1

    #compares the updated and not-updated list to find the difference and therefore the index of the pill clicked
    if len(st.session_state.escape)>len(st.session_state.before_selection):
        clicked = list(set(st.session_state.escape) - set(st.session_state.before_selection))
    else:
        clicked = list(set(st.session_state.before_selection) - set(st.session_state.escape))

    if len(clicked) == 0: #to make not run on/ no chage made on init
        pass

    #changes the state of the 2 pills next to clicked ONLY
    elif clicked[0] == 0: #very left
        to_change.append(clicked[0])
        to_change.append(clicked[0] +1)
    elif clicked[0] == len(map_escape_keys)-1: #very right
        to_change.append(clicked[0])
        to_change.append(clicked[0] -1)
    else:
        to_change.append(clicked[0])
        to_change.append(clicked[0] +1)
        to_change.append(clicked[0] -1)
    for i in to_change:
        toggle(i)

placeholder = st.empty()
with placeholder.container(): #so can delete after winning
    st.session_state.before_selection = st.pills(
        label="Select all the letters",
        key="escape",
        default=st.session_state.escape,
        options=map_escape_keys.keys(),
        format_func=lambda option: map_escape_keys[option],
        selection_mode="multi",
        on_change=alter_pill,
    )

#if all pills are selected/ game is finished
if len(st.session_state.escape) == len(map_escape_keys): 
    placeholder.empty() #delete pills
    st.subheader("ESCAPED 💨")
    st.write(f"You took {st.session_state.counter} steps to solve.")

    """""" #configure dict with updated data

    #checks if this number of guesses had been done before
    if st.session_state.counter in set(st.session_state.count_dict["guess_num"]):
        index = st.session_state.count_dict["guess_num"].index(st.session_state.counter)
        st.session_state.count_dict["population"][index] += 1 #adds 1 in population of that guess/index 
    else:   
        #if not, creates its index set of guess number
        st.session_state.count_dict["guess_num"].append(st.session_state.counter)
        st.session_state.count_dict["population"].append(1)
        index = st.session_state.count_dict["guess_num"].index(st.session_state.counter)

    #sets empty list of colots with all baby blue except current guess number
    for i in range(len(st.session_state.count_dict["guess_num"])):
        st.session_state.count_dict["colors"].append("xkcd:baby blue")
    st.session_state.count_dict["colors"][index] = "xkcd:dark blue"

    """""" #chart creation

    import matplotlib.pyplot as plt

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

    """""" #dataset saving

    st.session_state.count_dict["colors"] = [] #sets colors list empty

    #saves dict/dataset as json file
    save_json = json.dumps(st.session_state.count_dict)
    with open("saved_guess_data.json", "w") as outfile:
        outfile.write(save_json)