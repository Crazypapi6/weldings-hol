import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.streaming_write import write
import time
from streamlit_extras.stateful_chat import add_message, chat

def Reviews() -> None:
    response = """
    Adds a chat message to the chat container.
    This command can only be used inside the `chat` container. The message
    will be displayed in the UI and added to the chat history so that the same
    message will be automatically displayed on reruns.
"""
    colored_header(
             label="Reviews.",
             description="Take your time to talk to us about how you feel about our produce",
             color_name="gray-70"
             )
    st.sidebar.header(":gray[Weldings Hol.]")
    st.toast('Hello Valued Customer.')

Reviews()