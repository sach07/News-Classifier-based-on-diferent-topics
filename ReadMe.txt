Follow the below steps to proceed:

1.Open Overview.txt document to get understanding of high level implementation.
2.Please go through (News Classification using NLP) ppt to get an overview of what algorithms are implemented.
3.Once you have gone through the ppt ,open the jupyter notebook and have a walkthrough the code.
Note:
1.Lemmatizaion of text is not done as it is taking too long causing PC to dead.
3.The model is implemented using LinearSVC as base model.
2.Grid search can be implemented for further evaluation but is causing PC to dead.
3.Similary Bagging and Voting Classifier can be implemented for further evaluation.
4.However the base model is able to produce the necessary score
5.Similarly Ensembling (bagging and boosting )can tried which can further improve the score,code is share in jupyter notebook.

Deployment check:
1.Using Flask api:
	1.Open cmd and run app.py file,then open http://127.0.0.1:5000 and do the testing.
2.Using Heroku Cloud:
	1.Open any web browser and connect to https://newsclassifiermodel.herokuapp.com/ and do the testing.

Note:
The Look and Feel of the HTML page can be further changed or played around.

Doubts:
For Doubts mail-sachinsg873@gmail.com
