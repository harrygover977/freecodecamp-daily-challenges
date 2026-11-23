def longest_word(sentence: str) -> str:
    """Return the longest word found in sentence."""
    word_list = sentence.split()
    max_word = ""
    for word in word_list:
        letter_count = 0
        letters = ""
        for char in word:
            if char.isalpha():
                letter_count += 1
                letters += char
        if letter_count > len(max_word):
            max_word = letters
    return max_word

assert longest_word("The quick red fox") == "quick"
assert longest_word("Hello coding challenge") == "challenge"
assert longest_word("Do Try This At Home") == "This"
assert longest_word("This sentence... has commas, ellipses, and an exclamation point!") == "exclamation"
assert longest_word("A tie? No way!") == "tie"
assert longest_word("Wouldn't you like to know") == "Wouldnt"

