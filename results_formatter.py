# Results Formatter
# Will receive a dictionary and format it for printing to the console.


def format_results(results):
    for result in results:
        print(f"Name: {result['name']}")
        print(f"Description: {result['desc']}")
        print("---")