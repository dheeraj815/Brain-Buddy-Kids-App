import streamlit as st
import random


def main():
    st.title("🐾 Animal Quiz")
    st.write("Test your animal knowledge!")

    all_questions = [
        {"question": "Which animal is known as the King of the Jungle?", "answer": "lion"},
        {"question": "Which bird is known for its colorful tail?", "answer": "peacock"},
        {"question": "Which animal is the largest land animal?", "answer": "elephant"},
        {"question": "Which animal is known for hopping?", "answer": "kangaroo"},
        {"question": "Which sea creature has eight legs?", "answer": "octopus"},
        {"question": "Which animal has black and white stripes?", "answer": "zebra"},
        {"question": "Which bird can mimic human speech?", "answer": "parrot"},
        {"question": "Which animal is known as man's best friend?", "answer": "dog"},
        {"question": "Which animal has a long neck and spots?", "answer": "giraffe"},
        {"question": "Which slow animal carries its home on its back?", "answer": "turtle"},
        {"question": "Which animal is the tallest in the world?", "answer": "giraffe"},
        {"question": "Which fish is known for its bright orange color?",
            "answer": "goldfish"},
        {"question": "Which animal lives in Antarctica and loves cold?",
            "answer": "penguin"},
        {"question": "Which animal swings through trees and eats bananas?",
            "answer": "monkey"},
        {"question": "Which big animal lives in water and has a trunk?",
            "answer": "elephant"},
    ]

    if 'animal_questions' not in st.session_state:
        st.session_state.animal_questions = random.sample(all_questions, 10)
        st.session_state.animal_answers = {}
        st.session_state.animal_submitted = False
        st.session_state.animal_score = 0

    if not st.session_state.animal_submitted:
        with st.form("animal_quiz_form"):
            for i, q in enumerate(st.session_state.animal_questions):
                st.write(f"**{i+1}. {q['question']}**")
                st.session_state.animal_answers[i] = st.text_input(
                    "Your Answer:", key=f"animal_input_{i}")

            submitted = st.form_submit_button("✅ Submit All")

        if submitted:
            score = 0
            for i, q in enumerate(st.session_state.animal_questions):
                user_ans = st.session_state.animal_answers.get(
                    i, "").strip().lower()
                if user_ans == q['answer'].lower():
                    score += 1
            st.session_state.animal_score = score
            st.session_state.animal_submitted = True

            # Save progress for parent dashboard
            st.session_state.child_progress = st.session_state.get(
                "child_progress", {})
            st.session_state.child_progress["Animal Quiz"] = {
                "completed": score, "total": 10
            }
            st.rerun()

    else:
        st.success(f"🎉 You scored {st.session_state.animal_score} out of 10")
        st.write("✅ Correct Answers:")
        for i, q in enumerate(st.session_state.animal_questions):
            user_ans = st.session_state.animal_answers.get(i, "")
            st.write(f"**{i+1}. {q['question']}**")
            st.write(f"✅ Correct: {q['answer']} | ❌ Your Answer: {user_ans}")
            st.markdown("---")

        if st.button("🔄 Restart Quiz"):
            for key in list(st.session_state.keys()):
                if key.startswith("animal_"):
                    del st.session_state[key]
            st.rerun()
