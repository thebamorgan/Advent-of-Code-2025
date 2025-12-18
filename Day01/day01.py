pos = 50
count = 0
numRange = list(range(0,99))
file_path = "day01.txt"  # Replace with the actual path to your file

try:
    with open(file_path, 'r') as file:
        for line in file:   
            # Each 'line' variable will contain one line from the file,
            # including the newline character ('\n') at the end.
            # You might want to remove it using .strip() or .rstrip().
            processed_line = line.strip()  # Removes leading/trailing whitespace and newline
            number = int(processed_line[1:])
            direction = processed_line[0]
            if direction == 'R':
                pos += number
            elif direction == 'L':
                pos -= number
            while pos < 0:
                pos += 100
            while pos > 99:
                pos -= 100
            if pos == 0:
                count += 1
            


            print(count,direction, number, pos)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")