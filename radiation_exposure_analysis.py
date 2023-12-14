"""The objective of this program is to input and store radiation data from different environments; and calculate key
summary statistics"""

import statistics


def add_new_level(place):
    """This function takes a location as an input, receives a new value and appends it to the corresponding list of
    radiation levels"""
    while True:
        try:
            level = int(input("What is the new value?\n"))
            break
        except Exception:
            print("You have entered an invalid value. Please try again")
    place_index = locations.index(place)
    return radiation_levels[place_index].append(level)


def summary_statistics(places, levels):
    """This functions works out the average and standard deviation of the radiation levels in each location, prints
    it for the user, and provides a summary of what they mean."""

    # Store the averages and standard deviations in a list to later determine the highest and lowest values
    averages = []
    std = []
    for i, place in enumerate(places):
        average = sum(levels[i]) / len(levels[i])
        averages.append(average)
        std_deviation = statistics.stdev(levels[i])
        std.append(std_deviation)
        print(f"{place.capitalize()}\nAverage Radiation Level = {average:.1f}\nStandard Deviation = "
              f"{std_deviation:.3f}\n")
    highest_average_index = averages.index(max(averages))
    lowest_sd_index = std.index(min(std))
    print(f"\nThe environment with the highest levels of radiation is {locations[highest_average_index].capitalize()}")
    print(f"The environment with the most consistent levels of radiation is {locations[lowest_sd_index].capitalize()}")


locations = ["city centre", "industrial zone", "residential district", "rural outskirts", "downtown"]
radiation_levels = [[22, 19, 20, 31, 28], [35, 32, 30, 37, 40], [15, 12, 18, 20, 14], [9, 13, 16, 14, 7],
                    [25, 18, 22, 21, 26]]

print("This is the initial information:\n")
summary_statistics(locations, radiation_levels)

# Allow the user to enter more information if needed
while True:
    more_info = input("Would you like to enter more information? [Y/N]\n")
    if more_info.upper() not in ["Y", "N"]:
        print("You have entered an invalid choice. Please try again.")
    elif more_info.upper() == "N":
        print("Thank you. Goodbye.")
        break
    elif more_info.upper() == "Y":
        while True:
            area = input("Which environment would you like to add more information about? \nChoose from:\nCity centre\n"
                         "Industrial zone\nResidential district\nRural outskirts\nDowntown\n\n")
            if area.lower() not in locations:
                print("You have entered an invalid choice. Please try again.")
            else:
                add_new_level(area)
                print("This is the updated information:\n")
                summary_statistics(locations, radiation_levels)
                break
