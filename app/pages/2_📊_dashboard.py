import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title='Customer Churn Dashboard',
    page_icon='😎'
)

st.title('stats dashboard')

st.sidebar.success('Select a page above')

df = st.session_state['df']
columns = st.session_state['columns']

selected_feature = st.selectbox("Features:", columns)



if selected_feature:
    st.title(f'Displaying graph for {selected_feature}')

if selected_feature == 'Churn':
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(df['Churn'].value_counts(), labels=['No churn', 'Yes churn'], autopct='%1.2f%%')
    ax.set_title('Churn Percentage')
    st.pyplot(fig)
elif selected_feature == 'Gender':
    # view relation between gender and customer churn
    sns.countplot(x = 'Gender', data = df, hue = 'Churn')
    plt.title('Gender vs. Churn')
    plt.xlabel('Gender') # title x axis
    plt.ylabel('Churn count') # title y axis
    st.pyplot()
elif selected_feature == 'Age':
    # view age distribution
    sns.histplot(data = df, x= 'Age', hue = 'Churn', multiple='stack', kde=True)
    plt.title('Age vs. Churn')
    st.pyplot()
elif selected_feature == 'CreditScore':
    # make plots for credit score
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    sns.boxplot(x='Churn', y='CreditScore', data=df, ax=ax[0])
    sns.violinplot(x='Churn', y='CreditScore', data=df, ax=ax[1])
    st.pyplot(fig)
elif selected_feature == 'Geography':
    sns.countplot(x = 'Geography', hue = 'Churn', data = df)
    plt.title('Geography vs. Churn')
    plt.xlabel('Country of residence')
    plt.ylabel('Churn count')
    st.pyplot()
elif selected_feature == 'Tenure':
    sns.countplot(x='Tenure', hue='Churn', data=df)
    st.pyplot()
elif selected_feature == 'Balance':
    sns.histplot(data=df, x='Balance', hue='Churn', multiple='stack')
    st.pyplot()
elif selected_feature == 'NumOfProducts':
    sns.countplot(x='NumOfProducts', hue='Churn', data=df)
    st.pyplot()
elif selected_feature == 'HasCrCard':
    sns.countplot(x='HasCrCard', hue='Churn', data=df)
    st.pyplot()
elif selected_feature == 'IsActiveMember':
    sns.countplot(x='IsActiveMember', hue='Churn', data=df)
    st.pyplot()
elif selected_feature == 'EstimatedSalary':
    sns.histplot(x='EstimatedSalary', hue='Churn', multiple='stack', data=df)
    st.pyplot()