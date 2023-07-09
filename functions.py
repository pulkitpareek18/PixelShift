import cv2
from werkzeug.utils import secure_filename

def processImage(filename,operation):
    img = cv2.imread(f"uploads/{filename}")

    match operation:
        # Grayscale
        case "cgray":
            imgProcessed = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"static/processedImages/{filename}", imgProcessed)
            return(filename)

        # Image Fromats
        case "cwebp":
                imgProcessed = cv2.imwrite(f"static/processedImages/{filename.split('.')[0]}.webp", img)
                return(f"{'_'.join(filename.split('.')[0:-1])}.webp")
        case "cpng":
                imgProcessed = cv2.imwrite(f"static/processedImages/{filename.split('.')[0]}.png", img)
                return(f"{'_'.join(filename.split('.')[0:-1])}.png")
        case "cjpg":
                imgProcessed = cv2.imwrite(f"static/processedImages/{filename.split('.')[0]}.jpg", img)
                return(f"{'_'.join(filename.split('.')[0:-1])}.jpg")
        case "cjpeg":
                imgProcessed = cv2.imwrite(f"static/processedImages/{filename.split('.')[0]}.jpeg", img)
                return(f"{'_'.join(filename.split('.')[0:-1])}.jpeg")
        case "ctif":
                imgProcessed = cv2.imwrite(f"static/processedImages/{filename.split('.')[0]}.tif", img)
                return(f"{'_'.join(filename.split('.')[0:-1])}.tif")
        case "cbmp":
                imgProcessed = cv2.imwrite(f"static/processedImages/{filename.split('.')[0]}.bmp", img)
                return(f"{'_'.join(filename.split('.')[0:-1])}.bmp")
        case "ctiff":
                imgProcessed = cv2.imwrite(f"static/processedImages/{filename.split('.')[0]}.tiff", img)
                return(f"{'_'.join(filename.split('.')[0:-1])}.tiff")