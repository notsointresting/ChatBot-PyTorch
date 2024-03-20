import streamlit as st
from chat import get_response, bot_name

# Color constants (you can customize these)
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

# Font constants (you can customize these)
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


def _insert_message(msg, sender = "You"):
    if not msg:
        return

    msg1 = f"{sender}: {msg}\n\n"
    st.session_state.chat_history += msg1

    msg2 = f"{bot_name}: {get_response(msg)} \n\n"
    st.session_state.chat_history += msg2



def main():
    st.title("Chat Application")

    # Initialize chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = ""

    # Display chat history
    st.text_area("Chat History", st.session_state.chat_history, height=300, disabled=True)

    # Message input and send button
    user_input = st.text_input("Your Message", on_change=_insert_message, args=("You",), key="user_input")
    if st.button("Send"):
        _insert_message(user_input)
        user_input = ""  # Clear input after sending
    # Footer
    st.markdown(
        """
        <style>
        .st-eu {  /* Target the footer container */
            text-align: center;
            font-size: 12px;
            color: gray;
            position: fixed;  /* Fix the footer to the bottom */
            bottom: 0;
            width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="st-eu">Dr. Babasaheb Ambedkar Technological University, Lonere</div>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()