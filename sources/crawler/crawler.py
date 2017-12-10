from bs4 import BeautifulSoup
import requests

class Crawler:

    def __init__(self, url):
        self.url = url
        request = requests.get(url)
        self.soup = BeautifulSoup(request.content, "html.parser")
        self.title = self.get_title()
        print(self.title)
        self.document_id = hash(self.title) # change the hashing function
        print(self.document_id)
        self.date = self.get_date()
        print(self.date)
        self.author = self.get_author()
        print(self.author)
        self.author_wording = self.get_author_wording()
        self.quote = self.get_quote()


    """
    Retrieve the title for a given article
    """
    def get_title(self):
        h1 = self.soup.find("h1", { "class" : "name post-title entry-title" })
        title = h1.find("span", { "itemprop" : "name" })
        return title.text

    """
    Retrieve the date for a given article
    """
    def get_date(self):
        entry = self.soup.find("div", { "class" : "entry" })
        p = entry.find("p")
        brs = p.text.split("\n")
        date = brs[2]
        return date


    """
    Retrieve the name of the author for a given article
    """
    def get_author(self):
        author_div = self.soup.find("div", { "class" : "vcard author" })
        return author_div.text

    """
    Retrieve the content write by an author for a given article
    """
    # To be implemented
    def get_author_wording(self):
        return None

    """
    Retrieve the different quotations for a given article
    """
    # To be implemented
    def get_quote(self):
        return None


Crawler("https://dailystormer.red/women-should-shut-the-fuck-up/")
