import csv

def extract_info_from_csv(csv_file, id_column, data_IDs, column_name):
    ids = []

    with open(csv_file, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row[column_name] in data_IDs: 
                ids.append(row[id_column])

    ids = [float(x) for x in ids if x]    

    return ids
