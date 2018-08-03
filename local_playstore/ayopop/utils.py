from models import AppDetails
from web_scraping_helper import get_play_store_data


def get_search_data(search_str):

    data = []
    db_data = AppDetails.objects.filter(search_str__icontains = search_str)

    if db_data:
        # if data not in db
        for obj in db_data:
            data.append(obj.ayopop_model_to_dict())

    else:
        # if data not in db
        data_list = get_play_store_data(search_str)
        data_list = data_list[0:12]
        for obj in data_list:
            try:
                app = AppDetails.objects.get(app_url=obj.get("app_url"))
                app.search_str = app.search_str + ", " + search_str
                app.save()
            except Exception as e:
                app = AppDetails()
                app.app_url = obj.get("app_url")
                app.app_title = obj.get("app_title")
                app.app_sub_title = obj.get("app_sub_title")
                app.app_desc = obj.get("app_desc")
                app.search_str = search_str
                app.save()

            data.append(obj.ayopop_model_to_dict())

    return data
