# rl-stats-eda
Exploring significant relationships between the ball, boost, and best in the game of Rocket League.
#
#
## Why am I interested?
Wow! Quite simply, I love the game.  Rocket League's major appeal to me is its core pillar of being easy to pick up while maintaining itself as a bonified eSport with an incredible skill ceiling.  Three years after playing my very first match, I am now nearing my 1000th hour.  Rocket League is my sport.  _This is Rocket League!_
<ul><iframe width="560" height="315" src="https://www.youtube.com/embed/KNG7r1n6Jk8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></ul>

Hastily writing the game off as merely "soccer but with cars having rocket engines on the back" does a disservice to the beautiful complexity that ermerges in higher brackets of play.  
#
## Where will I get the data?
The bulk of the data will come from a site named for the style of play where making contact with the ball becomes more import than controlled touches towards a teammate.  What can you do, ballchasing is life to some! [Ballchasing.com](https://ballchasing.com/) ([api](https://ballchasing.com/doc/api)) is home to over 14 million replay files, each one a treasure trove of both individual- and team-focused match statistics.




In addition to the replay files, I will have the option to scrape from the Rocket League section of Tracker Network for information on specfic players relating to [Matchmaking](https://www.theloadout.com/rocket-league/ranks), [Leaderboards](https://rocketleague.tracker.network/rocket-league/leaderboards/playlist/all/default?page=1&playlist=11), and [Player Lifetime Stats](https://rocketleague.tracker.network/rocket-league/profile/steam/76561198994386260/overview), as well as the
[Skill Rating Distribution](https://rocketleague.tracker.network/rocket-league/distribution?playlist=13).

#
## What will the data look like?
To understand what the data will look like, I should briefly explain how the game is played.  All professional games are played in the "Standard" format.  Standard matches assume the following format:
* 2 teams
* 3 players each team
* 5 minute countdown timer per match
* a point is scored when the ball completely crosses the goal line

The timer comes with a caveat:
play continues at the end of 5 minutes **_until the ball touches the ground or a point is scored._**
If the game is tied when play stops, the game will go into overtime.  Overtime has no time limit and will continue until the first point is scored, defining the winner.

As the players drive around the field, they drive over orange pads on the ground.  Doing so will incrementally increases the amount of boost, up to a maximum of 100, available for use at the player's discretion.  This mechanic of acquiring/saving/spending boost leads to a deep and satisfying moment-to-moment gameplay loop. Should the player use their precious resource to advance up the field to provide support?  Should they takeoff and let it out in short bursts to carefully place themselves in the right spot for a shot?  Of course, if they are in goal and their tanks are low, the ball may go right over the goalie's head into the net for an easy goal.

Careful boost management can send a skilled player to new heights (literally) with one of the most precise and skill intensive aspects of the game, aerial control. Some players stick to ground maneuvers until they have a few hundred hours of experience!
#
## Okay, so what will the data actually look like?
Depending on how many Pro level games I can find, I would like to sample 10,000 or so games, preferably from the highest level of play and ideally including as many matches as possible from the Rocket League Championship Series (the pro circuit).  In each file, I will be looking for the following features with a focus on those in bold:
### Core Information
1. Score
2. **Goals**
3. Shots
4. Assists
5. **Saves**
6. **Demos** *
      ###### * Driving into someone at max speed will "demolish" them, causing the struck vehicle to explode, thus removing them from the field for a few seconds and causing the demolished player to spawn back at their own goal.

### Boost Information
1. **Boost Collected per Minute**
2. **Boost Consumed per Minute**

### Other Potential Data
1. Speed
    * Average speed
    * % of time spent at Supersonic (max) Speed\
2. Positional
    * Distance from teammates
    * % of time spent in offensive third
    * % of time spent in defensive third

#

## Some ideas on statistical tests
Two main hypothesis include:

##### _H0 = The team that scores the first goal wins the game_

and/or

##### _H0 = The player that collects the most boost is the most impactful (has the most score in a winning game or most saves in a losing game)_


#
### If time permits I would like to...
1. set up a pipeline to handle the scraping and cleaning of many more samples/replays
2. upload my own replay data to compare my stats against the pros
3. compare the sample data to the population data found on ballchasing.com


## What will I learn?
* How to collect data by way of web scraping and API integration
