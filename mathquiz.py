import streamlit as st
import random


def main():
    st.title("➕ Math Quiz")
    st.write("Test your math skills with fun medium & advanced questions!")

    all_questions = [
        {"question": "12 + 15 =", "answer": "27"},
        {"question": "25 - 9 =", "answer": "16"},
        {"question": "8 x 7 =", "answer": "56"},
        {"question": "81 ÷ 9 =", "answer": "9"},
        {"question": "14 + 19 =", "answer": "33"},
        {"question": "45 - 28 =", "answer": "17"},
        {"question": "6 x 9 =", "answer": "54"},
        {"question": "64 ÷ 8 =", "answer": "8"},
        {"question": "35 + 47 =", "answer": "82"},
        {"question": "90 - 55 =", "answer": "35"},
        {"question": "12 x 5 =", "answer": "60"},
        {"question": "100 ÷ 4 =", "answer": "25"},
        {"question": "18 + 26 =", "answer": "44"},
        {"question": "72 ÷ 6 =", "answer": "12"},
        {"question": "15 x 3 =", "answer": "45"},
    ]

    if 'math_questions' not in st.session_state:
        st.session_state.math_questions = random.sample(all_questions, 10)
        st.session_state.math_answers = {}
        st.session_state.math_submitted = False
        st.session_state.math_score = 0

    if not st.session_state.math_submitted:
        with st.form("math_form"):
            for i, q in enumerate(st.session_state.math_questions):
                st.text(f"{i + 1}. {q['question']}")
                st.session_state.math_answers[i] = st.text_input(
                    "Your Answer:", key=f"math_q{i}", placeholder="Type your answer"
                )
            submitted = st.form_submit_button("✅ Submit All")

        if submitted:
            score = 0
            for i, q in enumerate(st.session_state.math_questions):
                user_ans = st.session_state.math_answers[i].strip()
                correct_ans = q["answer"].strip()
                if user_ans == correct_ans:
                    score += 1
            st.session_state.math_score = score
            st.session_state.math_submitted = True

            # ✅ Save to child_progress
            if "child_progress" not in st.session_state:
                st.session_state.child_progress = {}

            st.session_state.child_progress["Math Quiz"] = {
                "completed": score,
                "total": 10
            }

            st.rerun()

    else:
        st.success(f"🎉 You scored {st.session_state.math_score} out of 10!")
        st.write("✅ Correct Answers:")
        for i, q in enumerate(st.session_state.math_questions):
            user_ans = st.session_state.math_answers.get(i, "").strip()
            correct_ans = q['answer']
            if user_ans == correct_ans:
                st.markdown(
                    f"✅ {i+1}. {q['question']} **Your Answer: {user_ans}** (Correct)")
            else:
                st.markdown(
                    f"❌ {i+1}. {q['question']} **Your Answer: {user_ans}** | Correct: **{correct_ans}**")
            st.markdown("---")

        if st.button("🔄 Restart Quiz"):
            for key in list(st.session_state.keys()):
                if key.startswith("math_"):
                    del st.session_state[key]
            st.rerun()
