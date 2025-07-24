import streamlit as st


def initialize_progress():
    st.session_state.child_progress = {
        "Math Quiz": {"completed": 0, "total": 10},
        "Vocabulary Quiz": {"completed": 0, "total": 10},
        "Animal Quiz": {"completed": 0, "total": 10},
        "Fun Facts Quiz": {"completed": 0, "total": 10},
        "Riddles Quiz": {"completed": 0, "total": 10},
        "Spelling Quiz": {"completed": 0, "total": 10},
        "Story Page": {"completed": 0, "total": 10}
    }


def main():
    st.title("👨‍👩‍👧 Parent Dashboard")

    # Initialize if missing
    if "child_progress" not in st.session_state:
        initialize_progress()

    st.subheader("Child's Quiz Progress")

    for quiz, progress in st.session_state.child_progress.items():
        completed = progress["completed"]
        total = progress["total"]
        percentage = int((completed / total) * 100) if total > 0 else 0
        st.markdown(
            f"**{quiz}:** {completed} / {total} completed ({percentage}%)")
        st.progress(percentage)

    st.markdown("---")
    st.info("This dashboard shows a snapshot of your child's progress in different quizzes and activities.")

    if st.button("🔄 Reset All Progress"):
        initialize_progress()
        st.success("✅ All progress has been reset.")
        st.rerun()


if __name__ == "__main__":
    main()
