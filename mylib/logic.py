import wikipedia
from recipe_scrapers import scrape_me

def recipe(url):
    scraper = scrape_me(url)
    instructions = [i.strip() for i in scraper.instructions().split("\n") if i.strip()]
    recipe = {
        'name': scraper.title(),
        'ingredients': scraper.ingredients(),
        'instructions': instructions,
        'image': scraper.image(),
        'url': url,
    }
    return recipe


def wiki(name="War Goddess", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for Names"""

    return wikipedia.search(name)
