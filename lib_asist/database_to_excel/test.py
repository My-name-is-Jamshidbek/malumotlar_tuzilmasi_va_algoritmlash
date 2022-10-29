# import sqlite3
# from sqlite3 import Error
# from openpyxl.styles import colors
# from openpyxl.styles import Font, Color
# from openpyxl.worksheet.table import Table, TableStyleInfo
# from openpyxl import Workbook
# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by the db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except Error as e:
#         print(e)
#
#     return conn
# wb = Workbook()
# ws = wb.active
# conn = create_connection('db.sqlite3')
# cur = conn.cursor()
# table = pd.read_sql_query("SELECT * from table_name", db)
# table.to_csv(table_name + '.csv', index_label='index')# cur.execute("SELECT * FROM accounts_students")
#
# rows = cur.fetchall()
# ws.append(["T/r", "Kitob nomi", "Inventar rakami" ,"Muallif", "Bazaga qo'shilgan sana", "Kitob turi",'Kitob tili','Varaqlar soni','Narxi','Organizator','nashriyot','yili','isbn'])
# for i in rows:
#     ws.append(i)
# tab = Table(displayName="Table1", ref="A1:M1")
#
# # Add a default style with striped rows and banded columns
# style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
#                        showLastColumn=False, showRowStripes=True, showColumnStripes=True)
# tab.tableStyleInfo = style
# ws.add_table(tab)
#
# wb.save('test1.xlsx')
# accounts_accept_book qabul qilingan kitoblar
# accounts_book
# accounts_return_book qaytarilgan kitoblar
# accounts_students


import sqlite3
import pandas as pd


def to_csv():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(tables)
    for table_name in tables:
        table_name = table_name[0]
        table = pd.read_sql_query("SELECT * from %s" % table_name, db)
        table.to_csv(table_name + '.xlsx', index_label='index')
    cursor.close()
    db.close()
to_csv()