# Udacity_ML_nanodegree_projects
In this repository, I publish my end-of-chapter projects I completed whilst following the Udacity Introduction to Machine Learning Nanodegree Program.

I am new in the area of Machine Learning, so decided to follow the mentioned program with Udacity. 
The course covers the 3 main fields of Machine Learning: Supervised, Unsupervised and Deep Learning. 
At the end of each chapter I carried out a project.

For supervised learning project, I created a model that helps an imaginary charity to find potential donors. Using the 1994. U.S. Census data, my model predicts with good accuracy whether or not a person makes more than 50k dollars a year. After exploring and preprocessing the data, I priliminarely chose Decision Tree, SVM and Gaussian Naive Bayse models to test their performance and to choose the most proper one for the job. Finally, I chose SVM because it worked with higher accuracy, however, it was a bit slower. At the end of the project I carried out feature selection to reduce time and computational capacity, and investigated how feature selection affects beta score and accuracy. You can find my completed project in a Jupyter Notebook.

For deep learning project I worked on an image classifier trained on the Oxford Flowers 102 dataset using Tensorflow and Keras. After exloring the data I applied transfer learning and imported MobileNet v2 from TensorFlow Hub. Redesigning the neural network I trained and tested my model and checked its performance. I let my model to carry out inference and tested it how it performs when make predictions using a separate test dataset. My project can be seen not only in a Jupyter Notebook but I created a Python program that can be run from command line and does the same job that the one in the Jupyter Notebook. 

For unupervised learning project I worked on a customer segment identifier that can find segments of the population that can be a core customer of a mail-order company. Those segments could then be used to direct marketing campaigns towards audiences that will have the highest expected rate of returns. The data I used has been provided by Bertelsmann Arvato Analytics. In this project I was busy with data wrangling and preprocessing, so this project helped me levelling up not only my machine learnig skills but my data engineering skills, too. After managing cleaning the data I carried out an unsupervised classification using KMenas on the demographuc data provided. I did the same on a customer dataset (fetures in the dataset were the same, so the same data cleaning steps could be carried out) and I applied the same clustering model gained with the previous clustering. Then I compared the clusters on the 2 different datasets.



