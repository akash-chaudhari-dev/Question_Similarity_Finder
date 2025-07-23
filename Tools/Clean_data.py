import csv
import os

def Clean_Data(CSV_PATH):  
    print("Found Some Issues with CSV file. Cleaning Data...")

    rows = []
    with open(CSV_PATH, 'r', encoding='utf-8') as file:
        next(file)  # skip header
        for line in file:
            line = line.strip()
            if line:
                answer, difficulty, category, question = line[::-1].split(',', 3)
                rows.append([question[::-1], category[::-1], difficulty[::-1], answer[::-1]])

    # Write header + rows in one go
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Question', 'Category', 'Difficulty', 'Answer'])  # header
        writer.writerows(rows)

    print("Data Cleaned Successfully")
    return CSV_PATH

if __name__ == "__main__":
    # print(Clean_Data(r'../data/data.csv'))
    pass
