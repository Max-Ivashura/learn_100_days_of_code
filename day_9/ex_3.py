# Nesting dict in a dict
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stutgart"], "total_visits": 5},
}

# Nesting dict in a list
travel_log = [
    {
        "France": {
            "cities_visited": ["Paris", "Lille", "Dijon", "Other"],
            "total_visits": 12,
        }
    },
    {
        "Germany": {
            "cities_visited": ["Berlin", "Hamburg", "Stutgart"],
            "total_visits": 5,
        }
    },
]
