def generate_zeros_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            data = f.read()

        num_zeros = len(data)//2
        zeros = "0 " * num_zeros

        with open(output_file, 'w') as f:
            f.write(zeros)

        print("Zeros generated successfully! Output saved to:", output_file)
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    input_file = "10_perc_unaged_filtered.txt"  # Replace with the path to your input file
    output_file = "0_matrix_split.txt"  # Replace with the desired output file path

    generate_zeros_file(input_file, output_file)