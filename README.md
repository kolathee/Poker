Poker best hand calculator
=======
version 1.0 - 10/7/2013

------

This python script will help you to find out which is the best hand(s) from a list of hands.
## System requirements ##
Any OS with Python 2.7 installed.  


## Installation ##
Just place `poker.py` to any preferred location.


## How to use ##
### Running the program ###
there are several ways to run Python script such as _command line_, _Python IDLE_, etc.

### Cards representation ###
This program recognise what card it is by using 2 characters for each card.  

- **Ranks:**  `1 = 1`, `2 = 2`, `3 = 3`, ..., `9 = 9`, **`10 = T`**, `J = J`, `Q = Q`, `K = K`, `A = A`  
- **Suits.**  `Clubs = C`, `Diamonds = D`, `Hearts = H`, `Spades = S`  
> **Note:**  All alphabets **must** be written in upper case.

Examples.  

- `2C` = two of clubs.
- `TS` = ten of spades.

### Usage ###
Simply input `a list of a list of each hand` then press `Enter` button, it will shows you a list of the best hand(s). 

> **Help:** `list` is one of Python's data type which can be written as a list of comma-separated values between square brackets.  
> **Note:** each card must be enclosed by single quote(`'`) or double quote(`"`).

Here's some examples of correct input.  

- **Multiple hands.**  
	`[['7D', '2S', 'QS', '8S', '8H'],['QS', '8C', 'JC', '5C', 'JD'],['KD', '2D', 'JD', '8C', '7S']]`  
- **One hand also works!**  
	`[['7D', '2S', 'QS', '8S', '8H']]`


## Contributors ##
**Advisor:** Assoc. Prof. Dr. Chotipat Pornavalai  
**Coding:**  
1. Kolathee Payuhawutthana  
2. Noppawit Chartkajekaew  
3. Nattakit Intarasorn


## Contact ##
If you have experienced a bug or have something to tell us, please don't hesitate to contact us at [s6070002@kmitl.ac.th](mailto:s6070002@kmitl.ac.th)