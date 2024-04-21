import streamlit as st
from streamlit_extras.colored_header import colored_header

def Reviews() -> None:
    colored_header(
             label="Reviews.",
             description="Take your time to talk to us about how you feel about our produce",
             color_name="gray-70"
             )
    st.sidebar.header(":gray[Shopping 24..]")
    st.toast('Hello Valued Customer.')

    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")


Reviews()