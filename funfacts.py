import streamlit as st
import random


def main():
    st.title("📚 Fun Facts Quiz")
    st.write("Test your general knowledge with fun medium & advanced questions!")

    all_questions = [
        {"question": "What is the hottest planet in our solar system?", "answer": "venus"},
        {"question": "How many legs does a spider have?", "answer": "8"},
        {"question": "What is the tallest mountain on Earth?",
            "answer": "mount everest"},
        {"question": "Which country is known as the Land of the Rising Sun?",
            "answer": "japan"},
        {"question": "What is the main ingredient in guacamole?", "answer": "avocado"},
        {"question": "Which animal is known to have a memory span of several years?",
            "answer": "elephant"},
        {"question": "What is the largest ocean on Earth?", "answer": "pacific"},
        {"question": "What gas do plants absorb from the air?",
            "answer": "carbon dioxide"},
        {"question": "How many bones are in the adult human body?", "answer": "206"},
        {"question": "Which famous scientist developed the theory of relativity?",
            "answer": "albert einstein"},
        {"question": "Which metal is liquid at room temperature?", "answer": "mercury"},
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "What organ pumps blood through the body?", "answer": "heart"},
        {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
        {"question": "Which instrument has black and white keys?", "answer": "piano"},
    ]

    # Initialize session state for quiz
    if "funfacts_questions" not in st.session_state:
        st.session_state.funfacts_questions = random.sample(all_questions, 10)
        st.session_state.funfacts_answers = {}
        st.session_state.funfacts_submitted = False
        st.session_state.funfacts_score = 0

    # Initialize child progress tracker
    if "child_progress" not in st.session_state:
        st.session_state.child_progress = {}

    if not st.session_state.funfacts_submitted:
        with st.form("funfacts_form"):
            for i, q in enumerate(st.session_state.funfacts_questions):
                st.write(f"**{i + 1}. {q['question']}**")
                st.session_state.funfacts_answers[i] = st.text_input(
                    "Your Answer:", key=f"funfacts_q{i}")
            submitted = st.form_submit_button("✅ Submit All")

        if submitted:
            score = 0
            for i, q in enumerate(st.session_state.funfacts_questions):
                user_ans = st.session_state.funfacts_answers[i].strip().lower()
                correct_ans = q["answer"].strip().lower()
                if user_ans == correct_ans:
                    score += 1

            st.session_state.funfacts_score = score
            st.session_state.funfacts_submitted = True

            # ✅ Update child progress
            st.session_state.child_progress["Fun Facts Quiz"] = {
                "completed": score,
                "total": 10
            }

            st.rerun()

    else:
        st.success(f"🎉 You scored {st.session_state.funfacts_score} out of 10")
        st.write("📘 Correct Answers:")
        for i, q in enumerate(st.session_state.funfacts_questions):
            user_ans = st.session_state.funfacts_answers.get(i, "").strip()
            st.write(f"**{i+1}. {q['question']}**")
            st.write(
                f"✅ Correct: `{q['answer']}` | ❌ Your Answer: `{user_ans}`")
            st.markdown("---")

        if st.button("🔄 Restart Quiz"):
            for key in list(st.session_state.keys()):
                if key.startswith("funfacts_"):
                    del st.session_state[key]
            st.rerun()
