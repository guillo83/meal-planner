from mylib.logic import recipe


def test_wiki():
    parsed = recipe("https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/")
    print(parsed)
    assert len(parsed.get('title')) > 0
