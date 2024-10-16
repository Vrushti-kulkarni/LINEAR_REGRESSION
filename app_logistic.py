import streamlit as st
import joblib
import pandas as pd

# working_dir = os.path.dirname(os.path.abspath(__file__))
# model_path = f"{working_dir}\random_forest_model.pkl"
loaded_model = joblib.load('logistic_rain.pkl')

st.title("Will it Rain?")

def predict(input_data):
    input_data = pd.DataFrame(input_data)
    prediction = loaded_model.predict(input_data)
    return prediction


MinTemp = st.number_input("Minimum Temperature", min_value=0.0, max_value=100.0)
MaxTemp = st.number_input("Maximum Temperature", min_value=0.0, max_value=100.0)
Rainfall = st.number_input('RainFall', min_value=0.0, max_value=1.0)
WindGustSpeed = st.number_input('WindGustSpeed', value=30.0)
WindSpeed9am = st.number_input('WindSpeed9am', value=10.0)
WindSpeed3pm = st.number_input('WindSpeed3pm', value=15.0)
Humidity9am = st.number_input('Humidity9am', value=80.0)
Humidity3pm = st.number_input('Humidity3pm', value=60.0)
Pressure9am = st.number_input('Pressure9am', value=1015.0)
Pressure3pm = st.number_input('Pressure3pm', value=1010.0)
Temp9am = st.number_input('Temp9am', value=15.0)
Temp3pm = st.number_input('Temp3pm', value=25.0)
RISK_MM = st.number_input('RISK_MM', value=0.0)
RainToday_encoded = st.selectbox('Rain Today (1: Yes, 0: No)', [0, 1])
# List of locations
locations = ['Location_Adelaide', 'Location_Albury', 'Location_AliceSprings', 
             'Location_BadgerysCreek', 'Location_Ballarat', 'Location_Bendigo', 
             'Location_Brisbane', 'Location_Cairns', 'Location_Canberra', 
             'Location_Cobar', 'Location_CoffsHarbour', 'Location_Dartmoor', 
             'Location_Darwin', 'Location_GoldCoast', 'Location_Hobart', 
             'Location_Katherine', 'Location_Launceston', 'Location_Melbourne', 
             'Location_MelbourneAirport', 'Location_Mildura', 'Location_Moree', 
             'Location_MountGambier', 'Location_MountGinini', 'Location_Nhil', 
             'Location_NorahHead', 'Location_NorfolkIsland', 'Location_Nuriootpa', 
             'Location_PearceRAAF', 'Location_Penrith', 'Location_Perth', 
             'Location_PerthAirport', 'Location_Portland', 'Location_Richmond', 
             'Location_Sale', 'Location_SalmonGums', 'Location_Sydney', 
             'Location_SydneyAirport', 'Location_Townsville', 'Location_Tuggeranong', 
             'Location_Uluru', 'Location_WaggaWagga', 'Location_Walpole', 
             'Location_Watsonia', 'Location_Williamtown', 'Location_Witchcliffe', 
             'Location_Wollongong', 'Location_Woomera']

location_inputs = {}

for loc in locations:
    location_inputs[loc] = st.selectbox(f'{loc}', [0, 1], index=0)



