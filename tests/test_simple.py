import pytest
from pq import PriorityQueue


def test_pop_empty():
    my_pq = PriorityQueue()
    assert len(my_pq) == 0, "Queue must be empty when created"
    with pytest.raises(KeyError):
        my_pq.pop()
        pytest.fail("Popped from empty queue without exception")

    my_pq.add('one')
    my_pq.remove('one')
    assert len(my_pq) == 0, "Queue must be empty"
    with pytest.raises(KeyError):
        my_pq.pop()
        pytest.fail("Popped from empty queue without exception")


def test_remove_empty():
    my_pq = PriorityQueue()
    my_pq.add('hello')
    assert my_pq.pop() == 'hello', "Bad item removed from queue"
    assert len(my_pq) == 0, "Queue must be empty"
    with pytest.raises(KeyError):
        my_pq.remove('hello')
        pytest.fail("Removed from empty queue without exception")


def test_add_pop_one():
    my_pq = PriorityQueue()
    my_pq.add('one')
    assert my_pq.pop() == 'one', "Bad item removed from queue"
    assert len(my_pq) == 0, "Queue must be empty"


def test_remove_unknown():
    my_pq = PriorityQueue()
    my_pq.add('one')
    my_pq.add('two')
    my_pq.remove('one')
    with pytest.raises(KeyError):
        my_pq.remove('three')
        pytest.fail("No exception when removing unknown item")

    my_pq.remove('two')
    with pytest.raises(KeyError):
        my_pq.remove('one')
        pytest.fail("No exception when removing unknown item")


def test_add_pop_few():
    my_pq = PriorityQueue()

    my_pq.add('one')
    my_pq.add('two')

    assert my_pq.pop() == 'one', "Bad item removed from queue"

    my_pq.add('three')
    my_pq.add('four')

    assert my_pq.pop() == 'two', "Bad item removed from queue"
    assert my_pq.pop() == 'three', "Bad item removed from queue"
    assert my_pq.pop() == 'four', "Bad item removed from queue"

    assert len(my_pq) == 0, "Queue must be empty"


def test_add_remove_one():
    my_pq = PriorityQueue()
    my_pq.add('one')
    my_pq.remove('one')
    assert len(my_pq) == 0, "Queue must be empty"


def test_add_pop_few():
    my_pq = PriorityQueue()

    my_pq.add('one')
    my_pq.add('two')

    my_pq.remove('one')

    my_pq.add('three')
    my_pq.add('four')

    my_pq.remove('four')
    my_pq.remove('two')
    my_pq.remove('three')

    assert len(my_pq) == 0, "Queue must be empty"


def test_len():
    my_pq = PriorityQueue()

    for i in range(10):
        my_pq.add(i)

    assert len(my_pq) == 10

    for i in range(5):
        my_pq.remove(i)

    assert len(my_pq) == 5

    for i in range(5):
        my_pq.pop()

    assert len(my_pq) == 0
