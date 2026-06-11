command = ""
while command.lower() != "exit":
    command = input(">")
    print("ECHO", command)


# ------------------------------
#      E X E R C I S E
# ------------------------------

count = 0
for x in range(2, 10, 2):
    print(x)
    count += 1
print(f"We have {count} even numbers")

new_count = 0
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        new_count += 1
print(f"We have {new_count} even numbers")
