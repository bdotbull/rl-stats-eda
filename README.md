# Demolitions: Deployable or Deplorable?
Statistical analysis on 5,000 games of Rocket League to determine if demos are a broken mechanic or balanced tide-turner. 
#
#
## Why am I interested?
Wow! Quite simply, I love the game.  Rocket League's major appeal to me is its core pillar of being easy to pick up while maintaining itself as a bona fide eSport with an incredible skill ceiling.  Three years after playing my very first match, I am now nearing my 1000th hour.  Rocket League is my sport.  _This is Rocket League!_


[![](http://img.youtube.com/vi/KNG7r1n6Jk8/0.jpg)](http://www.youtube.com/watch?v=KNG7r1n6Jk8 "Best Goal In RL History")

Hastily writing the game off as merely "soccer but with cars having rocket engines on the back" does a disservice to the beautiful complexity that emerges in higher brackets of play.  
#
## What is a demo?
In Rocket League, when a vehicle passes a high speed threshold, the vehicle is flagged as travelling at "supersonic" speed.  When a vehicle traveling supersonic hits another vehicle, the slower vehicle is "demolished" or "demo'd".  The demolished vehicle is blown up in a blinding cloud of smoke and removed from the game for 3 seconds before spawning in their defensive third, free to resume play.

This mechanic is a point of contention due to it being an easily executed way to remove a player's ability to influence the game for a set time, though it is also argued as a high-risk, high-reward maneuver.
#
## Hypothesis
Scoring goals leads to wins. If there is a mechanic players can use to score more goals, it would at least be used at the highest levels. Professional players do not focus on demos more than any other mechanic. Therefore, the hypothesis is that demos will not directly contribute to scoring a goal. To test the hypothesis, the number of goals will be considered between two groups:
* The players with the top 25% of inflicted demolitions
* The players with the bottom 25% of inflicted demolitions

_H0: The mean number of goals scored by players with the top 25% of demos is more than the mean number of goals scored by players with the bottom 25% of demos._

_Ha: The mean number of goals scored by players with the bottom 25% of demos is more than the mean number of goals scored by players with the top 25% of demos._
#
## Workflow and Tech Stack
### Python 3 and MongoDB
##### Numpy, Pandas, Matplotlib, Seaborn, SciPy, PyMongo 
#
## Data
[Ballchasing.com](https://ballchasing.com/) ([api](https://ballchasing.com/doc/api)) is home to over 14 million replay files, each one a treasure trove of both individualized and team-focused match statistics. Using the API, a scraper was built to retrieve replay files according to a filter. To be used in the test, replays must match the following criteria:
* replay files must have complete information (no missing data such as player name or match id)
* games must be from the Standard Ranked playlist (3v3, Soccar, Online w/Matchmaking)
* games must have at least 1 professional player

When cleaned, the number of applicable records is over 5,800.
#
## Stats Test
A Welch's t-test was employed due to the high variance in the group with the top 25% of demos compared to the group with the bottom 25% of demos.
#
## Results

#
## Future Steps
###