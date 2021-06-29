import json
import csv

if __name__ == '__main__':
    # Read from JSON
    # with open('standings.json') as json_file:
    #     standings = json.load(json_file)
    # print('[JSON] standings', standings)

    # Read from CSV
    with open('standings.csv') as csv_file:
        standings = []

        csv_rows = csv.reader(csv_file)
        csv_rows = list(csv_rows)

        columns = csv_rows[0]

        for row in csv_rows[1:]:
            standings.append({
                column: value for column, value in zip(columns, row)
            })

    print('[CSV] standings', standings)
