def merge_files(file_paths, output_path, separator='\n'):
    with open(output_path, 'w') as output_file:
        for file_path in file_paths:
            with open(file_path, 'r') as input_file:
                file_content = input_file.read()
                output_file.write(file_content)
                output_file.write(separator)
