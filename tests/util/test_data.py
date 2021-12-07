import pytest
from pathlib import Path
from aoc.util.data import get_lines, read


EXPECTED_OUTPUT = ["entry1", "entry2", "entry3", "entry4"]


class TestGetLines:
    test_file = (Path(__file__).parent / Path(__file__).name).with_suffix(".txt")

    def test_returns_a_list_of_lines(self) -> None:
        assert get_lines(self.test_file) == EXPECTED_OUTPUT


class TestRead:
    mock_data_path = Path(__file__).parent

    def test_reads_the_right_file(self) -> None:
        assert read("test_data", self.mock_data_path) == EXPECTED_OUTPUT

    def test_raises_error_when_files_does_not_exist(self) -> None:
        with pytest.raises(RuntimeError) as r:
            read("X_NOT_EXISTS_X", self.mock_data_path)
