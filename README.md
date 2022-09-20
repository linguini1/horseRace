# Horse Race
### Matteo Golin
Runs several sample games to determine which horse has the highest probability of winning, and displays the information in a graph using Matplotlib.

## Requirements
- Python 3.10+
- Matplotlib

## Research

### Background

The game starts when players roll the dice once each in order to determine which horses will be stuck at the line. These horses automatically lose. Hence, horse 7 is
most likely to lose since it is most likely to be rolled on the first cast of the dice.

Then the players take turn rolling the dice. Horses whose numbers are rolled advance one spot. Since 2 and 12 are the two numbers that are least likely to be rolled, they
have the least amount of spaces to advance, and 7 the most as it is the most common outcome.

### Numbers
The probability of the number 12 (or 2) being rolled is 1/36. The probability of the number 7 being rolled is 1/6.

However, the probability of rolling 12 twice is (1/36)^2. The probability of rolling 7 seven times is (1/6)^7.

Not only is the number 7 more likely to instantly lose during the preliminary round, it is also less likely to be rolled seven times (the number of spaces it must 
advance) during the game than 2 is to be rolled twice.

Therefore, the expected outcome is of course, that the numbers with the least probability of being rolled are actually the most likely to win the game.
