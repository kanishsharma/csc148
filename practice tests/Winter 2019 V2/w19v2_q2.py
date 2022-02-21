

def append_sometimes(lst, new):
    answer = lst
    for item in answer:
        if new not in item:
            item.append(new)
    return answer
