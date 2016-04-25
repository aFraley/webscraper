"""
Web Scraper

Author: Alan Fraley
Date: 4/24/2016
"""
from urllib import request
from bs4 import BeautifulSoup


class Website:
    """A new website to fetch."""
    def __init__(self, url='https://www.google.com/?gws_rd=ssl'):
        """
        Initialize the new website object.

        :param url: url address for the new site.
        """
        self.url = url

    def open_page(self):
        """
        Get the web page.

        Add prettify() to the end of this object method to print the HTML as readable text.
        Like this, google.open_page().prettify()

        :return: the html file requested
        """
        response = request.urlopen(self.url)
        soup = BeautifulSoup(response)
        return soup

    def get_tag_by_class(self, tag_name='span', attr_type='id', attr_name='footer'):
        """
        Get a specific tag.

        :param tag_name: name of the tag
        :param attr_type: type of tag attribute
        :param attr_name: name of the attribute
        :return: the specified tags
        """
        return self.open_page().find_all(tag_name, attrs={attr_type: attr_name})


if __name__ == '__main__':

    # Instantiate a new website object.
    google = Website()
    print()

    # Print the text that is inside of the specified tags.
    for tag in google.get_tag_by_class():
        print(tag.text)
