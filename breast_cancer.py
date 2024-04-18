import streamlit as st
import joblib

def run_breast_cancer_prediction_app():

    model = joblib.load('logistic_reg_model.joblib')
    
    
    def predict_diabetes(Clump_thickness,Uniformity_of_cell_size,Marginal_adhesion,Single_epithelial_cell_size,Bare_nuclei,Bland_chromatin,Normal_nucleoli,Mitoses):
        input_data = [[Clump_thickness,Uniformity_of_cell_size,Marginal_adhesion,Single_epithelial_cell_size,Bare_nuclei,Bland_chromatin,Normal_nucleoli,Mitoses]]
        result = model.predict(input_data)
        return result[0]
    
    
    
    
    st.title('Breast Cancer Prediction')

    
    col1, col2, col3 = st.columns(3)

    # Input widgets in the first column
    with col1:
        Clump_thickness = st.number_input('Clump thickness',min_value=1,max_value=10, step=1)
        Single_epithelial_cell_size = st.number_input('Single epithelial cell size',min_value=1,max_value=10)
        Normal_nucleoli = st.number_input('Normal nucleoli',min_value=1,max_value=10)
    # Input widgets in the second column
    with col2:
        Uniformity_of_cell_size = st.number_input('Uniformity of cell size',min_value=1,max_value=10)
        Bare_nuclei = st.number_input('Bare nuclei',min_value=1.0,max_value=10.0)
        Mitoses = st.number_input('Mitoses',step=1,min_value=1,max_value=10)
    # Input widgets in the third column
    with col3:
        Marginal_adhesion = st.number_input('Marginal adhesion',min_value=1,max_value=10)
        Bland_chromatin = st.number_input('Bland chromatin',min_value=1,max_value=10)
        

    # Predict button
    if st.button('Predict'):
        prediction = predict_diabetes(Clump_thickness,Uniformity_of_cell_size,Marginal_adhesion,Single_epithelial_cell_size,Bare_nuclei,Bland_chromatin,Normal_nucleoli,Mitoses)
        if prediction == 2:
            st.write('Prediction: Benign')
            
        else:
            st.write('Prediction: Malignant')
            



