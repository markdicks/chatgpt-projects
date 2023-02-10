import streamlit as st
import requests

def chatbot():
    st.set_page_config(page_title="Chatbot", page_icon=":robot:", layout="wide")
    st.title("Chatbot")

    # Introduction
    st.write("Hi there! I'm a simple chatbot. How can I help you today?")

    # Get user input
    user_input = st.text_input("Enter your message:")

    # Make API request
    if user_input:
        # Replace the API endpoint with a real one
        api_endpoint = "https://api.example.com/respond"
        try:
            response = requests.get(f"{api_endpoint}?message={user_input}").json()
            st.write(response["response"])
        except requests.exceptions.RequestException as e:
            st.write("An error occurred while making the API request. Please try again later.")
        except KeyError:
            st.write("The API response is missing the expected key. Please check the API documentation.")
        except AttributeError:
             st.write("An error occurred while making the API request.")
        except Exception as e:
            st.write("An error occurred while making the API request.")

        # Clear the user input
        st.set_input_value("Enter your message:", "")

if __name__ == '__main__':
    chatbot()
