from dnd_cli_tool.api_interaction import get_data, get_data_by_url

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

    def __update_data(self, new):
        self.data = get_data_by_url(new)

    #returns the number of pages of results
    def count_pages(self):
        return (self.count // 50) + (1 if self.count % 50 > 0 else 0)

    #return the list of results unlikely to be used in the CLI tool, but useful for testing and debugging and in other applications that use the API
    def results_list(self):
        return self.results

    #return a list of the names of the results
    def results_names(self):
        return [result.get("name") for result in self.results]

    def check_data(self, name):
        for item in self.results:
            if item.get("name") == name:
                return item

    def expected_page(self, name):
        #create search algorithm that uses the first letter of the name and the total number of pages to guess on which page the result is on.
        first_letter_ascii = ord(name[0].lower())
        if first_letter_ascii-96 == 1:
            expected_page = 1
        else:
            expected_page = int(((first_letter_ascii-96)/26)*self.count_pages())
        return expected_page

    



magic_items_response = APIResponse("magicitems")
print(magic_items_response.count_pages())
print(magic_items_response.expected_page("Gmulet of Health"))