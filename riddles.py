import streamlit as st
import random


def main():
    st.title("🧩 Riddles Quiz")
    st.write("Solve these fun riddles!")

    all_questions = [
        {"question": "What has keys but can't open locks?", "answer": "piano"},
        {"question": "What has hands but can’t clap?", "answer": "clock"},
        {"question": "I’m tall when I’m young and short when I’m old. What am I?",
            "answer": "candle"},
        {"question": "What has to be broken before you can use it?", "answer": "egg"},
        {"question": "I speak without a mouth and hear without ears. What am I?",
            "answer": "echo"},
        {"question": "What gets wetter the more it dries?", "answer": "towel"},
        {"question": "What has a face and two hands but no arms or legs?",
            "answer": "clock"},
        {"question": "What runs but never walks?", "answer": "water"},
        {"question": "What can travel around the world while staying in the corner?",
            "answer": "stamp"},
        {"question": "The more you take, the more you leave behind. What are they?",
            "answer": "footsteps"},
        {"question": "What has teeth but can’t bite?", "answer": "comb"},
        {"question": "What has a neck but no head?", "answer": "bottle"},
        {"question": "What comes down but never goes up?", "answer": "rain"},
        {"question": "What can fill a room but takes no space?", "answer": "light"},
        {"question": "What has one eye but can’t see?", "answer": "needle"},
    ]

    if 'riddles_data' not in st.session_state:
        st.session_state.riddles_data = {
            'questions': random.sample(all_questions, 10),
            'answers': {},
            'submitted': False,
            'score': 0
        }

    data = st.session_state.riddles_data

    if not data['submitted']:
        with st.form("riddles_form"):
            for i, q in enumerate(data['questions']):
                st.markdown(f"**{i+1}. {q['question']}**")
                data['answers'][i] = st.text_input(
                    "Your Answer:", key=f"riddles_q{i}")
            submitted = st.form_submit_button("✅ Submit All")

        if submitted:
            score = 0
            for i, q in enumerate(data['questions']):
                user_ans = data['answers'][i].strip().lower()
                correct_ans = q["answer"].strip().lower()
                if user_ans == correct_ans:
                    score += 1
            data['score'] = score
            data['submitted'] = True
            st.rerun()

    else:
        st.success(f"🎉 You scored {data['score']} out of 10")
        st.subheader("🧩 Correct Answers:")
        for i, q in enumerate(data['questions']):
            user_ans = data['answers'].get(i, "").strip()
            st.write(f"**{i+1}. {q['question']}**")
            st.write(
                f"✅ Correct: `{q['answer']}` | ❌ Your Answer: `{user_ans}`")
            st.markdown("---")

        if st.button("🔄 Restart Quiz"):
            del st.session_state['riddles_data']
            st.rerun()
