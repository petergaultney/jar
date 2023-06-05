import pickle
from pathlib import Path

from jar import _absolute_from_relative

from .goo import Bar, Foo

# Foo used to be defined in tests.foo, and I pickled it when it was defined there.
# below you'll see I can now unpickle that 'old' pickle successfully as the new pickle.

_THIS_DIR = Path(__file__).parent


def test_unpickle_old_pickle_from_foo_successfully():
    with open(_THIS_DIR / "foo.pickle", "rb") as f:
        foo = pickle.load(f)
        assert Foo(8) == foo


def test_new_pickle_from_goo_identical_to_old_from_foo():
    assert pickle.dumps(Foo(8)) == open(_THIS_DIR / "foo.pickle", "rb").read()


def test_absolute_modules_work_too():
    assert Bar(9) == pickle.loads(pickle.dumps(Bar(9)))


def test_absolute_from_relative():
    assert "root.gp.first_cousin.second_cousin.second_cousin_once_removed" == _absolute_from_relative(
        "root.gp.parent.self", "..first_cousin.second_cousin.second_cousin_once_removed"
    )

    assert "root.gp" == _absolute_from_relative("root.gp.parent.self", "..")
