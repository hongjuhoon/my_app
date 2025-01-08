import streamlit as st

st.title('여러나라의 수도찾기')
st.text('\n\n')
st.write('안녕하세요. 저는 🫃입니다')
st.write('저의 이메일 주소는 24_10124@daejin.sen.hs.kr 입니다.')

country_capitals = {
    "대한민국": "서울",
    "미국": "워싱턴 D.C.",
    "일본": "도쿄",
    "중국": "베이징",
    "프랑스": "파리",
    "영국": "런던",
    "독일": "베를린",
    "러시아": "모스크바",
    "이탈리아": "로마",
    "스페인": "마드리드"
}

st.text('\n\n')
st.write('나라 이름을 입력하면 해당 나라의 수도를 알려줍니다.')

# 사용자 입력
country_name = st.text_input("나라 이름을 입력하세요:", '')

# 사용자가 입력한 나라의 수도를 출력
if country_name:
    capital = country_capitals.get(country_name)
    if capital:
        st.write(f"{country_name}의 수도는 {capital}입니다.")
    else:
        st.write(f"{country_name}의 수도 정보를 찾을 수 없습니다.")
