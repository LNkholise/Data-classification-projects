# Water Strider Classification and Behavioral Pattern Analysis

![Data Source](https://img.shields.io/badge/Data%20Source-Royal%20Society%20Publishing-blue)
![DOI](https://img.shields.io/badge/DOI-10.1098/rspb.2018.2400-yellow)
![PubMed](https://img.shields.io/badge/PubMed-30991924-green)
![Online ISSN](https://img.shields.io/badge/Online%20ISSN-1471--2954-orange)

## Abstract

In the realm of agriculture and farming, effective pest and parasite management is paramount. Identifying and understanding the behavior of problem pests is crucial for implementing targeted control measures. This project delves into the identification, prediction, and classification of subspecies of collected insects, with a specific focus on water striders, using the k-means clustering method.

By leveraging the k-means clustering algorithm, the project partitions collected insect samples into distinct species clusters. Further analysis, utilizing logistic regression, is then conducted on the predicted species clusters to classify insects within each species as either male or female. This analysis provides insights into mating preference variations among different species of water striders or similar insects, whether they are pests, parasites, or otherwise.

The project achieves these objectives by utilizing insect dimensions, such as average leg length and body size, as key features for classification and analysis.

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



---

*Data from: Royal Society Publishing*  
*DOI: 10.1098/rspb.2018.2400*  
*PubMed: 30991924*  
*Online ISSN: 1471-2954*

