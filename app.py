import streamlit as st
from pages import page_1, page_2

if 'page' not in st.session_state:
	st.session_state.page = 1

def set_page(pgNumber):
	st.session_state = pgNumber

if st.session_state.page == 1:
	page_1(set_page)
elif st.session_state.page == 2:
	page_2(set_page)
