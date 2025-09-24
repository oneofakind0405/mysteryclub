import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="Hidden Message", page_icon="🔒", layout="centered")

# HTML 파일 불러오기
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# HTML 렌더링
st.components.v1.html(html_code, height=800, scrolling=True)
