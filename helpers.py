import settings


def get_next_app(app_index, step):
    return settings.APP_KITS[app_index]['sequence'][step]
