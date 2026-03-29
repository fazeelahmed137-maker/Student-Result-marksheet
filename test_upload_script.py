import requests
import sys

url = "http://127.0.0.1:8000/import-students/upload/"

# Create a dummy blank excel file to upload
with open("dummy.xlsx", "wb") as f:
    f.write(b"PK\x03\x04")

files = {'excel_file': ('dummy.xlsx', open('dummy.xlsx', 'rb'), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
data = {
    'department': '1',
    'year': '1',
    'semester': '1'
}

print("Sending POST request to", url)
try:
    response = requests.post(url, data=data, files=files)
    print("Status code:", response.status_code)
    print("History:")
    for h in response.history:
        print("  ", h.status_code, h.url)
    print("Response snippet:", len(response.text))
    
    if "✅" in response.text:
        print("Success message found!")
    elif "❌" in response.text or "errors" in response.text.lower():
        print("Error message found!")
    else:
        print("No expected message found.")
except Exception as e:
    print("Error:", e)
