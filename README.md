# Football results prediction in Premier League

<p align="center">
	<img width="200px" height="150px" src="https://upload.wikimedia.org/wikipedia/commons/6/6e/Football_%28soccer_ball%29.svg" />
</p>

## Introduction




## Business Model



## Data sources



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

 
