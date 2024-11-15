import streamlit as st
from dice_module import Dice, DiceGame 
def main():
    st.title("Dice Game")

    st.write("**Game Rules:**")
    st.write("- Roll two dice.")
    st.write("- If the total is greater than 10, you win!")
    st.write("- Otherwise, hard luck, try again.")

    game = DiceGame()

    if 'show_button' not in st.session_state:
        st.session_state.show_button = True

    if st.session_state.show_button:
        if st.button("Roll the Dice", key="roll_button"):
            total = game.roll_dice()

            st.write("Dice 1: ", game.dice1.value,"Dice 2: ", game.dice2.value,"Total: ", total)

            if total >= 10:
                st.success("Congratulations! You scored better than 10!")
            else:
                st.warning("Hard luck, try again.")
main()