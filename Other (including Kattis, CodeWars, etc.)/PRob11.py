cases = int(input())
total = ""
new_word = ""
new_phrase = ""
for case in range(cases):
    read = input()
    phrase = read.split(" ")
    for word in phrase:
        for letter in word:
            new_word = letter + new_word
        new_phrase = new_phrase + new_word + " "
        new_word = ""
    total = total + new_phrase + "\n"
    new_phrase = ""
print(total)