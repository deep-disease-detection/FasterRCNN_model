import os
from csv import writer


train_label_path = 'Dataset/dataset-yolo/labels/augmented'
train_image_path = 'Dataset/dataset-yolo/images/augmented'
test_image_path = 'Dataset/dataset-yolo/images/test'
test_label_path = 'Dataset/dataset-yolo/labels/test'


dic = {
    '0' : 'Adenovirus',
    '1': 'Astrobirus',
    '2': 'CCHF',
    '3': 'Cowpox',
    '4': 'Ebola',
    '5': 'Marburg',
    '6':'Norovirus',
    '7': 'Orf',
    '8': 'Papilloma',
    '9' : 'Rift Valley',
    '10':'Rotavirus'
}


for file in os.listdir(train_label_path):
    with open(os.path.join(train_label_path, file), 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(' ')
            class_ = dic[line[0]]
            width = 1000
            height = 1000
            filename = file.replace("txt", "jpg")
            xmin = float(line[1]) - float(line[3])/2
            ymin = float(line[2]) - float(line[4])/2
            xmax = float(line[1]) + float(line[3])/2
            ymax = float(line[2]) + float(line[4])/2
            row = [filename, width, height, class_, xmin, ymin, xmax, ymax]
            print(row)
            with open ('trainset.csv', 'a') as cfile:
                writer_object = writer(cfile)
                writer_object.writerow(row)
                cfile.close()
