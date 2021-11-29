import streamlit as st

from bbquote_764.lib import get_quote

quote = get_quote()  # assuming the function returns an author and a quote

st.write(f"{quote}")
