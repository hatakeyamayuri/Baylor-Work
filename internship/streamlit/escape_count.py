import streamlit as st

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
    st.session_state.counter = 0 

#effectively changes the state of the pill at index inputted thru presence in list
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
with placeholder.container(): #so can dynamically delete after winning
    st.session_state.before_selection = st.pills(
        label="Select all the letters",
        key="escape",
        default=st.session_state.escape,
        options=map_escape_keys.keys(),
        format_func=lambda option: map_escape_keys[option],
        selection_mode="multi",
        on_change=alter_pill,
    )

if len(st.session_state.escape) == len(map_escape_keys): #if all pills are selected
    placeholder.empty() #delete pills
    st.subheader("ESCAPED 💨")
    st.write(f"You took {st.session_state.counter} steps to solve.")

""""""

