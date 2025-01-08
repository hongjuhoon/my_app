import streamlit as st

st.title('나의 첫번째 앱')
st.text('\n\n')
st.write('안녕하세요. 저는 🫃입니다')
st.write('저의 이메일 주소는 24_10124@daejin.sen.hs.kr 입니다.')

st.button("Reset", type="primary")
if st.button("난수 생성"):
    st.write(random.randint(1,1000))
else:
    st.write("안녕")
