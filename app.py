from pathlib import Path

import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import tensorflow as tf

from PIL import Image

@st.cache_resource
def load_prediction_model():
    model_path = Path("outputs/models/cherry_leaf_cnn.keras")
    return tf.keras.models.load_model(model_path)

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

    st.markdown("""
    Upload one or more cherry-leaf images to check whether
    they appear healthy or affected by powdery mildew.

    The CNN analyses each image and returns a predicted
    classification with estimated probabilities.
    """)

    uploaded_files = st.file_uploader(
        "Upload cherry-leaf images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if uploaded_files:
        model = load_prediction_model()

        results = []

        for uploaded_file in uploaded_files:
            try:
                image = Image.open(uploaded_file).convert("RGB")

                # Match the image size used during model training
                resized_image = image.resize((100, 100))

                # Convert the image to a NumPy array
                image_array = np.asarray(
                    resized_image,
                    dtype=np.float32
                )

                # Add the batch dimension expected by TensorFlow
                image_batch = np.expand_dims(image_array, axis=0)

                # Predict probability of powdery mildew
                probability_mildew = float(
                    model.predict(image_batch, verbose=0)[0][0]
                )

                probability_healthy = 1.0 - probability_mildew

                predicted_class = (
                    "Powdery Mildew"
                    if probability_mildew >= 0.5
                    else "Healthy"
                )

                st.divider()

                col1, col2 = st.columns([1, 2])

                with col1:
                    st.image(
                        image,
                        caption=uploaded_file.name,
                        use_container_width=True
                    )

                with col2:
                    st.subheader(uploaded_file.name)

                    st.write(
                        f"**Prediction:** {predicted_class}"
                    )

                    st.write(
                        f"**Healthy probability:** "
                        f"{probability_healthy:.2%}"
                    )

                    st.write(
                        f"**Powdery mildew probability:** "
                        f"{probability_mildew:.2%}"
                    )

                    st.progress(probability_mildew)

                results.append({
                    "Filename": uploaded_file.name,
                    "Prediction": predicted_class,
                    "Healthy Probability": round(
                        probability_healthy, 4
                    ),
                    "Powdery Mildew Probability": round(
                        probability_mildew, 4
                    )
                })

            except (OSError, ValueError) as error:
                st.error(
                    f"Could not process {uploaded_file.name}: {error}"
                )

        if results:
            st.divider()
            st.subheader("Prediction Results")

            results_df = pd.DataFrame(results)

            st.dataframe(
                results_df,
                use_container_width=True
            )

            csv_data = results_df.to_csv(index=False)

            st.download_button(
                label="Download Prediction Results",
                data=csv_data,
                file_name="cherry_leaf_predictions.csv",
                mime="text/csv"
            )

    st.info(
        "This model is intended to support visual assessment "
        "and should not be considered a definitive plant diagnosis."
    )

elif page == "Project Hypothesis":
    st.header("Project Hypothesis and Validation")

    st.markdown("""
    This page presents the two project hypotheses and evaluates
    them using the findings from the visual study and CNN model.

    ## Hypothesis 1 — Visual Differences

    **Hypothesis:**

    Healthy cherry leaves and leaves affected by powdery mildew
    have distinguishable visual characteristics.

    **Validation approach:**

    We examined random leaf samples, image montages,
    average images, variability images and the difference
    between the two class averages.

    **Findings:**

    - Healthy leaves generally appeared green.
    - Powdery mildew leaves frequently displayed white,
      powder-like patches.
    - Average and variability images showed differences
      in pixel colour and distribution between the classes.

    **Conclusion:**

    The visual analysis supports Hypothesis 1.

    ---

    ## Hypothesis 2 — Model Accuracy

    **Hypothesis:**

    A CNN can distinguish healthy cherry leaves from leaves
    affected by powdery mildew with at least 97% accuracy.

    **Validation approach:**

    We trained a CNN using the training dataset and monitored
    its performance using a separate validation dataset.

    The final model was evaluated using 646 held-out test images.

    **Findings:**

    - Test accuracy: **99.69%**
    - Correct predictions: **644 out of 646**
    - Healthy recall: **100%**
    - Powdery mildew recall: **99.37%**
    - Exact duplicate files across dataset splits: **0**

    **Conclusion:**

    Hypothesis 2 is supported by the held-out test results.
    The model exceeded the client's 97% accuracy target.

    ---

    ## Overall Conclusion

    Both hypotheses are supported by the evidence collected
    during the project.

    The visual study identified differences between the
    two categories, and the CNN achieved strong classification
    performance on the provided dataset.
    """)

    st.warning(
        "The model incorrectly classified two powdery mildew "
        "images as healthy. Further testing on independently "
        "collected photographs is recommended before relying "
        "on the model in real-world agricultural decisions."
    )

elif page == "Model Performance":
    st.header("Model Performance")

    st.markdown("""
    This page presents the performance of the trained
    Convolutional Neural Network (CNN) on the held-out
    test dataset.

    The model was evaluated using 646 images that were
    not used during training or validation.
    """)

    evaluation_path = Path("outputs/evaluation")

    # Load saved evaluation results
    with open(evaluation_path / "test_metrics.json") as file:
        metrics = json.load(file)

    classification_df = pd.read_csv(
        evaluation_path / "classification_report.csv",
        index_col=0
    )

    confusion_df = pd.read_csv(
        evaluation_path / "confusion_matrix.csv",
        index_col=0
    )

    # Display key performance metrics
    st.subheader("Test Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Test Accuracy",
            value=f"{metrics['test_accuracy']:.2%}"
        )

    with col2:
        st.metric(
            label="Test Loss",
            value=f"{metrics['test_loss']:.4f}"
        )

    with col3:
        st.metric(
            label="Accuracy Target",
            value=f"{metrics['target_accuracy']:.0%}"
        )

    if metrics["target_met"]:
        st.success(
            "The model meets the client's 97% accuracy target."
        )
    else:
        st.warning(
            "The model does not yet meet the 97% accuracy target."
        )

    # Confusion matrix
    st.subheader("Confusion Matrix")

    fig, ax = plt.subplots(figsize=(7, 5))

    sns.heatmap(
        confusion_df,
        annot=True,
        fmt="d",
        cmap="Blues",
        ax=ax
    )

    ax.set_title("Cherry Leaf CNN — Confusion Matrix")
    ax.set_xlabel("Predicted Class")
    ax.set_ylabel("Actual Class")

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.markdown("""
    **Interpretation:**

    - 330 healthy leaves were correctly classified.
    - 314 powdery mildew leaves were correctly classified.
    - Two powdery mildew leaves were incorrectly classified
      as healthy.
    - No healthy leaves were incorrectly classified as
      powdery mildew.

    The two false-negative predictions are important because
    they represent diseased leaves that the model failed to
    identify.
    """)

    # Classification report
    st.subheader("Classification Report")

    st.dataframe(
        classification_df,
        use_container_width=True
    )

    st.markdown("""
    **Understanding the metrics:**

    - **Precision:** How often predictions of a class are correct.
    - **Recall:** How many actual examples of a class are detected.
    - **F1-score:** A combined measure of precision and recall.
    - **Support:** The number of images belonging to each class.
    """)

    st.info(
        "The model achieved 99.69% accuracy on the provided "
        "test dataset. Performance on independently collected "
        "images has not yet been established."
    )