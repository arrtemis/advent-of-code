# converter
def converter(value):
    # teach the code what the spelled out numbers will be, and what their numerical equivalent is
    spelled_out_digits = {
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
    # .lower() makes the function case-insensitive and value gives the value
    return spelled_out_digits.get(value.lower(), value)

file_path = "fucked up values.txt"
total_calibration = 0

with open(file_path, 'r') as file:
    for line in file:
        # declare some variables
        first_digit = None
        last_digit_index = None
        converted = ""

        # security guards. job: do spelled out numbers --> numbers, dispell gibberish, allow numbers to pass only
        for i, character in enumerate(line):
            if character.isdigit():
                converted+=character
            if character.isalpha():
                substring = character
                for j in range(i+1, i+5):
                    if j < len(line) and line[j].isalpha():
                        substring += line[j]
                        converted_value = converter(substring)
                        if converted_value.isdigit():
                            converted+=converted_value

        for n, digit in enumerate(converted):
            if first_digit is None:
                first_digit = digit
            last_digit_index = n
        if first_digit is not None and last_digit_index is not None:
            last_digit = converted[last_digit_index]
            calibration = int(first_digit + last_digit)
            total_calibration += calibration

    print(f"Total: {total_calibration}")