__author__ = 'Elliot Hutchins'

# example database item


# empty lists
chipavail = []
chipPlayer = []
ordered_chips = []
final_lists = []

# maximum number of each type of chip to give each person
max_of_chip = 10

# larger number means less big chips
weighted_multiplier = 3
weighted_multiplier2 = 0

# re-order chips from greatest to smallest
def order_chips(ch_value):
    for order in ch_value:
        ordered_chips.append(order[2])
        ordered_chips.sort(reverse=True)
    return ordered_chips


# Find the Chips owned or color, of each owned chip with the chip value
def reverse_lookup_total(chipwanted, wanted):
    for each in chipavail:
        if each[2] == chipwanted:
            return each[wanted]


# Create chips per player list with value per chip
def create_chipPlayer(chipavailable):
    for chips in chipavailable:
        chipPlayer.append([chips, 0])
    return chipPlayer


# calculate the correct chip amount per player
def chip_calculate(value, players):
    create_chipPlayer(order_chips(chipavail))
    total = []
    # calculate the weighted multiplier by using the value as a guide
    if value <= 200:
        weighted_multiplier = 3
        weighted_multiplier2 = (value * .01)
    elif value <= 500:
        weighted_multiplier = 3
        weighted_multiplier2 = (value * .01) - 0.1
    elif value <= 1000:
        weighted_multiplier = 7
        weighted_multiplier2 = (value * .001)
    elif value <= 2000:
        weighted_multiplier = 4
        weighted_multiplier2 = (value * .001)
    elif value <= 3000:
        weighted_multiplier = 4
        weighted_multiplier2 = (value * .001) - .01
    elif value <= 5000:
        weighted_multiplier = 3
        weighted_multiplier2 = (value * .001) - .01
    else:
        weighted_multiplier = 4
        weighted_multiplier2 = (value * .0001) - .001


    for sequence in chipPlayer:
        # counts the existing chips and checks if it will go over the amount desired while also splitting denominations
        while ((sum(total) + sequence[0]) <= value) and (sequence[0] * (sequence[1]) * weighted_multiplier <= value) \
                and sequence[0] * weighted_multiplier2 < value:
            # if we have enough chips available then keep adding, but don't give anymore than max_of_chip per person
            if sequence[1] < max_of_chip and (sequence[1] + 1) * players <= reverse_lookup_total(sequence[0], 1):
                sequence[1] += 1
                total.append(sequence[0])
            else:
                break
    # Print response if the calculator is unable to come up with a good calculation
    if sum(total) < value:
        print "The value per player is too high, and we are unable to optimize a chip list"
        print "The most most efficient chips available per player is: %s" % (round(sum(total) * .01) * 100)
        print "Another option is to change maximum chips of each color per player"

    return chipPlayer, sum(total),

# creates the final list
def final_list(value, players, chiptable):
    chipavail.append(chiptable)
    chip_calculate(value, players)
    for each in chipPlayer:
        final_lists.append([each[1], reverse_lookup_total(each[0], 0)])
    return final_lists


# 8 available options:
# 200
# 500
# 1,000
# 2,000
# 3,000
# 5,000
# 10,000
# 20,000








