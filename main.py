#!/usr/bin/env python3

import random, time


def get_words():
    with open('./words', 'r') as f:
        words = f.readlines()
        words = list(w.lower().strip() for w in words)
        random.shuffle(words)
        return words
    raise ValueError


def get_word():
    return random.choice(get_words()).lower().strip()


def get_guess(guessed: list, candidates: list, result: list, absent: list):
    if len(guessed) <= 0:
        if len(candidates) > 0:
            return random.choice(candidates)
        raise ValueError

    guess = guessed[-1]
    if len(result[0]) > 0 or len(result[1]) > 0:
        for candidate in candidates:
            if candidate in guessed:
                continue
            found = True
            for c in candidate:
                if c in absent:
                    found = False
                    break
            if found:
                for i in result[0]:
                    if candidate[i] != guess[i]:
                        found = False
                        break
            if found:
                for i in result[1]:
                    if guess[i] not in candidate:
                        found = False
                        break
            if found:
                return candidate
    while True:
        found = True
        candidate = random.choice(candidates)
        for c in candidate:
            if c in absent:
                found = False
                break
        if found:
            return candidate


def run():
    attempts = []
    try:
        while True:
            word = get_word()
            print(f'\nthe word is {word}')
            candidates = get_words()
            guessed = []
            result = (
                [],
                []
            )
            absent = []
            while True:
                guess = get_guess(guessed, candidates, result, absent)
                guessed.append(guess)
                if guess.lower().strip() == word.lower().strip():
                    print('Found the word after '+str(len(guessed))+' guesses:')
                    print(', '.join(guessed))
                    attempts.append(len(guessed))
                    break
                else:
                    result = (
                        [],
                        []
                    )
                    for i in range(len(guess)):
                        if i < len(guess) and i < len(word):
                            if guess[i] == word[i]:
                                result[0].append(i)
                            elif guess[i] in word:
                                result[1].append(i)
                            else:
                                absent.append(guess[i])
    except KeyboardInterrupt:
        print('average number of guesses per word (sample size: '+str(len(attempts))+' words): '+str(sum(attempts)/len(attempts)))


if __name__ == '__main__':
    run()

