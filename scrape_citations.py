from bs4 import BeautifulSoup
import requests


def get_citations_needed(markup): #shared function to find "citations needed"
    soup = BeautifulSoup(markup,"html.parser")
    citations_needed_soup = soup.find_all("sup", "noprint Inline-Template Template-Fact") #finds all <sup> tags with the class "noprint Inline-Template Template-Fact"
    return citations_needed_soup #returns a list


def get_citations_needed_count(url):
    response = requests.get(url)
    count = len(get_citations_needed(response.text)) #returns the length of the list, which is the number of "citation needed" <sup> tags
    return count


def get_citations_needed_report(url):
    response = requests.get(url) 
    citation_sups = get_citations_needed(response.text)
    report = "Citations needed for this article: \n" 
    
    for sup in citation_sups: #iterate through the list of <sup> tags
        sup_parent = sup.parent #get the parent of the <sup> tag
        report += "\n" + sup_parent.text #add the text of the parent to the report and insert an empty line for spacing
    return report    
