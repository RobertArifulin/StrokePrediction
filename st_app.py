import streamlit as st
import os

class App:
    def __init__(self) -> None:
        self.pages = []

    def add_page(self, title, func) -> None:
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        page = st.sidebar.selectbox(
            'Page selection',
            self.pages,
            format_func=lambda page: page['title']
        )

        page['function']()