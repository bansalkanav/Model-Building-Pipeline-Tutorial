# Identify Input and Output
import streamlit as st

st.title("Identify Target Variable and Predictors")

with st.expander("See explanation"):
    st.write("""
            **Identifying Target Variable (i.e. y):** Helps in choosing Algorithm and Evaluation Metrics.  
            **Identifying Predictor Variables (i.e. X):** Helps in choosing correct Data Preparation Strategy.
            """)

CODE_SNIPPET_1 = '''
# Code Snippet 1
y = df['target']
X = df[['predictor_1', 'predictor_2', ...]]
'''

CODE_SNIPPET_2 = '''
# Code Snippet 2
y = df.pop("target")
X = df
'''

st.code(CODE_SNIPPET_1, language='python')

st.code(CODE_SNIPPET_2, language='python') 

with st.expander("Important Note"):
    st.write("""
        There can be many predictors given in the dataset. You must have already done an end-to-end EDA.  
        Now it is your responsibility to choose the best predictors.  
        Identifying best predictor can make sure that you are building the model on **Good Quality Data**.
        """)
