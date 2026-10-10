from models import TodoList


def test_add(tmp_path):
    t = TodoList(tmp_path / "todo.json")
    t.add("买菜")   
    assert t.count() == 1


def test_add_empty(tmp_path):
    t = TodoList(tmp_path / "todo.json")
    t.add("   ")
    assert t.count() == 0


def test_remove_out_of_range(tmp_path):
    t = TodoList(tmp_path / "todo.json")
    t.add("买菜")
    t.remove(99)
    assert t.count() == 1


def test_remove_zero(tmp_path):
    t = TodoList(tmp_path / "todo.json")
    t.add("买菜")
    t.remove(0)
    assert t.count() == 1