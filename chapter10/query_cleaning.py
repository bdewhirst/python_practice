import re


def remove_spaces(query):
    query = query.strip()
    query = re.sub(r"\s+", ' ', query)
    return query

def normalize(query):
    query = query.casefold()  # more aggressive .lower() --> "german B" --> ss
    return query

def remove_quotes(query):
    query = re.sub(r'"', '', query)
    return query


if __name__ == '__main__':
    search_query = input('Enter your search query: ')
    search_query = remove_spaces(search_query)
    search_query = normalize(search_query)
    print(f"Running a search for '{search_query}'")