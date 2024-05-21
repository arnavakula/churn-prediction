import streamlit as st

def page_1(setPg):
	st.sidebar.title("Customer Churn")

	gr_page = st.button("Graph something")
	mod_page = st.button("Model something")

	if gr_page:
		setPg(2)
		st.rerun()

def page_2(setPg):
	selected_features = st.setbox("Features:", ["Option 1", "Option 2", "Option 3"])
	if selected_features:
		st.title(f'You selected {selected_features}!!!');
		   
		
