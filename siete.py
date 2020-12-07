# ---------------------------------------- FUNCTIONS ---------------------------------------- #
# function that reads input and fills bag_dictionary
# returns dictionary containing "bag color":[list of possible bag colors on outside]
def parse_input(inputs):
    return {}  # return empty dict


# function that calculates all possible bag colors on outside
# returns list of all possible bag colors on outside
def calculate_bags(color):
    return []  # return empty list


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

    bag_dictionary = {}
    parse_input(test_input)

    # assertions for dictionary keys and values
    assert len(bag_dictionary) == 9
    assert dict["light red"] == []
    assert dict["dark orange"] == []
    assert dict["bright white"] == ["light red", "dark orange"]
    assert dict["muted yellow"] == ["light red", "dark orange"]
    assert dict["shiny gold"] == ["bright white", "muted yellow"]
    assert dict["dark olive"] == ["shiny gold"]
    assert dict["vibrant plum"] == ["shiny gold"]
    assert dict["faded blue"] == ["muted yellow", "vibrant plum"]
    assert dict["dotted black"] == ["dark olive", "vibrant plum"]

    # assertions for bag calculations
    assert len(calculate_bags("light red")) == 0
    assert len(calculate_bags("dark orange")) == 0
    assert len(calculate_bags("bright white")) == 2
    assert len(calculate_bags("muted yellow")) == 2
    assert len(calculate_bags("shiny gold")) == 4
    assert len(calculate_bags("dark olive")) == 5
    assert len(calculate_bags("vibrant plum")) == 5
    assert len(calculate_bags("faded blue")) == 7
    assert len(calculate_bags("dotted black")) == 7


# ---------------------------------------- MAIN ---------------------------------------- #
# run the test
test()
