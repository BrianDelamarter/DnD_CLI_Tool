import requests

class search:
    def __init__(self):
        self.base_url = "https://api.open5e.com/v2/"
        self.data = {}

    def api_request(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print(f"Error: {response.status_code}")

    def next_page(self):
        self.url = self.data["next"]

    def previous_page(self):
        self.url = self.data["previous"]

    def update_data(self, page_direction):
        if page_direction == 0:
            self.next_page()
            self.api_request()
        elif page_direction == 1:
            self.previous_page()
            self.api_request()
        else:
            return None



class category_search(search):
    def __init__(self, category, filter=None):
        super().__init__()
        self.category = category
        self.url = self.base_url+self.category
        if filter:
            self.url += ("/?type="+filter)
        self.url += "&?fields=name"
        self.api_request()



class general_search(search):
    def __init__(self, query):
        super().__init__()
        self.query = query
        self.url = self.base_url + "search/?query=" + self.query
        self.api_request()


creatures = category_search("creatures",filter="dragon")
print(creatures.url)
print(creatures.data["results"][0])
creatures.update_data(0)
print(creatures.url)
print(creatures.data["results"][0])


'''goblin_search = general_search("goblin")
print(goblin_search.data['previous'])'''
