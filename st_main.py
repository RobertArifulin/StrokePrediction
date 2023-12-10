import streamlit as st
from st_app import App
from st_pages import table, charts


def main():
    app = App()
    st.markdown("# Stroke prediction")

    app.add_page("General info", table)
    app.add_page("Charts", charts)

    app.run()


main()