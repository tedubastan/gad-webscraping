import os
import csv
import json
import requests
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup

lpf_domain = 'https://lpf.ro/'
columns = ['position', 'image', 'name', 'games', 'goals', 'points']
folder_name = 'data/team_images'

if __name__ == '__main__':
    Path(folder_name).mkdir(parents=True, exist_ok=True)

    standings = []
    page = requests.get(f'{lpf_domain}liga-1')
    soup = BeautifulSoup(page.content, features='html.parser')

    # table_parent = soup.find(id='clasament_ajax_playoff')
    # table = table_parent.find('table')
    table = soup.find(id='clasament_ajax_playoff').find('table')
    table_rows = table.find_all('tr', class_='echipa_row')
    for table_row in table_rows:
        # Get standings data
        text_from_tds = [
            td for td in table_row.find_all('td')
            if 'hiddenMobile' not in td.get('class', [])
        ]
        team_dict = {
            col: (data.text or lpf_domain + data.find('img')['data-src'])
            for col, data in zip(columns, text_from_tds)
        }
        standings.append(team_dict)

        # Download image locally
        # image = requests.get(team_dict['image'])
        # print('image', image.content)
        urllib.request.urlretrieve(team_dict['image'], f'{folder_name}/{team_dict["name"].lower().replace(" ", "_")}.png')

    # print(standings)

    with open('standings.json', mode='w') as json_file:
        json.dump(standings, json_file, indent=2)

    with open('standings.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(columns)
        csv_writer.writerows([team_data.values() for team_data in standings])
