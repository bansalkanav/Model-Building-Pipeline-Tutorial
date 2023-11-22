# Data Preparation on Training Data
import streamlit as st

st.title("Feature Engineering: Preparing the Training Data (i.e. X_train)")


with st.expander("See explanation"):
    st.write("""
            Here we have covered Feature Engineering for Continuous and Discrete Features.
            """)

CODE_SNIPPET_1 = '''
# Rescaling the Numerical Features using Standardization
from sklearn.preprocessing import StandardScaler

# Creating object of StandardScaler class
scaler = StandardScaler()

# column names are (annoyingly) lost after Scaling
# (i.e. the dataframe is converted to a numpy ndarray)
X_train_transformed = pd.DataFrame(scaler.fit_transform(X_train), 
				columns=X_train.columns, 
				index=X_train.index)

X_train_transformed.head()
'''

CODE_SNIPPET_1_2_TEST = '''
X_test_transformed = pd.DataFrame(scaler.transform(X_test), 
                                   columns=X_test.columns, 
                                   index=X_test.index)
'''


CODE_SNIPPET_2 = '''
# Rescaling the Numerical Features using Normalization
from sklearn.preprocessing import MinMaxScaler

# Creating object of MinMaxScaler class
scaler = MinMaxScaler()

# column names are (annoyingly) lost after Scaling
# (i.e. the dataframe is converted to a numpy ndarray)
X_train_transformed = pd.DataFrame(scaler.fit_transform(X_train), 
				columns=X_train.columns, 
				index=X_train.index)

X_train_transformed.head()
'''

CODE_SNIPPET_3 = '''
# OneHotEncoding the categorical features
from sklearn.preprocessing import OneHotEncoder

# Creating object of OneHotEncoder
encoder = OneHotEncoder(drop='first', sparse=False)

# column names are (annoyingly) lost after OneHotEncoding
# (i.e. the dataframe is converted to a numpy ndarray)
X_train_transformed = pd.DataFrame(encoder.fit_transform(X_train), 
				columns=encoder.get_feature_names_out(X_train.columns), 
				index=X_train.index)

X_train_transformed.head()
'''

CODE_SNIPPET_3_TEST = '''
X_test_transformed = pd.DataFrame(encoder.fit_transform(X_test), 
                        columns=encoder.get_feature_names_out(X_train.columns), 
                        index=X_test.index)
'''


CODE_SNIPPET_4 = '''
# Create an empty dataframe which will contain the transformed data
X_train_transformed = pd.DataFrame(index=X_train.index)

# Define an encoding based on the ranking of each category
cut_encoder = {'Fair' : 1, 'Good' : 2, 'Very Good' : 3, 'Ideal' : 4, 'Premium' : 5}
color_encoder = {'J':1, 'I':2, 'H':3, 'G':4, 'F':5, 'E':6, 'D':7}

# Apply the encoding
X_train_transformed['cut'] = X_train['cut'].apply(lambda x : cut_encoder[x])
X_train_transformed['color'] = X_train['color'].apply(lambda x : color_encoder[x])
'''

CODE_SNIPPET_4_TEST = '''
X_test_transformed = pd.DataFrame(index = X_test.index)
X_test_transformed['cut'] = X_test['cut'].apply(lambda x : cut_encoder[x])
X_test_transformed['color'] = X_test['color'].apply(lambda x : color_encoder[x])
'''


CODE_SNIPPET_5 = '''
# Separate Discrete and Continuous Columns
X_train_cat = X_train.select_dtypes(include=['object'])
X_train_num = X_train.select_dtypes(include=['int64', 'float64'])

# Apply Standardization/Normalisation for X_train_num
# Apply OHE/Label Encoding for X_train_cat

# Concatenate the two
X_train_transformed = pd.concat([X_train_num_transformed, X_train_cat_transformed], axis=1)
'''


option = st.selectbox('Select the datatypes of columns in your X_train?',
                      ('Continuous', 'Discrete', 'Both'))

if(option=='Continuous'):
    st.write("""
            For Continuous Predictors, it is very important that we rescale them.  
            This is because every predictor might be measured on a different scale.  
            Many machine learning and deep learning algorithms won't be able to learn patterns.  
            There are two strategies to rescale the Continuous Data:
            1. Standardization
            2. Normalization
            """)
    tab1, tab2 = st.tabs(["Standardization", "Normalization"])
    with tab1:
        st.code(CODE_SNIPPET_1, language='python')
    with tab2:
        st.code(CODE_SNIPPET_2, language='python')
    toggle = st.toggle("Click here to learn how to rescale the X_test Data")
    if toggle:
        st.code(CODE_SNIPPET_1_2_TEST, language='python')
elif(option=='Discrete'):
    st.write("""
            For Discrete Predictors (if non numerical), it is very important that we transform them.  
            This is because algorithms can't take non numerical data as input.  
            There are two strategies for this transformation:
            1. One Hot Encoding
            2. Label Encoding
            """)
    tab1, tab2 = st.tabs(["One Hot Encoding", "Label Encoding"])
    with tab1:
        st.code(CODE_SNIPPET_3, language='python')
        toggle_1 = st.toggle("Click here to learn how to encode the X_test Data", key='c_1')
        if toggle_1:
            st.code(CODE_SNIPPET_3_TEST, language='python')

    with tab2:
        st.code(CODE_SNIPPET_4, language='python')
        toggle_2 = st.toggle("Click here to learn how to encode the X_test Data", key='c_2')
        if toggle_2:
            st.code(CODE_SNIPPET_4_TEST, language='python')

elif(option=="Both"):
    st.code(CODE_SNIPPET_5, language='python')