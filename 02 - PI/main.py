# Sivert Utne

import math


def main():
    pi = archimedesPI(number_of_correct_decimals=5)  # 3.14159
    print("Calculated value of pi:", pi)


def archimedesPI(number_of_correct_decimals=5):
    # constant
    DIAMETER = 2

    # Starting values
    number_of_sides = 6
    side_length = 1
    pi_value = 0

    while True:
        # keep track of the previous pi value
        previous_pi_value = pi_value

        # calculate new value of pi
        perimeter_of_polynomial = number_of_sides * side_length
        pi_value = perimeter_of_polynomial / DIAMETER

        # check if we have acheved the requested accuracy
        if abs(pi_value - previous_pi_value) < 0.1.__pow__(number_of_correct_decimals + 1):
            # cut off decimals after the ones that have stabilized, then finish
            pi_value = math.trunc(10.0 ** number_of_correct_decimals * pi_value) / 10.0 ** number_of_correct_decimals

            print(f'{number_of_sides} sides needed for {number_of_correct_decimals} correct decimal places.')
            # 6144 sides needed for 5 correct decimal places.
            return pi_value

        # if accuracy was too low, double number of sides for the next polynomial
        number_of_sides = number_of_sides * 2

        # Find length of new side using pythagoren theorem: hyp^2 = cath1^2 + cath2^2
        cathetus1 = 1 - math.sqrt(1 - (side_length / 2) * (side_length / 2))
        cathetus2 = side_length / 2
        hypotenuse_squared = cathetus1 * cathetus1 + cathetus2 * cathetus2

        side_length = math.sqrt(hypotenuse_squared)


if __name__ == "__main__":
    main()
