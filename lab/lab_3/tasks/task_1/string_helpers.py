def shout(text):
    return text.upper() + "!!!"


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for c in text:
        if c in vowels:
            count += 1

    return count


if __name__ == "__main__":
    print(shout("original file"))
    print(count_vowels("original file"))