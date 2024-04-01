# DBATU Chatbot
---

## Introduction
This Python script utilizes Streamlit, a web application framework, to create a simple chatbot interface. The chatbot allows users to interact by typing messages and receiving responses. The script imports the necessary libraries and defines some color and font constants for customizing the appearance of the chat interface. It also includes a footer with information about Dr. Babasaheb Ambedkar Technological University, Lonere.

## Key Concepts
**Streamlit**: Streamlit is a Python library used for building interactive web applications. It simplifies the process of creating and deploying data-driven apps.

## Code Structure
The code is structured as follows:

1. **Import the necessary libraries**: The script imports the streamlit library, as well as the message function from streamlit_chat and the get_response and bot_name functions from chat.

2. **Define color and font constants**: The script defines constants for customizing the appearance of the chat interface, such as background color, text color, and font style.

3. **Initialize session state variables**: The script checks if the session state variables generated and past exist. If they don't, it initializes them as empty lists.

4. **Define the _insert_message function**: This function takes a message as input and inserts it into the chat interface as a bot message. It calls the get_response function to generate a response based on the user input.

5. **Define the get_text function**: This function displays a text input box where the user can enter their message. It returns the user input.

6. **Define the main function**: This function sets up the Streamlit application title and user input text box. It checks if the user has entered a message and, if so, displays the user message and the bot response in the chat interface. It also adds a footer with information about Dr. Babasaheb Ambedkar Technological University, Lonere.

7. **Run the main function**: The script runs the main function if it is being executed as the main script.

