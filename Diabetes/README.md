# Predictive Modeling for Diabetes Detection using Generalized Regression Neural Network (GRNN)

![Data Source](https://img.shields.io/badge/Data%20Source-Ahlam%20Rashid-blue)
![Published](https://img.shields.io/badge/Published-18%20July%202020-green)
![DOI](https://img.shields.io/badge/DOI-10.17632/wj9rwkp9c2.1-yellow)
![Research Journal](https://img.shields.io/badge/Research%20Journal-Iraq%20Patient%20Dataset%20of%20Diabetes(IPDD)-orange)

## Abstract

This project investigates the application of a sophisticated Generalized Regression Neural Network (GRNN) for the precise identification of diabetes in patients. Leveraging a meticulously curated dataset sourced from the esteemed lab of Medical City Hospital in Iraq, the study endeavors to forge a robust predictive model capable of discerning subtle diabetic markers amidst intricate medical data.

The study, conducted within the confines of Jupyter Notebook under the auspices of Anaconda, epitomizes a concerted effort to transcend the 90% threshold in classification accuracy. Notably, a bespoke neural network architecture is meticulously crafted and meticulously trained on an array of salient features encompassing Creatine ratio, Hemoglobin A1C, Cholesterol, Triglycerides, HDL Cholesterol, and the patient's diabetes disease class.

## Data Attributes

- **Cr**: Creatine ratio
- **hbA1c**: Hemoglobin A1C (normal range below 5.7%, with +6.5% indicating diabetes)
- **chol**: Cholesterol
- **TG**: Triglycerides
- **HDL**: HDL Cholesterol
- **CLASS**: Patient's diabetes disease class, being Non-Diabetic(N), Diabetic(Y), Predict-diabetic(P)

## Deep Neural Network Architecture

### Generalized Regression Neural Network (GRNN)
- 2 hidden layers
- 1 input and output layer 
- 12 features
- Regression:
  - Has one output unit without any activation function.
  - Loss functions used.

## Methodology

This endeavor mandates the following prerequisites:

- **Python 3.xx**
- **Jupyter Notebook**
- **Anaconda (Keras, NumPy, Pandas, Matplotlib, Scikit-Learn)**

## Result

The developed GRNN model has yielded prodigious outcomes, boasting an unprecedented average F1 score exceeding 90% (0.98). This monumental achievement underscores the efficacy of the GRNN paradigm in discerning latent diabetic predilections with unparalleled precision.

---

*Data from: Ahlam Rashid*  
*Published: 18 July 2020*  
*DOI: 10.17632/wj9rwkp9c2.1*  
*Research journal title: Iraq Patient Dataset of Diabetes(IPDD)*
