# T.C: O(nlog(n))
# S.C: O(n)
def mergeOverlappingIntervals(intervals):
    intervals.sort()
     _, i, intervals_len = [], 0, len(intervals)
    while i < intervals_len:
        current_pair = intervals[i]
        i += 1
        while i < intervals_len and current_pair[1] >= intervals[i][0]:
            current_pair = [current_pair[0], max(current_pair[1], intervals[i][1])]
        i += 1
        _.append(current_pair)
    return _

