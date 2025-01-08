import streamlit as st

st.title('🌍여러나라의 수도찾기🌏')
st.text('\n\n')
st.write('안녕하세요. 저는 🫃입니다')
st.write('저의 이메일 주소는 24_10124@daejin.sen.hs.kr 입니다.')

country_capitals = {
    '대한민국' : '서울',
    '중국' : '베이징',
    '일본' : '도쿄',
    '인도' : '뉴델리',
    '인도네시아' : '자카르타',
    '파키스탄' : '이슬라마바드',
    '방글라데시' : '다카',
    '베트남' : '하노이',
    '필리핀' : '마닐라',
    '태국' : '방콕',
    '말레이시아' : '쿠알라룸푸르',
    '이란' : '테헤란',
    '이라크' : '바그다드',
    '사우디아라비아' : '리야드',
    '터키' : '앙카라',
    '영국' : '런던',
    '독일' : '베를린',
    '프랑스' : '파리',
    '이탈리아' : '로마',
    '스페인' : '마드리드',
    '러시아' : '모스크바',
    '네덜란드' : '암스테르담',
    '벨기에' : '브뤼셀',
    '스웨덴' : '스톡홀름',
    '스위스' : '베른',
    '폴란드' : '바르샤바',
    '그리스' : '아테네',
    '이집트' : '카이로',
    '나이지리아' : '아부자',
    '남아프리카공화국' : '프리토리아(행정), 케이프타운(입법), 블룸폰테인(사법)',
    '케냐' : '나이로비',
    '에티오피아' : '아디스아바바',
    '알제리' : '알제',
    '가나' : '아크라',
    '미국' : '워싱턴 D.C.',
    '캐나다' : '오타와',
    '멕시코' : '멕시코시티',
    '쿠바' : '아바나',
    '자메이카' : '킹스턴',
    '브라질' : '브라질리아',
    '아르헨티나' : '부에노스아이레스',
    '칠레' : '산티아고',
    '콜롬비아' : '보고타',
    '페루' : '리마',
    '오스트레일리아' : '캔버라',
    '뉴질랜드' : '웰링턴',
    '피지' : '수바',
    '파푸아뉴기니' : '포트모르즈비',
    '바티칸시국' : '바티칸 시티',
    '아이슬란드' : '레이캬비크',
    '몰디브' : '말레',
    '싱가포르' : '싱가포르'
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
        # '남아프리카공화국'이 입력된 경우 선물 상자 표시
        if country_name == "남아프리카공화국":
            st.write("수도가 3개인 나라를 찾으셨군요! 큰 선물이 주어집니다.")
            st.balloons()  # 선물 효과로 풍선 등장
            st.image("https://upload.wikimedia.org/wikipedia/commons/0/0b/Present_icon.svg", width=100)  # 선물 상자 이미지
    else:
        st.write(f"{country_name}의 수도 정보를 찾을 수 없습니다.")
