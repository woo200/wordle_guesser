# Wordle Guesser

Usage: `python3 guesser.py`

### How to use it

Once you run the program, it will ask you to guess the first word, enter that into the game, then type the response that wordle gives you. `-` for black, `*` for yellow, `+` for green.<br />

Once you enter this, it will give you a list of possible words, then you will select a word, at random or however you want, then you will enter the word into wordle AND into the program, and then after you enter it into the program, enter the response wordle gives you. Repeat until you win.

## EXAMPLE
```
$ python3 guesser.py
Initial Guess: CRANE
Use - for black, + for green and * for yellow
Enter Response: +----
Available Words:
COULD, CHILD, CLOTH, CLOUD, CLOCK, CLIMB, COSTS, CIVIL, CUBIC, CLIFF, CLUBS, COOLS, CHILL, COMIC, COUCH, CHIPS, COOKS, CLUMP, COUGH, CLICK, COLTS, COILS, CUFFS, CLIPS, CIVIC, CHUCK, CHOPS, CHICK, COLDS, CHILI, COOKY, COMBS, COCKS, CLUCK, CLOGS, CLODS, CHIMP, CLOUT, CHUGS, CLOTS, COCKY, COYLY, CHUMS, COCCI, CYSTS, COOPS, COCOS, CULLS, COLIC, COWLS, CUPID, CHOWS, CUBIT, COMBO, CULTS, COHOS, CLOMP, COUPS, CUSPS, COYPU, COMFY, COOTS, CUBBY, CHUMP, CHOMP, CHOCK, CUSHY, CUTUP, CLOPS, COMPS, CHIFF, CUSPY, CHITS, CLOYS, COIFS, CILLS, CHOOS, COQUI, COOCH, CUPPY, CHUFF, COUTH, CIVVY,
Guess: cloud
NEXT GUESS: cloud
Use - for black, + for green and * for yellow
Enter Response: +-*--
Available Words:
COSTS, COMIC, COMBS, COCKS, COCKY, COCCI, COCOS, COMBO, COHOS, COMFY, COMPS, COIFS,
etc...
```
