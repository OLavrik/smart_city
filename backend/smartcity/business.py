from smartcity.db import region_stats_collection


def get_stats():
    result = {
        "headers": ["Москва", "Санкт-Петербург", "Калуга"],
        "data": {
            "Точки Wi-fi": [108, 62, 11],
            "Автобусы с ГЛОНАСС": [8, 3, 0]
        }
    }

    res = region_stats_collection.find_one({"tag": "green_energy_costs"})
    print("Res is", res)
    del res["_id"]
    return res
