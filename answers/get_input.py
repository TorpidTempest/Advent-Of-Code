def get_input(text_file):
    input_file = open(text_file, "r")
    input_data = input_file.read()
    input_list = input_data.splitlines()
    input_file.close()
    return input_list