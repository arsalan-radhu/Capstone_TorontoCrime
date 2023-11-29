import base64
import streamlit as st

def show():

    def connect_with_me():
        st.title("Connect with Me")
        st.markdown("##### Let's stay connected! Feel free to reach out via any of these platforms:")

        col1, col2 = st.columns(2)  # Divide the layout into two columns

        # Display LinkedIn as an image link
        with col1:
            st.markdown(
            """<a href="https://www.linkedin.com/in/arsalanarifradhu/">
            <img src="data:image/png;base64,{}" width="100">
            </a>""".format(
                base64.b64encode(open("./Streamlit/linkedin-logo.png", "rb").read()).decode()
                    ),
            unsafe_allow_html=True,
            )
            #b = st.image("./linkedin-logo.png", width=100)
            #st.markdown("[![LinkedIn]({b})](https://www.linkedin.com/arsalanradhu)")
        
        # Display GitHub as an image link
        with col2:

            st.markdown(
            """<a href="https://github.com/arsalan-radhu/">
            <img src="data:image/png;base64,{}" width="100">
            </a>""".format(
                base64.b64encode(open("./Streamlit/github.png", "rb").read()).decode()
                    ),
            unsafe_allow_html=True,
            )
            #a = st.image("./github.png", width=100)
            #st.markdown("[![GitHub]({a})](https://github.com/arsalan-radhu)")
            
        st.markdown("")
        # Email
        st.markdown("##### You can also reach me via email: arsln.radhu@gmail.com")

    connect_with_me()