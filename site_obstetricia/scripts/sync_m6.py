import os
import shutil

base_dir = r"c:\Users\Admin\Downloads\INTERNATO GO\hub_master\site_obstetricia"
index_file = os.path.join(base_dir, "index.html")
comp_file = os.path.join(base_dir, "components", "modulo-6-ctg-doppler.html")
backup_file = os.path.join(base_dir, "scratch", "index.html.bak_before_m6")

os.makedirs(os.path.join(base_dir, "scratch"), exist_ok=True)
shutil.copyfile(index_file, backup_file)
print("Backup of index.html created at:", backup_file)

with open(index_file, "r", encoding="utf-8") as f:
    index_lines = f.readlines()

with open(comp_file, "r", encoding="utf-8") as f:
    comp_content = f.read().strip()

# Find start index (the comment above modulo-6 or modulo-6 itself)
m6_comment_or_section_idx = None
m7_comment_or_section_idx = None

for i, line in enumerate(index_lines):
    if 'id="modulo-6"' in line:
        if i > 0 and 'MÓDULO 6' in index_lines[i-1].upper() or 'MODULO 6' in index_lines[i-1].upper():
            m6_comment_or_section_idx = i - 1
        else:
            m6_comment_or_section_idx = i
        break

for i, line in enumerate(index_lines):
    if 'id="modulo-7"' in line:
        if i > 0 and ('MÓDULO 7' in index_lines[i-1].upper() or 'MODULO 7' in index_lines[i-1].upper()):
            m7_comment_or_section_idx = i - 1
        else:
            m7_comment_or_section_idx = i
        break

print(f"M6 replacement range: line {m6_comment_or_section_idx + 1} to line {m7_comment_or_section_idx + 1}")
print(f"Index line at m6 start: {repr(index_lines[m6_comment_or_section_idx])}")
print(f"Index line at m7 start: {repr(index_lines[m7_comment_or_section_idx])}")

prefix = index_lines[:m6_comment_or_section_idx]
suffix = index_lines[m7_comment_or_section_idx:]

new_index_content = "".join(prefix) + comp_content + "\n\n    " + "".join(suffix)

with open(index_file, "w", encoding="utf-8") as f:
    f.write(new_index_content)

print("Updated index.html successfully!")
print("New total lines in index.html:", len(new_index_content.splitlines()))
