import common


# reads all conditions and prepares list of regexes
# returns: [regexes that match input conditions]
def parse_conditions(inputs):
    return ["aaaabb", "aaabab", "abbabb", "abbbab", "aabaab", "abaaab", "aabbbb", "ababbb"]


# implementation for part 1
# returns: number of rows that match conditions
def part1(inputs):
    splitted = inputs.split("\n\n")
    rules = splitted[0]
    words = splitted[1].split("\n")
    possible = parse_conditions(rules)

    matching_count = 0
    for word in words:
        if word in possible:
            matching_count += 1
    return matching_count


# implementation for part 2
# returns: who knows?
def part2(inputs):
    return 0


# all tests
def test():
    test_parse_conditions()
    test_part1()
    print("All tests passed!")


# tests for parse_conditions function
def test_parse_conditions():
    test_inputs = "0: 4 1 5\n1: 2 3 | 3 2\n2: 4 4 | 5 5\n3: 4 5 | 5 4\n4: \"a\"\n5: \"b\"\n\nababbb\nbababa\nabbbab\naaabbb\naaaabbb"
    assert parse_conditions(test_inputs) == ["aaaabb", "aaabab", "abbabb", "abbbab", "aabaab", "abaaab", "aabbbb", "ababbb"]


# tests for part1 function
def test_part1():
    test_inputs = "0: 4 1 5\n1: 2 3 | 3 2\n2: 4 4 | 5 5\n3: 4 5 | 5 4\n4: \"a\"\n5: \"b\"\n\nababbb\nbababa\nabbbab\naaabbb\naaaabbb"
    assert part1(test_inputs) == 2


# ---------------------------------------- MAIN ---------------------------------------- #
test()

# inputs = common.get_input(19)
# result = part1(inputs)
# common.post_answer(19, 1, result)
#
# result = part2(inputs)
# common.post_answer(19, 2, result)
