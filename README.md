# Nutriscore Grade Prediction

<p align="center">
	<img width="200px" height="150px" src="https://github.com/k3nz0/nutriscore-prediction/raw/06c4cc51a7a024e36adc4ac3a8886260aced771f/resources/nutriscore.jpg" />
</p>

## Introduction

In 2016, "Santé Publique France" unveiled the nutriscore, a 5-Color label that conveys information on the nutrional quality of food products. Every product is rated with a letter from "A" (the best grade) to "E" (the worst grade). As of today, this system has been used by the majority of companies and retailers, despite the fact that it is not mandatory.

In January 2020, members of the European parliament suggested to extend the use of the Nutriscore. Moreover, a petition on the website "European Citizens Initiative" (eci.ec.europa.eu) was launched in 2019 in order to impose the Nutriscore on food products.


## Business Model

The Nutriscore uses a determinist formula using the nutritional value of the products, but since it is not yet mandatory to display it on a product, would it be possible to estimate the Nutriscore even if we missed some information? This is the goal of this competition: using incomplete information and non-numerical clues in order to assess as accurately as possible the Nutriscore of an item.

## Data sources

The data comes exclusively from the Open Food Facts database, accessible on http://openfoodfacts.org/. The database is available under the Open Database License and is managed by the non-profit organization Open Food Facts. Most of the data is provided by invidual contributors that wish to help the project.

We have gathered data from their database and only selected the features we were interested in for this challenge. In addition, some product data are dirty and have incomplete information.

## Metric
There are only five possible outputs (A, B, C, D and E) and the classes are moderately unbalanced. The metric used should penalize depending on the distance between the predicted letter and the true letter. In other words, it should penalize more heavily the prediction of a "E" instead of an "A" than the prediction of a "B" instead of an "A". Moreover, since believing junk food to be health is a greater problem than the opposite, the loss function should reflect that by strongly penalizing overestimates. So, we will convert the letter into an integer between 0 and 4 (E being 0 and A being 4) and then use the following loss function:


<p align="center">
	<img src="https://render.githubusercontent.com/render/math?math=L%28%5Chat%7B%5Ctheta%7D%2C%20%5Ctheta%29%20%3D%20%5Cmathbb%7BE%7D%5Cleft%5B%282f%5E%2B%28%5Chat%7B%5Ctheta%7D-%5Ctheta%20%29%29%5E2%20%2B%20%282f%5E%2B%28%5Ctheta-%5Chat%7B%5Ctheta%7D%29%29%5E%7B3%2F2%7D%5Cright%5D&mode=display" />
</p>

## Submission

Before submitting make sure to test your model and check that everything works fine. 
In order to do that you can run : 

`ramp_test_submission --submission starting_kit` 

or for a quick test : 

`ramp_test_submission --submission starting_kit --quick-test`


Notice that this unit test run in the folder submissions/starting_kit.

Before running the test, make sure you have :
* Installed ramp-workflow.
* Installed the requirements ( `pip install -r requirements.txt` ).
* Put your python file under the `submissions/starting_kit` folder.
* Downloaded the data by running `python download_data.py` 

 
