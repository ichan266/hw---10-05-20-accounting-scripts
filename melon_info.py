"""Print out all the melons in our inventory."""
# Need to keep track of flesh color, rind color, and average weight

from melons import melon


# def print_melon(melon_attribute):
#     """Print each melon with corresponding attribute information."""




for melon_name in melon:
    print(melon_name.upper())
    for key, value in melon[melon_name].items():
        print(f"    {key}: {value}")





#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
