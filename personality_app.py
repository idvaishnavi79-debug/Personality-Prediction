import streamlit as st

st.set_page_config(page_title="Personality Prediction System", page_icon="🧠", layout="centered")

# Title
st.title("🧠 Personality Prediction System")
st.write("Answer the following questions to find out your personality type.")

# Questions
questions = [
    "I enjoy social gatherings.",
    "I prefer detailed planning over spontaneity.",
    "I focus more on facts than theories.",
    "I make decisions based on logic rather than emotions.",
    "I prefer working alone than in a team.",
    "I like exploring possibilities rather than sticking to practical solutions.",
    "I am energized by spending time with people.",
    "I stick to schedules and deadlines."
]

scores = []

# Answer options
for q in questions:
    score = st.radio(q, ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], index=2)
    scores.append(score)

# MBTI logic (simple)
if st.button("Predict My Personality"):
    # Convert answers to numbers
    mapping = {"Strongly Disagree": 1, "Disagree": 2, "Neutral": 3, "Agree": 4, "Strongly Agree": 5}
    scores_num = [mapping[s] for s in scores]

    # Determine MBTI traits
    extroversion = scores_num[0] + scores_num[6]
    introversion = (6 - scores_num[0]) + (6 - scores_num[6])

    sensing = scores_num[2] + (6 - scores_num[5])
    intuition = (6 - scores_num[2]) + scores_num[5]

    thinking = scores_num[3] + (6 - scores_num[4])
    feeling = (6 - scores_num[3]) + scores_num[4]

    judging = scores_num[1] + scores_num[7]
    perceiving = (6 - scores_num[1]) + (6 - scores_num[7])

    personality = ""
    personality += "E" if extroversion > introversion else "I"
    personality += "S" if sensing > intuition else "N"
    personality += "T" if thinking > feeling else "F"
    personality += "J" if judging > perceiving else "P"

    st.subheader(f"Your Personality Type: {personality}")
    
    descriptions = {
        "INTJ": "The Architect, Imaginative, strategic, and Long-term Planners.",
        "ENTP": "The Debater, curious, smart, and intellectual.",
        "INFJ": "The Advocate, quiet, mystical, and idealist.",
        "ENFP": "The Campaigner, creative, enthusiastic, and sociable.",
        "INTP": "The Logician, innovative, curious, and logical.",
        "ENTJ": "The Commander, bold, imaginative, and strong-willed.",
        "INFP": "The Mediator, Poetic, Kind, and Altruistic.",
        "ENFJ": "The Protagonist, charismatic, inspiring, and Natural Leaders.",
        "ISTJ": "The Logistician, practical, fact-minded, and reliable.",
        "ESFJ": "The Consul, caring, social, and popular.",
        "ISTP": "The Virtuoso, bold, practical, and experimental.",
        "ESFP": "The Entertainer, spontaneous, energetic, and enthusiastic.",
        "ISFJ": "The Defender, protective, warm, and caring.",
        "ESTJ": "The Executive, organized, punctual, and leader.",
        "ISFP": "The Adventurer, artistic, charming, and explorers.",
        "ESTP": "The Entrepreneur, smart, energetic, and perceptive.",
    }

    st.write(descriptions.get(personality, "A unique personality type with special strengths!"))




