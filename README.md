# Penguins Classifier App

## Overview

This Penguins Classifier app utilizes machine learning to classify penguins based on their bill height, bill depth, flipper length, and body mass. The application is built using the scikit-learn library for machine learning, and it has the capability to read penguin data from a CSV file.

## Installation

To run the Penguins Classifier App, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/samtechy26/penguin-classification-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd penguins-classifier-app
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the app, run the following command:

```bash
streamlit run app.py
```

This will open a new tab in your default web browser with the Penguins Classifier App.

## Demo

Click [here](https://samtechy26-penguin-classification-app-app-oogyne.streamlit.app/) for a live demo of the Penguins Classifier App.

## Input Parameters

The app takes the following input parameters for penguin classification:

- **Bill Height:** Height of the penguin's bill.
- **Bill Depth:** Depth of the penguin's bill.
- **Flipper Length:** Length of the penguin's flipper.
- **Body Mass:** Mass of the penguin's body.

## Reading Data from CSV

The app supports reading penguin data from a CSV file. To use this feature:

1. Click the "Upload CSV" button.
2. Select a CSV file containing penguin data with columns for bill height, bill depth, flipper length, body mass, and class label.
3. The app will load the data, and you can proceed with classification.

## How to Use

1. Enter the values for bill height, bill depth, flipper length, and body mass in the input fields.
2. Alternatively, upload a CSV file to load penguin data automatically.
3. Click the "Classify" button to initiate the classification process.
4. The app will display the predicted penguin class based on the provided parameters.

## Technologies Used

- **scikit-learn:** Utilized for machine learning and classification tasks.
- **Streamlit:** Used for building the interactive and user-friendly web application.

## Directory Structure

- **app.py:** Main application script containing the Streamlit app.
- **penguins_clf.pkl:** Pre-trained machine learning model for penguin classification.
- **requirements.txt:** List of dependencies required to run the application.


Feel free to explore, modify, and enhance the application as needed for your own use or learning purposes. If you have any questions or feedback, please reach out to [samakan061@gmail.com].
