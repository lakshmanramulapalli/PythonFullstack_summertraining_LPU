text = input("Enter a string: ")
vowels = 0
consonants =0

text = text.lower()
for char in text:
    if char.isalpha():
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print(f'Number of vowels: {vowels}')
print(f'Number of consonants: {consonants}')