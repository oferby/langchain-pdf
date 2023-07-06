import streamlit as st

def main():
    st.set_page_config(page_title="Chat on PDFs", page_icon=":books:")
    st.header("Chat on PDFs")
    st.text_input("Ask me something...")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your files here")
        st.button("Process")

if __name__ == '__main__':
    main()

