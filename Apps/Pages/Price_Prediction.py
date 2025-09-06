import streamlit as st 
import pickle 
import pandas as pd 
import numpy as np 

st.set_page_config(page_title='Price Prediction')
st.title('Price Prediction')

with open('Models/df.pkl' , 'rb') as file:
    df = pickle.load(file)

with open('Models/final_xgb_pipeline.pkl','rb') as model :
    pipeline = pickle.load(model)

# st.dataframe(df)
st.header('Enter your Inputs')

# property type
property_type = st.selectbox('Property Type' , ['flat','house'])

# sector 
sector = st.selectbox('Sector' , sorted(df['sector'].unique().tolist()))

bedroom = float(st.selectbox('Number of BedRooms' , sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('Number of BathRooms' , sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('Balconies' , sorted(df['balcony'].unique().tolist()))

property_age  = st.selectbox('Property Age' , sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area'))

servant_room = float(st.selectbox('Servant Room' , sorted(df['servant room'].unique().tolist())))

store_room = float(st.selectbox('Store Room' , sorted(df['store room'].unique().tolist())))

furnishing_type = st.selectbox('Furnishing Type' , sorted(df['furnishing_type'].unique().tolist()))
luxury_score = st.selectbox('Luxury Category' , sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category' , sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    # Create a df 
    data = [[property_type , sector,bedroom,bathroom,balcony,property_age,built_up_area,servant_room,store_room,furnishing_type,luxury_score,floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    # st.dataframe(one_df)
    # Prediction After runnning Pipeline 
    base_price = np.expm1(pipeline.predict(one_df))[0]

# Convert to Crores 
    low_price = float(base_price - 0.21)
    high_price = float(base_price + 0.21)

    st.write(
    f"The Price of the Property with Selected Inputs lies between {low_price:.2f} Cr and {high_price:.2f} Cr"
    )



    



