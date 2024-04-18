import streamlit as st
import joblib

def run_cardio_disease_prediction_app():

    model = joblib.load('heart_svm_model.joblib')
    
    
    def predict(age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active):
        age = age*365
        if gender=='Female':
            gender = int(1)
        elif gender=='Male':
            gender=int(2)
        if cholesterol == 'Low':
            cholesterol=int(1)
        elif cholesterol== 'Medium':
            cholesterol=int(2)
        elif cholesterol=='High':
            cholesterol=int(3)
        if gluc == 'Low':
            gluc=int(1)
        elif gluc== 'Medium':
            gluc=int(2)
        elif gluc=='High':
            gluc=int(3)
        if smoke =='Yes':
            smoke=int(1)
        elif smoke=='No':
            smoke=int(0)
        if alco =='Yes':
            alco=int(1)
        elif alco=='No':
            alco=int(0)
        if active =='Yes':
            active=int(1)
        elif active=='No':
            active=int(0)
        

        
        input_data = [[age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active]]
        result = model.predict(input_data)
        return result[0]
    
    
    
    
    st.title('Cardiovascular Prediction')

    
    col1, col2, col3 = st.columns(3)

    
    with col1:
        age = st.number_input('Age in years',min_value=0, step=1)
        weight = st.number_input('Weight(Kg)',min_value=1,step=1)
        cholesterol =st.selectbox( 'Colesterol',('Low', 'Medium','High'), index=1)
        alco=st.selectbox( 'Alcohol',('Yes', 'No'), index=1)
    # Input widgets in the second column
    with col2:
        gender = st.selectbox( 'Gender',('Female', 'Male'), index=0)
        ap_hi = st.number_input('High BP',min_value=0)
        gluc = st.selectbox( 'Glucos',('Low', 'Medium','High'), index=1)
        active=st.selectbox( 'Active',('Yes', 'No'), index=1)
    # Input widgets in the third column
    with col3:
        height = st.number_input('Height(Cm)',min_value=1)
        ap_lo = st.number_input('Low BP', min_value=0)
        smoke =st.selectbox( 'Smoke',('Yes', 'No'), index=1)
        
    
    # Predict button
    if st.button('Predict'):
        prediction = predict(age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active)
        if prediction == 0:
            st.write('Prediction: No')
            
        else:
            st.write('Prediction: Yes')
            
