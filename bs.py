from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.covid19india.org/').text

soup = BeautifulSoup(source, 'lxml')

# csv_file = open('cms_scrape.csv', 'w')
#
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video_link'])

def scrape(default):

    for row in soup.find_all('state-name')==default:
        region = row.text
        print(state)

        summary = article.find('div', class_='entry-content').p.text
        print(summary)

        try:
            vid_src = article.find('iframe', class_='youtube-player')['src']

            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]

            yt_link = f'https://youtube.com/watch?v={vid_id}'
        except Exception as e:
            yt_link = None

        print(yt_link)

        print()

        csv_writer.writerow([headline, summary, yt_link])

    csv_file.close()