# **IB Computer Science (2027) – HL OOP Extension Tasksheet**

## **Banking System – Advanced OOP Features (Extension to SL Workbook)**

This tasksheet is an **extension** to the SL Banking OOP workbook. It assumes you have already implemented a working `BankAccount` class with:

* constructor  
* deposit / withdraw / balance access  
* basic validation  
* simple encapsulation

In this document you will extend your banking system while exploring advanced OOP concepts:

* **Inheritance** (B3.2.1)  
* **Polymorphism** (B3.2.2)  
* **Abstraction** (B3.2.3)  
* **Composition & Aggregation** (B3.2.4)  
* **Design Patterns** (B3.2.5)

Example code and UML diagrams use **non‑banking contexts**. Your job is to apply the ideas to the **banking** system yourself.

## 

## **Challenge 6 – Inheritance for Specialised Account Types**

**Specification point: B3.2.1 – Explain and apply the concept of inheritance in OOP to promote code reusability.**

### **6.1 Identify a class hierarchy**

You already have a `BankAccount` class. You will now design **specialised account types** that share its core behaviour but add extra rules or features.

1. Propose at least **two** specialised account types, for example:  
   * `SavingsAccount` (interest, strict withdrawals)  
   * `CurrentAccount` / `CheckingAccount` (overdraft, fees)  
2. For each specialised type, list:  
   * What it **inherits** from the generic `BankAccount`.  
   * What **new attributes** or **new behaviours** it needs.

Write this as short bullet lists.

### **6.2 Design the inheritance structure (UML)**

Draw a small UML diagram that shows a parent–child relationship.

Use this example as a pattern only:

```
-------------------        --------------------
|    Vehicle       |<|-----|   Car            |
-------------------        --------------------
| - speed : Int    |        | - seats : Int    |
-------------------        --------------------
| + move()         |        | + honk()         |
-------------------        --------------------
```

Now create a UML diagram with:

* `BankAccount` as the **parent (superclass)**  
* Your specialised accounts as **children (subclasses)**.

### **6.3 Plan what gets reused and what gets extended**

For each subclass, categorise the methods:

* **Inherited unchanged** from `BankAccount`.  
* **Overridden** (same name, different behaviour).  
* **New methods** (only in that subclass).

Write one paragraph explaining how inheritance:

* Avoids duplicating code.  
* Allows each subclass to enforce different rules.

### **6.4 Implement the hierarchy in code**

Implement your inheritance structure in Python by:

1. Turning `BankAccount` into a clear **base class**.  
2. Creating at least **two subclasses** that `class SubAccount(BankAccount):` from it.  
3. Moving any common logic into `BankAccount` so it is not duplicated.

#### **Example (Shapes)**

```py
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

Use the structure, but apply it to **bank accounts**, not shapes.

## 

## **Challenge 7 – Polymorphism and Method Overriding**

**Specification point: B3.2.2 – Construct code to model polymorphism and its various forms, such as method overriding.**

Polymorphism allows **different classes** to respond to the **same method call** in different ways.

### **7.1 Polymorphic withdrawals**

You should already have subclasses like `SavingsAccount` and `CurrentAccount`.

1. Decide how `withdraw(amount)` should behave **differently** in each subclass. For example:  
   * `SavingsAccount` may not allow overdrafts at all.  
   * `CurrentAccount` may allow an overdraft up to a limit.  
2. Write out (in words) the **withdrawal rule** for each subclass.

### **7.2 Implement method overriding**

Implement `withdraw(self, amount)` in each subclass so that:

* The **method name and parameters** match the parent `BankAccount`.  
* The **behaviour** matches your written rules.  
* Each overridden method still calls any necessary shared logic (if appropriate).

#### **Example (Animal sounds)**

```py
class Animal:
    def speak(self):
        return "(silence)"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

`Dog` and `Cat` both override `speak()`.

### **7.3 Use polymorphism in a collection**

Create a list that holds **different account objects** but treats them all as `BankAccount` references, e.g.

```py
accounts = [
    SavingsAccount(...),
    CurrentAccount(...),
    SavingsAccount(...)
]
```

Write a loop that:

* Calls `withdraw()` on some of these accounts.  
* Prints the result or final balance.

Show that:

* The **same method call** (`withdraw`) produces different behaviours depending on the concrete subclass.

### **7.4 Static polymorphism in Python**

Python doesn’t have classic “overloading” like some languages, but you can use features such as:

* Default parameter values  
* `*args` / `**kwargs`  
* Functions that accept different types (duck typing)

Design and implement **one** example of *static‑style polymorphism* in your banking code, such as:

* A method that can accept **either** a single `amount` or a **list of amounts**.  
* A method that can accept **either** an `account_number` or a full `BankAccount` object.

#### **Example (Logger)**

```py
class Logger:
    def log(self, message, level="INFO"):
        print(f"[{level}] {message}")

logger = Logger()
logger.log("System started")          # uses default level
logger.log("Something odd", "WARN")  # explicit level
```

Explain in a few sentences how your design shows **polymorphic behaviour** and why this helps reuse and flexibility.

## 

## **Challenge 8 – Abstraction and Abstract Accounts**

**Specification point: B3.2.3 – Explain the concept of abstraction in OOP.**

Abstraction focuses on **what** an object does rather than **how** it does it. Abstract classes define a **common interface** for multiple subclasses.

### **8.1 Identify common account behaviour**

Look across all your account types:

* List behaviours that **every account type** must support (for example: deposit, withdraw, get\_balance, show\_details).  
* List behaviours that are **specific** to only some account types (for example: apply\_interest, charge\_overdraft\_fee).

### **8.2 Design an abstract account interface**

Design an abstract base class (e.g. `AbstractAccount`) that:

* Declares the core methods that **all accounts must implement**.  
* Does not provide full concrete implementations for those methods.

Draw a UML diagram **separate** from the SL design, showing:

* `AbstractAccount` at the top (abstract)  
* Your concrete account types inheriting from it

Use this example as a pattern:

```
---------------------------
| <<abstract>> Sensor     |
---------------------------
| - id : String           |
---------------------------
| + read_value()          |
| + calibrate()           |
---------------------------
          ^
          |
---------------------------
| TemperatureSensor       |
---------------------------
| + read_value()          |
| + calibrate()           |
---------------------------
```

### **8.3 Implement abstraction in Python**

Use Python’s `abc` module to define an abstract account type. For example:

```py
from abc import ABC, abstractmethod

class AbstractAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass
```

Your task:

* Create an abstract base class for accounts.  
* Make your concrete account types inherit from it and implement all required abstract methods.

### **8.4 Explain the benefit of abstraction**

Write a short paragraph explaining how abstraction:

* Helps you write **modular**, **replaceable** account types.  
* Supports building features that work with “any account” that follows the abstract interface.

## **Challenge 9 – Building a Multi‑Class Banking System (Aggregation \+ Composition)**

**Specification point: B3.2.4 – Explain the role of composition and aggregation in class relationships.**

In this challenge you will extend your system beyond a single class. You will now:

* Create a **Transaction** class and attach multiple transactions to a single bank account (composition).  
* Create a **Bank** class that manages multiple accounts (aggregation).  
* Understand clearly why one relationship is composition and the other is aggregation.

This redesign mirrors the structure used in the previous specification, but aligns fully with the new B3.2.4 expectations.

---

### **9.1 Composition: The BankAccount → Transaction relationship**

A `Transaction` is tightly coupled to a `BankAccount`. It only makes sense *because* the account exists.

1. **Design the Transaction class**  
   * Choose appropriate attributes:  
     * `transaction_id`  
     * `timestamp` / date string  
     * `amount`  
     * `type` (e.g. "DEPOSIT", "WITHDRAWAL")  
     * optional: description or merchant  
   * Decide whether the transaction should hold a reference back to the account. Write a short justification.  
2. **Implement composition in code** Inside your `BankAccount` class:  
   * Add `self._transactions = []` to store Transaction objects.  
   * Modify `deposit` and `withdraw` so that **every successful operation** creates and stores a `Transaction` object.  
3. **Add a transaction‑history method** Implement a method such as `print_transaction_history()` or `get_transactions()` that outputs all stored transactions in a readable form.  
4. **Explain why this is composition** Write 2–3 sentences explaining why:  
   * A transaction does not make sense without its owning account.  
   * The account *owns* the lifetime of the transactions.

---

### **9.2 Aggregation: The Bank → Accounts relationship**

A `Bank` manages many accounts, but those accounts can still exist independently.

1. **Design the Bank class** Your Bank class should manage multiple accounts. Include:  
   * A collection of accounts (`self.accounts = []` or a dictionary)  
   * Methods such as:  
     * `add_account(account)`  
     * `find_account(account_number)`  
     * `total_funds()`  
     * (optional) `print_all_accounts()`  
2. **Implement aggregation in code**  
   * Create the `Bank` class.  
   * Write the methods listed above.  
   * Ensure that accounts remain valid objects even if they are not part of a Bank.  
3. **Explain why this is aggregation** Write 2–3 sentences explaining why:  
   * A bank *has* accounts, but those accounts do not depend on the Bank for survival.  
   * The accounts can be moved to another Bank or used in isolation.

---

### **9.3 Implementing Inter-Account Transfers (Aggregation \+ Composition)**

Inter-account transfers combine several of your design ideas:

* The **Bank** aggregates multiple accounts and can coordinate between them.  
* Each `BankAccount` uses **composition** to record its own `Transaction` objects.  
1. **Design the transfer behaviour** Decide where the main transfer logic should live. You may choose either:  
   * A method on `Bank`, e.g. `transfer(from_account_number, to_account_number, amount)`; or  
   * A method on `BankAccount`, e.g. `transfer_to(other_account, amount)`.  
2. Write a brief justification of your choice.  
3. **Define the transfer rules** In words, specify the rules for a valid transfer, for example:  
   * The amount must be positive.  
   * The source account must have sufficient available funds (respecting overdraft rules, if any).  
   * Both the debit and credit must succeed, or the whole transfer fails.  
4. **Implement the transfer in code** Implement your chosen transfer method so that it:  
   * Validates the transfer amount.  
   * Attempts to withdraw from the source and deposit into the destination.  
   * Only completes if both operations succeed (no partial state).  
   * Creates two `Transaction` objects:  
     * One of type `"TRANSFER_OUT"` for the source account.  
     * One of type `"TRANSFER_IN"` for the destination account.  
5. **Test the transfer feature** Write a short test script that:  
   * Creates at least two accounts.  
   * Performs several valid and invalid transfers between them.  
   * Prints balances and transaction histories so you can verify correctness.  
6. **Explain the relationships involved** In 3–4 sentences, explain how this feature demonstrates:  
   * Aggregation (the Bank coordinating multiple accounts).  
   * Composition (each account owning its own Transaction objects).

---

### **9.4 UML design for the multi-class system**

Draw a UML diagram showing all three classes and their relationships. Use this example for formatting only:

```
Aggregation (A has B):
Library *---- Book

Composition (A owns B):
House *-◼ Room
```

Your UML must show:

* `Bank` → `BankAccount` (aggregation)  
* `BankAccount` → `Transaction` (composition)  
* Key attributes and important methods in each class (including any transfer-related method)

---

### **9.5 Reflection on system design**

Write a short paragraph explaining:

* How composition and aggregation make your system modular.  
* How splitting the system into smaller classes improves clarity and reusability.  
* How the inter-account transfer feature relies on your relationships and transaction log.  
* How this prepares the system for the abstraction, inheritance, and polymorphism challenges that follow.

## 

## **Challenge 10 – Applying OOP Design Patterns**

– Applying OOP Design Patterns  
**Specification point: B3.2.5 – Explain commonly used design patterns in OOP.**

You will explore **three design patterns** and sketch how they might apply to a banking system:

* Singleton  
* Factory  
* Observer

### **10.1 Singleton pattern**

A **Singleton** ensures there is **only one instance** of a particular class (for example, one global configuration or one logger).

#### **Example (Configuration)**

```py
class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

Your tasks:

1. Explain in your own words why some banking concepts might need **exactly one** instance (examples: central bank rules, global interest rate configuration, audit logger).  
2. Sketch (in pseudocode or simple Python) how you might implement such a singleton in your banking system.

### **10.2 Factory pattern**

A **Factory** creates objects of different types but hides the details from the caller.

#### **Example (Shape factory)**

```py
class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Unknown shape")
```

Your tasks:

1. Design a simple `AccountFactory` that can create different types of accounts (e.g. savings, current) based on input parameters.  
2. Describe how using a factory makes your code easier to extend when you add new account types.

You may implement a basic factory class or a factory **function**.

### **10.3 Observer pattern**

The **Observer** pattern allows objects (observers) to be **notified automatically** when another object (subject) changes state.

#### **Example (Weather station)**

```py
class WeatherStation:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, temperature):
        for obs in self.observers:
            obs.update(temperature)
```

Your tasks:

1. In the banking context, identify at least two potential observers that might want to be notified when something in an account changes (e.g. large withdrawal, low balance).  
2. Sketch a simple design where:  
   * `BankAccount` acts as the **subject**.  
   * One or more notifier classes (e.g. `SmsNotifier`, `EmailNotifier`) act as **observers**.  
3. Write a short explanation (3–4 sentences) of how the observer pattern can improve modularity and flexibility in your system.

### **10.4 Pattern comparison and reflection**

Write a short comparison paragraph:

* Summarise, in 1–2 sentences each, the main purpose of **Singleton**, **Factory**, and **Observer**.  
* Choose one pattern that you think would be **most valuable** in a real banking application and explain why.

## 

## **Optional Extension – Bringing It All Together**

If you have time, try to integrate several of these ideas into a **single prototype**:

* A `Bank` that aggregates multiple abstract-account instances (aggregation).  
* An abstract base account type with multiple concrete subclasses (abstraction \+ inheritance).  
* Polymorphic behaviour for deposits/withdrawals (polymorphism).  
* At least one composed helper object inside an account (composition).  
* One design pattern applied in a simple, working way (singleton, factory, or observer).

Document your final design using:

* A high‑level UML sketch.  
* Short written notes explaining where each specification point B3.2.1–B3.2.5 is demonstrated in your code.

---

### **Optional Extension – Thinking About Persistence (Signposting Only)**

In a real banking system, data must **persist** between program runs. Your prototype currently stores everything in memory, which disappears when the program stops.

You are **not required** to implement persistence here, but think about how you *could* extend your design in the future.

1. **Decide what needs to be saved**  
   * Which objects or data would need to be stored permanently? (Examples: accounts, balances, transaction history.)  
   * At what points in the program would you save or load this data?  
2. **Consider possible storage formats**  
   * Plain text, CSV, or JSON files.  
   * A simple database.  
   * Some form of object serialisation.  
3. **Sketch a persistence boundary**  
   * Which class (or new helper class) would be responsible for talking to permanent storage?  
   * How would your existing classes (Bank, BankAccount, Transaction) **ask** for data to be saved or loaded without knowing the low-level details?  
4. **Reflect briefly**  
   * Write a few sentences on how adding persistence might change your design (for example: additional methods, new classes, or the use of another design pattern such as a repository or data-access layer).

You do not need to write any code for persistence, but this thinking will help you understand how small teaching examples scale towards real applications.

