from pathlib import Path


def get_input(*, file_name: str = "", puzzle_number: str | int = 0) -> list[str]:
    """Opens the input data from the input_data directory

    Args:
        text_file (str): filename in the directory

    Returns:
        list[str]: an array of the files lines
    """
    DIRECTORY = Path("C:\\Users\\lis4d\\Desktop\\python_stuff\\Advent\\input_data\\")
    file = DIRECTORY / file_name if file_name else DIRECTORY / f"puzzle{puzzle_number}.txt"
    with open(file, "r", encoding="utf-8") as f:
        input_data = f.read()
        input_list = input_data.splitlines()
    return input_list