import streamlit as st
import  requests  

def get_api_data(test_url):

    try:
        response = requests.get(test_url)
   
        data = response.json()
        

        return data
   

    except Exception as e:
        return(f"❌ Error: {e}")


st.title("API explorer")
st.write(
    "Paste your base URL below:"
)

input_url = st.text_input("URL", "")

st.write("The URL  is", input_url)

if st.button("Get API Data"):

    if input_url != "":

        data = get_api_data(input_url)
        st.write(data)

        
     


