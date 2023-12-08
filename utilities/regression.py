import streamlit as st
import pandas as pd
from utilities import regressionFunctions,projectPlots
from utilities import upload

def app():
    st.markdown("<h2 style='text-align: center; color: green;'>Linear Regression Analysis</h2>", unsafe_allow_html=True)
    
   
    result = object
    data = st.session_state.get("data_file")
    #st.write(data)
    #default = ["GRE Score","TOEFL Score","CGPA","University Rating","Research","SOP","LOR"]
   
    models = ["Linear Regression","Gaussian Poly"]
    default = ["GRE Score","TOEFL Score","CGPA"]
    with st.sidebar:
        st.subheader("1. Preprocessing")
        with st.expander("Preprocessing"):
            features = st.multiselect("Pleaase Select Feature",data.columns,default=default)
            # with col2:
            target = st.selectbox("Please Select Target",[data.columns[-1]])
            col1,col2 = st.columns(2)
            with col1:
                transformation_option= st.selectbox("Data Transformation",[None,"Standardize","Normalize"])
            with col2:
                st.selectbox("Drop",[False,True])
       
       # with col2:
        #st.markdown("___")
        st.subheader("2. Build Model")
        with st.expander("Build Model"):
            size_split = st.number_input("Train Size %",min_value=20,max_value=80,value=80)

            model_type = st.selectbox("Please Select Regression Model",models)
        #st.markdown("___")
        st.subheader("3. Model Evaluation")
        inputs = st.radio("Pick Test Data",["Test Original Data","Input test Data"])
        
        cols= st.columns(len(features))
        data_user = {}
        #if inputs =="Input test Data":
       
        if inputs == "Input test Data":
            st.markdown("___")
            user_input= st.radio("Options",["Input manual data","Upload Data"])
            if user_input == "Input manual data":
                cols= st.columns(len(features))
                for i in range(0,len(features)):
                    with cols[i]:
                        data_user[features[i]] = st.number_input(f"{features[i]}", min_value=0, value=0,key=i)
                    #for i in range(len(features))
            elif "Upload Data":
                data_user = upload.file_uploaded()
                
        user_inputs = pd.DataFrame([data_user])
        # st.markdown("___")
        # st.subheader("4. Model Validation")
    #st.write(features)
    st.markdown(f"""The application constructs a model utilizing {",".join(features)} as 
                input variables to predict the Chance of admission. This model is designed to offer insights 
                into the probability of admission based on the specified features.\n""")
    
    data  = data[1:]
    #write(data)
    tab1,tab2,tab3 = st.tabs(["1-PREPROCESSING", "2-BUILD MODEL","3-MODEL EVALUATION"])
    with tab1:
        st.markdown("#### 1. Preprocessing")
        if transformation_option == "Normalize":
            data_feature = regressionFunctions.normalized_data(data)
            # user_data = regressionFunctions.normalized_data(user_inputs)
        elif transformation_option == "Standardize":
            data_feature = regressionFunctions.standardized_data(data)
            # user_data = regressionFunctions.standardized_data(user_inputs)
        else:
            data_feature = data

        data_main = pd.DataFrame(data_feature,columns=data.columns)
        #user_inputs = pd.DataFrame(user_inputs,columns=features)
        
        data_feature = data_main[features]
        #st.write(data_feature)
        data_target = data_main[target]
        column1,column2 = st.columns(2)
        # st.write("this is the main")
        # st.write(data_feature)
        with column1:
            st.caption("Independent variables")
            st.write(data_feature.T)
        with column2:
            st.caption("Dependent variable")
            st.write(pd.DataFrame(data_target).T)
    with tab2:
        st.markdown("#### 2. Build Model")
        st.markdown("""
                    $$y=w_0 + w_1x_1+w_2x_2,... w_nx_n$$ \n
                    Where 
                    $w_1,w_2,...,w_n$ are the coefficients, and $w_0$ is the intercept point for the model equation.
                    """)
        if model_type == "Linear Regression":
            #st.write("reach here")
            
            result= regressionFunctions.linear_regression(data_feature,data_target,size_split)
        #[lin_reg.intercept_]+list(lin_reg.coef_)
        #st.write([result["model"].intercept_]+list(result["model"].coef_))
        data_reg = regressionFunctions.construct_regression_table(result["model"],features)
        data_reg = pd.DataFrame(data_reg)
        cofficient_only = data_reg.loc[1:]
        #[max(data_reg["Coeff_value"])]
        #st.write("index",data_reg[max(data_reg['Coeff_value'])])
        min_cof= cofficient_only.loc[cofficient_only['Coeff_value'].idxmin()]
        max_cof= cofficient_only.loc[cofficient_only['Coeff_value'].idxmax()]
        
        st.write(data_reg.T)
        st.markdown(f"""
                    The attribute {max_cof["Columns"]} exhibits the highest coefficient ({max_cof["Coeff_value"]}) indicating a more substantial contribution compared to other attributes.
                    Conversely, the variable  {min_cof["Columns"]} exhibits the lowest coefficient of {min_cof["Coeff_value"]}, signifying a relatively  minimal impact on the model.
                    """)
    with tab3:
        st.markdown("#### 3. Model Evaluation")
        st.markdown("""
                    Assessing the comprehensive performance of the linear regression model involves 
                    evaluating key metrics such as mean absolute error,
                    mean squared error, r-squared score, etc…. 
                    These metrics collectively provide insights into the model's effectiveness in predicting outcomes, 
                    offering understanding of its overall performance and areas for potential refinement.
                    """)
        evaluation = regressionFunctions.model_evaluation(result)
        st.write(pd.DataFrame([evaluation]))
        #================= plot ===============
        st.write("#### Plots")
        fig = projectPlots.plot_regression(result["y_test"],evaluation["predicted"])
        st.plotly_chart(fig,use_container_width=True)
        fig = projectPlots.seaborn_plot_residual(result["y_test"],evaluation["predicted"])
        
        #fig = projectPlots.scatter_plot(result["y_test"],evaluation["predicted"])
        st.pyplot(fig)
        #=======================================
    
        with st.sidebar:
            try:
                #user_inputs = user_inputs.to_numpy()
                
                #if user_inputs[features[0]][0] != 0:
                st.write(user_inputs[features])
                user_prediction = regressionFunctions.predict_incoming(result["model"],user_inputs)
                #if user_prediction[0]
                if user_prediction[0]>0:
                    st.write("Chance of Admission Based on Input:",user_prediction)
                else:
                    st.write("Chance of Admission Based on Input:",pd.DataFrame([{}]))
            except:
                pass
        #st.write(user_inputs)
        
    #feature neeed to do linear regression
    #slope(weigth) value, intercept
    # train and test dataset size
    #RMSE,RQUARE,ETC..
    #drop down selection for matrices,
    # Adjust slope value and intercept,
    # Run multiple lines manually to fit the best one.
    # simple linear and multiple linear correlation
    #user input to predict:
    #USE THE MODEL WITH INSIDE data
    #USING THE MODEL WITH OUSIDE DATA