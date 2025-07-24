import streamlit as st
import os
import mathquiz
import riddles
import animal
import funfacts
import parent
import spelling
import storypage
import rewardspage

# Set page config
st.set_page_config(page_title="Brain Buddy Kids App 🧠",
                   page_icon="🧠", layout="centered")

# Unlock system using checkbox in sidebar
if 'unlocked' not in st.session_state:
    st.session_state['unlocked'] = False

# Sidebar Menu
st.sidebar.title("🧠 Brain Buddy")
menu = st.sidebar.radio("Go to:", [
    "🏠 Home",
    "➕ Math Quiz",
    "🧩 Riddles",
    "🐾 Animal Quiz",
    "📚 Fun Facts",
    "👨‍👩‍👧 Parent Dashboard",
    "🧠 Spelling Quiz",
    "📖 Story Page",
    "🏆 Rewards & Badges",
])

# Unlock Section
st.sidebar.markdown("---")
st.sidebar.subheader("🔓 Unlock Full App")
unlock_checkbox = st.sidebar.checkbox("✅ I have paid ₹149 (one-time)")

# Update unlock status
st.session_state['unlocked'] = unlock_checkbox

# Header or cover image
if os.path.exists("cover.jpg"):
    st.image("cover.jpg", use_container_width=True)
else:
    st.title("🧠 Welcome to Brain Buddy Kids App")
    st.markdown("""
    **Brain Buddy** is a fun and educational app for kids!  
    Unlock **all features** for just ₹149 (one-time).  
    You'll get access to quizzes, stories, rewards, and more!
    """)

# Feature loading
if menu == "🏠 Home":
    st.markdown("### 👋 Welcome to Brain Buddy Kids App!")
    st.markdown("Explore fun educational quizzes, stories, and more.")
elif menu == "➕ Math Quiz":
    if st.session_state['unlocked']:
        mathquiz.main()
    else:
        st.warning("🔒 Please unlock to access the Math Quiz.")
elif menu == "🧩 Riddles":
    if st.session_state['unlocked']:
        riddles.main()
    else:
        st.warning("🔒 Please unlock to access Riddles.")
elif menu == "🐾 Animal Quiz":
    if st.session_state['unlocked']:
        animal.main()
    else:
        st.warning("🔒 Please unlock to access Animal Quiz.")
elif menu == "📚 Fun Facts":
    if st.session_state['unlocked']:
        funfacts.main()
    else:
        st.warning("🔒 Please unlock to access Fun Facts.")
elif menu == "👨‍👩‍👧 Parent Dashboard":
    if st.session_state['unlocked']:
        parent.main()
    else:
        st.warning("🔒 Please unlock to access Parent Dashboard.")
elif menu == "🧠 Spelling Quiz":
    if st.session_state['unlocked']:
        spelling.main()
    else:
        st.warning("🔒 Please unlock to access Spelling Quiz.")
elif menu == "📖 Story Page":
    if st.session_state['unlocked']:
        storypage.main()
    else:
        st.warning("🔒 Please unlock to access Story Page.")
elif menu == "🏆 Rewards & Badges":
    if st.session_state['unlocked']:
        rewardspage.main()
    else:
        st.warning("🔒 Please unlock to access Rewards.")
