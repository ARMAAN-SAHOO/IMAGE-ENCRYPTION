import cv2
def convert_to_png(img_path):
    extension=img_path[img_path.rindex('.'):]
    if(extension!=".png"):
        image = cv2.imread(img_path)
        path=img_path[:img_path.rindex('.')]+".png"
        cv2.imwrite(path,image)
        return path
    return img_path

