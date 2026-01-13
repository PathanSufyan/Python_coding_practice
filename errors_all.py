

# Absolutely! Let's explore the **types of errors in Python**, understand **why** they occur,
# **where** they happen, and **how to handle them properly** — all with detailed examples.

## 🧨 What Are Errors in Python?

# Errors are problems in a program that **stop execution**. They occur due to:
#
# * Invalid syntax
# * Invalid operations
# * Incorrect logic
# * External factors (like file not found)
#
# Python errors are broadly classified into two types:


## 🧱 1. **Syntax Errors** (Compile-Time Errors)
### 🧾 What?

# * These occur when **Python can't parse** the code because it breaks the **grammar rules**.
# * Detected **before execution**.

### 💥 Example:

print("Hello")  # ❌ Missing closing parenthesis


### ✅ Handling:

# * **Fix the syntax** before running.
# * Can't use `try-except` because program won’t even run.


## 🛠️ 2. **Exceptions** (Runtime Errors)
### 🧾 What?

# * Occur **while the program is running**.
# * Python throws an exception object and **halts execution** unless you handle it.

### 🔍 Common Built-in Exception Types:

# | Exception           | Cause/Reason                                 | Example                         |
# | ------------------- | -------------------------------------------- | ------------------------------- |
# | `ZeroDivisionError` | Division by zero                             | `10 / 0`                        |
# | `TypeError`         | Invalid type operations                      | `'2' + 3`                       |
# | `ValueError`        | Invalid value for a function                 | `int("abc")`                    |
# | `IndexError`        | Accessing out-of-bound list index            | `lst[5]` if `lst = [1,2,3]`     |
# | `KeyError`          | Accessing a non-existent key in a dictionary | `d['missing']`                  |
# | `NameError`         | Using undefined variable                     | `print(x)` without defining `x` |
# | `AttributeError`    | Invalid attribute for object                 | `"abc".append(1)`               |
# | `FileNotFoundError` | File access when file doesn’t exist          | `open('missing.txt')`           |
# | `ImportError`       | Importing a module that doesn't exist        | `import missing_module`         |


## 🧯 How to Handle Exceptions

### ✅ Using `try`...`except`

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


### ✅ Catching Multiple Exceptions

try:
    num = int("abc")
except (ValueError, TypeError) as e:
    print("Error:", e)


### ✅ Using `else` and `finally`

try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)
finally:
    print("This always runs")


## 🔁 Real-Time Scenario Examples

### 🧾 1. File Handling

try:
    with open("data.csv", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found!")


### 🧾 2. Dictionary Key Lookup

user = {"id": 101, "name": "Sufyan"}
try:
    print(user["email"])
except KeyError:
    print("Email key is missing")


### 🧾 3. Custom Exception

class AgeTooSmallError(Exception):
    pass

age = 15
if age < 18:
    raise AgeTooSmallError("Age should be at least 18")


## 📌 Best Practices

# | Practice                        | Reason                                         |
# | ------------------------------- | ---------------------------------------------- |
# | Use specific exceptions         | Avoid catching all errors blindly (`except:`)  |
# | Use `finally` for cleanup       | Always release resources (e.g., close file/db) |
# | Log exceptions (not just print) | Helps in debugging production code             |
# | Avoid using `except:` alone     | It catches system-exiting exceptions too       |
# | Raise exceptions purposefully   | For validation and enforcing constraints       |

## 🚨 What Not to Do

# try:
#     # risky code
# except:
#     pass  # ❌ Bad: Swallows all errors silently


## 🧠 Summary Table

# | Error Type        | Happens When?    | Can Be Handled? | How to Handle        |
# | ----------------- | ---------------- | --------------- | -------------------- |
# | Syntax Error      | Before execution | ❌ No            | Fix code manually    |
# | Runtime Exception | During execution | ✅ Yes           | `try`-`except` block |


