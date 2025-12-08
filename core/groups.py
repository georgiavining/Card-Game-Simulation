def is_sequence(cards):
    if len(cards) < 3:
        return False

    colour = cards[0].colour
    for c in cards:
        if c.colour != colour:
            return False


    nums = sorted([int(c.number) for c in cards])
    for i in range(len(nums) - 1):
        if nums[i+1] != nums[i] + 1:
            return False

    return True


def is_set(cards):
    if len(cards) < 4:
        return False


    num = cards[0].number
    for c in cards:
        if c.number != num:
            return False


    colours = []
    for c in cards:
        if c.colour in colours:
            return False
        colours.append(c.colour)

    return True


def is_valid_group(cards):
    if is_sequence(cards):
        return "sequence"
    if is_set(cards):
        return "set"
    return None

