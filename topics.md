# Python Course Study Guide — Topics 1–7

In-depth notes covering all course topics, with explanations and runnable examples.

---

# Topic 1: Python Basics and Data Types

## Core data types

Python has four fundamental scalar types you'll use constantly:

```python
age = 25          # int — whole numbers, arbitrary precision
price = 19.99      # float — decimal numbers (IEEE 754 double precision)
name = "Ali"       # str — text, immutable sequence of characters
is_active = True   # bool — True/False (actually a subclass of int: True == 1)
```

A subtlety worth knowing: `bool` is technically a subclass of `int`. That's why `True + True == 2` works, and why `isinstance(True, int)` returns `True`.

## Mutable vs. immutable

This distinction is one of the most important ideas in Python and explains a huge number of bugs beginners hit.

**Immutable** — once created, the object's value cannot change. Any "modification" actually creates a brand new object:

```python
s = "hello"
s2 = s
s += " world"   # creates a NEW string object
print(s)   # "hello world"
print(s2)  # "hello"  — s2 still points to the original object
```

Immutable types: `int`, `float`, `str`, `bool`, `tuple`, `frozenset`.

**Mutable** — the object can be changed in place, and anything else referencing the same object sees the change:

```python
lst = [1, 2, 3]
lst2 = lst          # lst2 points to the SAME list object
lst.append(4)
print(lst2)          # [1, 2, 3, 4] — lst2 changed too!
```

Mutable types: `list`, `dict`, `set`.

**Why this matters in practice — the classic trap:**

```python
def add_item(item, target=[]):   # DANGER: mutable default argument
    target.append(item)
    return target

print(add_item("a"))   # ['a']
print(add_item("b"))   # ['a', 'b']  — the SAME list is reused across calls!
```

Default argument values are evaluated **once**, at function-definition time, not on every call — so a mutable default is shared across all calls that don't override it. The fix: use `None` as the default and create a fresh list inside:

```python
def add_item(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
```

## Collections: list, tuple, dict, set

| Type    | Ordered?                    | Mutable? | Duplicates?          | Syntax      |
| ------- | --------------------------- | -------- | -------------------- | ----------- |
| `list`  | Yes                         | Yes      | Yes                  | `[1, 2, 3]` |
| `tuple` | Yes                         | No       | Yes                  | `(1, 2, 3)` |
| `dict`  | Yes (insertion order, 3.7+) | Yes      | Unique keys          | `{"a": 1}`  |
| `set`   | No                          | Yes      | No (unique elements) | `{1, 2, 3}` |

**When to choose which:**

- **list** — an ordered, changeable sequence (a shopping cart, a queue of tasks).
- **tuple** — fixed data that shouldn't change (coordinates `(x, y)`, a database row), and it's hashable if its contents are, so it can be used as a dict key.
- **dict** — when you need fast lookup by a key rather than a position (a phone book: name → number).
- **set** — when you need uniqueness and fast membership testing (`x in my_set` is O(1) average, vs O(n) for a list), and don't care about order.

## Aliasing vs. mutation — the trap that trips everyone up

**Aliasing** means two variable names point to the _same_ object in memory — no copying happens on assignment for mutable types.

```python
original = [1, 2, 3]
alias = original          # NOT a copy — same object
alias.append(4)
print(original)            # [1, 2, 3, 4]  — original changed too!
print(original is alias)  # True — same object in memory
```

To actually get an independent copy:

```python
copy1 = original.copy()        # shallow copy
copy2 = original[:]            # shallow copy via slicing
copy3 = list(original)         # shallow copy via constructor

import copy
copy4 = copy.deepcopy(original)  # deep copy — needed for nested mutable structures
```

A **shallow copy** copies the outer container but not nested objects inside it — if you have a list of lists, mutating an inner list still affects both copies. A **deep copy** recursively copies everything, so the two are fully independent.

```python
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0].append(99)
print(nested)   # [[1, 2, 99], [3, 4]] — inner list was shared!
```

---

# Topic 2: Control Structures and Functions

## Control structures

```python
age = 20
if age < 13:
    category = "child"
elif age < 20:
    category = "teen"
else:
    category = "adult"
```

`for` loops iterate over any **iterable** (list, string, range, dict, file, etc.):

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for char in "abc":
    print(char)

for key, value in {"a": 1, "b": 2}.items():
    print(key, value)
```

`while` loops run as long as a condition holds:

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

`break` exits a loop early; `continue` skips to the next iteration; loops can have an `else` clause that runs only if the loop completed _without_ hitting `break`:

```python
for n in range(2, 10):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, "is prime")
```

## Functions: positional vs. keyword arguments

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Ali")                       # positional — "Hello, Ali!"
greet("Ali", "Hi")                  # positional — "Hi, Ali!"
greet(name="Ali", greeting="Hey")   # keyword — order doesn't matter
greet(greeting="Hey", name="Ali")   # same result, reordered
```

- **Positional arguments** are matched to parameters by position/order.
- **Keyword arguments** are matched by name, so order doesn't matter, and it makes call sites more readable for functions with many parameters.
- **Default parameters** (`greeting="Hello"`) make an argument optional — but remember the mutable-default trap from Mövzu 1.

You can force arguments to be keyword-only or positional-only:

```python
def f(a, b, *, c):     # c MUST be passed as a keyword: f(1, 2, c=3)
    pass

def g(a, b, /, c):     # a, b MUST be positional: g(1, 2, c=3)
    pass
```

## Return values

A function without `return` implicitly returns `None`. A function can return multiple values as a tuple:

```python
def divide(a, b):
    return a // b, a % b   # returns a tuple

quotient, remainder = divide(17, 5)
```

## Scope: Local, Global, Nonlocal — the LEGB rule

Python resolves a variable name by searching, in this exact order:

**L**ocal → **E**nclosing → **G**lobal → **B**uilt-in

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)   # "local" — found in Local scope first
    inner()
    print(x)       # "enclosing"

outer()
print(x)           # "global"
```

**Reading** a variable from an outer scope works automatically. **Writing/reassigning** one requires an explicit declaration:

```python
counter = 0

def increment():
    global counter      # without this, counter += 1 would raise UnboundLocalError
    counter += 1

def outer():
    total = 0
    def inner():
        nonlocal total   # needed to modify a variable in the enclosing (not global) scope
        total += 1
    inner()
    inner()
    print(total)   # 2
```

Without `global`/`nonlocal`, assigning to a name inside a function creates a **new local variable** that shadows the outer one, rather than modifying it — a very common source of confusion.

---

# Topic 3: Advanced Python Concepts

## Comprehensions

A comprehension builds a new collection in one concise expression instead of a multi-line loop with `.append()`.

```python
# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]        # with a filter

# Dict comprehension
doubled = {k: v * 2 for k, v in {"a": 1, "b": 2}.items()}

# Set comprehension
unique_lengths = {len(word) for word in ["cat", "dog", "fish"]}
```

**Why use them:** they're more concise, and often faster than an equivalent explicit loop, because the looping happens in optimized C code under the hood rather than interpreted bytecode. The trade-off: very complex nested comprehensions can hurt readability — if it takes more than a glance to understand, a regular loop is often the better (more readable) choice.

## Generators

A generator is a function that produces values **lazily**, one at a time, using `yield` instead of `return`.

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)   # 1, 2, 3, 4, 5, printed one at a time
```

**How it differs from a regular function:** calling `count_up_to(5)` doesn't run the function body immediately — it returns a generator object. Each call to `next()` (implicit in a `for` loop) resumes execution right after the last `yield`, keeping all local variables intact, until the function ends or hits another `yield`.

**How it differs from a list:** a list holds _all_ its values in memory at once. A generator holds only its current state and produces the next value on demand.

```python
# This tries to build a list of 10 million items in memory:
squares_list = [x**2 for x in range(10_000_000)]

# This creates values one at a time as needed, using almost no memory:
squares_gen = (x**2 for x in range(10_000_000))   # generator expression
```

**Memory-saving logic:** this matters enormously for large or infinite data streams — reading a huge log file line by line, or processing an endless sequence — where loading everything into a list at once would exhaust RAM. The cost is that a generator can only be iterated **once**; after it's exhausted, you'd need to create a new one.

## Decorators

A decorator is a function that wraps another function to modify or extend its behavior **without changing its source code**.

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()   # prints: slow_function took 1.0001s
```

`@timer` above `def slow_function():` is just syntactic sugar for:

```python
slow_function = timer(slow_function)
```

**What problems decorators solve:** cross-cutting concerns that would otherwise require repeating the same code in every function — logging, timing, authentication/permission checks, caching (`functools.lru_cache` is a built-in example), and input validation.

---

# Topic 4: Modules, Packages, and the Standard Library

## Splitting code into modules

Any `.py` file is a module. Code in one file can be reused elsewhere via `import`:

```python
# math_utils.py
def add(a, b):
    return a + b

# main.py
import math_utils
print(math_utils.add(2, 3))

# or import specific names directly:
from math_utils import add
print(add(2, 3))
```

This keeps related functionality grouped together, avoids duplicating code, and makes large projects manageable by breaking them into logical, independently testable pieces.

## The role of `__init__.py`

A **package** is a directory containing multiple modules. Adding an `__init__.py` file to that directory tells Python "treat this folder as an importable package":

```
myproject/
    shapes/
        __init__.py
        circle.py
        square.py
    main.py
```

```python
# main.py
from shapes import circle
from shapes.square import Square
```

`__init__.py` can be empty (its mere presence is enough in most cases, and modern Python even supports "namespace packages" without it), but it's commonly used to:

- Run package-initialization code when the package is first imported.
- Control what gets exposed with `from package import *` via an `__all__` list.
- Re-export names from submodules for a simpler public API, e.g. `from .circle import Circle` inside `__init__.py` so users can write `from shapes import Circle` instead of `from shapes.circle import Circle`.

## Python Standard Library

Python ships with a huge collection of built-in modules that solve common problems without needing any third-party install — no `pip install` required:

| Module        | Purpose                                                         |
| ------------- | --------------------------------------------------------------- |
| `os`          | Filesystem paths, environment variables, OS interaction         |
| `sys`         | Interpreter internals, command-line args                        |
| `math`        | Mathematical functions                                          |
| `random`      | Random number generation                                        |
| `datetime`    | Dates and times                                                 |
| `json`        | JSON encoding/decoding                                          |
| `re`          | Regular expressions                                             |
| `collections` | Specialized containers (`Counter`, `defaultdict`, `namedtuple`) |
| `itertools`   | Efficient looping/combinatorics tools                           |

Knowing the standard library well is a real productivity skill — a huge number of "how do I do X in Python" problems already have a built-in, battle-tested solution before you'd need to write your own or reach for a third-party package.

---

# Topic 5: Object-Oriented Programming (OOP)

## Class, object, instance vs. class attributes

```python
class Dog:
    species = "Canis familiaris"    # CLASS attribute — shared by ALL instances

    def __init__(self, name):
        self.name = name              # INSTANCE attribute — unique per object

    def bark(self):
        return f"{self.name} says Woof!"

d1 = Dog("Rex")
d2 = Dog("Fido")
print(d1.species, d2.species)   # same value, shared from the class
print(d1.name, d2.name)          # different values, per instance
```

**Instance attributes** live on the individual object (`self.name`) — each object gets its own copy. **Class attributes** live on the class itself and are shared by every instance, unless an instance explicitly overrides it (which creates a _new_ instance attribute shadowing the class one, rather than modifying the shared value).

```python
d1.species = "Modified"   # this creates a NEW instance attribute on d1 only
print(d1.species)   # "Modified"
print(d2.species)   # "Canis familiaris" — unaffected
print(Dog.species)  # "Canis familiaris" — the class attribute itself is unchanged
```

## Inheritance

**Inheritance** lets one class (the subclass/child) derive attributes and methods from another class (the superclass/parent), so the subclass automatically reuses that behavior instead of rewriting it.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):          # overrides the parent's version
        return "Woof"

d = Dog("Rex")
print(d.eat())      # "Rex is eating." — inherited unchanged from Animal
print(d.speak())     # "Woof" — Dog's own overridden version
```

`Dog` gets `eat()` for free just by inheriting from `Animal` — no need to redefine it. It only needs to write `speak()` because it wants different behavior than the parent's default.

**`super()`** lets a subclass call the parent's version of a method — most commonly `__init__` — without hardcoding the parent class's name:

```python
class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name)     # runs Animal's __init__ to set self.name
        self.indoor = indoor

    def speak(self):
        return "Meow"

c = Cat("Whiskers")
print(c.name, c.speak())   # Whiskers Meow
```

This matters because if you didn't call `super().__init__(name)`, `Cat` would need to duplicate `self.name = name` itself — and if `Animal`'s constructor ever changed, every subclass duplicating that logic would need updating too. `super()` keeps that logic in one place.

## Polymorphism

**Polymorphism** means the same method call behaves differently depending on the actual type of the object it's called on — the caller doesn't need to know or check which specific subclass it's dealing with.

```python
class Animal:
    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

animals = [Cat(), Dog(), Animal()]
for animal in animals:
    print(animal.speak())   # Meow, Woof, ...
```

Notice the loop doesn't contain a single `if isinstance(animal, Cat)` check anywhere — it just calls `.speak()` and trusts that whatever type of object it's holding knows how to respond correctly. This is sometimes summarized as "duck typing" in Python's flexible style: if it walks like a duck and quacks like a duck (i.e. it has the method you're calling), you can treat it like a duck, regardless of its exact class.

**Why this is powerful in real code:** you can add a brand-new subclass, e.g. `Bird`, later on, and the exact same loop above will handle it correctly without any modification — as long as `Bird` also defines `speak()`. This is what makes large systems extensible: new behavior slots in without rewriting the code that consumes it.

## Composition — the alternative to inheritance

**Composition** means building a class out of _other objects_ as attributes, rather than inheriting behavior from a parent class. The relationship is "has-a" instead of "is-a".

```python
class Engine:
    def start(self):
        return "Engine starting..."

class Car:
    def __init__(self):
        self.engine = Engine()   # Car HAS an Engine — composition

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())
```

Compare to inheritance, which would model `Car` as _being_ an `Engine` (which doesn't make conceptual sense — a car isn't a type of engine, it _has_ one).

## "Composition over Inheritance"

This is a well-known OOP design principle: **prefer building functionality by combining smaller, focused objects rather than through deep inheritance hierarchies**, when either approach could work.

**Why inheritance can cause problems:**

- Deep hierarchies become rigid — changing a base class can unexpectedly break many subclasses.
- Multiple inheritance can get genuinely confusing. If a class inherits from two parents that both define the same method, Python has to decide which one "wins" using a fixed search order called the **Method Resolution Order (MRO)**:

```python
class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(A):
    def who(self):
        return "C"

class D(B, C):    # B listed before C
    pass

d = D()
print(d.who())       # "B" — Python finds B's version first
print(D.mro())        # [D, B, C, A, object] — the exact search order
```

Python computes this order (via an algorithm called C3 linearization) once, when the class is defined, so the result is always deterministic. But the fact that a resolution algorithm is needed at all — and that swapping the order to `class D(C, B)` would silently change which method runs — is exactly the kind of subtle complexity that deep or multi-parent inheritance hierarchies introduce.

- "Is-a" relationships don't always hold cleanly in the real world — e.g. is a `Penguin` really a `Bird` if `Bird` has a `fly()` method?

**Why composition is often more flexible:**

- You can swap out a component at runtime (e.g. give a `Car` a different `Engine` object) without restructuring the class hierarchy.
- It avoids forcing an awkward "is-a" relationship where "has-a" fits the real-world concept better.
- It keeps classes smaller and more focused on a single responsibility.

```python
# Flexible: swap engines without touching Car's class definition
class ElectricEngine:
    def start(self):
        return "Silent electric start..."

car.engine = ElectricEngine()
print(car.start())   # "Silent electric start..."
```

This doesn't mean "never use inheritance" — inheritance is still the right tool when there's a genuine, stable "is-a" relationship and you want to guarantee a shared interface across subclasses. A good example is an **abstract base class**, which defines methods that every subclass _must_ implement:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

# shape = Shape()          # TypeError: Can't instantiate abstract class
rect = Rectangle(4, 5)
print(rect.area())          # 20
```

Here, inheriting from `Shape` is exactly the right tool: every shape genuinely "is-a" `Shape`, and `ABC` + `@abstractmethod` guarantees at the language level that no subclass can be created without implementing `area()`. Composition wouldn't fit this use case — there's no natural "has-a" component to hand off to. The principle "favor composition over inheritance" is a _default lean_ when either design could reasonably work — not an absolute rule that rules out inheritance entirely.

## @classmethod, @staticmethod, and @property

```python
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @classmethod
    def margherita(cls):              # alternate constructor
        return cls(["tomato", "mozzarella"])

    @staticmethod
    def is_valid_topping(topping):     # utility function, no access to self or cls
        return topping in ["cheese", "tomato", "mozzarella", "basil"]

    @property
    def topping_count(self):           # computed, read-only attribute
        return len(self.toppings)

p = Pizza.margherita()          # classmethod used as alternate constructor
print(p.topping_count)           # property — accessed like an attribute, no ()
print(Pizza.is_valid_topping("basil"))  # staticmethod — called on the class directly
```

- **`@classmethod`** receives `cls` (the class itself) instead of `self`. Common use: alternate constructors that build an instance a different way.
- **`@staticmethod`** receives neither `self` nor `cls` — it's just a regular function namespaced inside the class for organizational purposes, with no access to instance or class state.
- **`@property`** turns a method into something accessed like a plain attribute (no parentheses), which lets you add validation on write, compute a value lazily on read, or expose a read-only field — all while keeping the external calling code exactly as simple as plain attribute access. This is the "Uniform Access Principle": the caller shouldn't need to know or care whether `obj.value` is a stored field or a method running behind the scenes.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius   # internal storage, underscore signals "internal use"

    @property
    def celsius(self):
        """Getter — runs when you read obj.celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter — runs when you write obj.celsius = ..."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computed, read-only — no setter defined, so it can't be assigned to"""
        return self._celsius * 9/5 + 32

t = Temperature(25)
print(t.celsius)      # 25 — calls the getter, looks like plain attribute access
t.celsius = 100        # calls the setter, validation runs first
print(t.fahrenheit)   # 212.0 — recomputed fresh from _celsius every time, no stored value

t.celsius = -300       # raises ValueError: Temperature below absolute zero
```

Two names are required here — the property `celsius` and the storage variable `_celsius` — because if the property and the underlying storage shared the same name, reading or writing inside the getter/setter would call the property again, and again, infinitely, causing a `RecursionError`.

---

# Topic 6: File Handling and Exception Handling

## File I/O with the `with` statement

```python
# Text file
with open("notes.txt", "r") as f:
    content = f.read()

with open("notes.txt", "w") as f:
    f.write("Hello, file!")

# CSV
import csv
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Ali", 25])

# JSON
import json
with open("data.json", "r") as f:
    data = json.load(f)

with open("data.json", "w") as f:
    json.dump({"name": "Ali", "age": 25}, f)
```

`with` guarantees the file is closed automatically — even if an exception is raised inside the block — because `open()` returns a **context manager**, an object that defines two special methods: `__enter__` (runs at the start of the `with` block) and `__exit__` (runs when the block ends, whether it finished normally or an exception occurred partway through).

```python
class FileOpener:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file            # this becomes the "as f" value

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()            # guaranteed cleanup
        return False                  # False means: don't suppress any exception

with FileOpener("notes.txt", "r") as f:
    content = f.read()
# __exit__ has already run here — the file is closed, even if .read() had raised an error
```

Without `with`, you'd need a manual `try/finally` to guarantee cleanup:

```python
f = open("notes.txt", "r")
try:
    content = f.read()
finally:
    f.close()   # runs even if .read() raises an exception
```

`with FileOpener(...) as f:` does exactly this, but hides the boilerplate behind `__enter__`/`__exit__` — which is _why_ it's the recommended pattern for files, database connections, network sockets, and locks: anything that needs guaranteed cleanup after use.

## Exception handling: try/except/else/finally

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:      # catching multiple exception types
    print(f"Bad input: {e}")
else:
    print("No exception occurred:", result)   # runs ONLY if no exception was raised
finally:
    print("This always runs")                  # cleanup — runs no matter what
```

- **`try`** — code that might raise an exception.
- **`except`** — handles a specific exception type (or a tuple of types).
- **`else`** — runs only if the `try` block completed without raising anything.
- **`finally`** — always runs, whether or not an exception occurred — used for cleanup (closing connections, releasing resources).

## Custom exceptions

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}, balance is only {balance}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)   # "Cannot withdraw 150, balance is only 100"
```

Custom exceptions subclass `Exception` (directly or indirectly), let you attach extra data relevant to the failure (like `balance` and `amount` above), and let calling code catch _your specific_ error type distinctly from generic built-in errors.

---

# Topic 7: REST APIs and HTTP Requests

## HTTP methods

| Method   | Purpose                                      |
| -------- | -------------------------------------------- |
| `GET`    | Retrieve data, no side effects               |
| `POST`   | Create a new resource                        |
| `PUT`    | Replace/update an existing resource entirely |
| `DELETE` | Remove a resource                            |

(A fifth you'll often see alongside these: `PATCH`, for a _partial_ update.)

## HTTP status codes

| Code  | Meaning                                               |
| ----- | ----------------------------------------------------- |
| `200` | OK — request succeeded                                |
| `400` | Bad Request — client sent invalid data                |
| `401` | Unauthorized — missing/invalid authentication         |
| `404` | Not Found — resource doesn't exist                    |
| `500` | Internal Server Error — something broke on the server |

A useful mental grouping: **2xx** = success, **4xx** = client's fault (bad request, missing auth, wrong URL), **5xx** = server's fault.

## Using the `requests` library

```python
import requests

# GET request
response = requests.get("https://api.example.com/users/1")
print(response.status_code)   # 200
data = response.json()         # parses JSON response body into a Python dict/list

# POST request with JSON payload
response = requests.post(
    "https://api.example.com/users",
    json={"name": "Ali", "age": 25}
)

# Query parameters
response = requests.get(
    "https://api.example.com/search",
    params={"q": "python", "limit": 10}
)

# Headers (e.g. authentication)
response = requests.get(
    "https://api.example.com/protected",
    headers={"Authorization": "Bearer YOUR_TOKEN"}
)
```

## Parsing JSON responses

```python
response = requests.get("https://api.example.com/users/1")
if response.status_code == 200:
    user = response.json()
    print(user["name"])
else:
    print(f"Request failed: {response.status_code}")
```

## Handling errors: timeouts and connection errors

Network calls can fail in ways a normal function call never would — the server might be slow, unreachable, or the network might drop entirely. Always wrap requests in error handling:

```python
import requests

try:
    response = requests.get(
        "https://api.example.com/data",
        timeout=5   # seconds — don't wait forever for a response
    )
    response.raise_for_status()   # raises an HTTPError for 4xx/5xx status codes
    data = response.json()

except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Failed to connect — check your network or the server URL")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as e:
    print(f"An unexpected request error occurred: {e}")   # catch-all fallback
```

**Key point:** `response.status_code` being `404` or `500` does **not** automatically raise a Python exception — `requests` will happily return that response object without complaint. You either need to check `response.status_code` manually, or call `response.raise_for_status()`, which converts a bad status code into a raised `HTTPError` you can catch — combining HTTP-level error handling with Python's normal try/except flow.

---

## What to review most carefully before an exam or interview

Based on where students most often stumble:

- Mutable default arguments (Mövzu 1) and aliasing vs. copying
- LEGB scope resolution, especially `nonlocal` vs `global` (Mövzu 2)
- Generators vs. lists — memory behavior, and that generators exhaust after one pass (Mövzu 3)
- Composition vs. inheritance — being able to argue _why_ one fits a given scenario (Mövzu 5)
- `raise_for_status()` vs. manually checking `status_code` (Mövzu 7)
