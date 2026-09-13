# Python Interview Question Bank — Answers

Concise answers to all 100 questions, organized by topic.

---

## Python Fundamentals

**1. Which characteristics make Python a popular general-purpose programming language?**
Readable syntax, dynamic typing, a huge standard library, cross-platform support, and a massive ecosystem of third-party packages for almost any domain (web, data science, ML, automation).

**2. Describe how Python source code is executed by the interpreter.**
Source (`.py`) is compiled to bytecode (`.pyc`), which the Python Virtual Machine (PVM) then interprets instruction-by-instruction at runtime. This is why Python is often called "interpreted" even though a compile step happens internally.

**3. What is PEP 8, and why does following it matter in real projects?**
PEP 8 is Python's official style guide (naming conventions, indentation, line length, spacing). Following it keeps code readable and consistent across a team, making collaboration and code review much easier.

**4. How does Python manage memory allocation and garbage collection?**
Python uses automatic memory management via reference counting — an object is freed once its reference count hits zero — plus a cyclic garbage collector that detects and cleans up reference cycles that counting alone can't catch.

**5. What built-in data types does Python provide?**
Numeric types (`int`, `float`, `complex`), sequences (`str`, `list`, `tuple`), mappings (`dict`), sets (`set`, `frozenset`), and booleans (`bool`), plus `None`.

**6. How do mutable and immutable objects differ? Give examples of each.**
Mutable objects can be changed in place after creation (`list`, `dict`, `set`); immutable objects cannot — any "change" creates a new object (`int`, `str`, `tuple`, `frozenset`).

**7. How are exceptions raised, caught, and handled in Python?**
Exceptions are raised with `raise`, caught with `try`/`except` blocks, optionally cleaned up with `finally`, and can run alternate code on success with `else`. Custom exceptions are made by subclassing `Exception`.

**8. When would you choose a list instead of a tuple, and vice versa?**
Use a list when the collection needs to change (add/remove/modify items); use a tuple for fixed, unchanging data — tuples are also hashable (if contents are) and slightly faster/more memory-efficient.

**9. How can you create and populate a dictionary in Python?**
Via literal syntax `{"key": "value"}`, the `dict()` constructor, `dict.fromkeys()`, or a dictionary comprehension like `{k: v for k, v in pairs}`. Populate further with `d[key] = value` or `d.update(...)`.

**10. What is the difference between the == operator and the is operator?**
`==` checks value equality (do these objects contain the same data?); `is` checks identity (are these the same object in memory?). Two equal-valued objects can still be different objects, so `==` and `is` can disagree.

---

## Functions and Modules

**11. How are functions defined, called, and used to return values in Python?**
Defined with `def name(params):`, called with `name(args)`, and values are returned with `return`. A function without an explicit `return` implicitly returns `None`.

**12. What is a lambda expression, and when is it useful?**
An anonymous, single-expression function: `lambda x: x * 2`. Useful for short, throwaway functions passed as arguments, e.g. as a `key=` for `sorted()` or `map()`.

**13. What roles do `*args` and `**kwargs` play in function definitions?**
`*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dict. They let a function accept a flexible, variable number of arguments.

**14. What are decorators, and what kinds of problems can they solve?**
Functions that wrap another function to extend its behavior without modifying its code (`@decorator` syntax). Common uses: logging, timing, access control, caching, and validation.

**15. How do you create your own reusable Python module?**
Save functions/classes in a `.py` file, then `import` that file (by its filename without the extension) from another script in the same directory or on the Python path.

**16. How can code in separate modules share configuration or global state safely?**
Common patterns: a dedicated `config` module imported wherever needed, environment variables, or a singleton/settings object — avoiding scattered mutable globals that are hard to track.

**17. Why is the if __name__ == '__main__': pattern commonly used?**
It lets a file be both an importable module and a standalone script — code inside that block only runs when the file is executed directly, not when it's imported elsewhere.

**18. What is a namespace in Python, and how does name lookup work?**
A namespace is a mapping from names to objects (e.g. a module's or function's variables). Lookup follows the LEGB rule: Local → Enclosing → Global → Built-in, searched in that order.

**19. How does Python decide where to search when importing a module?**
It searches, in order: already-imported modules in `sys.modules`, built-in modules, then directories listed in `sys.path` (script's directory, `PYTHONPATH`, and installation-dependent paths).

**20. What makes a collection of modules a Python package?**
A directory containing an `__init__.py` file (implicit namespace packages exist too, without it) alongside one or more module files, allowing dotted-name imports like `package.module`.

---

## Advanced Python Concepts

**21. What is a list comprehension, and how does it compare with a regular loop?**
A concise syntax for building a list in one line: `[x*2 for x in range(5)]`. It's generally more readable and often faster than an equivalent `for` loop with `.append()`.

**22. How does a dictionary comprehension work? Provide a simple use case.**
Same idea as a list comprehension but builds a dict: `{k: v*2 for k, v in d.items()}`. Useful for transforming or filtering an existing mapping in one expression.

**23. What are generators, and how do yield-based functions behave?**
Generators are functions using `yield` instead of `return`; they produce values lazily, one at a time, pausing state between calls. This avoids building the entire result in memory at once.

**24. What options does Python provide for running work concurrently?**
Threading (`threading` module, good for I/O-bound work due to the GIL), multiprocessing (`multiprocessing`, true parallelism for CPU-bound work), and asynchronous programming (`asyncio`).

**25. What are coroutines, and how do they differ conceptually from threads?**
Coroutines are functions (`async def`) that can pause and resume cooperatively at `await` points, running on a single thread via an event loop — unlike threads, there's no OS-level preemptive context switching.

**26. What is the Global Interpreter Lock (GIL), and why does it matter?**
A mutex in CPython ensuring only one thread executes Python bytecode at a time. It simplifies memory management but means threads don't achieve true CPU parallelism — multiprocessing is needed for that.

**27. What practical techniques can improve the performance of a Python program?**
Using built-in functions/libraries (often C-optimized), avoiding unnecessary loops via comprehensions or vectorized NumPy operations, caching results, profiling to find real bottlenecks, and using generators to reduce memory use.

**28. What is a context manager, and how is it used with the with statement?**
An object defining `__enter__`/`__exit__` that manages setup/teardown automatically, e.g. `with open("f") as file:` guarantees the file closes even if an exception occurs.

**29. How can you reduce memory usage in a Python application?**
Use generators instead of lists where possible, `__slots__` on classes to avoid per-instance `__dict__` overhead, process data in chunks, and release references to large objects when no longer needed.

**30. What is monkey patching, and what are its risks?**
Dynamically modifying or replacing a class/module's attributes or methods at runtime. It's powerful for testing (mocking) but risky in production — it can create confusing, hard-to-trace behavior and break with library updates.

---

## Object-Oriented Programming

**31. What is a class in Python, and how is an object created from one?**
A class is a blueprint defining attributes and methods (`class Name:`). An object (instance) is created by calling the class like a function: `obj = Name()`, which triggers `__init__`.

**32. Which object-oriented programming principles does Python support?**
All four classic pillars: encapsulation, inheritance, polymorphism, and abstraction (the last via `ABC`/`abstractmethod`, as we covered earlier).

**33. What is inheritance? Illustrate how a subclass can reuse behavior from a parent class.**
Inheritance lets a class (subclass) derive attributes/methods from another (superclass). E.g. `class Dog(Animal):` reuses `Animal`'s methods automatically, only overriding what needs to differ.

**34. How is encapsulation expressed in Python even without strict private members?**
Python uses naming conventions instead of enforced access control: a single underscore (`_attr`) signals "internal use," and a double underscore (`__attr`) triggers name mangling to discourage accidental access.

**35. How do instance methods, class methods, and static methods differ?**
Instance methods (`self`) operate on a specific object; class methods (`@classmethod`, `cls`) operate on the class itself (e.g. alternate constructors); static methods (`@staticmethod`) take neither and behave like a plain function namespaced inside the class.

**36. What does polymorphism mean in Python?**
The same method call behaves differently depending on the object's actual type — e.g. calling `.who()` on different subclasses (as in your `B`/`C`/`D` example) dispatches to each one's own implementation.

**37. What problem does super() solve in an inheritance hierarchy?**
It lets a subclass call a parent class's method (often `__init__`) without hardcoding the parent's name, which keeps multiple-inheritance chains and refactoring safe and consistent.

**38. What is method resolution order (MRO), and when does it become important?**
MRO is the specific order Python searches classes for a method/attribute, computed via C3 linearization. It matters mainly with multiple inheritance, resolving diamond-shaped hierarchies deterministically (as in your `D(B, C)` example).

**39. What are magic (dunder) methods, and what are some common examples?**
Special methods with double-underscore names that Python calls automatically for built-in syntax/operations: `__init__`, `__str__`, `__eq__`, `__len__`, `__add__`, `__getitem__`.

**40. What techniques can be used to discourage or prevent subclassing of a class?**
Raise an error in `__init_subclass__` if misused, or in modern Python, use `typing.final` (a static-analysis hint) — Python has no true "sealed class" enforcement at runtime by default.

---

## Debugging and Testing

**41. What approaches can you use to debug a Python program?**
Print/logging statements, interactive debuggers (`pdb`, IDE breakpoints), reading tracebacks carefully, and isolating the problem by testing smaller pieces of code independently.

**42. Which tools are commonly used for debugging Python code?**
`pdb` (built-in debugger), IDE debuggers (VS Code, PyCharm), `logging` module, and tools like `ipdb` or `pytest --pdb` for dropping into a debugger on test failure.

**43. What is unit testing, and what should a good unit test verify?**
Testing individual units (functions/methods) in isolation. A good unit test verifies one specific behavior, is repeatable, independent of other tests, and doesn't depend on external state.

**44. How do you create a basic test with Python's unittest framework?**
Subclass `unittest.TestCase`, write methods starting with `test_`, and use assertion methods like `self.assertEqual(a, b)`; run with `python -m unittest`.

**45. What is pytest, and why do many Python projects use it?**
A third-party testing framework that uses plain `assert` statements, requires less boilerplate than `unittest`, and supports powerful fixtures, parametrization, and a large plugin ecosystem.

**46. How can you test a function that changes files, databases, network state, or other external systems?**
Use mocking (`unittest.mock`) to replace the external dependency with a fake, use temporary test databases/files, or use fixtures that set up and tear down isolated test environments.

**47. What is a breakpoint, and how do you use one during debugging?**
A point where execution pauses so you can inspect program state. In Python, insert `breakpoint()` in code (or set one in an IDE) to drop into an interactive debugger at that line.

**48. How do you produce structured application logs in Python?**
Use the `logging` module instead of `print()` — configure loggers, handlers, and formatters, and set severity levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) appropriate to each message.

**49. What are assertions, and when are they appropriate?**
`assert condition, "message"` checks an internal invariant that should always be true; it raises `AssertionError` if false. Appropriate for catching programmer bugs, not for validating user input (assertions can be disabled with `-O`).

**50. What information does a traceback provide, and how do you read it?**
It shows the chain of function calls leading to an exception, listed from the outermost call down to where the error occurred — read from the bottom up to find the actual error and its originating line.

---

## File Handling and Data Processing

**51. What is the recommended way to open and close files in Python?**
Use a `with open(path, mode) as f:` block — it automatically closes the file even if an exception occurs, avoiding resource leaks from forgetting `f.close()`.

**52. What do common file modes such as r, w, a, and b mean?**
`r` = read (default), `w` = write (overwrites/creates), `a` = append (adds to end), `b` = binary mode (combine like `"rb"` or `"wb"` for non-text files).

**53. How do you read from and write to text files?**
Read with `f.read()`, `f.readline()`, or iterate `for line in f:`; write with `f.write(text)` or `f.writelines(list_of_lines)`.

**54. What is CSV data, and how can Python read it?**
Comma-separated values — a simple tabular text format. Python's built-in `csv` module reads/writes it (`csv.reader`, `csv.DictReader`), or `pandas.read_csv()` for larger, more structured workflows.

**55. What is JSON, and how does Python serialize and deserialize it?**
A lightweight, human-readable data-interchange format based on key-value structures. Python's `json` module converts objects to JSON text with `json.dumps()` and back with `json.loads()` (or `.dump()`/`.load()` for files).

**56. How are binary files handled differently from text files?**
Binary mode (`"rb"`/`"wb"`) reads/writes raw bytes without text encoding/decoding or newline translation — required for images, executables, or other non-text formats.

**57. What is pandas, and what kinds of data-processing tasks is it designed for?**
A library providing the `DataFrame` structure for labeled, tabular data — designed for cleaning, filtering, transforming, aggregating, and analyzing structured datasets efficiently.

**58. How can pandas process a dataset in chunks when it is too large to load at once?**
Pass `chunksize=N` to `pd.read_csv()`, which returns an iterator yielding DataFrame chunks that can be processed (and discarded) one at a time instead of loading everything into memory.

**59. Why are NumPy arrays often more efficient than nested Python lists for numerical work?**
NumPy arrays store homogeneous data in contiguous memory and use vectorized, compiled C operations, avoiding the overhead of Python-level loops and per-element type-checking that lists incur.

**60. How can the os and sys modules be used to interact with the operating system and Python runtime?**
`os` handles file/directory operations, environment variables, and paths (`os.path`, `os.listdir`); `sys` exposes interpreter-level details like command-line args (`sys.argv`), the import path (`sys.path`), and `sys.exit()`.

---

## Libraries and Frameworks

**61. What are the main features of the Flask web framework?**
A lightweight, minimalist "micro" web framework: simple routing, Jinja2 templating, built-in dev server, and a design that stays unopinionated — you add extensions (DB, auth) as needed.

**62. What are the basic steps for building a REST API with Flask?**
Create a Flask app instance, define routes with `@app.route()` mapped to HTTP methods (GET/POST/etc.), handle request data, and return JSON responses (often via `flask.jsonify`).

**63. What is Django, and what types of applications is it commonly used to build?**
A full-featured "batteries-included" web framework with a built-in ORM, admin panel, authentication, and templating — commonly used for larger, database-driven web applications.

**64. How do you start a new Django project?**
Install Django, then run `django-admin startproject projectname`, followed by `python manage.py startapp appname` to create individual apps within the project.

**65. What is an ORM, and how does Django's ORM map Python objects to database tables?**
An Object-Relational Mapper lets you interact with a database using Python classes/objects instead of raw SQL. Django models (`class Model(models.Model)`) map to tables, fields map to columns, and instances map to rows.

**66. What is the requests library used for?**
A popular third-party library for making HTTP requests (GET, POST, etc.) with a simpler, more readable API than the built-in `urllib`.

**67. Which Python libraries can be used to create plots and data visualizations?**
Matplotlib (foundational plotting), Seaborn (statistical visualizations built on Matplotlib), and Plotly (interactive, web-based charts).

**68. Which Python libraries are commonly used for machine learning?**
scikit-learn (classical ML algorithms), TensorFlow and PyTorch (deep learning), along with supporting libraries like NumPy and pandas for data handling.

**69. What options exist for scheduling recurring or delayed tasks in Python?**
The `schedule` library or `sched` module for simple in-process scheduling, `APScheduler` for more advanced scheduling, or OS-level tools like cron combined with a script.

**70. What is asyncio, and what kinds of workloads benefit from it?**
Python's built-in library for writing single-threaded concurrent code using `async`/`await` and an event loop. It benefits I/O-bound workloads with lots of waiting (network requests, file I/O) rather than CPU-heavy computation.

---

## Networking and Databases

**71. How can you build a basic socket-based client or server in Python?**
Use the `socket` module: create a socket, `bind()`/`listen()`/`accept()` on the server side, or `connect()` on the client side, then `send()`/`recv()` data over the connection.

**72. What steps are involved in sending a simple HTTP request from Python?**
Typically use `requests.get(url)` or `requests.post(url, data=...)`, then inspect `.status_code` and `.json()`/`.text` on the returned response object.

**73. How do Python applications connect to a relational SQL database?**
Via a database driver/adapter (e.g. `sqlite3`, `psycopg2` for PostgreSQL, `mysql-connector`) to open a connection and cursor, or through a higher-level ORM like SQLAlchemy or Django's ORM.

**74. How do you safely execute SQL queries from Python code?**
Use parameterized queries (placeholders like `?` or `%s`) instead of string-formatting user input directly into SQL, which prevents SQL injection attacks.

**75. What is a NoSQL database, and how might a Python application interact with one?**
A non-relational database (document, key-value, graph, or column-based) like MongoDB or Redis. Python typically interacts via a dedicated client library (e.g. `pymongo` for MongoDB).

---

## Scripting and Automation

**76. How would you identify and automate a repetitive workflow with Python?**
Identify a manual task performed regularly with clear, consistent steps, then script those steps using appropriate libraries (file handling, `requests`, `os`), and schedule it if it needs to run periodically.

**77. How can Python scripts support system-administration tasks?**
Through modules like `os`, `shutil`, and `subprocess` for file management, process control, and running shell commands, enabling automation of backups, monitoring, and deployment tasks.

**78. Which techniques can be used to parse structured and unstructured text files?**
For structured text: built-in parsers (`csv`, `json`) or splitting on known delimiters. For unstructured text: regular expressions, string methods, or NLP libraries for more complex extraction.

**79. How can Python be used to read, modify, and generate CSV files?**
The `csv` module's `reader`/`writer`/`DictReader`/`DictWriter` classes handle reading rows into lists/dicts and writing new rows back out; pandas offers a higher-level alternative for larger datasets.

**80. Which tools can automate browser interactions from Python?**
Selenium and Playwright are the most common — both can launch browsers, click elements, fill forms, and scrape rendered pages programmatically.

---

## Regular Expressions

**81. What are regular expressions, and what kinds of text-processing problems do they solve?**
Patterns describing sets of strings, used for searching, matching, validating, and extracting text — e.g. validating an email format or pulling phone numbers out of a document.

**82. How do you compile and reuse a regular-expression pattern in Python?**
Use `re.compile(pattern)` to create a reusable pattern object, then call `.match()`, `.search()`, or `.findall()` on it — more efficient than recompiling the same pattern repeatedly.

**83. What are some common regex patterns for matching text, numbers, whitespace, or repeated characters?**
`\d` (digit), `\w` (word character), `\s` (whitespace), `.` (any character), `+` (one or more), `*` (zero or more), `{n,m}` (n to m repetitions).

**84. How can regular expressions be used to replace matching text?**
`re.sub(pattern, replacement, text)` finds all matches of `pattern` in `text` and substitutes them with `replacement`, optionally using captured groups in the replacement string.

**85. When is regex a good choice, and when is a parser or another approach better?**
Regex is good for simple, flat pattern matching (validating formats, quick extraction). For nested or highly structured formats (HTML, JSON, code), a dedicated parser is more robust and maintainable.

---

## Environment and Configuration

**86. How do you create and manage an isolated Python environment with venv?**
Create one with `python -m venv env_name`, activate it (`source env_name/bin/activate` on Unix, `env_name\Scripts\activate` on Windows), then install packages that stay isolated to that environment.

**87. What problem does a virtual environment solve, and when should you use one?**
It prevents dependency conflicts between projects by giving each project its own isolated set of installed packages. Use one for essentially every project beyond a quick throwaway script.

**88. How are third-party Python packages installed?**
Typically via `pip install package_name`, which downloads and installs from the Python Package Index (PyPI).

**89. How can a project record and manage its dependencies reproducibly?**
Maintain a `requirements.txt` (via `pip freeze > requirements.txt`) or use a modern dependency manager like Poetry or Pipenv, which lock exact versions for reproducible installs.

**90. What is Docker, and how can it be used to package and run a Python application?**
A containerization platform that packages an application with its dependencies and runtime environment into a portable image, ensuring it runs consistently across machines. A Python app is containerized via a `Dockerfile` specifying the base image, dependencies, and run command.

---

## Python and Data Science

**91. What is data science, and why is Python widely used for it?**
The practice of extracting insights from data using statistics, programming, and domain knowledge. Python is popular due to its readable syntax and mature ecosystem (pandas, NumPy, scikit-learn, visualization libraries).

**92. What steps are commonly used to clean and preprocess raw data in Python?**
Handling missing values, removing duplicates, correcting data types, normalizing/scaling numeric features, and encoding categorical variables — typically done with pandas and scikit-learn utilities.

**93. What is a pandas DataFrame?**
A two-dimensional, labeled data structure (rows and columns) similar to a spreadsheet or SQL table, supporting flexible indexing, filtering, and transformation operations.

**94. How can missing values be detected and handled in pandas?**
Detect with `df.isnull()`/`df.isna()`; handle by dropping (`df.dropna()`) or filling them with a value, mean, or forward/backward fill (`df.fillna()`).

**95. How do you group and aggregate data with pandas?**
Use `df.groupby("column")` followed by an aggregation like `.sum()`, `.mean()`, or `.agg({...})` to compute statistics per group.

---

## Python and Machine Learning

**96. What is scikit-learn, and what parts of the machine-learning workflow does it support?**
A Python library providing a consistent API for classical ML algorithms (classification, regression, clustering), plus tools for preprocessing, model selection, and evaluation.

**97. How can you perform feature selection in a Python machine-learning project?**
Techniques include correlation analysis, scikit-learn's `SelectKBest` or recursive feature elimination (`RFE`), and using feature importance scores from tree-based models.

**98. What is cross-validation, and how is it implemented in Python?**
A technique that splits data into multiple folds, training and validating the model on different combinations to get a more reliable performance estimate. Implemented in scikit-learn via `cross_val_score()` or `KFold`.

**99. How can a trained machine-learning model be saved and loaded later?**
Serialize it with `pickle` or `joblib` (`joblib.dump(model, "model.pkl")`), then reload with `joblib.load("model.pkl")` without retraining.

**100. What are the main stages of training and evaluating a machine-learning model in Python?**
Data collection and cleaning, splitting into train/test sets, choosing and training a model, evaluating it with appropriate metrics, tuning hyperparameters, and finally deploying or saving the trained model.
</file_text>