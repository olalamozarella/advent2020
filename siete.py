# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# function that reads input and fills bag_dictionary
# returns dictionary containing "bag color":[list of possible bag colors on outside]
def parse_input(inputs):
    return {}  # return empty dict


# function that calculates all possible bag colors on outside
# returns list of all possible bag colors on outside
def calculate_bags(dict, color, result=None):
    if result is None:
        result = set()  # create empty set at the start of recursion
    for outside_color in dict[color]:
        result.add(outside_color)  # add outside color to set
        calculate_bags(dict, outside_color, result)  # recursively continue to outside color
    return result


# test of input parsing
def test():
    test_input = "light red bags contain 1 bright white bag, 2 muted yellow bags.\n"\
                 "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n"\
                 "bright white bags contain 1 shiny gold bag.\n"\
                 "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n"\
                 "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n"\
                 "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n"\
                 "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n"\
                 "faded blue bags contain no other bags.\n"\
                 "dotted black bags contain no other bags.\n"

    # assertions for dictionary keys and values
    bag_dictionary = parse_input(test_input)
    assert len(bag_dictionary) == 9
    assert dict["light red"] == []
    assert dict["dark orange"] == []
    assert dict["bright white"] == ["light red", "dark orange"]
    assert dict["muted yellow"] == ["light red", "dark orange"]
    assert dict["shiny gold"] == ["bright white", "muted yellow"]
    assert dict["dark olive"] == ["shiny gold"]
    assert dict["vibrant plum"] == ["shiny gold"]
    assert dict["faded blue"] == ["muted yellow", "dark olive", "vibrant plum"]
    assert dict["dotted black"] == ["dark olive", "vibrant plum"]

    # todo removeme after Evka finishes parsing implementation
    bag_dictionary["light red"] = []
    bag_dictionary["dark orange"] = []
    bag_dictionary["bright white"] = ["light red", "dark orange"]
    bag_dictionary["muted yellow"] = ["light red", "dark orange"]
    bag_dictionary["shiny gold"] = ["bright white", "muted yellow"]
    bag_dictionary["dark olive"] = ["shiny gold"]
    bag_dictionary["vibrant plum"] = ["shiny gold"]
    bag_dictionary["faded blue"] = ["muted yellow", "dark olive", "vibrant plum"]
    bag_dictionary["dotted black"] = ["dark olive", "vibrant plum"]

    # assertions for bag calculations
    assert len(calculate_bags(bag_dictionary, "light red")) == 0
    assert len(calculate_bags(bag_dictionary, "dark orange")) == 0
    assert len(calculate_bags(bag_dictionary, "dotted black")) == 7
    assert len(calculate_bags(bag_dictionary, "bright white")) == 2
    assert len(calculate_bags(bag_dictionary, "muted yellow")) == 2
    assert len(calculate_bags(bag_dictionary, "shiny gold")) == 4
    assert len(calculate_bags(bag_dictionary, "dark olive")) == 5
    assert len(calculate_bags(bag_dictionary, "vibrant plum")) == 5
    assert len(calculate_bags(bag_dictionary, "faded blue")) == 7

    print("All tests passed!")


# ---------------------------------------- MAIN ---------------------------------------- #
test()  # run the test
