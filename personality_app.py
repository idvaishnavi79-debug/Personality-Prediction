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
        "ENTP": "Innovative, curious, and love debating ideas.",
        "INFJ": "Idealists with a deep sense of purpose.",
        "ENFP": "Energetic, creative, and value relationships.",
        "INTP": "Strategic thinkers, love planning, and focus on long-term goals.",
        "ENTJ": "Innovative, curious, and love debating ideas.",
        "INFP": "Idealists with a deep sense of purpose.",
        "ENFJ": "Energetic, creative, and value relationships.",
        "ISTJ": "Strategic thinkers, love planning, and focus on long-term goals.",
        "ESFJ": "Innovative, curious, and love debating ideas.",
        "ISTP": "Idealists with a deep sense of purpose.",
        "ESFP": "Energetic, creative, and value relationships.",
        "ISFJ": "Strategic thinkers, love planning, and focus on long-term goals.",
        "ESTJ": "Innovative, curious, and love debating ideas.",
        "ISFP": "Idealists with a deep sense of purpose.",
        "ESTP": "Energetic, creative, and value relationships.",
    }

    st.write(descriptions.get(personality, "A unique personality type with special strengths!"))



