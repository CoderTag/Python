word_to_guess = "mangoman"

hangs = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

# unique letters is the total number of trial
wrong_guess = 7
trial = len(set(word_to_guess)) + wrong_guess

# initialize array with dashes equal to number of letters in the word to guess
show_guess = ['_'] * len(word_to_guess)

count = 0
while trial:
    match = 'no'
    choice = input('Enter a letter:').lower()
    for i, l in enumerate(word_to_guess):
        if l == choice:
            show_guess[i] = choice
            match = 'yes'

    print(' '.join(show_guess))

    if "_" not in show_guess:
        print("win")
        break

    if match == 'no':
        print(hangs[count])
        count += 1
        wrong_guess -= 1
        if wrong_guess == 0:
            print('lost')
            break

    trial -= 1


