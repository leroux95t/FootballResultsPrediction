# Projet DataCamp: Peut-on faire trembler les BookMakers?
Authors : Thomas Le Roux, Timothée Fassier, Vincent Mongkhoun, Ahmath Gadji 
<p align="center">
	<img width="200px" height="150px" src="https://upload.wikimedia.org/wikipedia/commons/6/6e/Football_%28soccer_ball%29.svg" />
	<img width="500" height="150" src="https://upload.wikimedia.org/wikipedia/commons/5/55/Parions_Sport_Logo_%282019%29.png" />
	<img width="200px" height="150px" src="https://upload.wikimedia.org/wikipedia/commons/f/fe/Logo_Betclic_2019.svg" />
	
</p>

## Context

In an era where most fields are undergoing their digital transformation, the world of sports is not spared : with the real increase of TV rights, and the support of global economic powers, some sports have become real businesses. This transformation involves the acquisition of brand new technologies: equipment and infrastructure, health, marketing, ultra-modern bikes, Formula 1 engines optimized in real time, ... and online betting. In all cases, the objective is the same: **to improve performance.**

Like all other areas, the sports betting industry has grown in recent years and is now considered a real industry. With the development of the internet and cell phones, online betting has never been easier, and this for all sports. Major players like Betclic, Winamax, Unibet, ZeBet, NetBet understood this early on, and have done everything to make betting as easy as possible. To generate hundreds of millions of euros, these companies exploit huge volumes of data every day. The main objective is to calculate "odds". According to the Compare BET website, an odds is "a number that defines both your potential gain and your chances of winning. It is calculated by the online betting operator based on multiple criteria and the transaction. The potential payout is the product of your stake and the odds".

By the terms "chances of winning" we mean "probabilities". But then, does it mean that every sports betting site calculates the probabilities of each sporting event for us? But what do they mean by "probabilities"? Is it a real probability? What is the model? Why do we have no visibility on this? And most importantly, why are the odds for the same game different for each betting site? As the definition says, the odds are calculated according to multiple criteria: the current ranking of the team, the number of goals scored in the last matches, the injured players. This information is fixed, these are facts. So why do the odds, which are supposed to be a probability, differ from site to site? This last point tells us that there is no absolute probability, given by an absolute model: if the odds of Winamax "PSG winning against Monaco" is 1.2, it does not necessarily mean that the probability of Paris winning against Monaco is 1/1.2=0.83. And why is that? Simply because, as we said, the goal is to improve the performance, and in this case, it is to make money. So each site puts an additional parameter into its models: money.

Faced with these biased probabilities that are the odds, which directly influence our choice, is it possible to establish a strategy that allows us to be more winning against these betting sites? How can we outsmart them? Is it possible to estimate the three probabilities of the events "Team A wins", "Draw", "Team B wins", with only the official parameters that everyone has (number of goals scored, ranking...)? Can we do it "by hand"? Every bettor knows: betting on a match is long and tedious. Indeed, a wise bettor takes into account a multitude of parameters, such as the history of results between the two teams, the form of these, the place of the match (home or away)... Making a strategy by hand is therefore very complicated. This is why we will use Machine Learning.



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
* Put your python file in the `submissions` folder.

 
