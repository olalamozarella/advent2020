import common


# check specified rule and add its string to results
def process_rule(rules_dict, rule, results, cache):
    # if current rule contains quotes, add specified character to all results
    if "\"" in rules_dict[rule]:
        character = rules_dict[rule].replace("\"", "")
        if len(results) == 0:
            results.append(character)
        else:
            for i in range(0, len(results)):
                results[i] += character
    # if there is |(or), add a copy of each result
    elif "|" in rules_dict[rule]:
        results1 = results.copy()
        results2 = results.copy()

        sub_rules1 = rules_dict[rule].split("|")[0].split()
        for sub_rule in sub_rules1:
            results1 = process_rule(rules_dict, sub_rule, results1)
        sub_rules2 = rules_dict[rule].split("|")[1].split()
        for sub_rule in sub_rules2:
            results2 = process_rule(rules_dict, sub_rule, results2)
        results = results1 + results2
    # there is no OR, just recurse through all sub-rules
    else:
        sub_rules = rules_dict[rule].split()
        for sub_rule in sub_rules:
            results = process_rule(rules_dict, sub_rule, results)
    return results


# reads all conditions and prepares list of regexes
# returns: [regexes that match input conditions]
def parse_conditions(rules):
    # store rules in dictionary
    rules = rules.split("\n")
    rules_dict = {}
    for rule in rules:
        splitted = rule.split(":")
        rules_dict[splitted[0]] = splitted[1][1:]

    # create list of possible words
    possible = []
    possible = process_rule(rules_dict, "0", possible)
    return possible


# implementation for part 1
# returns: number of rows that match conditions
def part1(inputs):
    splitted = inputs.split("\n\n")
    possible = parse_conditions(splitted[0])

    matching_count = 0
    words = splitted[1].split("\n")
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
    test_inputs = "0: 4 1 5\n1: 2 3 | 3 2\n2: 4 4 | 5 5\n3: 4 5 | 5 4\n4: \"a\"\n5: \"b\""
    calculated = parse_conditions(test_inputs)
    calculated.sort()
    assert calculated == ["aaaabb", "aaabab", "aabaab", "aabbbb", "abaaab", "ababbb", "abbabb", "abbbab"]


# tests for part1 function
def test_part1():
    test_inputs = "0: 4 1 5\n1: 2 3 | 3 2\n2: 4 4 | 5 5\n3: 4 5 | 5 4\n4: \"a\"\n5: \"b\"\n\nababbb\nbababa\nabbbab\naaabbb\naaaabbb"
    assert part1(test_inputs) == 2


# ---------------------------------------- MAIN ---------------------------------------- #
test()

inputs = common.get_input(19)
result = part1(inputs)
common.post_answer(19, 1, result)

# result = part2(inputs)
# common.post_answer(19, 2, result)
