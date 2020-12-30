import common


# reads all conditions and prepares list of regexes
# returns: [regexes that match input conditions]
def parse_conditions(inputs):
    return ["aabb", "bbaa"]


# implementation for part 1
# returns: number of rows that match conditions
def part1(inputs):
    return 0


# implementation for part 2
# returns: who knows?
def part2(inputs):
    return 0


# all tests
def test():
    assert test_parse_conditions() is True
    assert test_part1() is True
    print("All tests passed!")


# tests for parse_conditions function
def test_parse_conditions():
    return False


# tests for part1 function
def test_part1():
    return False


# ---------------------------------------- MAIN ---------------------------------------- #
test()

# inputs = common.get_input(19)
# result = part1(inputs)
# common.post_answer(19, 1, result)
#
# result = part2(inputs)
# common.post_answer(19, 2, result)
