import streamlit as st

# MBTI 유형 및 상세 설명과 이모지
mbti_info = {
    "ISTJ": {
        "description": "ISTJ는 신뢰할 수 있고 헌신적이며, 책임감이 강한 유형입니다. 실용적이고 체계적이며, 전통을 중시합니다.",
        "emoji": "📖"
    },
    "ISFJ": {
        "description": "ISFJ는 세심하고 배려가 깊으며, 남을 돕기를 좋아하는 유형입니다. 사람들과의 관계에 우선 순위를 두며, 조화를 중시합니다.",
        "emoji": "💖"
    },
    "INFJ": {
        "description": "INFJ는 이해력이 뛰어나고 창의적이며, 깊은 관계를 소중히 여깁니다. 직관적이고 진정성을 중시합니다.",
        "emoji": "🌟"
    },
    "INTJ": {
        "description": "INTJ는 분석적이고 전략적이며, 독립적인 성향을 가집니다. 목표 지향적이고 혁신적인 사고를 중요시합니다.",
        "emoji": "🔍"
    },
    "ISTP": {
        "description": "ISTP는 실용적이고 문제 해결 능력이 뛰어나며, 행동 지향적입니다. 즉흥적인 성향이 강하고, 경험을 통해 배우는 것을 좋아합니다.",
        "emoji": "🛠️"
    },
    "ISFP": {
        "description": "ISFP는 즉흥적이고 예술적인 감각이 뛰어나며, 감정을 중시합니다. 주변 환경에 민감하며, 자유로운 삶을 추구합니다.",
        "emoji": "🎨"
    },
    "INFP": {
        "description": "INFP는 이상적이고 진정한 자아를 추구하며, 감정을 소중히 여깁니다. 깊은 생각을 하며, 사람들과의 진정한 연결을 원합니다.",
        "emoji": "💭"
    },
    "INTP": {
        "description": "INTP는 논리적이고 탐구심이 강하며, 이론적 사고를 중요시합니다. 복잡한 문제를 해결하는 것을 즐깁니다.",
        "emoji": "🤔"
    },
    "ESTP": {
        "description": "ESTP는 활동적이고 모험을 좋아하며, 즉각적인 결정을 내리는 것을 선호합니다. 현실적인 문제를 해결하는 능력이 뛰어납니다.",
        "emoji": "🏄‍♂️"
    },
    "ESFP": {
        "description": "ESFP는 사교적이고 즐거움을 추구하며, 현재의 순간을 중요시합니다. 삶을 즐기고 사람들과의 관계를 중시합니다.",
        "emoji": "🎉"
    },
    "ENFP": {
        "description": "ENFP는 열정적이고 창의적이며, 새로운 가능성을 탐구하는 것을 좋아합니다. 사람들과의 소통을 즐기고, 긍정적입니다.",
        "emoji": "✨"
    },
    "ENTP": {
        "description": "ENTP는 아이디어가 풍부하고 혁신적이며, 문제 해결을 즐깁니다. 논쟁을 통해 깊은 논의하는 것을 좋아합니다.",
        "emoji": "💡"
    },
    "ESTJ": {
        "description": "ESTJ는 조직적이고 효율적이며, 리더십을 발휘하는 것을 중요시합니다. 명확한 규칙과 절차를 선호합니다.",
        "emoji": "📊"
    },
    "ESFJ": {
        "description": "ESFJ는 사교적이고 협력적이며, 공동체를 소중히 여깁니다. 다른 사람의 감정을 잘 이해하고 도와주기를 좋아합니다.",
        "emoji": "🤝"
    },
    "ENFJ": {
        "description": "ENFJ는 사람을 돕고 이끄는 것을 좋아하며, 인간관계에 뛰어난 역량을 가집니다. 강한 리더십 능력을 가지고 있습니다.",
        "emoji": "🌈"
    },
    "ENTJ": {
        "description": "ENTJ는 결단력이 있고, 목표 지향적이며, 리더십이 뛰어납니다. 비전을 실현하고 다른 사람을 동기부여하는 것을 즐깁니다.",
        "emoji": "🚀"
    }
}

# Streamlit 애플리케이션 시작
st.title("MBTI 유형 선택기")
st.write("아래에서 MBTI 유형을 선택하세요:")

# MBTI 유형 선택
mbti_type = st.selectbox("MBTI 유형", list(mbti_info.keys()))

if st.button("알아보기"):
    st.write(f"당신의 MBTI 유형은 **{mbti_type}** {mbti_info[mbti_type]['emoji']} 입니다.")
    st.write(mbti_info[mbti_type]['description'])
