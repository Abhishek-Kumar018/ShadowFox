import argparse
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import textwrap
import re

@dataclass
class PersonInfo:
    full_name: str = None
    birth_date: str = None
    birth_place: str = None
    death_date: str = None
    occupation: str = None
    biography: str = None

class WikipediaScraper:
    def __init__(self, name):
        self.name = name
        self.url = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    def fetch_page(self):
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def parse_page(self, html):
        return BeautifulSoup(html, 'html.parser')

    def clean_text(self, element):
        for sup in element.find_all('sup'):
            sup.decompose()
        return element.get_text(separator=' ', strip=True)

    def extract_info(self, soup):
        person_info = PersonInfo()
        h1_tag = soup.find('h1', id='firstHeading')
        person_info.full_name = h1_tag.text.strip() if h1_tag else (soup.title.text.split('-')[0].strip() if soup.title else None)
        infobox = soup.find('table', class_='infobox')
        if infobox:
            rows = infobox.find_all('tr')
            info_map = {}
            for row in rows:
                header = row.find('th')
                data = row.find('td')
                if header and data:
                    key = header.text.strip().lower()
                    value = self.clean_text(data)
                    info_map[key] = value
            if 'born' in info_map:
                birth_info = info_map['born']
                bday_span = infobox.find('span', class_='bday')
                person_info.birth_date = bday_span.text.strip() if bday_span else None
                clean_place = re.sub(r'\(.*?\)', '', birth_info)
                if person_info.birth_date:
                    clean_place = clean_place.replace(person_info.birth_date, '')
                person_info.birth_place = clean_place.strip(' ,')
            else:
                for k in ['birth date', 'date of birth']:
                    if k in info_map:
                        person_info.birth_date = info_map[k]
                for k in ['birth place', 'place of birth']:
                    if k in info_map:
                        person_info.birth_place = info_map[k]
            for k in ['died', 'death date', 'date of death']:
                if k in info_map:
                    person_info.death_date = info_map[k]
                    break
            for k in ['occupation', 'profession', 'career', 'position', 'sport']:
                if k in info_map:
                    person_info.occupation = info_map[k]
                    break
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            text = self.clean_text(paragraph)
            if text and paragraph.find_parent(['table', 'td', 'th']) is None and len(text) > 50:
                person_info.biography = text
                if not person_info.occupation:
                    lower_text = text.lower()
                    for keyword in ['is a', 'is an', 'was a', 'was an']:
                        if keyword in lower_text:
                            occ = text.split(keyword)[1].split('.')[0].strip()
                            person_info.occupation = occ.capitalize()
                            break
                break
        return person_info

def main():
    parser = argparse.ArgumentParser(description='Wikipedia Person Information Extractor')
    parser.add_argument('--name', type=str, required=True, help="Person's name (quote if it has spaces)")
    parser.add_argument('--output', type=str, default='output.txt', help='Output file name')
    args = parser.parse_args()
    scraper = WikipediaScraper(args.name)
    html = scraper.fetch_page()
    if not html:
        return
    soup = scraper.parse_page(html)
    person_info = scraper.extract_info(soup)
    print("\nDEBUG INFO (what we scraped):")
    print(person_info, "\n")
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write("Wikipedia Person Information\n")
        f.write("---------------------------\n")
        f.write(f"Full Name: {person_info.full_name}\n\n")
        f.write("Birth Information:\n")
        f.write(f"  Date: {person_info.birth_date}\n")
        f.write(f"  Place: {person_info.birth_place}\n\n")
        f.write(f"Death Date: {person_info.death_date}\n\n")
        f.write(f"Occupation: {person_info.occupation}\n\n")
        f.write("Biography:\n")
        f.write("---------------------------\n")
        if person_info.biography:
            wrapped_text = textwrap.fill(person_info.biography, width=120)
            f.write(wrapped_text + '\n')
    print(f"Information saved to {args.output}")

if __name__ == '__main__':
    main()
