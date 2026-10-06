from lib.most_often import MostOften


def test_add_new_item():
    most_often = MostOften([])
    most_often.add_new("Item 1")
    assert most_often.starting_list == ["Item 1"]


def test_add_multiple_items():
    most_often = MostOften(["Item 1"])
    most_often.add_new("Item 2")
    most_often.add_new("Item 3")
    assert most_often.starting_list == ["Item 1", "Item 2", "Item 3"]


def test_get_most_often_clear_winner():
    most_often = MostOften(["Item 1", "Item 1", "Item 2"])

    assert most_often.get_most_often() == "Item 1"


def test_get_most_often_no_clear_winnder():
    most_often = MostOften(["Item 1", "Item 1", "Item 2", "Item 2"])

    assert most_often.get_most_often() == "no clear winner"
