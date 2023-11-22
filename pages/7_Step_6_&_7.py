# Predicting on unseen data
import streamlit as st

st.title("Testing Phase: Prediction and Evaluation")

st.header("Predicting on Unseen Data")

CODE_SNIPPET = '''
y_test_pred = model.predict(X_test_transformed)
'''

st.code(CODE_SNIPPET, language='python')

st.header("Evaluating the Model")

CODE_SNIPPET_1 = '''
from sklearn import metrics
metrics.accuracy_score(y_test, y_test_pred)
'''

CODE_SNIPPET_2 = '''
from sklearn import metrics
metrics.confusion_matrix(y_test, y_test_pred)
'''

CODE_SNIPPET_3 = '''
from sklearn import metrics
metrics.classification_report(y_test, y_test_pred)
'''

CODE_SNIPPET_4 = '''
from sklearn import metrics
metrics.mean_absolute_error(y_test, y_test_pred)
'''

CODE_SNIPPET_5 = '''
from sklearn import metrics
metrics.mean_squared_error(y_test, y_test_pred)
'''

CODE_SNIPPET_6 = '''
from sklearn import metrics
np.sqrt(metrics.mean_squared_error(y_test, y_test_pred))
'''

CODE_SNIPPET_7 = '''
from sklearn import metrics
metrics.r2_score(y_test, y_test_pred)
'''

option = st.selectbox('Select the evaluation metric? (HINT: Step 1 - Based on target variable)',
                      ('Classification', 'Regression'))

if(option=='Classification'):
    tab1, tab2, tab3 = st.tabs(["Accuracy", "Confusion Matrix", 
                                "Classification Report"])
    with tab1:
        st.code(CODE_SNIPPET_1, language='python')
    with tab2:
        st.code(CODE_SNIPPET_2, language='python')
    with tab3:
        st.code(CODE_SNIPPET_3, language='python')
elif(option=='Regression'):
    tab1, tab2, tab3, tab4 = st.tabs(["MAE", "MSE", 
                                    "RMSE", 
                                    "R2 Score"])
    with tab1:
        st.code(CODE_SNIPPET_4, language='python')
    with tab2:
        st.code(CODE_SNIPPET_5, language='python')
    with tab3:
        st.code(CODE_SNIPPET_6, language='python')
    with tab4:
        st.code(CODE_SNIPPET_7, language='python')
