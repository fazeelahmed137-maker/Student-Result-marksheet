import os
import re

path = r'd:\Project\student_result_django\student_result_django\results\templates\results\marksheet.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the broken template tag formatting
# Matches: "Sem {{ sem_info.semester \n                    }}"
text = re.sub(r'Sem \{\{\s*sem_info\.semester\s*\n\s*\}\}', 'Sem {{ sem_info.semester }}', text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Tab text patched successfully.')
