def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_dict = {key:value for value, key in enumerate(id_list)}
    reported_list = [set() for _ in range(len(id_list))]
    
    for row in report:
        gahae, pihae = row.split()
        reported_list[id_dict[pihae]].add(gahae)
    
    for user_report_set in reported_list:
        if len(user_report_set) >= k:
            user_report_list = list(user_report_set)
            for user in user_report_list:
                answer[id_dict[user]] += 1
        
    return answer