import urllib.request
import urllib.parse
import mimetypes
import uuid

# Get CSRF Token
req_get = urllib.request.Request("http://127.0.0.1:8000/import-marks/")
opener = urllib.request.build_opener()
response_get = opener.open(req_get)
cookies = response_get.headers.get('Set-Cookie')
csrf_token = ""
for cookie in cookies.split(";"):
    if "csrftoken=" in cookie:
        csrf_token = cookie.split("csrftoken=")[1].strip()
        break
print(f"Got CSRF: {csrf_token}")

boundary = uuid.uuid4().hex
headers = {
    'Content-Type': f'multipart/form-data; boundary={boundary}',
    'Cookie': f'csrftoken={csrf_token}',
    'Referer': 'http://127.0.0.1:8000/import-marks/'
}

with open(r'c:\Users\ELCOT\Downloads\sample_marks.xlsx', 'rb') as f:
    file_data = f.read()

# Build multipart body
fields = {
    'csrfmiddlewaretoken': csrf_token,
    'department': '1', 
    'year': '1', 
    'semester': '1'
}

body = bytearray()
for key, val in fields.items():
    body.extend(f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"\r\n\r\n{val}\r\n'.encode('utf-8'))

body.extend(f'--{boundary}\r\nContent-Disposition: form-data; name="excel_file"; filename="sample_marks.xlsx"\r\nContent-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\r\n\r\n'.encode('utf-8'))
body.extend(file_data)
body.extend(f'\r\n--{boundary}--\r\n'.encode('utf-8'))

req_post = urllib.request.Request("http://127.0.0.1:8000/import-marks/upload/", data=bytes(body), headers=headers, method="POST")

try:
    response_post = opener.open(req_post)
    html = response_post.read().decode('utf-8')
    with open('browser_response.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS, wrote browser_response.html")
except urllib.error.HTTPError as e:
    html = e.read().decode('utf-8')
    with open('browser_response.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"HTTP ERROR {e.code}, wrote browser_response.html")
except Exception as e:
    print(f"FAILED: {e}")
