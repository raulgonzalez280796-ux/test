import pytest
from analyzer import get_directory_size, format_size

def test_get_directory_size(tmp_path):
    # Create a temporary file with exactly 10 bytes of data
    test_file = tmp_path / "test_file.txt"
    test_file.write_bytes(b"0123456789")
    
    size = get_directory_size(tmp_path)
    assert size >= 10

def test_format_size():
    assert format_size(1000) == "1000.00 B"
    assert format_size(1024) == "1.00 KB"
    assert format_size(1048576) == "1.00 MB"