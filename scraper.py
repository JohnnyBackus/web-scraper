from scrape_citations import get_citations_needed_count, get_citations_needed_report

url = "https://en.wikipedia.org/wiki/Valentine%27s_Day"

citations_count_results = get_citations_needed_count(url)
print("citations_count_results: ", citations_count_results)

citations_report_results = get_citations_needed_report(url)
print("citations_report_results: ", citations_report_results)

# with open("citations.txt","w") as f:
#     f.write("The wikipedia article at " + url + " needs " + str(citations_count_results) + " citations. The paragraphs in need of citations are as follows: \n\n" + citations_report_results)
