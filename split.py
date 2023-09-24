def split_lines_to_files(input_file_path, output_prefix, lines_per_file=30):
    try:
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
        return

    if not lines:
        print("Error: Input file is empty.")
        return

    num_blocks = (len(lines) + lines_per_file - 1) // lines_per_file

    for block_num in range(num_blocks):
        start_idx = block_num * lines_per_file
        end_idx = min((block_num + 1) * lines_per_file, len(lines))
        block_lines = lines[start_idx:end_idx]

        output_file_path = f"{output_prefix}_{block_num + 1}.txt"
        with open(output_file_path, 'w') as output_file:
            output_file.writelines(block_lines)

        print(f"Created file '{output_file_path}' with {len(block_lines)} lines.")


if __name__ == "__main__":
    input_file_path = "0_percent_diff_unaged.txt"  # Replace this with the path to your input file.
    output_prefix = "0_percent_unaged_Data_Part_"  # Replace this with the desired prefix for the output files.

    split_lines_to_files(input_file_path, output_prefix, lines_per_file=30)
