from string_utils import StringUtils


utils = StringUtils()

def test_capitilize():
    assert utils.capitilize("леха") == "Леха" #позитив
    assert utils.capitilize("Леха") == "Леха" #позитив

    assert utils.capitilize(" ") == " " #негатив (пробел за место строки)
    assert utils.capitilize("") == ""   #негатив


def test_trim():
    assert utils.trim(" леха") == "леха" #позитив
    assert utils.trim(" леха леха") == "леха леха" #позитив (пробел между строками)

    assert utils.trim("") == "" #негатив


def test_to_list():
    assert utils.to_list("л,е,х,а") == ["л" , "е" , "х" , "а"]  #позитив
    assert  utils.to_list("1,2,3,4") == ["1" , "2" , "3" , "4"] #позитив

    assert utils.to_list("") == [] #негатив


def test_contains():
    assert utils.contains("леха" , "л") is True #позитив
    assert utils.contains("леха", "р") is False #позитив

    assert utils.contains("", "р") is False #негатив


def test_delete_symbol():
    assert utils.delete_symbol("леха", "л") == "еха" #позитив
    assert utils.delete_symbol("леха", "еха") == "л" #позитив

    assert utils.delete_symbol("", "ех") == "" #негатив


def test_starts_with():
    assert utils.starts_with("леха", "л") is True  #позитив
    assert utils.starts_with("леха", "а") is False  #позитив

    assert utils.starts_with("", "а") is False  #негатив


def test_end_with():
    assert utils.end_with("леха", "а") is True #позитив
    assert utils.end_with("леха", "л") is False #позитив

    assert utils.end_with("", "л") is False  #негатив


def test_is_empty():
    assert utils.is_empty("") is True  #позитив
    assert utils.is_empty("  ") is True #позитив (два пробела вместо строки)
    assert utils.is_empty("леха") is False #позитив



def test_list_to_string():
    assert utils.list_to_string(["леха"]) ==  "леха" #позитив
    assert utils.list_to_string(["ле", "ха"], "-") == "ле-ха"  #позитив
    assert utils.list_to_string(["1,2,3,4"]) == "1,2,3,4"  #позитив

    assert utils.list_to_string([""]) ==  "" #негатив