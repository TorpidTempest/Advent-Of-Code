def get_input(text_file: str) -> list[str]:
    """Opens the input data from the input_data directory

    Args:
        text_file (str): filename in the directory

    Returns:
        list[str]: an array of the files lines
    """
    DIRECTORY = "C:\\Users\\lis4d\\Desktop\\python_stuff\\Advent\\input_data\\"
    input_file = open(DIRECTORY + text_file, "r", encoding="utf-8")
    input_data = input_file.read()
    input_list = input_data.splitlines()
    input_file.close()
    return input_list