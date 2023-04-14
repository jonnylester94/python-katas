
def years_of_growth(starting_population, end_population, growth, net_migration):

    if end_population <= starting_population:
        return 0

    growth_percentage = growth / 100

    count = 0
    while starting_population < end_population:
        starting_population += ((starting_population * growth_percentage) + net_migration)
        count += 1
    return count


# e.g. (1000, 2000, 2, 12) --> 25
# after 1st year: 1000 + (1000 * 0.02) + 12 = ans1
# after 2nd year: ans1 + (ans1 * 0.02) + 12 = ans2
# after 3rd year: ans2 + (ans2 * 0.02) + 12 = ans3


# previous bits of code
    # if difference >= starting_population:
    #     count = 0
    #     while difference <= end_population:
    #         difference += ((difference * growth_percentage) + net_migration)
    #         count += 1
    #     return count
        





