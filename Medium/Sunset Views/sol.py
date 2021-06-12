# T.C: O(n)
# S.c: O(n)
def sunsetViews(buildings, direction):
    ans, buildings_len, greatest_building_so_far, starting, ending, step = [], len(buildings), -1, 0, 0, 0
    if direction == "EAST":
        starting, ending, step = buildings_len - 1, -1, -1
    else:
        starting, ending, step = 0, buildings_len, 1
    for i in range(starting, ending, step):
        if buildings[i] > greatest_building_so_far:
            ans.append(i)
        greatest_building_so_far = max(greatest_building_so_far, buildings[i])
    return ans[::-1] if direction == "EAST" else ans

