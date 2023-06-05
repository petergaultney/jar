from typing import NamedTuple

from pyjar import jar


@jar(".foo")  # used to be foo.Foo
class Foo(NamedTuple):
    a: int


@jar("tests.totally_new")
class Bar(NamedTuple):
    b: int
