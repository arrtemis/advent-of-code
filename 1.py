def convert_to_digits(value):
    spelled_out_digits:{
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    return spelled_out_digits(value.lower(), value)

total_calibration = 0

# point to note: the file has to be in the directory from where the script is called
# file_path = "fucked up values.txt"

file_path = "test_cases.txt"

# iterate over the file for each line in file
with open(file_path, 'r') as file:
    for line in file:
        first_digit = None
        last_digit_index = None

    # keep track of indexes in iteration, i --> index; character --> member of the array
        for i, character in enumerate(line):
            if character.isdigit():
                if first_digit is None:
                    first_digit = character
                last_digit_index = i

    # first and last digits located, proceed to add
        if first_digit is not None and last_digit_index is not None:
            last_digit = line[last_digit_index]
            calibration = int(first_digit + last_digit)
            total_calibration += calibration

    print(f"Total: {total_calibration}")