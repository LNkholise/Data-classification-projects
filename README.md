![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

# Water Strider Classification and Behavioral Pattern Analysis

![Data Source](https://img.shields.io/badge/Data%20Source-Royal%20Society%20Publishing-blue)
![DOI](https://img.shields.io/badge/DOI-10.1098/rspb.2018.2400-yellow)
![PubMed](https://img.shields.io/badge/PubMed-30991924-green)
![Online ISSN](https://img.shields.io/badge/Online%20ISSN-1471--2954-orange)

## Abstract

This project investigates the mating behaviors and species distinctions within water strider populations using machine learning. Initially unfamiliar with water striders, I let the data guide the analysis, hoping it would illuminate aspects of speciation and mating behavior.

The analysis began with K-Means clustering to identify natural groupings within the collected water strider samples, revealing how size and leg length contribute to species-level differentiation. This unsupervised approach allowed an initial, unbiased view of species separation based solely on physical traits. However, to enhance precision, we transitioned from K-Means to K-Nearest Neighbors (KNN), which could use labeled data to classify known species with greater accuracy.

These clusters were further analyzed using logistic regression and Support Vector Machines (SVM) to classify individual insects by gender, providing insights into gender-specific mating preferences. This highlighted how subtle physical traits influence reproductive success and mating dynamics across different subspecies.

Overall, this project demonstrated how machine learning can uncover significant biological patterns, offering deeper insight into how species distinctions and mating strategies develop in water striders.

## Technologies Used

The projects in this repository primarily utilize the following technologies:

- Python 3.x
- Jupyter Notebook
- Various Python libraries for data manipulation, analysis, and machine learning (e.g., scikit-learn, pandas, numpy, matplotlib, seaborn)

## How to Use

To explore any of the projects in this repository, follow these steps:

1. Clone the repository to your local machine using `git clone`.
2. Navigate to the project directory.
3. Install the necessary dependencies using `pip install -r requirements.txt`.
4. Open the project notebooks using Jupyter Notebook or any compatible IDE.
5. Follow the instructions provided within each project notebook to run and experiment with the code.

## Methodology

### K-Means Clustering
- Identifies and partitions collected insect samples into distinct species clusters.

### Logistic Regression
- Classifies insects within each species cluster as male or female.
- Analyzes mating preference variations among different species.

## Data Attributes

- **Leg Length**: Average length of insect legs.
- **Body Size**: Average size of insect bodies.

## Result

- The successful classification of male and female water striders based on leg and body length using both **Logistic Regression** and **SVM** suggests a strong physical distinction clearly linked to mating behavior. For this project, it means these models can reliably separate genders based on these traits, enabling us to explore how these physical differences influence mating patterns and behaviors in water striders. Logistic Regression provides clear interpretability, while SVM offers adaptability, giving us robust tools to deepen our understanding of gender-based physical and behavioral dynamics in water strider species.
  
- Switching from KMeans to KNN was a key improvement for this project. While KMeans grouped data based on similarity, it couldn’t use species labels, making it less precise for known classifications. KNN, on the other hand, uses labeled data, allowing us to accurately classify water strider species by physical traits. This migration not only improved accuracy but also adds practical value by enabling researchers to quickly identify species in the field and build on existing research with a more adaptable model for future enhancements.



---
Prior research and dataset thanks to :

*Data from: Royal Society Publishing*  
*DOI: 10.1098/rspb.2018.2400*  
*PubMed: 30991924*  
*Online ISSN: 1471-2954*

