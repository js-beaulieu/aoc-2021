from pathlib import Path


def _get_data_path() -> Path:
    """
    Get the default path for the data files
    :return: The default path
    """
    return Path(__file__).parent.parent / "data"


def get_lines(path: Path) -> list[str]:
    """
    Get lines from a file
    :param path: Path to the file to read
    :return: The data as a list, one item per line
    """
    with open(path) as f:
        return [x for x in f.read().splitlines() if x]


def read(filename: str, data_path: Path = _get_data_path()) -> list[str]:
    """
    Read lines from a data file (assuming the file is in `aoc/data`)
    :param filename: The base name of the .txt file in aoc/data
    :param data_path: Override for the assumed data path
    :return: The data as a list, one item per line
    """
    full_path = (data_path / filename).with_suffix(".txt")
    if not full_path.exists():
        raise RuntimeError(f"Data file '{full_path}' does not exist")
    return get_lines(full_path)
