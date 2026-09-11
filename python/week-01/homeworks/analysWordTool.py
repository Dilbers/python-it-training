__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"
#Practice string methods, loops, conditions, lists, and sets.
#Ask the user for a sentence.
#Analyze:
#-Character count (excluding spaces)
#-Word count
#-Unique words (set)
#-Longest word
unique_words = set()
longest_word = None
len_longest_word = 0

sentance = input('Enter a sentence: ').strip()

character_count = len(sentance.replace(' ',''))

list_of_words = sentance.split(' ')

word_count = len(list_of_words)

for i in list_of_words:
    unique_words.add(i.lower())

    length_word = len(i)
    if(len_longest_word < length_word):
        len_longest_word = length_word
        longest_word = i

    
print('\nUnique words:') 

for i in unique_words:
    print(f'--{i}') 

print(f"\nCharacter count:{character_count} \nWord count:{word_count} \nLongest word:{longest_word}")