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

def test_remove_out_of_range_returns_false(tmp_path):
    t = TodoList(tmp_path / "todo.json")
    t.add("买菜")
    assert t.remove(99) is False

def test_remove_ok_returns_true(tmp_path):
    t = TodoList(tmp_path / "todo.json")
    t.add("买菜")
    assert t.remove(1) is True

def test_done_marks_item(tmp_path):
    t = TodoList(tmp_path / "todo.json")
    t.add("买菜")
    t.done(1)
    assert t.items[0]["done"] is True     # ← 真的变成 True 了吗

def test_done_out_of_range_returns_false(tmp_path):
    t = TodoList(tmp_path / "todo.json")
    t.add("买菜")
    assert t.done(99) is False

def test_done_empty_list_returns_false(tmp_path):
    t = TodoList(tmp_path / "todo.json")
    assert t.done(1) is False          # 空列表那一支

def test_undone_clears_item(tmp_path):
    t = TodoList(tmp_path / "todo.json")
    t.add("买菜")
    t.done(1)
    t.undone(1)
    assert t.items[0]["done"] is False