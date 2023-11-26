import csv

list = []

file_name = "museumvisitors_dataset.csv"



with open(file_name, "r") as this_csv_file:
    this_csv_reader = csv.reader(this_csv_file, delimiter=",")
    #this_csv_reader = csv.reader(this_csv_file)
    header = next(this_csv_reader)
    print(header)
    for row in this_csv_reader:
        print(row)


menu = """

"""
