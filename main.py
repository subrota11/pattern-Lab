import csv
import pickle

with open('dataset.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    List = []
    List2 = []
    for row in csv_reader:
        if (line_count < 300):
            List.append(row["peptide"])
            with open('datasetpositive.txt', 'wb') as fh:
                pickle.dump(List, fh)
        if (line_count >= 300):
            List2.append(row["peptide"])
            with open('datasetnegitive.txt', 'wb') as fh:
                pickle.dump(List2, fh)
        line_count+=1

    pickle_off = open("datasetpositive.txt", "rb")
    positive = pickle.load(pickle_off)
    print("Positive peptide list")
    print(positive)
    print("Negative peptide list")
    pickle_off2 = open("datasetnegitive.txt", "rb")
    negative = pickle.load(pickle_off2)
    print(negative)



