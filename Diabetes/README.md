Data from: Ahlam Rashid 
published: 18 July 2020
DOI: 10.17632/wj9rwkp9c2.1
Reseach journal title: Iraq Patiant Dataset of Diabetes(IPDD) 

<h>Description:</h>
Data collected from Iraqi society specifically the lab of Medical City Hospital. This data was used to create a 
simple neural network that helps in predicting diabetes in patients. This was done in Jupyter notebook through anaconda.
A custom neural network was written with the aim of improving the classification accuracy beyond 90% using conventional
machine Learning classification techniques.


<h>Data attributes:</h>

Cr------->Creatine ratio
hbA1c----> Hemoglobin A1C (normal range below 5.7%, with +6.5% indicating diabetes)
chol----->Cholesterol
TG------->Triglycerides
HDL------>HDL Cholesterol
CLASS---->Patient's diabetes disease class, being Non-Diabetic(N), Diabetic(Y), Predict-diabetic(P)

<h>Deep neural network used:</h>

GRNN(Generalized Regression Neural Network):
2 hidden layers
1 input and output layer 
12 features
regression -> has one output unit without any activation function.
           -> loss functions used.

<h>Prerequisites:</h>

Python 3.xx
Jupter Notebook
Anaconda (Keras, Numpy, Pandas, Matplotlib, Scikit Learn)

<h>Result</h> 

The neural network yielded an average F1 score significantly above 90% (0.98), proving the experiment successful.