import pytest

from src.hydrogen_hub import get_grid_nominal_value, get_csv_data, load_config

def main():
    test_grid_value_input()
    test_get_csv_data()
    test_load_config()


def test_grid_value_input():
    assert get_grid_nominal_value("100")  == 100000000.0
    assert get_grid_nominal_value("500")  == 500000000.0
    assert get_grid_nominal_value("50")  == 50000000.0
    with pytest.raises(SystemExit) as e:
        get_grid_nominal_value("49")
    assert str(e.value) == "Value must be between 50 MW and 500 MW"
    with pytest.raises(SystemExit) as e:
        get_grid_nominal_value("600")
    assert str(e.value) == "Value must be between 50 MW and 500 MW"
    with pytest.raises(SystemExit) as e:
        get_grid_nominal_value("cat")
    assert str(e.value) == "could not convert string to float: 'cat'"
    with pytest.raises(SystemExit) as e:
        get_grid_nominal_value("")
    assert str(e.value) == "could not convert string to float: ''"


def test_get_csv_data():
    example_csv = get_csv_data("U:\\ann82611\\04_Code\\hydrogen_hub\\hydrogen_hub\\example_files_for_unit_tests\\test_get_csv_data.csv", "Solar Power")
    assert example_csv.iloc[0] == 2
    assert example_csv.iloc[1] == 1
    assert example_csv.iloc[2] == 5


def test_load_config():
    example_yaml = load_config("U:\\ann82611\\04_Code\\hydrogen_hub\\hydrogen_hub\\example_files_for_unit_tests\\test_load_config_data.yaml")
    assert example_yaml["test1"] == "cat"
    assert example_yaml["test2"] == 2
    assert example_yaml["test3"] == ""


if __name__ == "__mainn__":
    main()