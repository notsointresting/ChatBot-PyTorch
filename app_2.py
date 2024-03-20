import streamlit as st
from streamlit_chat import message
from chat import get_response, bot_name

# Color constants (you can customize these)
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

# Font constants (you can customize these)
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def _insert_message(msg, sender = "You"):
    msg2 = f"{bot_name}: {get_response(msg)} \n\n"
    return msg2

def get_text():
   user_input = st.text_input("Your Message", key="user_input")
   return user_input
   
def main():
  st.title("DBATU Chatbot")

  # User Input
  user_input = get_text()
  
  if user_input:
    message(user_input, is_user=True)  # User message
    message(_insert_message(user_input), is_user=False)  # Bot response

  # Footer (Do not change)
    st.markdown(
        """
        <style>
        .st-eu { /* Target the footer container */
            text-align: center;
            font-size: 12px;
            color: gray;
            position: fixed; /* Fix the footer to the bottom */
            bottom: 0;
            width: 100%;
            left: 50%; /* Add this line to center the footer */
            transform: translateX(-50%); /* Add this line to center the footer */
        }
        </style>
        """,
        unsafe_allow_html=True,
)
    st.markdown(
      '''
      <div class="st-eu"><h6>Dr. Babasaheb Ambedkar Technological University, Lonere</h6></div>''',
      unsafe_allow_html=True,
  )


if __name__ == "__main__":
  main()
