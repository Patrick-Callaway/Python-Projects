def translate(phrase):
    translation = " "
    for letter in phrase:
        if letter.lower() in "AEIOU":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase:\n")))