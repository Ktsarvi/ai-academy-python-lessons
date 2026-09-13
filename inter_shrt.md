# Python Interview Prep — Quick Reminders

Condensed cheat-sheet version. One line (or a few key words) per question — for review, not first-time learning.

---

## Topic 1: Fundamentals & Data Types

1. **Basic types**: int, float, bool, str. Dynamically typed = type lives on the object, not the name. Strongly typed = no silent `"3"+3`.
2. **Mutable vs immutable**: mutable changes in place (list/dict/set); immutable makes a new object each "change" (int/str/tuple/frozenset).
3. **Aliasing**: `b = a` → same object, not a copy. Use `.copy()`, `[:]`, or `copy.deepcopy()` for nested.
4. **`==` vs `is`**: value equality vs identity (same object in memory).
5. **list/tuple/dict/set**: list = ordered+mutable; tuple = ordered+immutable+hashable; dict = key lookup O(1); set = unique+fast membership.
6. **Hashability**: dicts/sets need stable hashes → mutable types (list) can't be keys; tuples can, if contents are hashable too.
7. **Membership check**: list `in` = O(n); set/dict `in` = O(1) avg.
8. **String immutability pitfall**: `s += chunk` in a loop = O(n²); fix = collect in list, `"".join()` once.

## Topic 2: Control Structures & Functions

1. **for vs while**: for = known/finite iterable; while = unknown iteration count, condition-driven.
2. Indentation-based blocks, no parens needed. `for/while...else` runs if no `break`. `match/case` (3.10+) = switch-like.
3. **Positional vs keyword args**: order-matched vs name-matched; positional must come before keyword in a call.
4. **Mutable default arg bug**: defaults evaluated once at def-time → shared list across calls. Fix: default `None`, create inside.
5. No `return` → returns `None`.
6. **LEGB**: Local → Enclosing → Global → Built-in.
7. **global/nonlocal**: needed to _assign_ to an outer-scope name (reading doesn't need it); global → module scope, nonlocal → nearest enclosing function.
8. **`*args`/`**kwargs`**: extra positionals → tuple; extra keywords → dict. Order in signature: positional, `\*args`, keyword-only, `\*\*kwargs`.

## Topic 3: Advanced Concepts

1. **List comprehension**: `[expr for x in y if cond]` — concise, often faster (C-level looping).
2. **Dict/set comprehension**: `{k:v for...}` vs `{expr for...}` — same idea, different brackets.
3. **Generator vs return**: `yield` pauses & resumes, keeps state; `return` exits for good.
4. **Why generators save memory**: lazy, one value at a time vs list holding everything at once. Trade-off: single-pass, no len()/indexing.
5. Function w/ `yield` anywhere → generator function. Calling it doesn't run the body — returns a generator object; body runs on `next()`.
6. **Decorator**: wraps a function to add behavior (logging/timing/auth/caching) without touching its source. `@functools.wraps` preserves metadata.
7. **Stacked decorators**: bottom-up wrapping — closest to function wraps first; outermost's logic runs first on call.
8. **List comp vs gen expr**: `[]` eager/reusable vs `()` lazy/one-shot. Pick list if you need len/indexing/reuse; gen if large/one-pass/feeding into sum()/for.

## Topic 4: Modules, Packages, Stdlib

1. **Module** = one `.py` file; split code for organization, reuse, namespacing, testability.
2. **Package** = directory + `__init__.py`; marks it importable, can expose a clean public API.
3. `import module` (prefix needed) vs `from module import name` (no prefix) vs `as alias` (rename).
4. **Stdlib** ships with Python, no install needed: `os`/`sys`, `datetime`, `json`/`csv`, `collections`, `itertools`, `re`, `math`/`random`, `pathlib`.
5. **3rd-party**: on PyPI, `pip install`, usually inside a venv.

## Topic 5: OOP

1. **Class vs object**: blueprint vs concrete instance created by calling the class.
2. **Instance vs class attributes**: per-object (`self.x` in `__init__`) vs shared across all instances (defined in class body).
3. **Inheritance**: subclass reuses/extends parent behavior ("is-a"); `super()` calls parent's version.
4. **Polymorphism**: same method name → different behavior per actual class; Python leans on duck typing.
5. **Composition ("has-a")**: object holds other objects as attributes. "Favor composition over inheritance" — deep hierarchies get rigid/fragile; composition is more flexible/swappable.
6. **@staticmethod vs @classmethod**: static = no implicit arg, plain function in class; classmethod = gets `cls`, used for alt constructors/class state.
7. **@property**: access like an attribute, but runs code — validation on set, computed on get, keeps interface simple. Pair with `@x.setter`.
8. First-param recap: instance method → `self`; classmethod → `cls`; staticmethod → neither.
9. **Dunder methods**: `__init__`, `__str__`, `__repr__`, `__eq__`, `__len__`, `__iter__`/`__next__` — hook into Python's built-in syntax.
10. **Multiple inheritance & MRO**: `class C(A,B)`; MRO (C3 linearization) decides precedence; inspect via `.mro()`/`__mro__`.

## Topic 6: Files & Error Handling

1. `with open(...)` → auto-closes file even on exception (context manager).
2. Modes: `r` read, `w` write/truncate, `a` append, `x` exclusive create, `+b` = binary.
3. **CSV**: `csv.DictReader`/`csv.writer` — handles quoting/escaping properly (unlike raw `.split(",")`).
4. **JSON**: `json.load`/`json.dump` (files) vs `json.loads`/`json.dumps` (strings).
5. **try/except/else/finally**: try = risky code; except = handle specific error; else = runs only if no exception; finally = always runs (cleanup).
6. Catch narrow types, not bare `except:` — hides real bugs, even catches `SystemExit`/`KeyboardInterrupt`.
7. **Custom exceptions**: subclass `Exception`, add data via `__init__` + `super().__init__(msg)`.
8. `raise X from Y` = explicit chaining (shows original cause); bare `raise` in except = re-raise the current exception unchanged.

## Topic 7: REST APIs & HTTP

1. **Methods**: GET (read), POST (create), PUT (replace, idempotent), PATCH (partial update), DELETE (remove).
2. **Status codes**: 200 OK, 400 bad request, 401 unauthorized (no/invalid auth), 404 not found, 500 server error. (403 = forbidden, authenticated but not permitted — don't confuse with 401.)
3. `requests.get(url, params=...)` / `requests.post(url, json=...)`.
4. `.json()` parses response body → dict/list; check status first.
5. `.status_code` (raw int) vs `.ok` (bool, <400) vs `.raise_for_status()` (raises `HTTPError` on 4xx/5xx).
6. `timeout=N` — without it, request can hang forever; raises `Timeout` on expiry.
7. `ConnectionError` = network-level failure (DNS/refused) vs HTTP error = server responded but with bad status. `RequestException` = catch-all.
8. Common headers: `Content-Type`, `Authorization: Bearer <token>`, `Accept` — passed via `headers=`.
