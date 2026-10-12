***Cherry Leaf Powdery Mildew Detector***

Project Overview

This project develops a machine-learning image classifier to identify powdery mildew on cherry leaves.

Using a Convolutional Neural Network (CNN), the model predicts whether a cherry leaf is healthy or affected by powdery mildew.

The project is designed to support the early identification of potential leaf disease through image analysis. A Streamlit dashboard is planned to allow users to explore the dataset, review model performance, and upload images for classification.

Project status: Machine-learning development and evaluation completed. Streamlit dashboard and deployment are in development.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

Hypothesis 1: Healthy cherry leaves and leaves affected by powdery mildew exhibit distinguishable visual characteristics, particularly in colour and surface texture.

Hypothesis 2: A CNN trained on labelled cherry-leaf images can achieve at least 97% classification accuracy on a held-out test dataset.

Machine-Learning Workflow

1. Data Collection

Notebook: 01 data_collection.ipynb

Downloaded the dataset from Kaggle.

Verified the two image categories.

Confirmed 4,208 images in total.

Confirmed that the images are 256 × 256 pixels.

2. Data Visualisation

Notebook: 02_data_visualisation.ipynb

Displayed random image samples and image montages.

Generated average images for each class.

Generated pixel-variability images.

Compared average healthy and powdery mildew images.

Saved visual-study outputs for future dashboard integration.

3. Data Preparation

Notebook: 03_data_cleaning.ipynb

Checked all 4,208 images for corruption.

Identified 1,847 source-image groups using filename information.

Kept known augmented versions of each source photograph within the same dataset split.

Created training, validation and test datasets.

Recorded the split assignments in a manifest.

Dataset Split

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

4. Model Training

Notebook: 04_model_training.ipynb

A CNN was built using TensorFlow and Keras.

The model includes:

Image resizing to 100 × 100 pixels.

Pixel-value normalisation.

Convolutional layers for feature extraction.

Max-pooling layers for dimensionality reduction.

Dense layers for classification.

Dropout to reduce overfitting.

A sigmoid output for binary classification.

The model was trained using:

Adam optimiser.

Binary crossentropy loss.

Accuracy as a performance metric.

Early stopping based on validation loss.

Training ended after eight epochs, with the best validation-loss weights restored.

The trained model was saved as:

outputs/models/cherry_leaf_cnn.keras

5. Model Evaluation

Notebook: 05_model_evaluation.ipynb

The model was evaluated using the 646-image held-out test dataset, which was not used during training or validation.

Test Performance

Metric

Result

Accuracy

99.69%

Loss

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

The two errors were false negatives: diseased leaves incorrectly classified as healthy.

This is an important limitation because a missed disease prediction could delay appropriate action.

Accuracy Target

The model achieved 99.69% accuracy on the held-out test dataset, exceeding the client's 97% target by 2.69 percentage points.

This result applies to the available test dataset and does not guarantee equivalent performance on new photographs collected under different conditions.

Data Leakage Checks

The dataset contains augmented images, making careful splitting important.

To reduce the risk of data leakage:

Images were grouped using identifiers derived from their source filenames.

Known rotated and flipped versions were assigned to the same dataset split.

No source-image groups overlapped across training, validation and testing.

SHA-256 hashing identified 4,208 unique image files.

No byte-for-byte duplicate files were found across dataset splits.

These checks reduce leakage risk but do not rule out visually equivalent images stored with different transformations or compression.

Technologies Used

Python

Jupyter Notebook

NumPy

Pandas

Matplotlib

Seaborn

Pillow

Scikit-learn

TensorFlow / Keras

Streamlit (planned dashboard)

Git and GitHub

GitHub Codespaces

Heroku (planned deployment)

Repository Structure

.
├── jupyter_notebooks/
│   ├── 01 data_collection.ipynb
│   ├── 02_data_visualisation.ipynb
│   ├── 03_data_cleaning.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_model_evaluation.ipynb
├── outputs/
│   ├── visual_study/
│   ├── models/
│   │   ├── cherry_leaf_cnn.keras
│   │   └── training_history.csv
│   └── evaluation/
│       ├── test_metrics.json
│       ├── classification_report.csv
│       └── confusion_matrix.csv
├── data/
│   ├── raw/
│   └── processed/
├── requirements.txt
├── Procfile
├── setup.sh
├── .slugignore
└── README.md

The data/ folders contain local working datasets and are excluded from version control.

Running the Project Locally

The project was developed using Python in GitHub Codespaces.

Create and activate a virtual environment, then install the required packages:

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

Run the Jupyter notebooks in numerical order.

To reproduce the data collection process, obtain access to the Kaggle dataset and configure Kaggle credentials securely. Do not commit credentials or original client images.

Dashboard startup instructions will be added once the Streamlit application has been implemented.

Deployment

Status: Not yet deployed.

The intended deployment platform is Heroku.

Before deployment, the project will require:

A completed Streamlit dashboard.

Verification of the application startup configuration.

Confirmation that the trained model can be loaded in the deployed environment.

Dependency and file-size checks.

End-to-end testing of uploaded-image predictions.

The live application URL will be added after deployment.

Known Limitations

Evaluation was performed using images from the provided dataset.

The dataset contains augmented images, which can make generalisation assessment more challenging.

Exact-file hashing does not detect all visually duplicated or transformed photographs.

Two diseased leaves were incorrectly classified as healthy.

Model probability outputs have not been independently calibrated.

Performance on photographs from different cameras, lighting conditions or environments has not yet been established.

The Streamlit dashboard and deployment are still in development.

Future Improvements

Test the model using independently collected cherry-leaf photographs.

Investigate the two false-negative predictions.

Assess probability calibration and classification thresholds.

Compare the CNN with transfer-learning approaches.

Complete the Streamlit dashboard.

Deploy and test the application on Heroku.

Acknowledgements

Code Institute for the project dataset and educational framework.

Kaggle for dataset distribution.

TensorFlow, Keras, Scikit-learn and Streamlit for the tools used in the project.

## Bugs
Bugs, Issues and Resolutions

Several technical challenges were encountered during the development of this project. These issues provided opportunities to improve the code, understand the development environment and make the machine-learning workflow more reliable.

1. Python Virtual Environment and Package Installation

Issue: Package installation initially failed in GitHub Codespaces because the environment had the PIP_USER variable set to yes, which conflicted with installing packages inside the project's virtual environment.

Resolution: The environment variable was unset using unset PIP_USER, and the virtual environment was activated before installing the dependencies. The correct Python interpreter was also selected as the Jupyter notebook kernel.

2. Kaggle Dataset Authentication and File Paths

Issue: Downloading and accessing the Kaggle dataset required additional configuration. The extracted dataset also contained an extra nested directory, which initially complicated locating the image folders.

Resolution: The Kaggle API credentials were moved to the user's private .kaggle directory with restricted file permissions. The dataset directory structure was inspected, and the notebook paths were updated to reference the correct folders.

3. Image File Extension Differences

Issue: The dataset contained images using uppercase .JPG extensions. Initial file-filtering logic could miss these images when checking only lowercase extensions.

Resolution: File extensions were normalised using .suffix.lower() before checking supported image formats. This ensured all 4,208 images were included.

4. Jupyter Notebook Syntax and Working Directory Issues

Issue: A notebook template contained an incomplete try block, causing an IndentationError. There was also a risk of incorrect file paths when changing the working directory between the notebook folder and the project root.

Resolution: The invalid code block was replaced with valid folder-creation logic, and the working directory was checked before running file operations.

5. Kernel Crashing During Image Analysis

Issue: The Jupyter kernel crashed when calculating average and variability images because the original approach loaded large numbers of full-resolution images into memory simultaneously.

Resolution: The calculation was rewritten to process images one at a time using an incremental mean and variance algorithm. This substantially reduced memory usage and allowed the visual analysis to complete successfully.

6. Dataset Splitting and Augmented Images

Issue: The dataset contained rotated and flipped versions of source photographs. A conventional random image split could place related images in both training and testing datasets, creating a risk of data leakage. An initial attempt at constructing the split lists also produced zero group counts due to notebook execution or indentation issues.

Resolution: Images were grouped by identifiers derived from their filenames, and the groups were split rather than individual images. The corrected process assigned all 1,847 source-image groups to training, validation or testing, with no group overlap. A subsequent SHA-256 check found no exact duplicate files across splits.

7. TensorFlow Warnings During Training and Evaluation

Issue: TensorFlow displayed a warning about the shuffle parameter during training and an OUT_OF_RANGE: End of sequence message during evaluation.

Resolution: The warnings were reviewed. Training data was already shuffled when the dataset was created, and evaluation completed successfully despite the end-of-sequence message. No changes were required.

8. Saved Model Not Displaying in VS Code

Issue: VS Code reported that the saved Keras model was too large to display in the text editor.

Resolution: The .keras file was recognised as a binary model artifact rather than a text file. The model was saved successfully, and TensorFlow's model-loading functionality was used to verify that it could be opened programmatically.

Lessons Learned

These challenges reinforced the importance of checking environment configuration, validating file paths, managing memory efficiently, preventing data leakage and verifying saved model artifacts. They also highlighted the value of testing each stage of a machine-learning pipeline before moving on to the next.

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
