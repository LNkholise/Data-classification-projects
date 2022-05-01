Data from: Ahlam Rashid
</br>published: 18 July 2020
</br>DOI: 10.17632/wj9rwkp9c2.1
</br>Reseach journal title: Iraq Patiant Dataset of Diabetes(IPDD)</p1>

<h1>Description:</h1>
Data collected from Iraqi society specifically the lab of Medical City Hospital. This data was used to create a 
simple neural network that helps in predicting diabetes in patients. This was done in Jupyter notebook through anaconda.
A custom neural network was written with the aim of improving the classification accuracy beyond 90% using conventional
machine Learning classification techniques.


<h1>Data attributes:</h1>

Cr------->Creatine ratio
</br>hbA1c----> Hemoglobin A1C (normal range below 5.7%, with +6.5% indicating diabetes)
</br>chol----->Cholesterol
</br>TG------->Triglycerides
</br>HDL------>HDL Cholesterol
</br>CLASS---->Patient's diabetes disease class, being Non-Diabetic(N), Diabetic(Y), Predict-diabetic(P)

<h1>Deep neural network used:</h1>

GRNN(Generalized Regression Neural Network):
</br>2 hidden layers
</br>1 input and output layer 
</br>12 features
</br>
</br>regression: 
</br> -> has one output unit without any activation function.
</br> -> loss functions used.

<h1>Prerequisites:</h1>

</br>Python 3.xx
</br>Jupter Notebook
</br>Anaconda (Keras, Numpy, Pandas, Matplotlib, Scikit Learn)

<h1>Result</h1> 

The neural network yielded an average F1 score significantly above 90% (0.98), proving the experiment successful.
