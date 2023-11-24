## Deployment

This application is deployed on Streamlit Cloud. You can access it by following this [link](https://smsspamdetect-ccqnvyzj6trnj8vt7mhutr.streamlit.app/).

## Overview

SMS Spam Detect is an application designed to identify and classify SMS messages as spam or non-spam (ham). The app leverages a machine learning model for efficient and accurate detection of spam messages. There are two models integrated into the application:

- **Main Model (`model.pkl`):** This is the primary model created by combining the outputs of four different models. It is designed for robust and comprehensive spam detection.

   - **Accuracy:** The `model.pkl` achieves an accuracy of 89%, indicating its effectiveness in correctly classifying SMS messages.

   - **Precision:** The precision of the `model.pkl` is 100%, emphasizing its ability to accurately identify spam messages with minimal false positives.

- **Secondary Model (`mnb_model.pkl`):** This model is smaller in size and serves as an alternative. If you encounter any issues with the main model (`model.pkl`), you can opt to use this secondary model for spam detection.



## Features

- **Spam Detection:** The app employs a machine learning model to analyze incoming SMS messages and determine whether they are spam or not.

- **User-Friendly Interface:** The Streamlit-based interface which is very smooth and easy to use.



## How to Use

There are two approaches to open the SMS Spam Detect project:

### 1. Streamlit Cloud

- The optimal way is to open the [SMS Spam Detect](https://smsspamdetect-ccqnvyzj6trnj8vt7mhutr.streamlit.app/) link in your web browser.

### 2. Manual Deployment

If you prefer to run the project manually, follow these steps:

- Download the project by [downloading the zip file](https://github.com/your-username/sms-spam-detect/archive/main.zip) or cloning the repository.

- Navigate to the project directory.

- Install the required dependencies by command:- pip install -r requirements.txt

- Run the file app.py and enter streamlit command:- streamlit run app.py

## Acknowledgments
Thanks to Kaggle for the dataset.

#### Note:
While the precision of the app is 100%, there are instances where it might classify human-written spam messages as "not spam". Please use valid spam messages for testing purposes.

Click on this [link](https://huggingface.co/datasets/sms_spam/viewer/plain_text/train?p=1&row=120) to access some data to evaluate the web app. Note that this dataset is not same as the one used to train and test the web app.
