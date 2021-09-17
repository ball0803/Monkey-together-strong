def filter_similarity(data, t, u_or_s) -> list:
    if u_or_s == 'u':
        new_data = tuple((value[0], value[1], value[4]) for value in data)
    else:
        new_data = tuple((value[2], value[3], value[4]) for value in data)
    pairs = []

    for i, j, similarity in new_data:
        if similarity >= t:
            pairs.append([i, j])
    return pairs

def find_group(pairs) -> list:
    seen = []
    for i, j in pairs:
        if not seen:
            seen.append([i, j])
            continue
        
        for waiting in seen:
            if i in waiting or j in waiting:
                waiting.append(i if j in waiting else j)
                break
        else:
            seen.append([i, j])

    if seen[0][0].startswith('U_'):
        seen_sorted = [sorted(i, key=lambda x: int(x[2:])) for i in seen]
    else:
        seen_sorted = [sorted(i, key=lambda x: int(x)) for i in seen]

    return list(sorted(seen_sorted))


def find_number_of_similar_users(user_pairs, n):
    lookup = []
    for i, j in user_pairs:
        for index, val in enumerate(lookup):
            x, _ = val
            if i ==  x:
                lookup[index][1] += 1
                break
        else:
            lookup.append([i, 1])

        for index, val in enumerate(lookup):
            x, _ = val
            if j == x:
                lookup[index][1] += 1
                break
        else:
            lookup.append([j, 1])
    
    return [i[0] for i in sorted(lookup)[:n]]
    