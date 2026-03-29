import os

path = r'd:\Project\student_result_django\student_result_django\results\templates\results\marksheet.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the tags that the formatter split
text = text.replace('{%\\n                            else %}', '{% else %}')
text = text.replace('{%\\n                            endif %}', '{% endif %}')
text = text.replace('Absent{%\\n                            else %}', 'Absent{% else %}')
text = text.replace('Pending{%\\n                            endif %}', 'Pending{% endif %}')

# Just to be absolutely sledgehammer safe against any whitespace variations:
import re
text = re.sub(r'\{%\s*else\s*%\}', '{% else %}', text)
text = re.sub(r'\{%\s*endif\s*%\}', '{% endif %}', text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Patch applied bypassing IDE.')
