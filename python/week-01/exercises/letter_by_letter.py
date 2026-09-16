#2-Give that letter by letter from given text and new line every letter
sentance = input('give me sentance: ')

for i in sentance:
    print(i)

index = 0
while index < len(sentance):
    print(sentance[index])
    index +=1