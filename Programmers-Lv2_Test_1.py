def solution(cacheSize, cities):
    answer = 0
    cache = []
    cache_len = 0
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        if not city.lower() in cache:
            if cache_len < cacheSize:
                cache.append(city.lower())
                cache_len += 1
                answer += 5
            else:
                cache.pop(0)
                cache.append(city.lower())
                answer += 5
        else:
            cache.pop(cache.index(city.lower()))
            cache.append(city.lower())
            answer += 1


    return answer