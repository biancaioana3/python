from merger import merge_files

file_paths = ['file1.txt', 'file2.txt', 'file3.txt']
output_path = 'merged_output.txt'

separator = '\n\n'

merge_files(file_paths, output_path, separator)
print(f"Files merged successfully. Output saved to '{output_path}'.")
