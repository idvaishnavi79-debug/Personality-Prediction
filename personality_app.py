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

st.sidebar.image("Logo.jpeg", use_container_width=True)
st.title("PersonaX")

# Sidebar for navigation
st.sidebar.title("PersonaX Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Premium Upgrade", "About"])

# --- HOME PAGE ---
if page == "Home":
    st.image("Logo.jpeg", use_container_width=True)  
    st.title("PersonaX")

# --- PREMIUM UPGRADE PAGE ---
elif page == "Premium Upgrade":
    st.title("Upgrade to PersonaX Premium ✨")
    
    st.markdown("""
    🔓 Unlock exclusive features:
    - ✅ Detailed MBTI personality breakdown  
    - ✅ Career guidance based on your personality  
    - ✅ Strengths & Weaknesses explained in depth  
    - ✅ Retake quizzes & track progress  
    - ✅ Priority support during fest  

    """)
    
    st.subheader("Pricing 💰")
    st.write("Only **₹100** 🎉")  # affordable for students
    
    if st.button("Pay with Razorpay (Demo)"):
        st.write("🛒 Redirecting to Razorpay demo checkout...")

# --- ABOUT PAGE ---
elif page == "About":
    st.title("About PersonaX")
    st.write("""
    Welcome to **PersonaX** – your personal guide to self-discovery! 🌱  

    In today’s fast-paced world, most students struggle to understand **who they truly are**  
    and what career path suits them best. That’s where PersonaX steps in.  

    ### 🎯 Our Mission
    PersonaX is built to **empower youth** by:
    - Helping them **decode their personality** through scientific methods.  
    - Guiding them toward **career choices** aligned with their natural strengths.  
    - Building **confidence** by showing their unique potential.  
    - Encouraging **self-reflection** and personal growth.  

    ### ⚡ Why PersonaX?
    Unlike boring tests and generic results, PersonaX offers:
    - **Interactive and fun personality prediction** ✨  
    - **MBTI-style results** that are easy to understand and relate to.  
    - **Fest-Special Premium Upgrade** for detailed reports and career guidance.  
    - A **youth-focused approach** designed for students like YOU.  

    ### 🛠️ How Was PersonaX Built?
    PersonaX is the result of a student innovator’s vision.  
    It combines:
    - AI + Psychology  
    - Modern design with simple navigation  
    - Affordable solutions for students at fests and beyond  

    ### 💡 Our Belief
    *“When you truly know yourself, you can unlock the best version of your future.”*  

    PersonaX is more than just an app – it’s a **movement** to help the youth of today  
    step into tomorrow with clarity, confidence, and purpose.  

    ---  

    👩‍💻 **Created by Vaishnavi Kumari**  
    A passionate Class 10 student who believes in innovation, self-growth, and making  
    technology meaningful for others. PersonaX is my way of inspiring youth to discover themselves.  

    """)











