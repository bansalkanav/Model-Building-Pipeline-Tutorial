# Split the data into train and test

import streamlit as st

st.title("Split the data into Train and Test set")

with st.expander("See explanation"):
    st.write("""
            **Train Set (i.e. X_train, y_train):** Used to train a model/pattern.  
            **Test Set (i.e. X_test, y_test):** Used to test the models performance.
            """)

CODE_SNIPPET = '''
# Code Snippet
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                            train_size=0.7, 
                                            random_state=100)
'''

st.code(CODE_SNIPPET, language='python')

with st.expander("Important Note"):
    st.write("""
            Never apply data preparation before train_test_split.  
            It can lead to **Data Leakage** problem.
            **Never make this mistake.**
            """)
