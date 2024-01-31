from bs4 import BeautifulSoup




def get_citations_needed(markup):
    soup = BeautifulSoup(markup,"html.parser")
    citations_needed_soup = soup.find_all("sup", "noprint Inline-Template Template-Fact")
    # print("citation_needed_soup: ", citations_needed_soup)
    return citations_needed_soup


def get_citations_needed_count(markup):
    count = len(get_citations_needed(markup))
    # print(f"Number of citations needed: {count}")
    return count


def get_citations_needed_report(markup):
    citation_sups = get_citations_needed(markup)
    # print("citation_sups: ", citation_sups)
    report = "Citations needed for this article: \n\n"
    for sup in citation_sups:
        sup_parent = sup.parent
        # print("sup_parent: ", sup_parent)
        # print("sup_parent.text: ", sup_parent.text)
        report += sup_parent.text + "\n"
   
    return report    
  
#     report = 
#     for i in report:
#         print(i.text)
#         print(i.parent.parent.text)
#         print("------------------------------------------------------")