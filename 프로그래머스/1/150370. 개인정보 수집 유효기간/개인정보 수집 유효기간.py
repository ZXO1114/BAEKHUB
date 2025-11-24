import datetime as dt
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    today = dt.datetime.strptime(today, "%Y.%m.%d")
    # print(today)
    type_dict = {key: int(value) for key, value in (term.split() for term in terms)}
    # print(type_dict)
    
    for i, privacy in enumerate(privacies):
        p_date, p_type = privacy.split()
        # print(p_date,p_type)
        p_date = dt.datetime.strptime(p_date,"%Y.%m.%d")
        # print(p_date)
        p_date += relativedelta(months = type_dict[p_type])
        # print(p_date)
        if p_date <= today:
            answer.append(i+1)
    
    return answer