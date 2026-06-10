import streamlit as st

st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="⚡")

st.title("🎯 MBTI별 어울리는 포켓몬 추천")
st.write("MBTI를 선택하면 어울리는 포켓몬을 추천해드립니다!")

pokemon_data = {
    "INTJ": {
        "name": "뮤츠",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "reason": "전략적이고 독립적인 성향이 강하며, 높은 지능과 목표 지향성을 가진 당신은 뮤츠와 잘 어울립니다."
    },
    "INTP": {
        "name": "후딘",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
        "reason": "분석적이고 지적 호기심이 많은 INTP는 뛰어난 초능력을 가진 후딘과 닮았습니다."
    },
    "ENTJ": {
        "name": "리자몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        "reason": "리더십이 강하고 도전 정신이 뛰어난 ENTJ는 강력한 존재감을 가진 리자몽과 잘 맞습니다."
    },
    "ENTP": {
        "name": "팬텀",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
        "reason": "창의적이고 재치 있는 ENTP는 장난기 많고 예측 불가능한 팬텀과 비슷합니다."
    },
    "INFJ": {
        "name": "루기아",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
        "reason": "깊은 통찰력과 이상주의적 성향을 가진 INFJ는 신비로운 루기아와 잘 어울립니다."
    },
    "INFP": {
        "name": "이브이",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "reason": "따뜻한 감성과 무한한 가능성을 가진 INFP는 다양한 진화를 가진 이브이와 닮았습니다."
    },
    "ENFJ": {
        "name": "피카츄",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "reason": "사람들에게 긍정적인 에너지를 주는 ENFJ는 모두에게 사랑받는 피카츄와 잘 맞습니다."
    },
    "ENFP": {
        "name": "토게키스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/468.png",
        "reason": "밝고 자유로운 ENFP는 행복을 전하는 토게키스와 어울립니다."
    },
    "ISTJ": {
        "name": "강철톤",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/208.png",
        "reason": "책임감 있고 신뢰할 수 있는 ISTJ는 단단한 강철톤과 닮았습니다."
    },
    "ISFJ": {
        "name": "해피너스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
        "reason": "배려심이 많고 헌신적인 ISFJ는 치유의 상징인 해피너스와 잘 어울립니다."
    },
    "ESTJ": {
        "name": "거북왕",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "reason": "조직적이고 책임감 있는 ESTJ는 든든한 리더 같은 거북왕과 잘 맞습니다."
    },
    "ESFJ": {
        "name": "푸크린",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/40.png",
        "reason": "사교적이고 친절한 ESFJ는 사람들을 즐겁게 하는 푸크린과 닮았습니다."
    },
    "ISTP": {
        "name": "핫삼",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/212.png",
        "reason": "실용적이고 문제 해결 능력이 뛰어난 ISTP는 날카로운 핫삼과 어울립니다."
    },
    "ISFP": {
        "name": "나인테일",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png",
        "reason": "예술적 감각과 개성을 중시하는 ISFP는 아름다운 나인테일과 잘 맞습니다."
    },
    "ESTP": {
        "name": "루카리오",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
        "reason": "행동력이 뛰어나고 모험을 즐기는 ESTP는 루카리오와 잘 어울립니다."
    },
    "ESFP": {
        "name": "꼬부기",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
        "reason": "밝고 유쾌한 ESFP는 귀엽고 활발한 꼬부기와 닮았습니다."
    },
}

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(pokemon_data.keys())
)

if mbti:
    data = pokemon_data[mbti]

    st.subheader(f"✨ 당신에게 어울리는 포켓몬: {data['name']}")
    st.image(data["image"], width=250)
    st.write("### 추천 이유")
    st.info(data["reason"])
