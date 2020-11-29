from collections import Counter

# === Installing Python ===
import this


# === Variables and Some Arithmetic ===
a = 3
b = 5
# result = a**2 + b**2
print(f'{a}^2 + {b}^2 = {a**2 + b**2}')


# === Strings and Lists ===
wordOneStartPos = 22
wordOneEndPos = 27

wordTwoStartPos = 97
wordTwoEndPos = 102

txtStr = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."

print(
  f'{txtStr[wordOneStartPos:wordOneEndPos + 1]} {txtStr[wordTwoStartPos:wordTwoEndPos + 1]}')


# === Conditions and Loops ===
startPos = 100
endPos = 200
# result = 0

# for x in range(startPos, endPos + 1):
#     if x % 2 != 0:
#         result += x

result = sum(
    [x for x in range(startPos, endPos + 1) if x % 2 != 0]
        )

print(result)


# === Working with Files ===
outputFile = []

with open('input.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]
    
with open('output.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))


# === Dictionaries ===
wordCoutDict = {}

# for word in txtStr.split(' '):
#     if word in wordCoutDict:
#         wordCoutDict[word] += 1
#     else:
#         wordCoutDict[word] = 1
        
wordCoutDict = Counter(txtStr.split(' '))

for key, value in wordCoutDict.items():
    print(key, value)




