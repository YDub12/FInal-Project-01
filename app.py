import streamlit as st
from pathlib import Path

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

    st.markdown("""
    This page explores the visual differences between healthy
    cherry leaves and leaves affected by powdery mildew.

    Powdery mildew commonly appears as white, powder-like
    patches on the leaf surface.

    The images below were generated during the exploratory
    data analysis in Notebook 02.
    """)

    visual_path = Path("outputs/visual_study")

    st.subheader("Average Leaf Images")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            str(visual_path / "healthy_average.png"),
            caption="Average Healthy Leaf",
            use_container_width=True
        )

    with col2:
        st.image(
            str(visual_path / "mildew_average.png"),
            caption="Average Powdery Mildew Leaf",
            use_container_width=True
        )

    st.markdown("""
    **Interpretation:**

    These images represent the average pixel values across
    all images in each category.

    They help illustrate differences in overall colour and
    appearance between healthy and infected leaves.
    """)

    st.subheader("Leaf Image Variability")

    col3, col4 = st.columns(2)

    with col3:
        st.image(
            str(visual_path / "healthy_variability.png"),
            caption="Healthy Leaf Variability",
            use_container_width=True
        )

    with col4:
        st.image(
            str(visual_path / "mildew_variability.png"),
            caption="Powdery Mildew Variability",
            use_container_width=True
        )

    st.markdown("""
    **Interpretation:**

    Variability images show how much pixel values differ
    across images within the same category.

    Brighter areas indicate greater variation in pixel values.
    """)

    st.subheader("Difference Between Average Images")

    st.image(
        str(visual_path / "average_difference.png"),
        caption="Absolute Difference Between Class Averages",
        use_container_width=True
    )

    st.markdown("""
    **Interpretation:**

    The difference image highlights areas where the average
    pixel values differ between healthy and powdery mildew
    leaves.

    These visual differences support the hypothesis that
    the two classes have distinguishable characteristics.
    """)

elif page == "Disease Prediction":
    st.header("Disease Prediction")
    st.info("Image upload and prediction functionality will be added here.")

elif page == "Project Hypothesis":
    st.header("Project Hypothesis")
    st.info("Hypothesis findings will be added here.")

elif page == "Model Performance":
    st.header("Model Performance")
    st.info("Model evaluation results will be added here.")