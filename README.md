# PhishDec: Vigilant Cyber Reliability

PhishDec is a project aimed at detecting phishing websites using machine learning and deep neural networks. The project focuses on building a robust model to identify malicious websites early and accurately, ensuring users can avoid falling victim to phishing attacks. 

---

## **Introduction to Phishing**

Phishing is a prevalent form of social engineering and cyber-attack where attackers trick users into revealing sensitive information by mimicking legitimate websites. Preventing phishing requires:

- Awareness of phishing websites.
- A blacklist of known phishing websites.
- Early detection using **machine learning** and **deep neural network algorithms**.

Among these approaches, machine learning has proven to be the most effective.

---

## **Phishing Websites**

Phishing websites mimic trustworthy URLs and webpages to deceive users. The objective of this project is to:

1. Train machine learning and deep learning models using a carefully curated dataset of phishing and legitimate URLs.
2. Extract essential URL and content-based features.
3. Evaluate and compare model performances.

---

## **Data Collection**

### **Phishing URLs**:
- **Source**: [PhishTank](https://www.phishtank.com/developer_info.php)
- **Dataset**: 5,000 random phishing URLs downloaded in CSV format.
  
### **Legitimate URLs**:
- **Source**: [University of New Brunswick URL-2016 Dataset](https://www.unb.ca/cic/datasets/url-2016.html)
- **Dataset**: 5,000 random legitimate URLs extracted from benign URL data.

The datasets are stored in the `DataFiles` folder of this repository.

---

## **Technology Stack**

- **Python**: Used for machine learning and GUI development.
- **HTML & CSS**: Templates for web extensions.
- **JavaScript**: Executes the functionality of the web extension.

---

## **Approach**

The project involves the following steps:

1. **Data Collection**: Collect phishing and legitimate website URLs from open-source platforms.
2. **Feature Extraction**: Write a script to extract URL-based features for analysis.
3. **Data Analysis and Preprocessing**: Perform Exploratory Data Analysis (EDA) to clean and preprocess the data.
4. **Train-Test Split**: Split the dataset into training and testing subsets.
5. **Model Training**: Use machine learning and deep neural network algorithms like **XGBoost Classifier**.
6. **Evaluation**: Evaluate the models using accuracy metrics.
7. **Comparison**: Compare model results and select the best-performing one.

---

## **Feature Selection**

Features extracted from URLs fall into three main categories:

1. **Address Bar-Based Features**:
   - Domain of the URL.
   - Presence of redirection (`//`).
   - IP address in the URL.
   - HTTP/HTTPS in the domain name.
   - `@` symbol in the URL.
   - URL shortening services.
   - Length of the URL.
   - Prefix or suffix `-` in the domain.
   - Depth of the URL.

2. **Domain-Based Features**:
   - Examines the domain structure and properties.

3. **HTML & JavaScript-Based Features**:
   - Analyzes embedded HTML and JavaScript code.

---

## **Machine Learning Models**

This is a supervised classification task where URLs are classified as **phishing (1)** or **legitimate (0)**. The model trained for this project is:

### **Model: XGBoost Classifier**
- **Training Accuracy**: 86.8%
- **Testing Accuracy**: 85.7%

The trained model, achieving the highest performance, is saved as `XGBoostClassifier.pickle.dat`.

---

## **Procedure for Usage**

Refer to the `Procedure.md` file for step-by-step instructions on how to set up and use this project.

---

## **End Results**

- The **XGBoost Classifier** achieved the best performance with an accuracy of **86.8%** on the training dataset.
- The saved model (`XGBoostClassifier.pickle.dat`) is used to verify if a given URL is **legitimate** or **phishing**.
- Users can interact with the model via:
  - A **GUI application**.
  - A **web extension**.

---

## **Key Takeaways**

PhishDec is a reliable system for detecting phishing websites using advanced machine learning techniques. By leveraging robust datasets and efficient models, it ensures better cybersecurity and user awareness against phishing threats.

For further improvements, integrating additional features or using ensemble models can enhance detection accuracy.
