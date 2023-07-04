import streamlit as st

st.set_page_config(
    page_title="Happy birthday Sahana",
    page_icon=":stars:",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

def style():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

style()

st.markdown('<div class="New"><h1>Happy Birthday</h1></div>', unsafe_allow_html=True)

st.markdown("<p>Wishing you a very happy birthday, Sahana! May all your dreams come true and may this year bring you lots of joy and happiness.</p>", unsafe_allow_html=True)

st.subheader("Many many happy returns of the day")

st.markdown("<p>To the most caring and kind-hearted person I know, thank you for filling my life with enjoyment and laughter. Your smile brightens up my world every day. May this birthday be the beginning of an extraordinary year for you, filled with endless happiness, success, and fulfillment. You are the best thing that ever happened to me. Happy birthday, SAHANA</p>", unsafe_allow_html=True)

if st.button("Your Gift"):
    st.markdown('<div class="text-gift"><a href="https://sahana.onrender.com">Click Here</a></div>', unsafe_allow_html=True)

