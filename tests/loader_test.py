from src.prompt_generator.prompt_generator import load_list

def test_load_list():
    list = load_list("testdata/test.json", str, folder_name="tests")
    assert list == ["test1", "test2", "test3"]