import streamlit as st
import random


def main():
    st.title("🧠 Spelling Quiz")
    st.write("Test your spelling skills!")

    all_questions = [
        {"question": "Spell the word for a domestic animal: 'D_g'", "answer": "dog"},
        {"question": "Spell the word: 'C_t'", "answer": "cat"},
        {"question": "Spell the word for something you read: 'B__k'", "answer": "book"},
        {"question": "Spell the opposite of 'small': 'L__ge'", "answer": "large"},
        {"question": "Spell the word: 'H__se'", "answer": "house"},
        {"question": "Spell the word: 'F__wer'", "answer": "flower"},
        {"question": "Spell the word for yellow fruit: 'B__ana'", "answer": "banana"},
        {"question": "Spell the word for an insect: 'B__terfly'", "answer": "butterfly"},
        {"question": "Spell the word for the day after today: 'T__orrow'",
            "answer": "tomorrow"},
        {"question": "Spell the word for our planet: 'E__th'", "answer": "earth"},
        {"question": "Spell the word for winter flakes: 'S__w'", "answer": "snow"},
        {"question": "Spell the word for a place to learn: 'S__ool'", "answer": "school"},
        {"question": "Spell the word for a sweet snack: 'C__dy'", "answer": "candy"},
        {"question": "Spell the word for water in the sky: 'R__n'", "answer": "rain"},
        {"question": "Spell the word for your hand part: 'F__gers'", "answer": "fingers"},
    ]

    if 'spelling_started' not in st.session_state:
        st.session_state.spelling_started = True
        st.session_state.spelling_questions = random.sample(all_questions, 10)
        st.session_state.spelling_answers = {}
        st.session_state.spelling_submitted = False
        st.session_state.spelling_score = 0

    if not st.session_state.spelling_submitted:
        with st.form("spelling_form"):
            for i, q in enumerate(st.session_state.spelling_questions):
                st.text(f"{i + 1}. {q['question']}")
                st.session_state.spelling_answers[i] = st.text_input(
                    "Your Answer:", key=f"spelling_q{i}")
            submitted = st.form_submit_button(
                "✅ Submit All Answers", use_container_width=True)

        if submitted:
            score = 0
            for i, q in enumerate(st.session_state.spelling_questions):
                user_ans = st.session_state.spelling_answers[i].strip().lower()
                correct_ans = q["answer"].strip().lower()
                if user_ans == correct_ans:
                    score += 1
            st.session_state.spelling_score = score
            st.session_state.spelling_submitted = True

            # ✅ Update Parent Dashboard progress
            if "child_progress" not in st.session_state:
                st.session_state.child_progress = {}

            st.session_state.child_progress["Spelling Quiz"] = {
                "completed": score,
                "total": len(st.session_state.spelling_questions)
            }

            st.rerun()

    else:
        st.success(
            f"🎉 You scored {st.session_state.spelling_score} out of {len(st.session_state.spelling_questions)}")
        st.write("🧠 Correct Answers:")
        for i, q in enumerate(st.session_state.spelling_questions):
            user_ans = st.session_state.spelling_answers[i]
            st.write(f"{i+1}. {q['question']}")
            st.write(f"✅ Correct: {q['answer']} | ❌ Your Answer: {user_ans}")
            st.markdown("---")

        if st.button("🔄 Restart Quiz", use_container_width=True):
            for key in list(st.session_state.keys()):
                if key.startswith("spelling_"):
                    del st.session_state[key]
            st.rerun()
