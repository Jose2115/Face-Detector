import cv2
image = cv2.imread("image.jpg")
if image is None:
    print("Error: imagen no encontrada")
else:
    print("Imagen cargada correctamente")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("Imagen convertida a escala de grises")

detector = cv2.CascadeClassifier(
"haarcascade_frontalface_default.xml"
)
faces = detector.detectMultiScale(
gray,
scaleFactor=1.1,
minNeighbors=5
)
print("Rostros encontrados:", len(faces))