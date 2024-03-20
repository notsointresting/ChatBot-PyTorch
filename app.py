import customtkinter as ctk
from chat import get_response, bot_name

# Color constants
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"


class ChatApplication:
    def __init__(self):
        self.window = ctk.CTk()  # Create the window first

        # Font constants (created after window initialization and mainloop start)
        self.window.after(0, self._create_fonts)  # Schedule font creation

        self._setup_main_window()

    def _create_fonts(self):
        # Define font constants within this method
        self.FONT = ctk.CTkFont(family="Helvetica", size=14)
        self.FONT_BOLD = ctk.CTkFont(family="Helvetica", size=13, weight="bold")

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # Head label
        head_label = ctk.CTkLabel(
            self.window,
            text="Welcome",
            font=self.FONT_BOLD,  # Use the created font constants
            pady=10,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
        )
        head_label.place(relwidth=1)

        # Tiny divider
        line = ctk.CTkFrame(self.window, width=450, height=2, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07)

        # Text widget
        self.text_widget = ctk.CTkTextbox(
            self.window,
            width=20,
            height=2,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=self.FONT,  # Use the created font constants
            padx=5,
            pady=5,
        )
        self.text_widget.place(relheight=0.7, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=ctk.DISABLED)

        # Scroll bar
        scrollbar = ctk.CTkScrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Bottom label
        bottom_label = ctk.CTkFrame(self.window, height=80, bg=BG_GRAY)
        bottom_label.place(relwidth=1, rely=0.825)

        # Message entry box
        self.msg_entry = ctk.CTkEntry(
            bottom_label,
            bg="#2C3E50",
            fg=TEXT_COLOR,
            font=self.FONT,  # Use the created font constants
        )
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Send button
        send_button = ctk.CTkButton(
            bottom_label,
            text="Send",
            font=self.FONT_BOLD,  # Use the created font constants
            width=20,
            bg=BG_GRAY,
            command=lambda: self._on_enter_pressed(None),
        )
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        # Footer label
        footer_label = ctk.CTkLabel(
            self.window,
            text="Dr. Babasaheb Ambedkar Technological University, Lonere",
            font=self.FONT_BOLD,  # Use the created font constants
            pady=10,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
        )
        footer_label.place(relwidth=1, rely=0.925)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, ctk.END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=ctk.NORMAL)
        self.text_widget.insert(ctk.END, msg1)
        self.text_widget.configure(state=ctk.DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)} \n\n"
        self.text_widget.configure(state=ctk.NORMAL)
        self.text_widget.insert(ctk.END, msg2)
        self.text_widget.configure(state=ctk.DISABLED)

        self.text_widget.see(ctk.END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = ChatApplication()
    app.run()