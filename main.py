def main (): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print(count_words(file_contents))
        letter_count = count_letters(file_contents)
        for letter_count_item in letter_count:
            letter, count = letter_count_item
            print(f"The '{letter}' character was found {count} times")

def count_words(content):
    count = 0
    words = content.split()
    for word in words:
        count += 1
    return count

def count_letters(content):
    lower_content = content.lower()
    letters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for letter in lower_content:
        if letter in letters:
            letters[letter] += 1
    return sorted(letters.items(), key=lambda item: item[1], reverse=True)

main()
