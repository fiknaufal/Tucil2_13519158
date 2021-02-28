# NAMA  : MUHAMMAD FIKRI NAUFAL
# NIM   : 13519158
# KELAS : K03
import roman

## FUNGSI DAN PROSEDUR ##
def makeNodeArray(filename): # Mengubah input .txt menjadi array of array of string tiap barisnya
    # membaca file .txt
    filename2 = "../test/"+filename
    f = open(filename2, 'r')

    # membagi file txt. menjadi array of string tiap baris
    prenode_array = [ line.split() for line in f]

    # membagi tiap string dalam array menjadi array of string dengan isi per nama mata kuliah
    node_array = []
    for i in range (len(prenode_array)):
        node_array.append(prenode_array[i][0])
    for i in range (len(node_array)):
        node_array[i] = node_array[i].replace('.', '')
        node_array[i] = node_array[i].split(',')
    return node_array

def semesterChoosing(node_array): # Membuat array berisi array of string matkul yang dapat diambil tiap semesternya terurut berdasar indeks array
    semester = []
    while (len(node_array) != 0):

        # Mendapatkan mata kuliah yang tidak/ sudah tidak memiliki prerequisite
        sendiri = []
        for i in range (len(node_array)):
            if (len(node_array[i]) == 1):
                sendiri.append(node_array[i][0])
        
        # Menghapus matkul pada array node_array yang sudah dimasukkan ke dalam array "sendiri"
        for i in range (len(sendiri)):
            for k in range (len(node_array)):
                j = 0
                while (j < (len(node_array[k]))):
                    if (sendiri[i] == node_array[k][j]):
                        del node_array[k][j]
                    else:
                        j = j+1
        
        # Menghapus array-array kosong dalam array node_array
        l = 0
        while (l < len(node_array)):
            if (len(node_array[l]) == 0):
                del node_array[l]
            else:
                l = l+1
        
        # Memasukkan array "sendiri" ke dalam array semester
        semester.append(sendiri)
    return semester;

def printFormat(semester_array):
    # Mencetak matkul-matkul apa saja yang bisa diambil pada semester tertentu dengan format:
    # Semester I : A, B
    # Semester II : C, D, E
    # dst.

    for i in range (len(semester_array)):
        print("Semester", roman.toRoman(i+1), ":", end="")
        for j in range (len(semester_array[i])):
            if (j == len(semester_array[i])-1):
                print(" "+semester_array[i][j])
            else:
                print(" "+semester_array[i][j] + ",", end="")

## PROGRAM UTAMA ##
# Nama program
print();
print("        :::   :::       ::: ::::::::::: :::    ::: :::    ::: :::           ::::::::   ::::::::  ::::::::: ::::::::::: :::::::::: ::::::::: ")
print("      :+:+: :+:+:    :+: :+:   :+:     :+:   :+:  :+:    :+: :+:          :+:    :+: :+:    :+: :+:    :+:    :+:     :+:        :+:    :+: ")
print("    +:+ +:+:+ +:+  +:+   +:+  +:+     +:+  +:+   +:+    +:+ +:+          +:+        +:+    +:+ +:+    +:+    +:+     +:+        +:+    +:+  ")
print("   +#+  +:+  +#+ +#++:++#++: +#+     +#++:++    +#+    +:+ +#+          +#++:++#++ +#+    +:+ +#++:++#:     +#+     +#++:++#   +#++:++#:    ")
print("  +#+       +#+ +#+     +#+ +#+     +#+  +#+   +#+    +#+ +#+                 +#+ +#+    +#+ +#+    +#+    +#+     +#+        +#+    +#+    ")
print(" #+#       #+# #+#     #+# #+#     #+#   #+#  #+#    #+# #+#          #+#    #+# #+#    #+# #+#    #+#    #+#     #+#        #+#    #+#     ")
print("###       ### ###     ### ###     ###    ###  ########  ##########    ########   ########  ###    ###    ###     ########## ###    ###      ")
print()

# Masukkan nama file
file = input("Masukkan nama file: ")
print()

# Menampilkan output
printFormat(semesterChoosing(makeNodeArray(file)))