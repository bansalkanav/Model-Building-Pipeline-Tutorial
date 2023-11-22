# Building a Model
import streamlit as st

st.title("Training Phase: Building a Model")

CODE_SNIPPET_1 = '''
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(X_train_transformed, y_train)
'''

CODE_SNIPPET_2 = '''
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train_transformed, y_train)
'''

CODE_SNIPPET_3 = '''
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train_transformed, y_train)
'''

CODE_SNIPPET_4 = '''
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train_transformed, y_train)
'''

CODE_SNIPPET_5 = '''
from sklearn.svm import SCV
classifier = SVC()
classifier.fit(X_train_transformed, y_train)
'''

CODE_SNIPPET_6 = '''
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train_transformed, y
'''

CODE_SNIPPET_7 = '''
from sklearn.neighbors import KNeighborsRegressor
regressor = KNeighborsRegressor()
regressor.fit(X_train_transformed, y_train)
'''

CODE_SNIPPET_8 = '''
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train_transformed, y_train)
'''

CODE_SNIPPET_9 = '''
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train_transformed, y_train)
'''

CODE_SNIPPET_10 = '''
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor()
regressor.fit(X_train_transformed, y_train)
'''

option = st.selectbox('Select the Algorithm? (HINT: Step 1 - Based on target variable)',
                      ('Classification', 'Regression'))

if(option=='Classification'):
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["KNN", "DT", "Naive Bayes", 
                                                  "Logistic Regression", "SVC", 
                                                  "Random Forest"])
    with tab1:
        st.code(CODE_SNIPPET_1, language='python')
    with tab2:
        st.code(CODE_SNIPPET_2, language='python')
    with tab3:
        st.code(CODE_SNIPPET_3, language='python')
    with tab4:
        st.code(CODE_SNIPPET_4, language='python')
    with tab5:
        st.code(CODE_SNIPPET_5, language='python')
    with tab6:
        st.code(CODE_SNIPPET_6, language='python')
elif(option=='Regression'):
    tab1, tab2, tab3, tab4 = st.tabs(["KNN", "DT", 
                                    "Linear Regression", 
                                    "Random Forest"])
    with tab1:
        st.code(CODE_SNIPPET_7, language='python')
    with tab2:
        st.code(CODE_SNIPPET_8, language='python')
    with tab3:
        st.code(CODE_SNIPPET_9, language='python')
    with tab4:
        st.code(CODE_SNIPPET_10, language='python')
