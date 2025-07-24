import streamlit as st
import random


def main():
    st.title("📚 Story Time")
    st.write("Enjoy this short story and answer the questions!")

    # Define stories
    stories = [
        {
            "title": "🐇 The Clever Rabbit",
            "content": """
Once upon a time in a jungle, a fierce lion used to hunt and eat animals every day. All the animals were scared and decided to find a way to stop him. They chose a clever rabbit to trick the lion.

The rabbit told the lion that another lion claimed to be the king of the jungle. The angry lion asked the rabbit to show him the other lion. The rabbit led him to a deep well. The lion saw his own reflection and, thinking it was his enemy, jumped into the well.

All the animals were happy and the clever rabbit saved the jungle!

**Moral:** Intelligence wins over strength.
""",
            "questions": [
                "Who was troubling all the animals in the jungle?",
                "What trick did the rabbit play on the lion?",
                "What is the moral of the story?"
            ]
        },
        {
            "title": "🐦 The Honest Sparrow",
            "content": """
A small sparrow once lived in a tree near a village. One day, she found a shiny coin on the ground. Instead of keeping it, she flew to the village chief and gave it to him.

The villagers praised the sparrow for being honest. The chief rewarded her with grains and made her the village's 'honest bird'. The sparrow continued helping people and teaching kids about honesty.

**Moral:** Honesty is always rewarded.
""",
            "questions": [
                "What did the sparrow find on the ground?",
                "How did the villagers reward the sparrow?",
                "What is the moral of the story?"
            ]
        },
        {
            "title": "🐘 The Wise Elephant",
            "content": """
In a dry forest, animals were struggling to find water. A wise old elephant remembered a hidden pond deep in the jungle. He led the animals on a long journey to the pond and saved them all.

From that day, everyone respected the elephant and listened to his advice.

**Moral:** Wisdom and memory can save lives.
""",
            "questions": [
                "What problem were the animals facing?",
                "How did the elephant help the animals?",
                "What is the moral of the story?"
            ]
        }
    ]

    # Load a random story once
    if "current_story" not in st.session_state:
        st.session_state.current_story = random.choice(stories)

    story_data = st.session_state.current_story

    # Display the story
    st.markdown(f"### {story_data['title']}")
    st.markdown(story_data["content"])

    st.divider()
    st.subheader("📝 Answer These Questions")

    answers = []
    for i, q in enumerate(story_data["questions"], start=1):
        ans = st.text_input(f"{i}. {q}", key=f"story_q{i}")
        answers.append(ans)

    if st.button("✅ Submit Answers"):
        st.success("Thanks for answering! 🌟")
        st.markdown("### 📘 Your Answers")
        for i, ans in enumerate(answers, start=1):
            st.markdown(f"**Q{i}:** {ans}")

        # ✅ Save progress to parent dashboard
        if "child_progress" not in st.session_state:
            st.session_state.child_progress = {}

        st.session_state.child_progress["Story Time"] = {
            "completed": len(answers),
            "total": len(story_data["questions"])
        }

    if st.button("🔄 Read Another Story"):
        del st.session_state["current_story"]
        for i in range(1, 4):
            st.session_state.pop(f"story_q{i}", None)
        st.rerun()


if __name__ == "__main__":
    main()
