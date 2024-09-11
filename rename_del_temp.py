import os 

source_folder = r'D:\Simple Python Script test\Rename-Delete Temp format file'

for item in os.listdir(source_folder):
    #cek jika item berakhiran dengan format .temp atau bukan
    if os.path.isfile(os.path.join(source_folder, item)):
        if item.endswith('.temp'):
            try:
                #rename file dengan menghapus akhiran .temp
                os.rename(
                    os.path.join(source_folder, item),
                    os.path.join(source_folder, item).replace('.temp', '')
                )
            #Jika file sedang diakses, maka skip
            except PermissionError:
                continue
            except Exception as e:
                raise Exception(e)