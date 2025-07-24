import streamlit as st


def main():
    st.title("🏆 Achievements")

    if "child_progress" not in st.session_state or not st.session_state.child_progress:
        st.info("No quiz progress yet. Complete some quizzes to see achievements here.")
        return

    progress = st.session_state.child_progress

    st.markdown("### ⭐ Highest Scores")

    # Show top-performing quizzes
    high_scores = []
    for quiz, data in progress.items():
        if "score" in data and "total" in data:
            score_percent = (data["score"] / data["total"]) * 100
            high_scores.append((quiz, score_percent))

    if not high_scores:
        st.info("No scores to display yet.")
        return

    high_scores.sort(key=lambda x: x[1], reverse=True)

    for quiz, percent in high_scores:
        if percent >= 90:
            medal = "🥇"
        elif percent >= 75:
            medal = "🥈"
        elif percent >= 60:
            medal = "🥉"
        else:
            medal = "🎯"

        st.write(f"{medal} **{quiz}**: {percent:.1f}%")

    # Optional reset
    if st.button("🔁 Clear All Rewards Data"):
        if "child_progress" in st.session_state:
            del st.session_state.child_progress
        st.success("✅ All achievement data cleared.")
        st.rerun()
