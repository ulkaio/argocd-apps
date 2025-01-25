import streamlit as st
from typing import Any

def main() -> None:
    st.title("Welcome to My Streamlit App")
    
    # Add a text input with type hint
    user_input: str = st.text_input("Enter your name:", "")
    
    # Add a number input with type hint
    number: float = st.number_input("Enter a number:", min_value=0.0, max_value=100.0, value=50.0)
    
    # Display the inputs with type hints
    def display_message(name: str, value: float) -> None:
        if name:
            st.write(f"Hello {name}! Your number is: {value}")
    
    display_message(user_input, number)

if __name__ == "__main__":
    main() 