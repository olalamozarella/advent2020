import common


def match(rules_dict, current_rule, word, word_position):
    # if rule contains quotes, check it
    if "\"" in rules_dict[current_rule]:
        if word_position[0] > len(word) - 1:
            return False
        elif word[word_position[0]] == rules_dict[current_rule][1:-1]:
            word_position[0] += 1
            return True
        else:
            return False

    # check all subrules for each part, stop if at least one part matches
    splitted = rules_dict[current_rule].split("|")
    word_position_backup = word_position[0]
    for part in splitted:
        word_position[0] = word_position_backup
        matching_part = True
        for subrule in part.split():
            if match(rules_dict, subrule, word, word_position) is False:
                matching_part = False
                break
        if matching_part:
            return True
    word_position[0] = word_position_backup
    return False


def monster_messages(inputs, part2_flag=False):
    # store rules in dictionary "rule number":[rules]
    splitted = inputs.split("\n\n")
    rules = {}
    for rule in splitted[0].split("\n"):
        tmp = rule.split(":")
        rules[tmp[0]] = tmp[1][1:]

    if part2_flag:
        rules["8"] = "42 | 42 8"
        rules["11"] = "42 31 | 42 11 31"

    # go through all words, check if it is matching rules or not
    matching_count = 0
    for word in splitted[1].split("\n"):
        word_position = [0]
        if match(rules, "0", word, word_position):
            if word_position[0] != len(word):
                continue
            matching_count += 1
    return matching_count


# all tests
def test():
    test_inputs = "0: 3 3 4 4\n1: 3 3 | 4 4\n2: 3 4 | 4 3\n3: \"a\"\n4: \"b\"\n\nababbb\naabb\nbababa\nabbbab\naaabbb\naaaabbb"
    assert monster_messages(test_inputs) == 1
    test_inputs = "0: 1 2\n1: 3 3 | 4 4\n2: 3 4 | 4 3\n3: \"a\"\n4: \"b\"\n\naa\naaab\nbbab\nbababa\nabbbab\naaabbb\naaaabbb"
    assert monster_messages(test_inputs) == 2
    test_inputs = "0: 4 1 5\n4: \"a\"\n1: 2 3 | 3 2\n3: 4 5 | 5 4\n2: 4 4 | 5 5\n5: \"b\"\n\naaaba\nababbb\nbababa\nabbbab\naaabbb\naaaabbb\nababbb"
    assert monster_messages(test_inputs) == 3

    test_inputs = "42: 9 14 | 10 1\n9: 14 27 | 1 26\n10: 23 14 | 28 1\n1: \"a\"\n11: 42 31\n5: 1 14 | 15 1\n19: 14 1 | 14 14\n12: 24 14 | 19 1\n16: 15 1 | 14 14\n31: 14 17 | 1 13\n6: 14 14 | 1 14\n2: 1 24 | 14 4\n0: 8 11\n13: 14 3 | 1 12\n15: 1 | 14\n17: 14 2 | 1 7\n23: 25 1 | 22 14\n28: 16 1\n4: 1 1\n20: 14 14 | 1 15\n3: 5 14 | 16 1\n27: 1 6 | 14 18\n14: \"b\"\n21: 14 1 | 1 14\n25: 1 1 | 1 14\n22: 14 14\n8: 42\n26: 14 22 | 1 20\n18: 15 15\n7: 14 5 | 1 21\n24: 14 1\n\nabbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa\nbbabbbbaabaabba\nbabbbbaabbbbbabbbbbbaabaaabaaa\naaabbbbbbaaaabaababaabababbabaaabbababababaaa\nbbbbbbbaaaabbbbaaabbabaaa\nbbbababbbbaaaaaaaabbababaaababaabab\nababaaaaaabaaab\nababaaaaabbbaba\nbaabbaaaabbaaaababbaababb\nabbbbabbbbaaaababbbbbbaaaababb\naaaaabbaabaaaaababaa\naaaabbaaaabbaaa\naaaabbaabbaaaaaaabbbabbbaaabbaabaaa\nbabaaabbbaaabaababbaabababaaab\naabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"
    assert monster_messages(test_inputs) == 3
    assert monster_messages(test_inputs, True) == 12

    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()

# inputs = common.get_input(19)
# result = monster_messages(inputs)
# print("Result:" + str(result))
# # common.post_answer(19, 1, result)
#
# result = monster_messages(inputs, True)
# common.post_answer(19, 2, result)
