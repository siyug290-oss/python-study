from models import TodoList


def test_add():
    t = TodoList()
    t.add("买菜")   
    assert t.count() == 1


def test_add_empty():
    t = TodoList()
    t.add("   ")
    assert t.count() == 0


def test_remove_out_of_range():
    t = TodoList()
    t.add("买菜")
    t.remove(99)
    assert t.count() == 1


def test_remove_zero():
    t = TodoList()
    t.add("买菜")
    t.remove(0)
    assert t.count() == 1