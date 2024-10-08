import streamlit as st
import joblib
import pandas as pd

# working_dir = os.path.dirname(os.path.abspath(__file__))
# model_path = f"{working_dir}\random_forest_model.pkl"
loaded_model = joblib.load('random_forest_model.pkl')

st.title("Will it Rain?")

def predict(input_data):
    input_data = pd.DataFrame(input_data)
    prediction = loaded_model.predict(input_data)
    return prediction

locations = ['Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree',
       'NorahHead', 'NorfolkIsland', 'Penrith', 'Richmond', 'Sydney',
       'SydneyAirport', 'WaggaWagga', 'Williamtown', 'Wollongong',
       'Canberra', 'Tuggeranong', 'MountGinini', 'Ballarat', 'Bendigo',
       'Sale', 'MelbourneAirport', 'Melbourne', 'Mildura', 'Nhil',
       'Portland', 'Watsonia', 'Dartmoor', 'Brisbane', 'Cairns',
       'GoldCoast', 'Townsville', 'Adelaide', 'MountGambier', 'Nuriootpa',
       'Woomera', 'Witchcliffe', 'PearceRAAF', 'PerthAirport', 'Perth',
       'SalmonGums', 'Walpole', 'Hobart', 'Launceston', 'AliceSprings',
       'Darwin', 'Katherine', 'Uluru']

Location = st.selectbox("Choose your location:", locations)
MinTemp = st.number_input("Minimum Temperature", min_value=0.0, max_value=100.0)
MaxTemp = st.number_input("Maximum Temperature", min_value=0.0, max_value=100.0)
Rainfall = st.number_input('RainFall', min_value=0.0, max_value=1.0)
#WindGustDir = st.selectbox("WindGustDir",)
