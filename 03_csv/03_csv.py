import csv
import random
with open('occupations.csv') as csv_file:
    file = list(csv.DictReader(csv_file))
    del file[-1]
    stats = []
    weights = []
    for row in file:
        add = row['Job Class'], ", ", row['Percentage']
        stats.append(add)
        #row['Percentage'] = float(row['Percentage'])
        weights.append(float(row['Percentage']))
    print(random.choices(stats, weights = weights, k = 1))
    #print(picked.key(), picked.value());
