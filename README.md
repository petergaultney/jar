# jar

Move Python things to other modules, mostly for
backward-compatibility, such as when you want to refactor your code
but still need old pickles to be loadable, or particularly if you need
the new pickles to be byte-for-byte-identical to the old ones.


## installation

😄

You can `pip install jar` if you really want to, but you can also just
copy this public-domain code from `src/jar/__init__.py` directly into
your own project. You can even give it a name you like better.
