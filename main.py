import streamlit as st
st.title("첫 app")
st.write("hello")
name=st.text_input("이름 입력")
if name:
  if name=="정윤성":
    st.success("반갑습니다. 홍길동님!")
  else:
    st.warning("누구세요?)
