import requests

url = "http://127.0.0.1:8000/import-students/upload/"

# Create a fake "Marks" excel file in memory
import openpyxl
import io
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Reg No", "Name", "Sub1", "Sub2", "Sub3", "Sub4"]) # 6 columns! Should trigger the block
file_stream = io.BytesIO()
wb.save(file_stream)
file_stream.seek(0)

# We need the CSRF token and the form fields
# First get the page to get CSRF
client = requests.Session()
r_get = client.get("http://127.0.0.1:8000/import-students/")
csrf_token = client.cookies.get('csrftoken')

files = {'excel_file': ('test.xlsx', file_stream, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
data = {
    'csrfmiddlewaretoken': csrf_token,
    'department': '1',
    'year': '1',
    'semester': '1',
}

r_post = client.post(url, files=files, data=data)
print("STATUS:", r_post.status_code)
if "Wrong file uploaded" in r_post.text:
    print("SUCCESS: New logic is running!")
elif "Failed to read Excel file" in r_post.text:
    print("WARNING: Old logic or exceptions!")
else:
    print("WARNING: Unknown response!")
    with open('response.html', 'w', encoding='utf-8') as f:
        f.write(r_post.text)
