import streamlit as st

st.set_page_config(
    page_title='Customer Churn Dashboard',
    page_icon='😎'
)

st.title('our models')


model_type = st.selectbox("Models:", ['Decision Tree', 'Random Forest Classifier'])

is_gs = st.checkbox('GridSearch')


if is_gs:
    col1, col2 = st.columns(2)
    if model_type == 'Decision Tree':
        best_params = {'criterion': 'entropy',
                    'max_depth': 6,
                    'min_samples_leaf': 5,
                    'random_state': 0}
    elif model_type == 'Random Forest Classifier':
        best_params = {'criterion': 'entropy',
                    'max_depth': 10,
                    'min_samples_leaf': 5,
                    'random_state': 42}

    with col2:
        st.subheader('Best Parameters for GridSearch')
        if model_type:
            for key, value in best_params.items():
                st.write(f'{key}: {value}')
    with col1:
        if model_type == 'Decision Tree':
            st.write('Accuracy: 86.28%')
        elif model_type == 'Random Forest Classifier':
            st.write('Accuracy: 88.56%')
else:
    if model_type == 'Decision Tree':
        st.write('Accuracy: 85.89%')
    elif model_type == 'Random Forest Classifier':
        st.write('Accuracy: 86.86%')

st.sidebar.success('Select a page above')