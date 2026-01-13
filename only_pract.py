#
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
#

# file = open("C:\\Users\\pathan sufyan\\Desktop\\sample.txt", "r")
# rfile = file.read()
# print(rfile)
# file.close()
#
# file2 = open("C:\\Users\\pathan sufyan\\Desktop\\sample.csv","r")
# rfile2 = file2.read()
# print(rfile2)
# file2.close()

# with open("C:\\Users\\pathan sufyan\\Desktop\\sample.txt","r") as file:
#     print(file.read())
#
# with open("C:\\Users\\pathan sufyan\\Desktop\\sample.csv","r") as file:
#     print(file.read())

