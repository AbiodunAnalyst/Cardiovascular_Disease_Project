import pickle
import streamlit as st
import numpy as np

model = pickle.load(open('C:/Users/NEW USER/OneDrive/Desktop/PROJECT TWO PREDICT/random_forest_model_death.pkl','rb'))




def main():
    st.title('Prediction of Death due to Cardiovascular Disease')

    #input variables
    age  = st.text_input('Age')               
    anaemia  = st.text_input('Anaemia')                  
    creatinine_phosphokinase  = st.text_input('Creatinine_Phosphokinase')
    diabetes   = st.text_input('Diabetes')                 
    ejection_fraction  = st.text_input('Ejection_fraction')         
    high_blood_pressure  = st.text_input('High_blood_pressure')       
    platelets  = st.text_input('Platelets')          
    serum_creatinine  = st.text_input('Serum_creatinine')   
    serum_sodium  = st.text_input('Serum_sodium')         
    gender   = st.text_input('Gender')                   
    smoking  = st.text_input('Smoking')                 
    time     = st.text_input('Time')        

    # Reshape input as a 2D array
    try:
        input_data = [[float(age), float(anaemia), float(creatinine_phosphokinase), float(diabetes),
            float(ejection_fraction), float(high_blood_pressure), float(platelets), float(serum_creatinine), float(serum_sodium),
            float(gender), float(smoking), float(time)]]

        #prediction
        if st.button('Predict'):
            makeprediction = model.predict(np.array([input_data]).reshape(1,-1))
            output= makeprediction[0]
            
            decoded_output = 'Death' if output == 1 else 'No Death'
            
            st.success('Predicted condition: {}'.format(decoded_output))  

    except ValueError:
        st.error('Please enter valid numeric values for all input fields.')

if __name__ == '__main__':
    main()        
