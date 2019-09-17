import csv;
import random;
with open('occupations.csv') as csv_file:
    f = list(csv.DictReader(csv_file));
    del f[-1];
    values  = [];
    for row in f:
        row['Percentage'] = float(row['Percentage']);
        values.append(row['Percentage']);
    print(random.choices(f, weights = values, k = 1));
