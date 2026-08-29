from api_interaction import get_data

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

class APIResponse:
    def __init__(self, search_query):
        self.data = get_data(search_query)
        self.count = self.data.get("count") #Total Number of results available for the requested resource type
        self.next = self.data.get("next") #Previous page of results, or None if there are no previous results
        self.previous = self.data.get("previous") #Next page of results, or None if there are no more results
        self.results = self.data.get("results") #List of results up to 50 at a time. You can use the 'next' and 'previous' URLs to navigate through the pages of results.

    #returns the number of pages of results
    def count_pages(self):
        return (self.count // 50) + (1 if self.count % 50 > 0 else 0)


    def results_list(self):
        return self.results

    def results_names(self):
        return [result.get("name") for result in self.results]


magic_items_response = APIResponse("magicitems")
print(magic_items_response.results_names()) 