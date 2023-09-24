import matplotlib.pyplot as plt

input_filename = "clk_Part__2.txt"  # Replace with the name of your input file
output_filename = "clk_avg_p2.txt"  # Replace with the name of the output file

def calculate_column_average(data):
    num_rows = len(data)
    num_cols = len(data[0])
    column_sums = [0] * num_cols

    for row in data:
        for col_idx, cell in enumerate(row):
            try:
                cell_value = float(cell)
                column_sums[col_idx] += cell_value
            except ValueError:
                pass

    column_averages = [round(sum / num_rows) for sum in column_sums]  # Round to the nearest integer
    return column_averages

def parse_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split() for line in lines[1:]]  # Skip the first row

def read_numbers_from_file(file_path):
    arrays_list = []
    with open(file_path, 'r') as file:
    #   lines = file.readlines()[1:]
      for line in file:
            numbers = line.strip().split()
            numbers_array = list(map(float, numbers))
            arrays_list.append(numbers_array)
    return arrays_list

def plot_arrays(arrays_list):
    for i, numbers_array in enumerate(arrays_list, 1):
        plt.figure()
        plt.plot(numbers_array, marker='o')
        plt.title(f"Array {i}")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.grid(True)
    plt.show()

def main():
    data = parse_file(input_filename)
    column_averages = calculate_column_average(data)
    result_row = " ".join(str(avg) for avg in column_averages)
    with open(output_filename, 'w') as output_file:
        output_file.write(result_row)
    print(f"Averages row (excluding the first row) written to '{output_filename}'.")

if __name__ == "__main__":
    main()
    arrays_list = read_numbers_from_file(output_filename)
    # plot_arrays(arrays_list)