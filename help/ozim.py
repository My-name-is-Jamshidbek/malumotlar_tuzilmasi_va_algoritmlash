
import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook(r'C:\Users\PC\Favorites\Downloads\Telegram Desktop\Ходимлар РЎЙХАТИ 23.02.2024 й.xlsx')

# Select the active worksheet
worksheet = workbook.active

# Iterate over all rows in the worksheet and print each cell value
for row in worksheet.iter_rows(values_only=True):
    print(f"""            [
                'name' => '{row[1]}',
                'desc' => '
                Лавозим: {row[2]}
                Туғилган йили: {row[3]}
                Телефон рақами: {row[4]}
                ',
            ],""")

# Close the workbook after use
workbook.close()
