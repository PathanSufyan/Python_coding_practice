

# Certainly! Let's go **step-by-step** through **file handling in Python** with **concepts, syntax, modes, examples**,
# and **best practices**.

## 📁 What Is File Handling?

# File handling in Python allows you to:
# * **Create**, **read**, **write**, and **delete** files on your system.
# * Work with files such as **text**, **CSV**, **JSON**, etc.
# * Handle external data sources (logs, configs, datasets, etc.)


## 🧱 Basic Steps in File Handling
# 1. **Open** a file
# 2. **Read** or **write** to the file
# 3. **Close** the file
# Or use a **`with` block** to handle files safely (automatically closes).


## 🔧 1. Opening a File
### ✅ Syntax:
file = open("filename.txt", "mode")


### 🔁 Modes in Python:
# | Mode  | Name   | Description                                |
# | ----- | ------ | ------------------------------------------ |
# | `'r'` | Read   | Default mode. Fails if file doesn't exist  |
# | `'w'` | Write  | Creates file or truncates existing file    |
# | `'a'` | Append | Creates file or adds content at the end    |
# | `'x'` | Create | Fails if file already exists               |
# | `'b'` | Binary | Used with images, audio, etc. (`rb`, `wb`) |
# | `'t'` | Text   | Default mode (use with others like `rt`)   |

## 📖 2. Reading from a File

### ✅ Methods:
# | Method        | Description                     |
# | ------------- | ------------------------------- |
# | `read()`      | Reads entire file as one string |
# | `readline()`  | Reads one line at a time        |
# | `readlines()` | Returns list of lines           |

### 📦 Example:
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()


### ✅ Better Way: Using `with`
with open("example.txt", "r") as file:
    print(file.read())


## ✍️ 3. Writing to a File

### ✅ `write()` method
with open("output.txt", "w") as f:
    f.write("Hello World\n")
    f.write("This is a second line")


# * `'w'` mode overwrites existing content
# * `'a'` mode appends to the end of file


## 🧪 4. Checking If File Exists
import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File not found")


## 🧹 5. Deleting a File

import os

if os.path.exists("delete_me.txt"):
    os.remove("delete_me.txt")
else:
    print("File doesn't exist")


## 🧊 6. Working with Binary Files

### ✅ Writing Images, PDFs, etc.

with open("image.jpg", "rb") as img:
    data = img.read()

with open("copy.jpg", "wb") as out:
    out.write(data)


## 🛡️ 7. Exception Handling in File I/O

try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("Error reading file.")


## 📘 Real-Time Scenarios
# | Use Case                   | Example                        |
# | -------------------------- | ------------------------------ |
# | Log file processing        | `with open("app.log")`         |
# | Saving user input          | `open("userdata.txt", "w")`    |
# | Reading config/settings    | `config = open("config.json")` |
# | Parsing CSV/Excel/JSON     | `csv.reader`, `json.load`      |
# | Reading files line by line | `for line in file:`            |


## 🧠 Best Practices
# * Always use `with open(...)` — it automatically handles closing
# * Use `'b'` mode for binary files
# * Use exception handling (`try-except`) to avoid crashes
# * Close files manually if not using `with`


## 🧪 Advanced: Working with `os`, `shutil`, and `pathlib`
# * `os.path.exists()` → Check if file exists
# * `os.remove()` → Delete file
# * `os.rename()` → Rename file
# * `shutil.copy()` → Copy files
# * `pathlib.Path("file").read_text()` → Cleaner way to read files


## ✅ Summary Table

# | Operation     | Code Example                          |
# | ------------- | ------------------------------------- |
# | Open file     | `open("file.txt", "r")`               |
# | Read file     | `read()`, `readline()`, `readlines()` |
# | Write file    | `write()`                             |
# | Append file   | `open(..., "a")`                      |
# | Safe handling | `with open(...) as f:`                |
# | Check exists  | `os.path.exists()`                    |
# | Delete file   | `os.remove()`                         |


##############################################################
##############################################################

# # Creating the sample files with the specified contents
#
# # 1. sample.txt
# sample_txt_content = """Hello, this is a valid line.
# 12345
# !@#$%^&*()
# This line is fine.
# Bad line with \\x00 null char
# Another good line.
# """
#
# # 2. sample.csv
# sample_csv_content = """name,age,email
# Alice,30,alice@example.com
# Bob,notanumber,bob@example.com
# ,25,charlie@example.com
# Diana,40,diana@example
# Eve,35,eve@example.com
# """
#
# # 3a. sample.jsonl
# sample_jsonl_content = """{"name": "Alice", "age": 30, "email": "alice@example.com"}
# {"name": "Bob", "age": "notanumber", "email": "bob@example.com"}
# {"name": "Charlie", "age": 25, "email": "charlie@example.com"}
# INVALID JSON LINE
# {"name": "Diana", "age": 40, "email": "diana@example"}
# {"name": "Eve", "age": 35, "email": "eve@example.com"}
# """
#
# # 3b. sample_array.json
# sample_array_json_content = """[
#   {"name": "Alice", "age": 30, "email": "alice@example.com"},
#   {"name": "Bob", "age": "notanumber", "email": "bob@example.com"},
#   {"name": "Charlie", "age": 25, "email": "charlie@example.com"},
#   "INVALID ENTRY",
#   {"name": "Diana", "age": 40, "email": "diana@example"},
#   {"name": "Eve", "age": 35, "email": "eve@example.com"}
# ]
# """
#
# # Use raw strings or double backslashes for Windows paths, e.g.,
# with open(r"C:\Users\pathan sufyan\Desktop\sample.txt", "w") as f:
#     f.write(sample_txt_content)
#
# with open(r"C:\Users\pathan sufyan\Desktop\sample.csv", "w") as f:
#     f.write(sample_csv_content)
#
# with open(r"C:\Users\pathan sufyan\Desktop\sample.jsonl", "w") as f:
#     f.write(sample_jsonl_content)
#
# with open(r"C:\Users\pathan sufyan\Desktop\sample_array.json", "w") as f:
#     f.write(sample_array_json_content)

