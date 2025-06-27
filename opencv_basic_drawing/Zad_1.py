import numpy as np
import cv2

#Tworzymy czarne tło 300x300 pikseli, 3 kanały (BGR)
canvas = np.zeros((300, 300, 3), dtype="uint8")

# Punkt startowy – środek obrazu
center = (canvas.shape[1] // 2, canvas.shape[0] // 2)

# Punkt końcowy – prawy dolny róg
end = (canvas.shape[1] - 1, canvas.shape[0] - 1)  # (299, 299)

# Kolor niebieski w formacie BGR
blue = (255, 0, 0)

# Rysowanie linii grubości 2 px
cv2.line(canvas, center, end, blue, 2)

# Wyświetlenie wyniku
cv2.imshow("Linia od środka do prawego dolnego rogu", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
