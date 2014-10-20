#!/usr/bin/env python3


def count_words(arr):
    counted_words = {}
    unique = set(arr)
    for word in unique:
        counted_words[word] = arr.count(word)
    return counted_words
