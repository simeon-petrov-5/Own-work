__author__ = 'Simeon Petrov'
import xlsxwriter
storageEng ={}
glob = True
def new_tag():
    tag2 = input("Enter the tag of your link: ")
    name2 = input("Enter the name of your link: ")
    url2 = input("Enter the url of your link: ")
    desc2 = input("Enter description for your link (optional): ")
    new_item = any(tag2 == tag for tagg in storageEng)
    if new_item is True:
        storageEng[tag].append([name2, url2, desc2])
    else:
        new = {tag2: [name2, url2, desc2]}
        storageEng.update(new)
def view_storage():
    for tags in storageEng:
        print(tags)
        print(storageEng[tags])

while glob is True:
    print("Hello to your Storage for Links.")
    print("1) Make a new storage.")
    print("2) Append a new item.")
    print("3) View the storage.")
    print("4) Exit and make DefaultStorageEngine.xlsx file.")
    decision = input("Enter decision: ")
    if decision == "1":
        tag = input("Enter the tag of your link: ")
        name = input("Enter the name of your link: ")
        url = input("Enter the url of your link: ")
        desc = input("Enter description for your link (optional): ")
        storageEng = {tag: [[name, url, desc]]}
    elif decision == "2":
        new_tag()
    elif decision == "3":
        view_storage()
    elif decision == "4":
        glob = False
        workbook = xlsxwriter.Workbook("DefaultStorageEngine.xlsx")
        worksheet = workbook.add_worksheet()
        row = 0
        col = 0
        worksheet.write(row, col, "Tag")
        worksheet.write(row, col+1, "Name")
        worksheet.write(row, col+2, "Url")
        worksheet.write(row, col+3, "Description")
        row += 1
        for tags in storageEng:
            for values in storageEng[tags]:
                worksheet.write(row, col, tags)
                worksheet.write(row, col+1, values[0])
                worksheet.write(row, col+2, values[1])
                worksheet.write(row, col+3, values[2])
                row += 1
        workbook.close()
    else:
        print("Error. Incorrect entered decision.")

