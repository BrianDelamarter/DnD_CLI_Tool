import requests

#Dictionary of API endpoints for different resource types
url_dict = {'items': 'https://api.open5e.com/v2/items/',
'magicitems': 'https://api.open5e.com/v2/magicitems/',
'itemsets': 'https://api.open5e.com/v2/itemsets/',
'itemcategories': 'https://api.open5e.com/v2/itemcategories/',
'documents': 'https://api.open5e.com/v2/documents/',
'licenses': 'https://api.open5e.com/v2/licenses/',
'publishers': 'https://api.open5e.com/v2/publishers/',
'weapons': 'https://api.open5e.com/v2/weapons/',
'armor': 'https://api.open5e.com/v2/armor/',
'gamesystems': 'https://api.open5e.com/v2/gamesystems/',
'backgrounds': 'https://api.open5e.com/v2/backgrounds/',
'feats': 'https://api.open5e.com/v2/feats/',
'species': 'https://api.open5e.com/v2/species/',
'creatures': 'https://api.open5e.com/v2/creatures/',
'creaturetypes': 'https://api.open5e.com/v2/creaturetypes/',
'creaturesets': 'https://api.open5e.com/v2/creaturesets/',
'damagetypes': 'https://api.open5e.com/v2/damagetypes/',
'languages': 'https://api.open5e.com/v2/languages/',
'alignments': 'https://api.open5e.com/v2/alignments/', 
'conditions': 'https://api.open5e.com/v2/conditions/',
'spells': 'https://api.open5e.com/v2/spells/', 
'spellschools': 'https://api.open5e.com/v2/spellschools/',
'classes': 'https://api.open5e.com/v2/classes/',
'sizes': 'https://api.open5e.com/v2/sizes/',
'itemrarities': 'https://api.open5e.com/v2/itemrarities/',
'environments': 'https://api.open5e.com/v2/environments/',
'abilities': 'https://api.open5e.com/v2/abilities/',
'skills': 'https://api.open5e.com/v2/skills/',
'rules': 'https://api.open5e.com/v2/rules/',
'rulesets': 'https://api.open5e.com/v2/rulesets/',
'images': 'https://api.open5e.com/v2/images/',
'weaponproperties': 'https://api.open5e.com/v2/weaponproperties/',
'services': 'https://api.open5e.com/v2/services/'}
'''
def get_url(resource_type):
    for key, value in url_dict.items():
        if key == resource_type:
            return value


def get_data(RESOURCE_TYPE):
    url = get_url(RESOURCE_TYPE)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def get_data_by_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
'''
class APIRequest:
    def __init__(self, search_type, search_query):
        self.search_type = search_type
        self.search_query = search_query

    def category_url(self, search_query):
        for key, value in url_dict.items():
                if key == search_query:
                     self.url = value

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def category_results(self, search_query):
        url = self.get_url(search_query)
        self.fetch_data(url)

'''
API Response Explained:
- The API response is a JSON object that contains a dictionary with four keys: 'count', 'next', 'previous', 
and 'results'.
- 'count' is an integer that represents the total number of results available for the requested resource type.
- 'next' is a string that contains the URL for the next page of results, or None if there are no more results.
- 'previous' is a string that contains the URL for the previous page of results, or None if there are no previous results.
- 'results' is a list of dictionaries, where each dictionary represents a single result for the requested resource
type. MAX 50 at a time. You can use the 'next' and 'previous' URLs to navigate through the pages of results.
'''