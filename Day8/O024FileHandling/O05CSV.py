import csv

# with open("abc1.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["id", "Name", "Price"])
#     writer.writerow([101, "Paint", 100])
#     writer.writerow([102, "polish", 400])
#     writer.writerow([103, "brush", 500])

with open("abc1.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for r in reader:
        print(r)
