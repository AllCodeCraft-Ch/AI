def heuristic(current_city, unvisited_cities, distances):
    if not unvisited_cities:
        return 0
    nearest_distance = float('inf')
    for city in unvisited_cities:
        distance = distances.get((current_city, city), distances.get((city, current_city), float('inf')))
        if distance < nearest_distance:
            nearest_distance = distance
    return nearest_distance

def greedy_best_first_search(start_city, cities, distances):
    unvisited_cities = set(cities)
    unvisited_cities.remove(start_city)
    current_city = start_city
    route = [start_city]
    total_distance = 0

    while unvisited_cities:
        next_city = None
        min_heuristic = float('inf')
        for city in unvisited_cities:
            distance = distances.get((current_city, city), distances.get((city, current_city), float('inf')))
            h = heuristic(city, unvisited_cities - {city}, distances) + distance
            if h < min_heuristic:
                min_heuristic = h
                next_city = city
        route.append(next_city)
        total_distance += distances.get((current_city, next_city), distances.get((next_city, current_city), float('inf')))
        current_city = next_city
        unvisited_cities.remove(next_city)

    # Return to the start city
    return_distance = distances.get((current_city, start_city), distances.get((start_city, current_city), float('inf')))
    route.append(start_city)
    total_distance += return_distance

    return route, total_distance


cities = ["Bangkok", "Nakhon Sawan", "Sukhothai", "Uttaradit", "Lampang", "Lamphun", "Chiang Mai", "Phayao", "Phrae", "Tak"]
distances = {
    ("Bangkok", "Nakhon Sawan"): 240,
    ("Bangkok", "Phrae"): 520,
    ("Bangkok", "Chiang Mai"): 700,
    ("Bangkok", "Phayao"): 780,
    ("Bangkok", "Lampang"): 600,
    ("Bangkok", "Lamphun"): 670,
    ("Bangkok", "Uttaradit"): 490,
    ("Bangkok", "Sukhothai"): 410,
    ("Bangkok", "Tak"): 430,
    ("Nakhon Sawan", "Phrae"): 320,
    ("Nakhon Sawan", "Chiang Mai"): 460,
    ("Nakhon Sawan", "Phayao"): 480,
    ("Nakhon Sawan", "Lampang"): 360,
    ("Nakhon Sawan", "Lamphun"): 430,
    ("Nakhon Sawan", "Uttaradit"): 250,
    ("Nakhon Sawan", "Sukhothai"): 170,
    ("Nakhon Sawan", "Tak"): 190,
    ("Phrae", "Chiang Mai"): 200,
    ("Phrae", "Phayao"): 140,
    ("Phrae", "Lampang"): 220,
    ("Phrae", "Lamphun"): 250,
    ("Phrae", "Uttaradit"): 110,
    ("Phrae", "Sukhothai"): 150,
    ("Phrae", "Tak"): 180,
    ("Chiang Mai", "Phayao"): 150,
    ("Chiang Mai", "Lampang"): 100,
    ("Chiang Mai", "Lamphun"): 30,
    ("Chiang Mai", "Uttaradit"): 250,
    ("Chiang Mai", "Sukhothai"): 270,
    ("Chiang Mai", "Tak"): 280,
    ("Phayao", "Lampang"): 170,
    ("Phayao", "Lamphun"): 180,
    ("Phayao", "Uttaradit"): 210,
    ("Phayao", "Sukhothai"): 240,
    ("Phayao", "Tak"): 250,
    ("Lampang", "Lamphun"): 40,
    ("Lampang", "Uttaradit"): 140,
    ("Lampang", "Sukhothai"): 170,
    ("Lampang", "Tak"): 200,
    ("Lamphun", "Uttaradit"): 170,
    ("Lamphun", "Sukhothai"): 200,
    ("Lamphun", "Tak"): 230,
    ("Uttaradit", "Sukhothai"): 70,
    ("Uttaradit", "Tak"): 100,
    ("Sukhothai", "Tak"): 90,
}

start_city = "Bangkok"
route, total_distance = greedy_best_first_search(start_city, cities, distances)

print(route)
print(total_distance)
