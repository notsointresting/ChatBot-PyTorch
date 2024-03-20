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
    st.chat_history.append(msg2)
    return msg2

def get_text():
   user_input = st.text_input("Your Message", key="user_input")
   return user_input
   
def main():
  st.title("Chat Application")
  st.chat_history = []

  # User Input
  user_input = get_text()
  
  if user_input:
    message(user_input, is_user=True)  # User message
    st.session_state.past.append(user_input)

    message(_insert_message(user_input), is_user=False)  # Bot response
    st.session_state.generated.append(_insert_message(user_input))
    # i want print chath history also



    
    



  # Footer (remains unchanged)
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
      <div class="st-eu">Dr. Babasaheb Ambedkar Technological University, Lonere</div>''',
      unsafe_allow_html=True,
  )


if __name__ == "__main__":
  main()
