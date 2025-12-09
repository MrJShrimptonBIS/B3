# **IB Computer Science (2027) – SL OOP Workbook**

## **Banking System – Python Version (Single-Class OOP)**

This workbook is for **independent study** during HL lessons.  
Use your **class notes and slides** to help you. The examples in this booklet use **non-banking contexts** so that you must apply the ideas yourself to a **BankAccount** project.

## 

## **Challenge 1 — Fundamentals of OOP & Real-World Modelling**

**Specification point: B3.1.1 – Evaluate the fundamentals of OOP.**

You will model a **BankAccount** as a real entity using OOP concepts.

### **1.1 Identify attributes (data)**

List at least **three pieces of data** a bank account must store.  
Examples of questions to think about:

* What uniquely identifies the account?  
* What number changes when money is deposited or withdrawn?  
* What information belongs to the account holder?

Write your final list of attributes in bullet form.

### **1.2 Identify behaviours (methods)**

List at least **three actions** a bank account should perform, such as:

* “Add money to the account”  
* “Remove money if there is enough”  
* “Show the current balance”

Write these as method names with a short explanation, e.g.  
`deposit(amount)` – adds the given amount to the balance.

### **1.3 Why is BankAccount a good class?**

In 2–3 sentences, explain:

* Why a BankAccount fits the idea of a **class** in OOP.  
* How **objects** of this class would differ from each other.

### **1.4 Objects (instances) on paper**

Describe **two example accounts** as if they were objects:

* **Account A:**  
  * holder:  
  * account number:  
  * balance:  
  * account type:  
* **Account B:**  
  * holder:  
  * account number:  
  * balance:  
  * account type:

### **1.5 Advantages and disadvantages of OOP**

Using your notes, answer briefly:

1. One **advantage** of using OOP for a banking system.  
2. One **disadvantage** of using OOP for a very small, simple script.

#### **Helpful example (different context)**

This example is about a **GameCharacter**:

```py
class GameCharacter:
    def __init__(self, name, health):
        self.name = name          # attribute
        self.health = health      # attribute

    def take_damage(self, amount):
        self.health -= amount     # behaviour

    def is_alive(self):
        return self.health > 0
```

Use this example to guide the *structure*, then apply the ideas to **BankAccount** yourself.

**Focus for B3.1.1:**

* Understand classes, objects, attributes, methods  
* See where OOP helps and where it might not

## 

## **Challenge 2 — Designing the Class with UML**

**Specification point: B3.1.2 – Construct a design of classes, their methods and behaviour.**

Now you will design your **BankAccount** class using a **UML class diagram** and written requirements.

### **2.1 Requirements from Challenge 1**

From your work in Challenge 1, write:

* A final list of **attributes** (with rough types, e.g. `String`, `Int`, `Float` or Python equivalents).  
* A final list of **methods**, each with:  
  * Name  
  * Parameters  
  * Short purpose (“what it does”).

### **2.2 Draw a UML class box for BankAccount**

Draw a three-part UML box for your **BankAccount**:

1. Class name  
2. Attributes section  
3. Methods section

Use the example below as a **pattern only** (do not copy the content).

#### **Helpful UML example (different context: LibraryBook)**

| `LibraryBook` |
| ----- |
| `- title : String - author : String - pages : Int` |
| `+ read(pagesRead : Int) + getSummary() : String` |

Now create a **BankAccount** UML diagram with your own attributes/methods.

### **2.3 New requirement: track transactions (design only)**

Add this requirement (design stage only):

“A BankAccount should be able to track all transactions in order.”

Update your **attribute list** and **UML diagram** to show how you might support this within a single class for now (for SL, keep a single class; you might, for example, use a list of strings or records).

Briefly explain:

* What new attribute(s) you added.  
* What new method(s) you added or changed.

**Focus for B3.1.2:**

* Designing from requirements  
* Using UML to plan class structure  
* Thinking about future behaviours before coding

## 

## **Challenge 3 — Static vs Non-Static (Class vs Instance)**

**Specification point: B3.1.3 – Distinguish between static and non-static variables and methods.**

In Python:

* **Instance attributes/methods** belong to one object (`self.balance`).  
* **Class attributes/methods** belong to the class as a whole (`BankAccount.bank_name`).

### **3.1 Decide class vs instance attributes**

From your BankAccount design, classify each attribute:

* Which attributes should be **shared by all accounts** (class-level)?  
* Which should be **unique per account** (instance-level)?

For each attribute, write:

* `Class` or `Instance`  
* One sentence justifying your choice.

Examples of thinking (do not copy):

* A bank’s name is usually the same for all accounts → class.  
* A balance is different per account → instance.

### **3.2 Add static features to your design**

Update your **BankAccount UML diagram** to include at least:

* One **class variable** (e.g. a counter or shared setting).  
* One **class method** (e.g. to access the shared data).

You may mark these clearly in your UML (for example by underlining or adding a note “class variable” / “class method”).

#### **Helpful code example (different context: ParkingTicket)**

```py
class ParkingTicket:
    ticket_count = 0      # class variable

    def __init__(self, licence_plate, fine_amount):
        self.licence_plate = licence_plate  # instance variable
        self.fine_amount = fine_amount      # instance variable
        ParkingTicket.ticket_count += 1

    @classmethod
    def get_ticket_count(cls):
        return cls.ticket_count
```

Use the idea, but apply it to **BankAccount** yourself.

### **3.3 Predict program behaviour**

Consider this small example:

```py
class Counter:
    total_created = 0

    def __init__(self):
        self.id = Counter.total_created
        Counter.total_created += 1

a = Counter()
b = Counter()
print(a.id, b.id, Counter.total_created)
```

1. Predict what the output will be.  
2. Explain *why* in terms of:  
   * Instance attributes  
   * Class attributes

**Focus for B3.1.3:**

* Understanding shared vs per-object state  
* Integrating static ideas into your BankAccount design

## 

## **Challenge 4 — Implementing the Class & Creating Objects**

**Specification point: B3.1.4 – Construct code to define classes and instantiate objects.**

Now you will write your **first working Python implementation** of BankAccount.

### **4.1 Write the constructor (`__init__`)**

Implement `__init__` with at least:

* `holder_name`  
* `account_number`  
* `starting_balance`  
* (optional) `account_type`

Rules:

* Store these as **instance attributes** on `self`.  
* Prevent a **negative starting balance** (set to 0 or raise an error – your choice, but be consistent).

### **4.2 Implement core methods**

Add at least these methods:

* `deposit(amount)`  
  * Only allow positive amounts.  
  * Update the balance correctly.  
* `withdraw(amount)`  
  * Only allow withdrawals if there is enough balance.  
  * Otherwise, print or return an error message.  
* `get_balance()`  
  * Return the current balance.

You may add more methods if you wish.

### **4.3 Create and test objects**

In a separate part of your script (outside the class):

* Create **at least three** BankAccount objects with different data.  
* Call your methods to:  
  * Deposit into some accounts  
  * Withdraw from some accounts  
  * Print out the final balance of each account

#### **Helpful example (different context: MusicPlayer)**

```py
class MusicPlayer:
    def __init__(self, volume):
        self.volume = volume      # instance attribute

    def increase_volume(self, amount):
        if amount > 0:
            self.volume += amount

    def decrease_volume(self, amount):
        if 0 < amount <= self.volume:
            self.volume -= amount

    def get_volume(self):
        return self.volume
```

Use this structure as a guide, but build your own **BankAccount** class.

**Focus for B3.1.4:**

* Writing the class in Python  
* Using a constructor to set initial state  
* Creating and using objects in a test program

## 

## **Challenge 5 — Encapsulation & Information Hiding**

**Specification point: B3.1.5 – Explain and apply the concepts of encapsulation and information hiding in OOP.**

Encapsulation bundles data and behaviours.  
Information hiding means controlling how that data is accessed/changed.

Python uses **conventions** to signal access control:

* Public: `balance`  
* “Protected”: `_balance`  
* “Private” (name-mangled): `__balance`

### **5.1 Protect the balance**

Modify your BankAccount class so that:

* The balance attribute is renamed to `_balance` or `__balance`.  
* Direct access from outside the class is discouraged.

Explain briefly:

* Which naming style you chose and why.

### **5.2 Add controlled access methods/properties**

Implement one of these patterns:

**Option A – Getter and setter methods**

```py
def get_balance(self):
    return self._balance

def set_balance(self, new_balance):
    # validate here
    ...
```

**Option B – Property (Pythonic approach)**

```py
@property
def balance(self):
    return self._balance

@balance.setter
def balance(self, new_balance):
    # validate here
    ...
```

Your validation must ensure:

* The balance can never become negative.  
* Any invalid update is rejected or handled safely.

### **5.3 Show how encapsulation helps**

Write two small short-code examples **using your BankAccount class**:

1. An example where a **direct change** to balance (ignoring encapsulation) could cause a problem or inconsistency.  
2. An example where using your **method/property** prevents that problem.

Then write 3–4 sentences explaining:

* How encapsulation improves integrity and security of the account’s state.

#### **Helpful example (different context: TemperatureSensor)**

```py
class TemperatureSensor:
    def __init__(self):
        self.__celsius = 0.0   # private

    def set_temperature(self, value):
        if -50 <= value <= 150:
            self.__celsius = value

    def get_temperature(self):
        return self.__celsius
```

Apply these ideas to **BankAccount**, not to a sensor.

**Focus for B3.1.5:**

* Encapsulating sensitive data  
* Using methods/properties to control changes  
* Explaining why this matters for reliability and security

## 

## **Final Open-Ended SL Challenges (Extension)**

These are **SL-only extensions** for students who finish early or want to deepen their solution using the same single-class BankAccount.

### **Open Challenge A — New Behaviours**

Add at least **three** of the following features to your BankAccount:

* Method to calculate and apply **interest** once per year.  
* Method to **freeze/unfreeze** the account (no operations allowed when frozen).  
* Method to enforce a **daily withdrawal limit**.  
* Method to require a simple **PIN** before withdrawals.  
* Method that returns a **string summary** of the account (for printing in a statement).  
* Simple **console menu** loop to interact with one account.

### **Open Challenge B — Stronger Validation**

Improve your class by:

* Rejecting non-numerical deposit/withdrawal amounts.  
* Handling edge cases (e.g. deposit of 0, negative amounts).  
* Printing or returning clear error messages for invalid operations.

Explain in 2–3 sentences how your validation improves the reliability of the system.

### **Open Challenge C — Mini Simulation**

Write a script that:

1. Creates at least **three** BankAccount objects.  
2. Performs a series of operations (deposits, withdrawals, interest updates, freezes).  
3. Prints a **final summary** for each account, including:  
   * Holder  
   * Account number  
   * Final balance  
   * Any important status (frozen, over limit, etc.)

### **Open Challenge D — Reflection**

Write a short reflection (\~150 words):

* One key design decision (e.g. how you handled withdrawals, how you used a class variable).  
* One way encapsulation made your class safer or easier to maintain.  
* One improvement you would make if you had more time or were allowed to add more classes (HL extension will explore this).

