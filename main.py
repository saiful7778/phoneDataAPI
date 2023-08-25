import pandas as pd
import requests
from io import BytesIO
import json
from functions import makePhoneThumbnail, deleteAllFile




def mainFunc(filePath:str, fileType:str, sheetName:str = None, endItem = "end position"):
    if fileType == "csv":
        df = pd.read_csv(filePath)
    elif fileType == "xlsx":
        df = pd.read_excel(filePath, sheet_name=sheetName)
    counter:int = 1
    jsonData:list = []
    deleteAllFile("./outputData")
    for index, row in df.iterrows():
        index+=1
        phone_name = row['phoneName']
        image_url = row['phoneImage-src']
        res = requests.get(image_url)
        if res.status_code == 200:
            fileName = phone_name.lower().replace(" ", "_")
            outputFilePath = f"outputData/images/{fileName}_image.jpg"
            jsonData.append({
                "phoneName": phone_name,
                "imageLink": outputFilePath.replace("outputData",".")
            })
            makePhoneThumbnail(BytesIO(res.content), outputFilePath)
            print(f"{index}. {phone_name} is downloaded.")
        else:
            print(f"{index}. download failed {phone_name}")
        if endItem != "end position":
            if counter >= endItem:
                break
            counter += 1
    
    with open("outputData/phoneData.json", "w") as jsonFile:
        jsonFile.write(json.dumps({
            "allPhoneData": jsonData
        }))


if __name__ == "__main__":
    # mainFunc("inputData/allPhoneData.csv", "csv")
    mainFunc("inputData/allPhoneData.xlsx", "xlsx", "allPhoneData")    