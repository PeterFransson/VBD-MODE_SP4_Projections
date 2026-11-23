import pytest
from pathlib import Path

from hubAdmin.validation import validate_csv

DATA_FOLDER = Path("data")
config_file = "config/validationSchema.json"

@pytest.mark.parametrize(
    "csv_file",
    list(DATA_FOLDER.glob("*.csv")),
    ids=lambda csv_file: csv_file.name
)

def test_csv_validity(csv_file):
    assert validate_csv(config_file,csv_file) is True