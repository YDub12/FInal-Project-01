import streamlit as st

st.set_page_config(
    page_title="Cherry Leaf Disease Detector",
    page_icon="🍒",
    layout="wide"
)

st.title("Cherry Leaf Powdery Mildew Detector")

st.write(
    "A machine-learning application for identifying "
    "powdery mildew on cherry leaves."
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose a page",
    [
        "Project Summary",
        "Visual Study",
        "Disease Prediction",
        "Project Hypothesis",
        "Model Performance"
    ]
)

if page == "Project Summary":
    st.header("Project Summary")

    st.markdown("""
    ### Cherry Leaf Powdery Mildew Detection

    This project uses a Convolutional Neural Network (CNN)
    to identify whether cherry leaves are **healthy** or
    **affected by powdery mildew**.

    The application was developed to help users recognise
    potential signs of powdery mildew through image analysis.

    ### Business Requirements

    **1. Visual differentiation**

    Help users understand the visual differences between
    healthy cherry leaves and leaves affected by powdery mildew.

    **2. Disease prediction**

    Allow users to upload cherry-leaf images and receive
    predictions indicating whether each leaf is healthy
    or affected by powdery mildew.

    ### Dataset

    The project uses the Cherry Leaves dataset from Kaggle.

    - **Total images:** 4,208
    - **Healthy leaves:** 2,104
    - **Powdery mildew leaves:** 2,104
    - **Original image dimensions:** 256 × 256 pixels

    ### Machine Learning Approach

    A Convolutional Neural Network was trained to recognise
    visual characteristics associated with powdery mildew.

    The model uses image features such as colour, texture
    and surface patterns to distinguish between the two classes.

    ### Model Performance

    The trained model achieved **99.69% accuracy** on
    the held-out test dataset, exceeding the client's
    minimum accuracy requirement of **97%**.

    This result was obtained on the provided dataset.
    Performance on independently collected photographs
    has not yet been established.

    ### How to Use This Dashboard

    Use the navigation menu on the left to explore:

    - **Visual Study:** Compare healthy and infected leaves.
    - **Disease Prediction:** Upload images for classification.
    - **Project Hypothesis:** Review the hypotheses and findings.
    - **Model Performance:** Examine accuracy and evaluation results.
    """)

    st.info(
        "Predictions are intended to support visual assessment "
        "and should not be treated as a definitive plant diagnosis."
    )

elif page == "Visual Study":
    st.header("Visual Study")
    st.info("Visual study charts and images will be added here.")

elif page == "Disease Prediction":
    st.header("Disease Prediction")
    st.info("Image upload and prediction functionality will be added here.")

elif page == "Project Hypothesis":
    st.header("Project Hypothesis")
    st.info("Hypothesis findings will be added here.")

elif page == "Model Performance":
    st.header("Model Performance")
    st.info("Model evaluation results will be added here.")