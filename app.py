import streamlit as st
from recommender import recommend_resources


st.set_page_config(
    page_title="StudyMate",
    page_icon="📚",
    layout="centered"
)


st.title("📚 StudyMate")
st.subheader("Personalized Study Resource Recommendation System")

st.write(
    "Enter your subject and difficulty level to get personalized "
    "study resource recommendations."
)


# Subject selection
subject = st.selectbox(
    "Select Subject",
    [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "Web Development",
        "Database",
        "Cloud Computing",
        "Cyber Security"
    ]
)


# Difficulty selection
difficulty = st.selectbox(
    "Select Difficulty Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)


# Recommendation button
if st.button("🔍 Get Recommendations"):

    results = recommend_resources(
        subject,
        difficulty,
        top_n=5
    )

    st.success("Here are your recommended study resources:")

    for _, row in results.iterrows():

        st.markdown(
            f"### 📖 {row['title']}"
        )

        st.write(
            f"**Subject:** {row['subject']}"
        )

        st.write(
            f"**Difficulty:** {row['difficulty']}"
        )

        st.write(
            f"**Type:** {row['resource_type']}"
        )

        st.write(
            f"**Description:** {row['description']}"
        )

        st.divider()
