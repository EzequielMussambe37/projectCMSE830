import streamlit as st
from utilities import projectPlots as pp, read_data,EDA



def app():
        st.header("Conclusion")
        st.markdown("""
                In summary, the linear regression model in this app by default predicted graduate admission chances based on 
                CGPA, GRE, and TOEFL scores. With an R-squared value of .79, the model reliably explains 79% of admission chance variations. 
                This application offers valuable insights into predicting graduate admission outcomes.
                """)

        st.markdown("""
                While the model offers valuable insights, it has limitations, such as assuming linearity and potential unobserved variables. 
                Predictive power may vary among institutions or programs, requiring caution in generalizing results.
                This research adds to graduate admissions knowledge through a quantitative approach. 
                        """)
        st.markdown("""
                        Future studies can explore into additional features, nonlinear relationships or focus on specific academic programs for more refined predictive model.
                Universities and applicants alike can gain from understanding the contributing variables.

                        """)
#     data=EDA.load_data()

#     fig = pp.plotly_scatter(data,"CGPA", "Chance of Admit ","Chance of Admit ")
#     st.plotly_chart(fig)

#     fig = pp.plotly_scatter(data,"TOEFL Score", "Chance of Admit ","Chance of Admit ")
#     st.plotly_chart(fig)
#     fig = pp.plotly_scatter(data,"GRE Score", "Chance of Admit ","Chance of Admit ")
#     st.plotly_chart(fig)
#     fig = pp.plotly_scatter(data,"SOP", "Chance of Admit ","Chance of Admit ")
#     st.plotly_chart(fig)



