import csv

# Refernce: https://www.youtube.com/watch?v=q5uM4VKywbA

with open('example.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # for ln in csv_reader:
    # print(ln)
    # print(ln[2])

    # If you don't want to read the heading i.e the first line of the csv file
    next(csv_reader)
    for ln in csv_reader:
        print(ln[2])

    # Create a csv new file copy the existing file but with ':' as delimiter not comma
    # bring file descriptor back to 0. As it already went to the last during the first iteration
    csv_file.seek(0)
    with open('modified_example.csv', 'w') as mod_csv_file:
        csv_writer = csv.writer(mod_csv_file, delimiter=":")
        for ln in csv_reader:
            csv_writer.writerow(ln)

print('#' * 150)
# What if you want to read the new csv file which is having ":" as delimeter not comma

with open('modified_example.csv') as mod_csv_file:
    # have to specify delimeter as default is comma
    csv_reader = csv.reader(mod_csv_file, delimiter=":")
    for ln in csv_reader:
        print(ln)

    print('#' * 150)

    # read and write csv with DictReader. In this case header will not show by dafault. As it is already there in each row
    mod_csv_file.seek(0)
    csv_reader = csv.DictReader(mod_csv_file, delimiter=":")
    for ln in csv_reader:
        print(ln)
        print(ln['email'])
