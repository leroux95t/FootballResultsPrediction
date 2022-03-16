# Projet DataCamp: Peut-on faire trembler les BookMakers?

<p align="center">
	<img width="200px" height="150px" src="https://upload.wikimedia.org/wikipedia/commons/6/6e/Football_%28soccer_ball%29.svg" />
</p>

## Introduction

A l’ère où la majorité des domaines vivent leur transformation digitale, le monde du sport n’est pas épargné [1] : avec la véritable hausse des droits TV, et l’appui de puissances économiques mondiales, certains sports sont devenus de véritables business. Cette transformation passe par l’acquisition des toutes nouvelles technologies : équipements et infrastructures, santé, marketing, vélos ultra-modernes, moteurs de formule 1 optimisés en temps réel, … et les paris en ligne. Dans tous les cas, l’objectif est le même : améliorer les performances.



## Business Model

Comme tous les autres domaines, celui des paris sportifs s’est pleinement développé ces dernières années, et est considéré comme étant aujourd’hui une véritable industrie. Avec le développement d’internet et des téléphones portables, parier en ligne n’a jamais été aussi facile, et ceci pour tous les sports. Les acteurs principaux comme Betclic, Winamax, Unibet, ZeBet, NetBet l’ont compris très tôt, et ont tout fait pour faciliter un maximum le paris, dans. Pour générer des centaines de millions d’euros, ces entreprises exploitent chaque jour des volumes colossaux de données. L’objectif principal est de calculer des “cotes”. D’après le site Compare BET, une cote est  “un nombre qui définit à la fois votre gain potentiel et vos chances de l'emporter. Elle est calculée par l'opérateur de pari en ligne en fonction de multiples critères et l'opération. Le gain potentiel est le produit de votre mise par la cote”

Par les termes “chances de l’emporter”, on sous-entend le terme “probabilités”. Mais alors, cela veut-il dire que chaque site de paris sportifs calcule pour nous les probabilités de chaque événement sportif? Mais que disent-ils par “probabilités”? Est-ce une vraie probabilité? Quel est le modèle? Pourquoi n’a t-on aucune visibilité la-dessus? Et surtout, pourquoi une cote pour un même match est différente pour chaque site de paris? Comme le dit la définition, la cote est calculée en fonction de multiples critères : le classement actuel de l’équipe, le nombre de buts marqués au cours des derniers matches, les joueurs blessés. Ces informations sont fixées, ce sont des faits. Alors, pourquoi chaque cote, censée correspondre à une probabilité, diffère selon les sites? Ce dernier point nous indique qu’il n’y a pas de probabilité absolue, donnée par un modèle absolu : si la cote de Winamax “PSG gagnant face à Monaco” est de 1.2, cela ne veut pas nécessairement dire que la probabilité que Paris gagne contre Monaco soit de 1/1.2=0.83. Et pourquoi? Tout simplement parce que, comme on l’a dit, le but est d’améliorer les performances, et en l'occurrence ici, c’est faire de l’argent. Chaque site fait donc jouer un paramètre supplémentaire dans ses modèles : l’argent. 

Face à ces probabilités biaisées que sont les cotes, qui influent directement sur notre choix, est-il possible d’établir une stratégie qui nous permette d’être plus gagnant face à ces sites de paris? Comment les déjouer? Est-il possible d’estimer les trois probabilités des événements “Equipe A gagne”, “Match nul”, “Equipe B gagne”, avec seulement les paramètres officiels dont tout le monde dispose (Nombre de buts marqués, classement…)? Peut-on le faire “à la main”? Tout parieur le sait: parier sur un match, c’est long et fastidieux. En effet, un parieur avisé prend en compte une multitude de paramètres, comme l’historique des résultats entre les deux équipes, la forme de celles-ci, le lieu de la rencontre (domicile ou extérieur)... Faire une stratégie à la main s’annonce donc très compliqué. C’est pour cela que nous allons utiliser le Machine Learning. Ainsi les objectifs de notre étude seront les suivants:

Pour chaque match, prédire les trois probabilités des événements “Equipe A gagne”, “Match nul”, “Equipe B gagne”.
Déterminer les variables jouant un rôle important dans cette prédiction.
Comparer nos résultats avec les cotes d’un site de paris sportif pour voir si notre stratégie pourrait faire gagner de l’argent à notre parieur.


## Data sources

-Football : → 3 issues pour un match→ 3 probas

-Comment on construit le data set final : les paramtres n’ont à priori pas un eimportance différente quand on change de pays, et quand on change de saisons
→ On met tout dans la même base

-En général on peut parier jusqu’à 5 minutes avant le début du match. Depuis peu, on peut même parier pendant le match. Mais dans le cadre de notre étude, nous nous focaliserons sur le pari avant le début du match. Nous devons donc exploiter les données récoltées dans le passé. Or, la base de données dont on dispose n’est pas construite en ce sens : c’est une base de données qui associe à chaque match les statistiques de ce match. 

Comme le Football est un sport international, les données de matches sont générées de manière exponentielle. Il a donc fallu faire des choix par rapport à des contraintes techniques. Nous avons donc fait le choix de nous focaliser sur les aspects suivants : 

Matches à partir de la saison 2001/2002
Matches jusqu’à la saison 2019/2020
Pays : Angleterre
Ligue : Premier League

-description des variables du dataset à disposition

Div = League Division
Date = Match Date (dd/mm/yy)
Time = Time of match kick off
HomeTeam = Home Team
AwayTeam = Away Team
FTHG and HG = Full Time Home Team Goals
FTAG and AG = Full Time Away Team Goals
FTR and Res = Full Time Result (H=Home Win, D=Draw, A=Away Win)
HTHG = Half Time Home Team Goals
HTAG = Half Time Away Team Goals
HTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)

Match Statistics (where available)
Attendance = Crowd Attendance
Referee = Match Referee
HS = Home Team Shots
AS = Away Team Shots
HST = Home Team Shots on Target
AST = Away Team Shots on Target
HHW = Home Team Hit Woodwork
AHW = Away Team Hit Woodwork
HC = Home Team Corners
AC = Away Team Corners
HF = Home Team Fouls Committed
AF = Away Team Fouls Committed
HFKC = Home Team Free Kicks Conceded
AFKC = Away Team Free Kicks Conceded
HO = Home Team Offsides
AO = Away Team Offsides
HY = Home Team Yellow Cards
AY = Away Team Yellow Cards
HR = Home Team Red Cards
AR = Away Team Red Cards
HBP = Home Team Bookings Points (10 = yellow, 25 = red)
ABP = Away Team Bookings Points (10 = yellow, 25 = red)



## Métrique

Nous allons utiliser l'accuracy comme métrique de notre modèle. C'est une mesure assez simple qui permet d'avoir des résultats acceptable pour notre tâche de classification.

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

 
