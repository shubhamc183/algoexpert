def _get_any_index_of(char, index_map):
    idxs = index_map.get(char)
    idx = idxs.pop()
    index_map[char] = idxs
    return idx

# T.C: O(nlogn)
# S.C: O(n)
def taskAssignment(k, tasks):
    _, index_map, tasks_len = [], {}, len(tasks)
    for i in range(tasks_len):
        index_map[tasks[i]] = index_map.get(tasks[i], []) + [i]
    tasks_sorted = sorted(tasks)
    for i in range(int(tasks_len/2)):
        _.append([
            _get_any_index_of(tasks_sorted[i], index_map),
        _get_any_index_of(tasks_sorted[tasks_len-i-1], index_map)])
    return _
