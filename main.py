import streamlit as st
import streamlit as st

import wikipedia
import time
st.title("Hi 🙌")
st.text("Hello Welcome to this website:")
go = st.text_input("What do you want to search?\n")
time.sleep(2)
su = wikipedia.summary(go)
st.write(su)

st.subheader("Simplest Python code to make an ai")
st.code("""import wikipedia as wk
ask = input("Enter anything:\n")
summary = wk.summary(ask, sentences='3')
print("summary")""")
