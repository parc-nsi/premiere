import sys
import os

input_file = open(sys.argv[1])
absolute_path = os.path.abspath(sys.argv[1])
base_name, ext = os.path.splitext(absolute_path)
print(absolute_path, base_name)
output_file = open(''.join([base_name.rstrip('source') + 'tmp-mkdocs', ext]), 'w')
indentation = ' ' * 4
inside = False
for line in input_file:
    if line.lstrip()[:3] == ':::':
        inside = not inside
        output_file.write(line)
    elif inside:
        output_file.write(indentation + line)
    else:
        output_file.write(line)
output_file.close()
input_file.close()
    