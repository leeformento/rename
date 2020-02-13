import os

os.chdir('/Users/Lee/Desktop/New Fabrics/STI/Gabe_Bomber')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    # separates the words. either - or _

    f_name, f_supplier, f_pattern, f_one, f_two, f_three, f_four, f_five, f_resolution = file_name.split('_')
    print(f_supplier, f_pattern)


