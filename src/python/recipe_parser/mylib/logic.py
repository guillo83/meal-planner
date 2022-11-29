from recipe_scrapers import scrape_me

def recipe(url):
    """This fetch a recipe and parses it into a JSON object"""
    scraper = scrape_me(url)
    instructions = [i.strip() for i in scraper.instructions().split("\n") if i.strip()]
    recipe_object = {
        'title': scraper.title(),
        'ingredients': scraper.ingredients(),
        'instructions': instructions,
        'image': scraper.image(),
        'url': url,
    }
    return recipe_object
