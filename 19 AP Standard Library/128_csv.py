# ---------------------------------------------------------------------
# ---------------**## CSV ##**---------------------
import csv

# ************************* Task One
# *-*-*--*--*-*** Opening a CSV file and inserting simple data in it.

with open("users_info/users.csv", "w", newline="") as users_data:
    CSV_writer_dara = csv.writer(users_data)

    # row 1 ->>>> table heading
    CSV_writer_dara.writerow(["User Name", "User ID", "Status"])

    # row 2 ->>>> first row user data
    CSV_writer_dara.writerow(["coll555", "1111", "online"])

    # row 3 ->>>> first row user data
    CSV_writer_dara.writerow(["333awesome", "222", "offline"])

    # row 4 ->>>> first row user data
    CSV_writer_dara.writerow(["dog", "333", "online"])

    # row 5 ->>>> first row user data
    CSV_writer_dara.writerow(["cat", "111", "online"])

# ************************* Task Two
# *-*-*--*--*-*** Reading a CSV file

with open("users_info/users.csv") as users_data:
    CSV_writer_dara = csv.reader(users_data)
    for row in CSV_writer_dara:
        print(row)
