import csv

file = input()
dict = {}
with open(file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        for word in row:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
for word in dict:
    print(word, dict[word])
