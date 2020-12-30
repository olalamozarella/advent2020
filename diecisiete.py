import common


# reads input and stores all active fields to set as tuple (x,y,z)
def parse_input(inputs):
    result = set()
    x, y = 0, 0
    for row in inputs.rstrip().split("\n"):
        x = 0
        for char in row:
            if char == "#":
                result.add((x, y, 0, 0))
            x += 1
        y += 1
    return result


# returns: count of active neighboring fields
def get_active_neighbor_count(active_fields, current_field, part2_flag):
    count = 0
    x, y, z, w = current_field
    if part2_flag is False:
        minw, maxw = 0, 1
    else:
        minw, maxw = w-1, w+2
    for nw in range(minw, maxw):
        for nz in range(z-1, z+2):
            for ny in range(y-1, y+2):
                for nx in range(x-1, x+2):
                    if nw == w and nz == z and ny == y and nx == x:
                        continue
                    if (nx, ny, nz, nw) in active_fields:
                        count += 1
    return count


# checks all 26 neighboring cubes (part1) or 80 cubes (part2)
def update_neighbors(active_fields, active_field, next_active_fields, part2_flag):
    x, y, z, w = active_field
    if part2_flag is False:
        minw, maxw = 0, 1
    else:
        minw, maxw = w-1, w+2
    for nw in range(minw, maxw):
        for nz in range(z-1, z+2):
            for ny in range(y-1, y+2):
                for nx in range(x-1, x+2):
                    current_field = (nx, ny, nz, nw)
                    count = get_active_neighbor_count(active_fields, current_field, part2_flag)
                    if current_field in active_fields:
                        if count == 2 or count == 3:
                            next_active_fields.add(current_field)
                    else:
                        if count == 3:
                            next_active_fields.add(current_field)


def debug_print(cycle, active_fields):
    print("After " + str(cycle) + " cycles:")
    minx, maxx, miny, maxy, minz, maxz = 0, 0, 0, 0, 0, 0
    for item in active_fields:
        minx = min(minx, item[0])
        miny = min(miny, item[1])
        minz = min(minz, item[2])
        maxx = max(maxx, item[0])
        maxy = max(maxy, item[1])
        maxz = max(maxz, item[2])
    for z in range(minz, maxz+1):
        print("z=" + str(z))
        for y in range(miny, maxy+1):
            for x in range(minx, maxx+1):
                if (x, y, z) in active_fields:
                    print("#", end="")
                else:
                    print(".", end="")
            print("")
    print("")


def part1(inputs):
    active_fields = parse_input(inputs)
    for cycle in range(0, 6):
        next_active_fields = set()
        for active_field in active_fields:
            update_neighbors(active_fields, active_field, next_active_fields, False)
        active_fields = next_active_fields
    return len(active_fields)


def part2(inputs):
    active_fields = parse_input(inputs)
    for cycle in range(0, 6):
        next_active_fields = set()
        for active_field in active_fields:
            update_neighbors(active_fields, active_field, next_active_fields, True)
        active_fields = next_active_fields
    return len(active_fields)


def test():
    assert part1(".#.\n..#\n###") == 112
    print("P1 tests passed!")
    assert part2(".#.\n..#\n###") == 848
    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(17)
result = part1(inputs)
common.post_answer(17, 1, result)

result = part2(inputs)
common.post_answer(17, 2, result)
