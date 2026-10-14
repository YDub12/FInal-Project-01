# Cherry Leaf Powdery Mildew Detector

Project Overview

The Cherry Leaf Powdery Mildew Detector is a machine-learning application designed to identify whether a cherry leaf is healthy or affected by powdery mildew.

The project was developed in response to a business challenge faced by Farmy & Foods, whose cherry plantations require regular inspection for signs of disease.

A Convolutional Neural Network (CNN) was trained using labelled cherry-leaf images and integrated into an interactive Streamlit dashboard. Users can explore the visual differences between healthy and diseased leaves, upload images for classification, review model evaluation results and download predictions.

The trained model achieved 99.69% accuracy on 646 held-out test images, exceeding the client's required accuracy of 97%.

Project status: Machine-learning development, model evaluation, Streamlit dashboard development and Heroku deployment completed.

Live Application

The application is deployed on Heroku.

Launch the Live Application

The dashboard contains five pages:

Project Summary — Introduces the project, business requirements, dataset and machine-learning approach.

Visual Study — Explores differences between healthy and powdery mildew leaves using average images, variability images and visual comparisons.

Disease Prediction — Allows users to upload cherry-leaf images, receive CNN predictions, view classification probabilities and download results as a CSV file.

Project Hypothesis — Presents the project hypotheses and evaluates them against the evidence collected.

Model Performance — Displays test accuracy, loss, confusion matrix and classification metrics.

The application is intended as a demonstration of machine-learning image classification. It is not a replacement for professional agricultural diagnosis.

Business Requirements

Farmy & Foods operates cherry plantations across multiple farms and has experienced problems with powdery mildew affecting its crops.

The existing inspection process involves employees manually examining samples of leaves to determine whether a tree is healthy or affected by powdery mildew.

According to the project brief, inspecting a tree takes approximately 30 minutes. Where disease is identified, applying the appropriate treatment takes approximately one additional minute.

With thousands of cherry trees across multiple farms, this manual inspection process is time-consuming and difficult to scale.

The company is interested in investigating whether machine learning could support faster identification of potentially diseased leaves.

Business Requirement 1 — Visual Differentiation

The client wants to conduct a study to visually differentiate healthy cherry leaves from leaves affected by powdery mildew.

Project response:

Examine representative images from both classes.

Generate image montages and visual comparisons.

Calculate average images for each category.

Calculate pixel-variability images.

Compare average healthy and diseased images.

Present the findings in the Streamlit dashboard.

Business Requirement 2 — Disease Prediction

The client wants to predict whether a cherry leaf is healthy or affected by powdery mildew using an image.

Project response:

Prepare labelled training, validation and test datasets.

Train a CNN to classify cherry-leaf images.

Evaluate the model using held-out test data.

Aim for at least 97% classification accuracy.

Integrate the trained model into an interactive dashboard.

Allow users to upload images and download prediction results.

Project Hypotheses and Validation

Hypothesis 1 — Visual Differences

Hypothesis: Healthy cherry leaves and leaves affected by powdery mildew exhibit distinguishable visual characteristics, particularly in colour and surface texture.

Validation approach:

The visual study examined random samples, image montages, average images, variability images and differences between the average images of the two classes.

Findings:

Healthy leaves generally appeared green, while leaves affected by powdery mildew frequently displayed white, powder-like patches.

The average and variability images also showed differences in pixel colour and distribution between the two categories.

Conclusion: The visual analysis supports Hypothesis 1.

Hypothesis 2 — Model Accuracy

Hypothesis: A CNN trained on labelled cherry-leaf images can achieve at least 97% classification accuracy on a held-out test dataset.

Validation approach:

A CNN was trained using the training dataset, monitored using a separate validation dataset and evaluated on 646 held-out test images.

Findings:

Test accuracy: 99.69%

Correct predictions: 644 out of 646

Healthy recall: 100%

Powdery mildew recall: 99.37%

Conclusion: Hypothesis 2 is supported by the held-out test results. The model exceeded the client's 97% accuracy target.

These results apply to the provided dataset and do not guarantee equivalent performance on independently collected photographs.

Dataset

The dataset was obtained from Kaggle as part of the Code Institute machine-learning project.

It contains 4,208 cherry-leaf images divided equally between two categories:

Class

Number of images

Healthy

2,104

Powdery mildew

2,104

Total

4,208

The original images are 256 × 256 pixels.

The dataset includes rotated and flipped image variations, which required additional care when splitting the data to reduce the risk of leakage between training and testing.

Dataset Preparation

Images were checked for corruption and organised into three datasets.

Dataset

Healthy

Powdery mildew

Total

Training

1,464

1,472

2,936

Validation

310

316

626

Testing

330

316

646

Total

2,104

2,104

4,208

The split was approximately 70% training, 15% validation and 15% testing by image count.

The original and processed dataset images are excluded from version control.

Machine-Learning Workflow

The project was developed using five Jupyter notebooks.

1. Data Collection

Notebook: 01 data_collection.ipynb

The data collection notebook:

Downloaded the dataset from Kaggle.

Verified the two image categories.

Confirmed that the dataset contained 4,208 images.

Checked the original image dimensions.

Established the dataset directory structure.

Kaggle credentials were stored securely and excluded from version control.

2. Data Visualisation

Notebook: 02_data_visualisation.ipynb

The visualisation notebook:

Displayed random image samples.

Generated image montages.

Calculated average images for each class.

Generated pixel-variability images.

Compared average healthy and powdery mildew images.

Saved visual-study outputs for the dashboard.

The following files were generated:

outputs/visual_study/
├── healthy_average.png
├── mildew_average.png
├── healthy_variability.png
├── mildew_variability.png
└── average_difference.png

3. Data Cleaning and Preparation

Notebook: 03_data_cleaning.ipynb

The data preparation notebook:

Checked all 4,208 images for corruption.

Confirmed that no corrupt images were found.

Identified 1,847 source-image groups using filename information.

Kept known augmented versions of source photographs within the same dataset split.

Created training, validation and test datasets.

Recorded split assignments in a manifest.

The split manifest is stored locally within the processed-data directory and is excluded from version control.

4. Model Training

Notebook: 04_model_training.ipynb

A CNN was developed using TensorFlow and Keras.

The model architecture includes:

Input images resized to 100 × 100 pixels.

Pixel-value normalisation.

Convolutional layers for feature extraction.

Max-pooling layers for dimensionality reduction.

Dense layers for classification.

Dropout to reduce overfitting.

A sigmoid output for binary classification.

The model was compiled using:

Setting

Value

Optimiser

Adam

Learning rate

0.001

Loss function

Binary crossentropy

Performance metric

Accuracy

Early stopping

Validation loss

Early-stopping patience

3 epochs

Training ended after eight epochs, with the best validation-loss weights restored from epoch five.

The trained model was saved to:

outputs/models/cherry_leaf_cnn.keras

The training history was saved to:

outputs/models/training_history.csv

The saved model includes its own pixel-value rescaling layer. Therefore, uploaded images are resized and converted into numerical arrays before prediction but are not normalised a second time.

5. Model Evaluation

Notebook: 05_model_evaluation.ipynb

The final CNN was evaluated on the held-out test dataset containing 646 images.

The test images were not used during training or validation.

Test Performance

Metric

Result

Test accuracy

99.69%

Test loss

0.0289

Correct classifications

644

Incorrect classifications

2

Healthy precision

99.40%

Healthy recall

100.00%

Healthy F1-score

99.70%

Powdery mildew precision

100.00%

Powdery mildew recall

99.37%

Powdery mildew F1-score

99.68%

Confusion Matrix

Actual class

Predicted healthy

Predicted powdery mildew

Healthy

330

0

Powdery mildew

2

314

The model correctly classified all 330 healthy images and 314 of the 316 powdery mildew images.

The two incorrect predictions were false negatives: leaves affected by powdery mildew that were classified as healthy.

This is an important limitation because a missed disease prediction could delay appropriate action.

Accuracy Target

The model achieved 99.69% accuracy, exceeding the client's 97% target by approximately 2.69 percentage points.

The accuracy figure describes performance on the available held-out test dataset. It does not establish performance under all real-world conditions.

Data Leakage Checks

The dataset contains augmented images, including rotated and flipped versions of source photographs.

A conventional random image split could place related images in both training and testing datasets, potentially producing overly optimistic evaluation results.

To reduce this risk:

Images were grouped using identifiers derived from their filenames.

Known augmented versions were assigned to the same dataset split.

No identified source-image groups overlapped across training, validation and testing.

SHA-256 hashing identified 4,208 unique image files.

No byte-for-byte duplicate files were found across dataset splits.

These checks reduce leakage risk but do not rule out every possible visual duplicate or transformed photograph.

Streamlit Dashboard

The completed Streamlit dashboard provides an interactive interface for exploring the project and using the trained CNN.

Project Summary

Introduces the project, business requirements, dataset and machine-learning approach.

Visual Study

Displays average images, pixel-variability images and differences between healthy and powdery mildew leaves.

Disease Prediction

Allows users to:

Upload JPG, JPEG or PNG images.

Upload multiple images in one session.

View uploaded images.

Receive a healthy or powdery mildew prediction.

View classification probabilities.

Download prediction results as a CSV file.

The application uses a classification threshold of 0.5 for the CNN's sigmoid output.

Project Hypothesis

Presents the two hypotheses and explains how the visual analysis and model evaluation support them.

Model Performance

Displays:

Test accuracy.

Test loss.

Required accuracy target.

Confusion matrix.

Classification report.

Interpretation of the evaluation results.

The dashboard reads the saved model and evaluation files rather than recalculating the test results each time the page loads.

Dashboard Screenshots

Project Summary





Visual Study



Disease Prediction



Project Hypothesis





Model Performance





Technologies Used

Technology

Purpose

Python

Main programming language

Jupyter Notebook

Data exploration, preparation, training and evaluation

NumPy

Numerical arrays and image calculations

Pandas

Data manipulation, reports and prediction results

Matplotlib

Charts and visualisations

Seaborn

Statistical visualisations and confusion matrix

Pillow

Image loading, conversion and resizing

Scikit-learn

Dataset splitting and model evaluation

TensorFlow / Keras

CNN development, training and inference

Streamlit

Interactive web dashboard

PyArrow

DataFrame display support

Git

Version control

GitHub

Repository hosting

GitHub Codespaces

Development environment

Heroku

Application deployment

Repository Structure

.
├── app.py
├── jupyter_notebooks/
│   ├── 01 data_collection.ipynb
│   ├── 02_data_visualisation.ipynb
│   ├── 03_data_cleaning.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_model_evaluation.ipynb
├── outputs/
│   ├── visual_study/
│   │   ├── healthy_average.png
│   │   ├── mildew_average.png
│   │   ├── healthy_variability.png
│   │   ├── mildew_variability.png
│   │   └── average_difference.png
│   ├── models/
│   │   ├── cherry_leaf_cnn.keras
│   │   └── training_history.csv
│   └── evaluation/
│       ├── test_metrics.json
│       ├── classification_report.csv
│       └── confusion_matrix.csv
├── docs/
│   └── screenshots/
├── data/
│   ├── raw/
│   └── processed/
├── requirements.txt
├── requirements-dev.txt
├── Procfile
├── setup.sh
├── .python-version
├── .slugignore
├── .gitignore
└── README.md

The data/ directories contain local working datasets and are excluded from version control.

The saved CNN, evaluation outputs and visual-study images are required by the dashboard.

Running the Project Locally

The project was developed using Python 3.12 in GitHub Codespaces.

1. Clone the Repository

Clone the project repository and navigate into its root directory.

2. Create a Virtual Environment

python -m venv .venv
source .venv/bin/activate

3. Install Dependencies

To install the dashboard dependencies:

python -m pip install -r requirements.txt

To install the additional development dependencies used by the notebooks:

python -m pip install -r requirements-dev.txt

4. Launch the Dashboard

From the project root, run:

python -m streamlit run app.py

Open the local Streamlit address shown in the terminal.

In GitHub Codespaces, open the forwarded port through the Ports tab.

5. Run the Notebooks

Open the Jupyter notebooks and execute them in numerical order.

Reproducing the complete training workflow requires access to the original Kaggle dataset.

Kaggle credentials must be configured securely and must not be committed to the repository.

Testing

Testing was carried out throughout development to verify the dataset, machine-learning workflow and dashboard functionality.

Data Validation

Test

Result

Status

Verify dataset contains 4,208 images

4,208 images confirmed

Passed

Verify two image categories

Healthy and powdery mildew confirmed

Passed

Check image corruption

No corrupt images identified

Passed

Check dataset split totals

2,936 training, 626 validation, 646 testing

Passed

Check source-image group overlap

No identified groups shared across splits

Passed

Check exact duplicate files

No byte-for-byte duplicates across splits

Passed

Model Evaluation

Test

Expected result

Actual result

Status

Test accuracy

At least 97%

99.69%

Passed

Healthy classification

Correctly identify healthy leaves

330 of 330

Passed

Powdery mildew classification

Correctly identify diseased leaves

314 of 316

Passed with limitation

Held-out evaluation

Use separate test data

646 test images

Passed

The two false-negative predictions are documented as a model limitation.

Dashboard Functionality

Feature

Expected result

Status

Project Summary

Project information displays correctly

Passed

Visual Study

Average, variability and difference images display

Passed

Disease Prediction

Users can upload images and receive predictions

Passed

Multiple image uploads

Multiple images can be processed

Passed

Prediction probabilities

Classification probabilities display correctly

Passed

CSV download

Prediction results can be downloaded

Passed

Project Hypothesis

Hypotheses and conclusions display correctly

Passed

Model Performance

Accuracy, confusion matrix and classification report display

Passed

Navigation

Users can switch between dashboard pages

Passed

Local application startup

Streamlit starts in Codespaces

Passed

Heroku deployment

Application loads from its deployed URL

Passed

Testing Limitations

The model was evaluated using the provided cherry-leaf dataset.

Although the data-splitting process reduced the risk of leakage, further testing on independently collected photographs is required to establish performance under real-world agricultural conditions.

Classification probabilities have not been independently calibrated.

Deployment

Heroku

The application is deployed on Heroku.

Open the Deployed Application

Deployment Configuration

The deployment uses the following files:

File

Purpose

app.py

Main Streamlit application

requirements.txt

Production dependencies

requirements-dev.txt

Development and notebook dependencies

Procfile

Heroku web-process startup command

setup.sh

Streamlit server configuration

.python-version

Python 3.12 runtime specification

.slugignore

Excludes unnecessary files from deployment

The application loads its trained CNN from:

outputs/models/cherry_leaf_cnn.keras

The evaluation and visual-study files are loaded from the outputs/ directory.

The original and processed dataset images are not required to run the deployed dashboard.

Deployment Process

The deployment process involved:

Preparing the Streamlit application and saved model artifacts.

Separating dashboard dependencies from notebook development dependencies.

Configuring the Heroku startup command using Procfile.

Configuring Streamlit to use the hosting environment's assigned port.

Excluding unnecessary files from deployment using .slugignore.

Authenticating with Heroku using browser-based login and multifactor authentication.

Deploying the application to Heroku.

Opening the live application and checking that the dashboard loaded successfully.

Deployment Verification

The application was successfully launched on Heroku.

The dashboard's navigation, model prediction interface and evaluation pages were checked during development and deployment testing.

A PyArrow and NumPy compatibility issue was identified during dashboard testing and resolved by pinning PyArrow to version 17.0.0.

The application uses TensorFlow CPU for inference and does not require GPU hardware.

Bugs, Issues and Resolutions

Several technical challenges were encountered during development. The following issues were investigated and resolved.

1. Python Virtual Environment and Package Installation

Issue: Package installation initially failed in GitHub Codespaces because the environment had PIP_USER set to yes, which conflicted with package installation inside the virtual environment.

Resolution: The environment variable was unset using:

unset PIP_USER

The virtual environment was activated before installing dependencies, and the correct Python interpreter was selected as the Jupyter kernel.

2. Kaggle Authentication and Dataset Paths

Issue: Downloading the Kaggle dataset required authentication. The extracted dataset also contained an additional nested directory.

Resolution: Kaggle credentials were stored in the user's private .kaggle directory with restricted permissions. The extracted folder structure was inspected, and notebook paths were updated.

3. Image File Extension Differences

Issue: Some images used uppercase .JPG extensions, which could be missed by lowercase-only file filters.

Resolution: File extensions were normalised using .suffix.lower() before checking supported image formats.

This ensured that all 4,208 images were included.

4. Jupyter Notebook Syntax and Working Directory

Issue: A notebook template contained an incomplete try block, causing an IndentationError. File paths also required care when switching between notebook and project-root directories.

Resolution: The invalid code was corrected, and the working directory was verified before file operations.

5. Kernel Crashing During Image Analysis

Issue: The Jupyter kernel crashed when average and variability images were calculated by loading too many full-resolution images into memory simultaneously.

Resolution: The calculation was rewritten to process images incrementally using an online mean and variance algorithm.

This reduced memory usage and allowed the visual analysis to complete.

6. Dataset Splitting and Augmented Images

Issue: The dataset contained rotated and flipped versions of source photographs. Random image splitting could place related images in different datasets and increase leakage risk.

An initial attempt at constructing the split lists also produced incorrect group counts.

Resolution: Images were grouped using filename-derived source identifiers, and groups were assigned to training, validation or testing.

All 1,847 identified source-image groups were assigned without group overlap.

A subsequent SHA-256 check found no exact duplicate files across the splits.

7. TensorFlow Warnings

Issue: TensorFlow displayed warnings relating to dataset shuffling and an OUT_OF_RANGE: End of sequence message during evaluation.

Resolution: The messages were reviewed. Training data was already shuffled when the dataset was created, and evaluation completed successfully.

No further changes were required.

8. Saved Keras Model Not Displaying in VS Code

Issue: VS Code reported that the saved .keras file was too large to display in the text editor.

Resolution: The file was identified as a binary model artifact rather than a text file.

The model was loaded using TensorFlow/Keras to verify that it could be used.

9. PyArrow and NumPy Compatibility

Issue: The Model Performance page displayed an import error when attempting to show the classification report:

ImportError: pyarrow requires NumPy 2.0 or newer, found 1.26.1

Resolution: PyArrow was pinned to version 17.0.0, which is compatible with the project's NumPy version.

The classification report was tested again and displayed successfully.

10. Streamlit Port Already in Use

Issue: During local testing in Codespaces, Streamlit failed to restart because port 8501 was already occupied.

Some earlier Streamlit processes had remained running or had been suspended.

Resolution: Running Streamlit processes were identified using:

ps aux | grep '[s]treamlit'

The relevant processes were stopped, and Streamlit was restarted.

The dashboard was then accessed through the Codespaces forwarded port.

11. Streamlit CORS Configuration Warning

Issue: The original Streamlit setup disabled CORS while XSRF protection remained enabled, causing a configuration warning.

Resolution: The setup script was updated to remove the conflicting CORS setting while retaining Streamlit's default security protections.

Lessons Learned

These challenges reinforced the importance of:

Checking environment configuration before installing packages.

Validating file paths and image formats.

Managing memory efficiently when processing images.

Preventing data leakage during dataset preparation.

Verifying saved model artifacts.

Testing dependency compatibility.

Checking running processes and server ports.

Testing the application locally before deployment.

Known Limitations

The project has several limitations:

Evaluation was performed using images from the provided dataset.

The dataset includes augmented images, which can complicate assessment of model generalisation.

Exact-file hashing cannot identify every visually equivalent or transformed photograph.

Two diseased leaves were incorrectly classified as healthy.

Classification probabilities have not been independently calibrated.

Performance on photographs from different cameras, lighting conditions and environments has not been established.

The model performs binary classification and does not diagnose other cherry-leaf diseases.

The application is a demonstration and should not be used as the sole basis for agricultural treatment decisions.

Future Improvements

Potential future improvements include:

Testing the model using independently collected cherry-leaf photographs.

Investigating the two false-negative predictions.

Assessing probability calibration and alternative classification thresholds.

Comparing the CNN with transfer-learning approaches.

Introducing additional cherry-leaf disease categories.

Testing model robustness under different lighting and image-quality conditions.

Exploring ways to integrate predictions into a wider agricultural monitoring workflow.

Main Data Analysis and Machine Learning Libraries

NumPy

Used for numerical arrays, image preprocessing and pixel-level calculations.

Pandas

Used for dataset records, evaluation reports and downloadable prediction results.

Matplotlib and Seaborn

Used for image visualisation, charts and the confusion matrix.

Pillow

Used for loading, converting and resizing images.

Scikit-learn

Used for dataset splitting, classification metrics and evaluation.

TensorFlow and Keras

Used to build, train, save, load and evaluate the CNN.

Streamlit

Used to create the interactive web dashboard.

PyArrow

Used by Streamlit for DataFrame display.

Credits

Dataset and Project Brief

The project was developed using the Code Institute machine-learning project framework and the cherry-leaf image dataset distributed through Kaggle.

Documentation and Development Resources

Documentation and resources associated with Python, TensorFlow, Keras, Streamlit, NumPy, Pandas, Matplotlib, Seaborn, Pillow and Scikit-learn supported development.

AI Assistance

AI assistance was used for code explanations, debugging, documentation drafting and deployment troubleshooting.

The model training, evaluation results and application functionality were tested within the project environment.