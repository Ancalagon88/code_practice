# Prompt: https://adventofcode.com/2019/day/1
#!/usr/bin/python3
sum_of_fuel = 0
mass_divider = 3
mass_subtractor = 2
attempts = 0
try_limit = 5
fuel_per_module = []


def fuel_calculator(mass):
    fuel = mass/mass_divider
    if mass % mass_divider:
        fuel = int(fuel)
    fuel = fuel - mass_subtractor
    return fuel


def get_number():
    for retries in range(try_limit):
        try:
            whole_number = int(input(
                "Please enter a whole number: "))
        except:
            print("Incorrect input, please enter a whole number using number keys.\n")
            continue
        if isinstance(whole_number, int):
            return whole_number
    else:
        print("\nYou done messed up A-a-ron! (ノಠ益ಠ)ノ彡┻━┻\n")
        exit()


print("How many modules will your space ship have?")
number_of_modules = get_number()

#testing git_python

for module in range(number_of_modules):
    print("\nWhat is the weight of module number {}\n".format(module + 1))
    module_weight = get_number()
    module_fuel_req = fuel_calculator(module_weight)
    fuel_per_module.append(module_fuel_req)

print("The total required fuel for this trip is {}".format(
    int(sum(fuel_per_module))))
