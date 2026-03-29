html = """{% load static %}<!DOCTYPE html>
<html>
<head>
<title>Grade Card</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: Arial, sans-serif; background: #f4f1e6; padding: 40px 0; }
.marksheet {
    width: 1000px; min-height: 1350px; margin: 30px auto;
    background: #fff9dc; padding: 35px 45px;
    border: 3px double #000; box-shadow: 0 0 8px rgba(0,0,0,0.15);
    display: flex; flex-direction: column; justify-content: space-between; position: relative;
}
.marksheet::before {
    content: ""; position: absolute; top: 300px; left: 50%; transform: translateX(-50%);
    width: 550px; height: 550px;
    background: url("{% static 'images/logo.png' %}") no-repeat center;
    background-size: contain; opacity: 0.04; z-index: 0;
}
.content { position: relative; z-index: 1; }
.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; border-bottom: 2px solid #000; padding-bottom: 15px; }
.header-left img { width: 80px; }
.header-center { text-align: center; flex: 1; padding: 0 20px; }
.header-center h2 { font-size: 18px; font-weight: bold; text-transform: uppercase; }
.header-center p { font-size: 12px; margin-top: 3px; }
.header-center .title { font-size: 15px; font-weight: bold; margin-top: 6px; letter-spacing: 2px; border: 1px solid #000; display: inline-block; padding: 2px 12px; }
.header-right { text-align: right; font-size: 12px; }
.info-table { width: 100%; border-collapse: collapse; margin: 18px 0; }
.info-table td { border: 1px solid #333; padding: 6px 10px; font-size: 13px; background: transparent; }
.marks-table { width: 100%; border-collapse: collapse; margin-top: 5px; }
.marks-table th, .marks-table td { border: 1px solid #333; padding: 7px 6px; text-align: center; font-size: 12px; }
.marks-table th { background: #e6e6e6; font-weight: bold; }
.marks-table td { background: transparent; }
.marks-table td.left { text-align: left; }
.arrear-note { font-size: 11px; font-style: italic; }
.summary { margin-top: 18px; font-size: 13px; line-height: 2; }
.summary table { border: none; width: auto; margin: 0; }
.summary table td { border: none; padding: 1px 14px 1px 0; font-size: 13px; background: transparent; }
.summary-label { font-weight: bold; }
.footer { margin-top: 40px; padding-top: 14px; border-top: 1px solid #555; display: flex; justify-content: space-between; align-items: flex-end; }
.qr img { width: 72px; }
.qr p, .signature p { font-size: 10px; text-align: center; margin-top: 4px; }
.signature img { width: 100px; }
.download { text-align: center; margin-top: 20px; }
.download button { padding: 8px 22px; background: #1e3c72; color: white; border: none; cursor: pointer; font-size: 13px; border-radius: 3px; }
@media print { .download { display: none; } }
</style>
</head>
<body>
<div class="marksheet">
<div class="content">

<div class="header">
  <div class="header-left"><img src="{% static 'images/logo.png' %}"></div>
  <div class="header-center">
    <h2>C. Abdul Hakeem College (Autonomous)</h2>
    <p>Affiliated to Thiruvalluvar University | Melvisharam – 632 509</p>
    <p class="title">GRADE CARD</p>
  </div>
  <div class="header-right">
    <strong>Exam:</strong> """ + "{{ month_year }}" + """<br>
    <strong>Arrears:</strong> """ + "{% if total_arrears == 0 %}Nil{% else %}{{ total_arrears }}{% endif %}" + """
  </div>
</div>

<table class="info-table">
  <tr>
    <td><strong>Name:</strong> """ + "{{ student.name }}" + """</td>
    <td><strong>Register No:</strong> """ + "{{ student.roll_no }}" + """</td>
    <td><strong>Date of Birth:</strong> """ + "{{ student.dob }}" + """</td>
  </tr>
  <tr>
    <td><strong>Department:</strong> """ + "{{ student.department.name }}" + """</td>
    <td><strong>Year:</strong> """ + "{{ student.year }}" + """</td>
    <td><strong>Current Semester:</strong> """ + "{{ student.semester }}" + """</td>
  </tr>
</table>

<table class="marks-table">
  <thead>
    <tr>
      <th rowspan="2">S.No</th>
      <th rowspan="2">Sub Code</th>
      <th rowspan="2" class="left">Subject Title</th>
      <th colspan="2">CIA (25)</th>
      <th colspan="2">ESE (75)</th>
      <th colspan="2">Total (100)</th>
      <th rowspan="2">Credits</th>
      <th rowspan="2">Grade</th>
      <th rowspan="2">Pts</th>
      <th rowspan="2">Result</th>
      <th rowspan="2">Remark</th>
    </tr>
    <tr>
      <th>Max</th><th>Sec</th>
      <th>Max</th><th>Sec</th>
      <th>Max</th><th>Sec</th>
    </tr>
  </thead>
  <tbody>
""" + "{% for sem_info in semester_data %}" + """
""" + "{% for mark in sem_info.regular_marks %}" + """
    <tr>
      <td class="sno-cell"></td>
      <td>""" + "{{ mark.subject.code }}" + """</td>
      <td class="left">""" + "{{ mark.subject.name }}" + """</td>
      <td>25</td><td>""" + "{{ mark.internal }}" + """</td>
      <td>75</td><td>""" + "{{ mark.external }}" + """</td>
      <td>100</td><td>""" + "{{ mark.total_calc }}" + """</td>
      <td>""" + "{{ mark.subject.credits }}" + """</td>
      <td>""" + "{{ mark.grade }}" + """</td>
      <td>""" + "{{ mark.points }}" + """</td>
      <td>""" + "{{ mark.result }}" + """</td>
      <td class="arrear-note">""" + "{% if mark.result == 'F' %}Arrear{% elif mark.result == 'A' %}Absent{% else %}&mdash;{% endif %}" + """</td>
    </tr>
""" + "{% endfor %}" + """
""" + "{% for mark in sem_info.arrear_attempts %}" + """
    <tr>
      <td class="sno-cell"></td>
      <td>""" + "{{ mark.subject.code }}" + """</td>
      <td class="left">""" + "{{ mark.subject.name }}" + """</td>
      <td>25</td><td>""" + "{{ mark.internal }}" + """</td>
      <td>75</td><td>""" + "{{ mark.external }}" + """</td>
      <td>100</td><td>""" + "{{ mark.total_calc }}" + """</td>
      <td>""" + "{{ mark.subject.credits }}" + """</td>
      <td>""" + "{{ mark.grade }}" + """</td>
      <td>""" + "{{ mark.points }}" + """</td>
      <td>""" + "{{ mark.result }}" + """</td>
      <td class="arrear-note">""" + "{% if mark.result == 'P' %}Arrear Cleared{% else %}Arrear Pending{% endif %}" + """</td>
    </tr>
""" + "{% endfor %}" + """
""" + "{% endfor %}" + """
  </tbody>
</table>

<div class="summary">
  <table>
    <tr>
      <td class="summary-label">Overall Total Marks:</td><td>""" + "{{ total_marks }}" + """</td>
      <td class="summary-label">Overall Percentage:</td><td>""" + "{{ percentage }}" + """%</td>
      <td class="summary-label">Overall GPA:</td><td>""" + "{{ gpa }}" + """</td>
    </tr>
    <tr>
      <td class="summary-label">Arrear Status:</td>
      <td colspan="5">""" + "{% if total_arrears == 0 %}All Subjects Cleared{% else %}{{ total_arrears }} Subject{{ total_arrears|pluralize }} Pending{% endif %}" + """</td>
    </tr>
  </table>
</div>

</div>

<div class="footer">
  <div class="qr">
    <img src=\"""" + "{{ qr_code_url }}" + """\">
    <p>Scan for verification</p>
  </div>
  <div class="signature">
    <img src="{% static 'images/controller.jpeg' %}">
    <p>Controller of Examinations</p>
  </div>
</div>

</div>
<div class="download">
  <button onclick="window.print()">Print / Download PDF</button>
</div>
<script>
document.addEventListener("DOMContentLoaded", function() {
    let cells = document.querySelectorAll(".sno-cell");
    cells.forEach((cell, index) => {
        cell.innerText = index + 1;
    });
});
</script>
</body>
</html>
"""

import os
path = r"d:\Project\student_result_django\student_result_django\results\templates\results\marksheet.html"
with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Marksheet written successfully.")
