from collections import deque

def solution(cacheSize, cities):
    answer = 0
    time = [1,5]
    
    if cacheSize == 0: return len(cities) * time[1]
    cache_deque = deque(["가짜도시" for _ in range(cacheSize)])
    # print(cache_deque)
          
    for city in cities:
        city = city.lower()
        if city in cache_deque:
            cache_deque.remove(city)
            answer += 1
        else:
            cache_deque.popleft()
            answer += 5
        cache_deque.append(city)
        # print(cache_deque)
        
        
    return answer