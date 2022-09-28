#!/usr/bin/env python3

import random, time


def get_words():
    with open('./words', 'r') as f:
        words = f.readlines()
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
            for i in result[0]:
                if candidate[i] != guess[i]:
                    found = False
                    break
            for i in result[1]:
                if guess[i] not in candidate:
                    found = False
                    break
            for c in candidate:
                if c in absent:
                    found = False
                    break
            if found:
                return candidate
    return random.choice(candidates)


def run():
    while True:
        word = get_word()
        print(f'the word is {word}')
        candidates = get_words()
        guessed = []
        result = (
            [],
            []
        )
        absent = []
        while True:
            time.sleep(0.5)
            guess = get_guess(guessed, candidates, result, absent)
            guessed.append(guess)
            print(f'guessing {guess}')
            if guess.lower().strip() == word.lower().strip():
                print('Correct!')
                break
            elif len(guessed) == len(candidates):
                print('Unable to guess word...')
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
                output = ''
                for i in range(len(guess)-1):
                    if i in result[0]:
                        output = output + guess[i]
                    elif i in result[1]:
                        output = output + f'({guess[i]})'
                    else:
                        output = output + '_'
                print(output)


if __name__ == '__main__':
    run()

