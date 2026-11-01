import cv2
image = cv2.imread("image.jpg")
if image is None:
    print("Error: imagen no encontrada")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detector = cv2.CascadeClassifier(
"haarcascade_frontalface_default.xml"
)
faces = detector.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)
print("Rostros encontrados:", len(faces))
for (x, y, w, h) in faces:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (255, 0, 0),
2
)
cv2.imshow("Resultado", image)
cv2.waitKey(0)
cv2.destroyAllWindows()