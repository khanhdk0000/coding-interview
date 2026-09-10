# OOP Interview Notes

Cheat sheet for HackerEarth-style OOP MCQs. Question bank is **C++-flavored** (friend
functions, copy constructors, private inheritance) — study in C++ terms even if you
code Python. Python notes at the end.

Study order: **1 → 4 → 5 → 6** first (most questions come from these), then 2, 3, 7, 8, 9, 10.

---

## 1. Four pillars

| Pillar | One-line definition |
|---|---|
| **Encapsulation** | Bundle data + methods together; hide data behind access specifiers |
| **Abstraction** | Hide *implementation*, expose only the interface |
| **Inheritance** | "is-a" — reuse by deriving a new class from a base |
| **Polymorphism** | One interface, many forms; compiler/runtime picks the right behavior |

Encapsulation = hide **data**. Abstraction = hide **implementation**. Most-asked trap.

Docs: [learncpp — Intro to OOP](https://www.learncpp.com/cpp-tutorial/introduction-to-object-oriented-programming/) · [GfG — OOP in C++](https://www.geeksforgeeks.org/cpp/object-oriented-programming-in-cpp/)

---

## 2. Class anatomy

- **class** = blueprint/type. **object** = instance of it.
- **member variable** = data in a class. **member function** = function defined in a class.
- `this` — implicit pointer to the current object; enables method chaining.
- **static member** — one copy shared by all objects, not per-object.
- **const member function** — promises not to modify the object; callable on const objects.

Docs: [cppreference — Classes](https://en.cppreference.com/w/cpp/language/classes) · [learncpp — `this`](https://www.learncpp.com/cpp-tutorial/the-hidden-this-pointer-and-member-function-chaining/) · [learncpp — static members](https://www.learncpp.com/cpp-tutorial/static-member-variables/)

---

## 3. Access specifiers + friend

| Specifier | Accessible from |
|---|---|
| `public` | anywhere |
| `protected` | the class itself + derived classes |
| `private` | the class itself (+ its friends) only |

**friend function** — a non-member function granted the same access as a member: it can
read `private` and `protected` data. Key facts:

- Not a member of the class (no `this`).
- **Not inherited**, not transitive, not reciprocal.
- Deliberately breaks encapsulation — use sparingly.
- `friend` is **not** a type of constructor.

Docs: [cppreference — Access](https://en.cppreference.com/w/cpp/language/access) · [cppreference — friend](https://en.cppreference.com/w/cpp/language/friend) · [learncpp — friend functions](https://www.learncpp.com/cpp-tutorial/friend-non-member-functions/)

---

## 4. Constructors and destructors

**Constructor types:** `default`, `parameterized`, `copy` (+ `move` in C++11).
No such thing as a "friend constructor".

- **Copy constructor** `T(const T&)` — builds a new object from an existing one.
- **Copy constructor vs assignment operator** — ctor constructs a *new* object;
  `operator=` overwrites an *already-constructed* one.
- **Shallow vs deep copy** — shallow copies the pointer (both objects share memory,
  double-free risk); deep copies the pointed-to data. Write a copy ctor when the class
  owns raw memory.
- **Member initializer list** — `T() : a(1), b(2) {}`. Required for const/reference
  members; initializes in declaration order, not list order.

**Destructor** — `~T()`. One per class, no parameters, cannot be overloaded.
Called in reverse order of construction.

**Virtual destructor** — mandatory when deleting a derived object through a base
pointer. Without it, only the base destructor runs → derived resources leak.

Docs: [learncpp — Constructors](https://www.learncpp.com/cpp-tutorial/constructors/) · [learncpp — Copy constructor](https://www.learncpp.com/cpp-tutorial/the-copy-constructor/) · [cppreference — Copy constructor](https://en.cppreference.com/w/cpp/language/copy_constructor) · [learncpp — Virtual destructors](https://www.learncpp.com/cpp-tutorial/virtual-destructors-virtual-assignment-and-overriding-virtualization/)

---

## 5. Inheritance

### Access table — memorize this

| Base member | `public` inherit | `protected` inherit | `private` inherit |
|---|---|---|---|
| `public` | public | protected | **private** |
| `protected` | protected | protected | **private** |
| `private` | inaccessible | inaccessible | inaccessible |

So for `class D : private B` — all three statements are true:
public members of B become private in D, protected members of B become private in D,
and private members of B are never accessible.

Private base members are inaccessible in the derived class — touching them is a
**compile error**.

### Types of inheritance

| Type | Shape | Example |
|---|---|---|
| **Single** | one base, one derived | `class B : public A` |
| **Multiple** | one derived, several bases | `class M : public N, public P` |
| **Multilevel** | chain | `A → B → C` |
| **Hierarchical** | one base, many derived | `A → B`, `A → C` |
| **Hybrid** | mix of the above | — |

There is no "distributive" inheritance.

### Order and pitfalls

- Constructors run **base → derived**. Destructors **derived → base**.
- **Diamond problem** — `D` inherits `B` and `C`, both from `A` → two copies of `A`.
  Fix with `virtual` inheritance (`class B : virtual public A`).

Docs: [learncpp — Intro to inheritance](https://www.learncpp.com/cpp-tutorial/introduction-to-inheritance/) · [learncpp — Inheritance and access specifiers](https://www.learncpp.com/cpp-tutorial/inheritance-and-access-specifiers/) · [learncpp — Multiple inheritance](https://www.learncpp.com/cpp-tutorial/multiple-inheritance/) · [cppreference — Derived classes](https://en.cppreference.com/w/cpp/language/derived_class)

---

## 6. Polymorphism

Polymorphism is what lets the compiler/runtime process objects differently based on
their type or class.

### Compile-time (static binding, early binding)

| Mechanism | Formal name |
|---|---|
| **Function overloading** — same name, different parameter list | **ad-hoc polymorphism** |
| **Operator overloading** | ad-hoc polymorphism |
| **Templates / generics** | **parametric polymorphism** |

Function overloading ≡ ad-hoc polymorphism. Term is Christopher Strachey's.
"Virtual", "transient", and "pseudo" polymorphism are not real terms.

### Runtime (dynamic binding, late binding)

- **Function overriding** — derived class redefines a base `virtual` function.
- **`virtual` functions** — dispatched through the **vtable** (per class) and
  **vptr** (per object). Without `virtual`, the call binds statically to the base version.
- **Subtype / inclusion polymorphism** — via inheritance + base pointers/references.

### Overloading vs overriding vs hiding

| | Signature | Scope | Binding |
|---|---|---|---|
| **Overloading** | must differ | same class | compile-time |
| **Overriding** | must match | base vs derived, base is `virtual` | runtime |
| **Name hiding** | any | derived redeclares a base name | base version hidden, not overridden |

Docs: [learncpp — Function overloading](https://www.learncpp.com/cpp-tutorial/introduction-to-function-overloading/) · [learncpp — Operator overloading](https://www.learncpp.com/cpp-tutorial/introduction-to-operator-overloading/) · [learncpp — Virtual functions](https://www.learncpp.com/cpp-tutorial/virtual-functions/) · [learncpp — The virtual table](https://www.learncpp.com/cpp-tutorial/the-virtual-table/) · [cppreference — virtual](https://en.cppreference.com/w/cpp/language/virtual) · [cppreference — Overload resolution](https://en.cppreference.com/w/cpp/language/overload_resolution)

---

## 7. Abstraction mechanics

- **Pure virtual function** — `virtual void f() = 0;` no body required in the base.
- **Abstract class** — has ≥1 pure virtual function; **cannot be instantiated**.
  Can still have data members and normal methods.
- **Interface class** — abstract class where *all* functions are pure virtual, no data.

Docs: [learncpp — Pure virtual, abstract, interfaces](https://www.learncpp.com/cpp-tutorial/pure-virtual-functions-abstract-base-classes-and-interface-classes/) · [cppreference — Abstract class](https://en.cppreference.com/w/cpp/language/abstract_class)

---

## 8. Object relationships

| Relationship | Meaning | Lifetime | Example |
|---|---|---|---|
| **Composition** | "has-a", owns the part | part dies with whole | `Car` has `Engine` |
| **Aggregation** | "has-a", doesn't own | part outlives whole | `Team` has `Player` |
| **Association** | "uses-a", peers | independent | `Doctor` ↔ `Patient` |
| **Dependency** | transient use | none | `Class` uses `Logger` in one method |
| **Inheritance** | "is-a" | — | `Dog` is an `Animal` |

**Composition is what allows a class object to be used inside another class.**
Not inheritance — that is "is-a".

Principle: **favor composition over inheritance**. Composition is looser coupling and
avoids fragile deep hierarchies.

Docs: [learncpp — Object relationships](https://www.learncpp.com/cpp-tutorial/object-relationships/) · [learncpp — Composition](https://www.learncpp.com/cpp-tutorial/composition/) · [learncpp — Aggregation](https://www.learncpp.com/cpp-tutorial/aggregation/) · [learncpp — Association](https://www.learncpp.com/cpp-tutorial/association/)

---

## 9. Design principles and patterns

**SOLID**

| Letter | Principle | Meaning |
|---|---|---|
| S | Single Responsibility | one class, one reason to change |
| O | Open/Closed | open for extension, closed for modification |
| L | Liskov Substitution | a derived object must work anywhere its base does |
| I | Interface Segregation | many small interfaces beat one fat one |
| D | Dependency Inversion | depend on abstractions, not concretions |

Also: **coupling** (low is good) vs **cohesion** (high is good), DRY.

**Patterns worth knowing for the onsite:** Singleton, Factory, Observer, Strategy,
Decorator, Adapter.

Docs: [Refactoring.Guru — Design pattern catalog](https://refactoring.guru/design-patterns/catalog)

---

## 10. Python-specific OOP

If you interview in Python, the rules differ from C++:

- **No true private.** `_x` is a convention; `__x` triggers name mangling to
  `_ClassName__x` — obfuscation, not enforcement.
- **Duck typing** — behavior over declared type. No interfaces needed for polymorphism.
- **No overloading** — a second `def` with the same name replaces the first.
  Use default args or `functools.singledispatch`.
- **Multiple inheritance + MRO** — resolution order via C3 linearization; inspect with
  `ClassName.__mro__`. `super()` follows the MRO, not just the parent.
- `@staticmethod` (no implicit arg) vs `@classmethod` (gets `cls`) vs instance method (gets `self`).
- `@property` — computed attribute, the Pythonic getter/setter.
- **Abstract classes** — `abc.ABC` + `@abstractmethod`. Instantiating raises `TypeError`.
- **Dunder methods** — `__init__`, `__repr__`, `__str__`, `__eq__`, `__hash__`, `__len__`.
- `__slots__` — drop `__dict__` to cut memory.
- `@dataclass` — auto `__init__`/`__repr__`/`__eq__`.

Docs: [Python — Classes tutorial](https://docs.python.org/3/tutorial/classes.html) · [Python — `abc`](https://docs.python.org/3/library/abc.html) · [Python — Data model (dunders)](https://docs.python.org/3/reference/datamodel.html) · [Python — MRO](https://docs.python.org/3/howto/mro.html)

---

## Questions already seen (HackerEarth practice test)

| # | Question | Answer |
|---|---|---|
| 1 | Concept allowing a class object inside another class | Composition |
| 2 | Not a type of constructor | Friend |
| 3 | Function given same access as methods to private/protected data | Friend |
| 4 | A function defined in a class | Member function |
| 5 | True when a derived class inherits a base class privately | All of these |
| 6 | Synonym for function overloading | Ad-hoc polymorphism |
| 7 | Helps the compiler process objects differently by data type/class | Polymorphism |
| 8 | Not a type of inheritance | Distributive |
| 9 | `class M : public N, public P` is which inheritance | Multiple |
| 10 | Function that throws an error when a class is inherited | Private |

Pattern: definitions, taxonomies, and access rules — not code tracing. Memorize the
tables in sections 3, 5, 6, and 8.
