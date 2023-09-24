import matplotlib.pyplot as plt

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readline().strip().split()
        return [int(item) for item in data]

def subtract_rows(list1, list2):
    return [item1 - item2 for item1, item2 in zip(list1, list2)]

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(' '.join(map(str, data)))

def plot_data(data):
    plt.plot(data)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('dBM')
    plt.grid(True)
    plt.show()

def main():
    try:
        file1_path = 'weights_all_1_filtered.txt' # Input data to subtract from here weights_all_0_filtered.txt
        file2_path = 'weights_all_0_filtered.txt'# Input clk data here - data to be subtracted
        result_path = 'weights_all_1_isolated.txt'

        list1 = read_file(file1_path)
        list2 = read_file(file2_path)

        if len(list1) != len(list2):
            raise ValueError("Files should have the same number of elements")

        result_data = subtract_rows(list1, list2)
        write_file(result_path, result_data)
        print("Subtraction result has been saved")

        plot_data(result_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()