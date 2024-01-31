import requests
from scrape_citations import get_citations_needed_count, get_citations_needed_report


url = "https://en.wikipedia.org/wiki/Valentine%27s_Day"
response = requests.get(url)
# print("response:", response.text)

citations_count_results = get_citations_needed_count(response.text)
print("citations_count_results: ", citations_count_results)

citations_report_results = get_citations_needed_report(response.text)
print("citations_report_results: ", citations_report_results)

# with open("courses.txt","w") as f:
#     f.write(citations_count_results)
    # f.close()