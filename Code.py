from PIL import Image
import numpy as np
import keras
import tensorflow
import glob
import csv

class MyImage():
    name=None
    nationality=None
    idnumber=None
    PID=None
    HajjAgency=None
    Image_url=None
    Barcode_url=None
    ImageID=None
    ImagePixles=[]
    BarcodePixles=[]



def LoadData():
    with open('C:/Users/t430/Desktop/Dataset/Data.csv', 'r') as csvfile: 
        spamreader = csv.reader(csvfile, delimiter=',')
        next(spamreader)
        for row in spamreader:
            Myimage=MyImage()
            Myimage.name=row[0]
            Myimage.nationality=row[1]
            Myimage.idnumber=row[2]
            Myimage.PID=row[3]
            Myimage.HajjAgency=row[4]
            Myimage.Image_url=row[5]+".jpg"
            Myimage.Barcode_url=row[6]+".png"
            imagepath=Myimage.Image_url
            im1=Image.open(imagepath)
            im2=Image.open(barcodepath)
            im1 = im1.resize((128, 128))
            im2 = im2.resize((128, 128))
            Myimage.ImagePixles=(list(im1.getdata()))
            Myimage.BarcodePixles=(list(im2.getdata()))
            tmp=imagepath.split("/")[7]
            tmp2=tmp.split(".")
            Myimage.ImageID=tmp2[0]
            Images.append(Myimage)
           

def PrintHajjInfo(i):   
    Image.open(Images[i].Image_url).show()
    Image.open(Images[i].Barcode_url).show()
    print(Images[i].name)
    print(Images[i].idnumber)
    print(Images[i].PID)
    print(Images[i].ImageID)
    print(Images[i].nationality)
    print(Images[i].HajjAgency)


    

def main():
    image_list = []
    image_pixles=[]
    names=[]
    Images=[]
    LoadData()
    PrintHajjInfo(3) 
	
DatasetPath  = []
for i in os.listdir("C:/Users/t430/Desktop/Dataset/images/Training/"):
    DatasetPath.append(os.path.join("C:/Users/t430/Desktop/Dataset/images/Training/", i))
	
imageData  = []
imageLabels = []

for i in DatasetPath:
    imgRead = io.imread(i,as_grey=True)
    imageData.append(imgRead)    
    labelRead = int(os.path.split(i)[1].split(".")[0].replace("subject", "")) - 1
    imageLabels.append(labelRead)