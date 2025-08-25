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
