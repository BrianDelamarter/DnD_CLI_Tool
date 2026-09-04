import requests

from print_effects import printer

class search:
    def __init__(self):
        self.base_url = "https://api.open5e.com/v2/"
        self.api_request(self.base_url)

    def api_request(self, url=None):
        if url:
            self.url = url
        response = requests.get(self.url)
        #print("Making API request to:", self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print(f"Error: {response.status_code}")

    def next_page(self):
        #print("next page")
        self.url = self.data["next"]
        self.api_request()

    def previous_page(self):
        #print("previous page")
        self.url = self.data["previous"]
        self.api_request()

    def page_data(self, page_direction):
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
        self.api_request()

    def expected_page(self, query):
        first_letter_ascii = ord(query[0].lower())
        if first_letter_ascii-96 == 1:
            expected_page = 1
        else:
            expected_page = int(((first_letter_ascii-96)/26)*(self.data["count"]/50))
        return expected_page

    def search_page(self, query):
        self.right_page = False
        print("Searching for the right page...")
        expected_page = self.expected_page(query)
        self.url = self.base_url+self.category+"/?page="+str(expected_page)
        self.api_request()
        while not self.right_page:
            if self.data["results"][0]["name"][0] <= query[0] and self.data["results"][-1]["name"][0] >= query[0]:
                print("Found the right page!")
                self.right_page = True
            else:
                if self.data["results"][0]["name"][0] > query[0]:
                    self.previous_page()
                elif self.data["results"][-1]["name"][0] < query[0]:
                    self.next_page()         
        for result in self.data["results"]:
            if result["name"].lower() == query.lower():
                return result



DnD = search()  
print(DnD.data)

'''
class general_search(search):
    def __init__(self, query):
        super().__init__()
        self.query = query
        self.url = self.base_url + "search/?query=" + self.query
        self.api_request()


monsters = category_search("creatures")
#printer(f"There are {monsters.data['count']} creatures in the Open5e database. Search for a specific creature by name.")
query = input("Creature name: ")
monsters.search_page(query)'''
