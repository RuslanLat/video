import streamlit as st

st.write("You Tube")


with st.form("my_form"):
    st.write("Просмотр видео")
    title = st.text_input("URL видео", "https://www.youtube.com/...")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Смотреть")
if submitted:
    st.video(title)
