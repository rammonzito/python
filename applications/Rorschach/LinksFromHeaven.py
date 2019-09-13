from bs4 import BeautifulSoup
import re

class LinksFromHeaven():

    def extract(content):
        links = []
        soup = BeautifulSoup(content, 'lxml')
        for tag in soup.find_all():
            if tag.name == 'a' and 'href' in tag.attrs:
                url = re.search("(?P<url>https?://[^\s]+)",tag.attrs['href']).group("url")
                url = url.replace('"','').replace('=','')
                links.append(url)
        return links

    # if __name__ == "__main__":
    #     links = extract(content)