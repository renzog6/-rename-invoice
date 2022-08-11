import file_list
import read_qr
import rename_file

if "__main__" == __name__:
    path='././sample/'
    try:
        lst = file_list.get_list_files(path)
        for f in lst:
            #Get name for file
            name_file = read_qr.get_name_file(path+f)
            if name_file != 'ERROR':
                rename_file.rename(path+f, path+name_file+'.pdf')
                print(name_file)
    except:
        print("An exception occurred")