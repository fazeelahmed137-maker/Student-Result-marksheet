import os
import sys

file_path = r'C:\Users\ELCOT\Downloads\sample_marks.xlsx'

with open('result_log.txt', 'w', encoding='utf-8') as f:
    f.write("Starting check...\n")
    if not os.path.exists(file_path):
        f.write(f"FILE DOES NOT EXIST: {file_path}\n")
    else:
        f.write(f"File exists, size: {os.path.getsize(file_path)}\n")
        
        try:
            import openpyxl
            wb = openpyxl.load_workbook(file_path)
            ws = wb.active
            for i, row in enumerate(ws.iter_rows(min_row=1, max_row=3, values_only=True), 1):
                f.write(f"Row {i}: {row}\n")
        except Exception as e:
            f.write(f"FAILED TO READ: {type(e).__name__} {str(e)}\n")

    f.write("Done.\n")
