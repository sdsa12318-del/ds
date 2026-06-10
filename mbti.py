import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천 🌈",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 MBTI 진로 추천 프로그램")
st.markdown("### 🌟 나의 MBTI에 어울리는 진로를 찾아보자!")
st.write("MBTI를 선택하면 추천 진로 2개와 관련 학과를 알려줄게 😎")

career_data = {
    "INTJ": [
        {
            "career": "🧠 데이터 사이언티스트",
            "major": "컴퓨터공학과, 데이터사이언스학과, 통계학과",
            "personality": "논리적으로 문제를 해결하고 분석하는 걸 좋아하는 사람"
        },
        {
            "career": "🔬 연구원",
            "major": "자연과학계열, 공학계열",
            "personality": "깊이 탐구하고 새로운 아이디어를 만들어내는 사람"
        }
    ],
    "INTP": [
        {
            "career": "💻 소프트웨어 개발자",
            "major": "컴퓨터공학과, 소프트웨어학과",
            "personality": "호기심이 많고 새로운 기술을 배우는 걸 좋아하는 사람"
        },
        {
            "career": "🔭 과학자",
            "major": "물리학과, 화학과, 생명과학과",
            "personality": "원리를 탐구하고 분석하는 걸 즐기는 사람"
        }
    ],
    "ENTJ": [
        {
            "career": "📈 경영 컨설턴트",
            "major": "경영학과, 경제학과",
            "personality": "리더십이 강하고 목표 달성을 좋아하는 사람"
        },
        {
            "career": "🏢 기업 CEO",
            "major": "경영학과, 산업공학과",
            "personality": "조직을 이끌고 전략을 세우는 데 자신 있는 사람"
        }
    ],
    "ENTP": [
        {
            "career": "🚀 창업가",
            "major": "경영학과, 창업학과",
            "personality": "새로운 아이디어를 실현하는 걸 좋아하는 사람"
        },
        {
            "career": "📢 마케팅 기획자",
            "major": "광고홍보학과, 경영학과",
            "personality": "창의적이고 사람들과 소통하는 걸 좋아하는 사람"
        }
    ],
    "INFJ": [
        {
            "career": "🩺 상담심리사",
            "major": "심리학과, 상담학과",
            "personality": "다른 사람의 마음을 이해하고 돕고 싶은 사람"
        },
        {
            "career": "📚 교사",
            "major": "교육학과, 사범대학",
            "personality": "학생들의 성장을 돕는 데 보람을 느끼는 사람"
        }
    ],
    "INFP": [
        {
            "career": "✍️ 작가",
            "major": "문예창작학과, 국어국문학과",
            "personality": "상상력이 풍부하고 감성이 깊은 사람"
        },
        {
            "career": "🎨 디자이너",
            "major": "시각디자인학과, 산업디자인학과",
            "personality": "창의적인 표현을 좋아하는 사람"
        }
    ],
    "ENFJ": [
        {
            "career": "🎤 강사",
            "major": "교육학과, 심리학과",
            "personality": "사람들에게 긍정적인 영향을 주고 싶은 사람"
        },
        {
            "career": "🤝 인사담당자(HR)",
            "major": "경영학과, 심리학과",
            "personality": "사람을 이해하고 소통하는 능력이 뛰어난 사람"
        }
    ],
    "ENFP": [
        {
            "career": "📺 크리에이터",
            "major": "미디어커뮤니케이션학과",
            "personality": "에너지가 넘치고 새로운 도전을 좋아하는 사람"
        },
        {
            "career": "🎉 이벤트 기획자",
            "major": "관광경영학과, 문화콘텐츠학과",
            "personality": "사람들과 함께 아이디어를 실현하는 걸 좋아하는 사람"
        }
    ],
    "ISTJ": [
        {
            "career": "⚖️ 공무원",
            "major": "행정학과, 법학과",
            "personality": "책임감이 강하고 꼼꼼한 사람"
        },
        {
            "career": "📊 회계사",
            "major": "회계학과, 경영학과",
            "personality": "체계적이고 정확한 일을 좋아하는 사람"
        }
    ],
    "ISFJ": [
        {
            "career": "🏥 간호사",
            "major": "간호학과",
            "personality": "배려심이 많고 사람을 돕는 걸 좋아하는 사람"
        },
        {
            "career": "👶 유치원 교사",
            "major": "유아교육과",
            "personality": "따뜻하고 책임감 있는 사람"
        }
    ],
    "ESTJ": [
        {
            "career": "🏛️ 행정가",
            "major": "행정학과",
            "personality": "조직을 체계적으로 운영하는 능력이 뛰어난 사람"
        },
        {
            "career": "📋 프로젝트 매니저",
            "major": "경영학과",
            "personality": "계획을 세우고 추진하는 걸 좋아하는 사람"
        }
    ],
    "ESFJ": [
        {
            "career": "💉 의료 코디네이터",
            "major": "보건행정학과",
            "personality": "친절하고 사람들과 협력하는 걸 좋아하는 사람"
        },
        {
            "career": "🎓 교사",
            "major": "교육학과",
            "personality": "주변 사람들을 챙기고 돕는 걸 좋아하는 사람"
        }
    ],
    "ISTP": [
        {
            "career": "🔧 기계 엔지니어",
            "major": "기계공학과",
            "personality": "실습과 문제 해결을 좋아하는 사람"
        },
        {
            "career": "✈️ 항공정비사",
            "major": "항공정비학과",
            "personality": "손으로 직접 작업하는 걸 좋아하는 사람"
        }
    ],
    "ISFP": [
        {
            "career": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "감각적이고 예술적인 사람"
        },
        {
            "career": "🎵 음악 프로듀서",
            "major": "실용음악과",
            "personality": "자신만의 감성을 표현하는 걸 좋아하는 사람"
        }
    ],
    "ESTP": [
        {
            "career": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "활동적이고 사람 만나는 걸 좋아하는 사람"
        },
        {
            "career": "🎬 방송인",
            "major": "방송영상학과",
            "personality": "즉흥적이고 에너지가 넘치는 사람"
        }
    ],
    "ESFP": [
        {
            "career": "🎭 배우",
            "major": "연극영화과",
            "personality": "표현력이 풍부하고 사람들과 어울리기를 좋아하는 사람"
        },
        {
            "career": "🎤 아나운서",
            "major": "미디어커뮤니케이션학과",
            "personality": "밝고 소통 능력이 뛰어난 사람"
        }
    ]
}

mbti = st.selectbox(
    "🌈 MBTI를 선택해줘!",
    list(career_data.keys())
)

if st.button("✨ 진로 추천 받기"):
    st.success(f"🎉 {mbti} 유형에게 추천하는 진로야!")

    for idx, item in enumerate(career_data[mbti], start=1):
        st.markdown(f"## {idx}. {item['career']}")
        st.markdown(f"**🎓 추천 학과**")
        st.write(item["major"])

        st.markdown(f"**💡 이런 성격에게 잘 맞아요!**")
        st.write(item["personality"])

        st.divider()

    st.balloons()

st.markdown("---")
st.caption("🌟 MBTI는 참고용이야! 진로는 자신의 관심사와 강점을 함께 고려해서 선택하자 😊")
