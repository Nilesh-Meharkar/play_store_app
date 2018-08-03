import requests
from bs4 import BeautifulSoup
import urlparse

# base_url = 'https://play.google.com/store/search?q=social&c=apps'
base_url = 'https://play.google.com/store/search?q={search_str}&c=apps'


def get_play_store_data(search_str):

    search_url = base_url.format(search_str=search_str)
    page = requests.get(search_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    app_container = soup.find(class_='id-card-list card-list two-cards')
    app_list_dom = app_container.find_all(class_='square-cover')
    app_list = []

    for app_div in app_list_dom:
        # print app_div
        obj = {}
        app_relative_url = app_div.find_all(class_="card-click-target")[0]['href']
        abs_url = urlparse.urljoin(base_url, app_relative_url)
        app_title = app_div.find_all(class_="title")[0]['title']
        app_sub_title = app_div.find_all(class_="subtitle-container")[0].a['title']
        app_desc = app_div.find_all(class_="description")[0].text
        obj["app_url"] = abs_url
        obj["app_title"] = app_title
        obj["app_sub_title"] = app_sub_title
        obj["app_desc"] = app_desc
        app_list.append(obj)

    # print app_list
    return app_list


if __name__ == "__main__":
    from pprint import pprint
    pprint (get_play_store_data("shooting"))
