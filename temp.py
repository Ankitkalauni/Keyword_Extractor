import streamlit as st

from streamlit_quill import st_quill


def main_():   
    content = st_quill(
        placeholder="Write your text here",
        key="quill",
    )

    if content:
        st.subheader("Content")
        st.text(content)


if __name__ == "__main__":
    main_()