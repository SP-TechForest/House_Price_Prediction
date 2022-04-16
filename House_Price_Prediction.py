import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import streamlit as st
st.header(
    "Get the price of your home"
)
data = pd.read_csv("final.csv")
feature = data.drop(columns= ['price','Unnamed: 0'])
target = data['price']
x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, random_state = 0)
from sklearn.linear_model import LinearRegression
le = LinearRegression()
le.fit(x_train, y_train)
area_list = list(feature.columns[5:])
area_name = st.selectbox("Select Area Name", area_list)
sqft = st.text_input("Enter Sq.foot area")
bhk = st.text_input("Enter the number of BHK")
bal = st.text_input("Enter the number of balcony")
br = st.text_input("Enter the number of bath-room")

# y_pred = le.predict(x_test)
# import sklearn
# print(sklearn.metrics.r2_score(y_test,y_pred))

def model_predict_function(location, total_sqft, bath, balcony, bhk):
    index = np.where(feature.columns == location)[0][0]
    x = np.zeros(len(feature.columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if index >= 0:
        x[index] = 1

    return le.predict([x])

vell = st.button("Get Price")
if vell == True:
    val = model_predict_function(area_name, sqft, br, bal,bhk)
    val = int(val)
    if val > 0:
        st.write("Expected price of you house, on the bases of your preferences is: ", val)
    else:
        st.write("Sorry, You entered something wrong, Check your Choices")
print(feature)


