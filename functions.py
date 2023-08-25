import os
from PIL import Image


def makePhoneThumbnail(inputImage: str, outputPath: str):
    original_image = Image.open(inputImage)
    backgroundSize = (500, 350)
    background = Image.new('RGB', backgroundSize, (255, 255, 255))
    imageXPosition: int = int(
        (backgroundSize[0] / 2) - (original_image.size[0] / 2))
    imageYPosition: int = int(
        (backgroundSize[1] / 2) - (original_image.size[1] / 2))
    imagePosition: tuple = (imageXPosition, imageYPosition)
    background.paste(original_image, imagePosition, (0))
    background.save(outputPath)


def deleteAllFile(folderDir):
    fileList = os.listdir(folderDir)
    for fileName in fileList:
        filePath = os.path.join(folderDir, fileName)
        if os.path.isfile(filePath):
            os.remove(filePath)
            print(f"Deleted: {fileName}")
        else:
            print(f"Skipped: {fileName} (not a file)")
    print("All file is deleted")
