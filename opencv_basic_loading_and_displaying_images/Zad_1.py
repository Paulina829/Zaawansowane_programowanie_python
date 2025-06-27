import cv2

path = input("Podaj ścieżkę do obrazu: ").strip().replace('"', '').replace('\\', '/')

image = cv2.imread(path)

if image is None:
    print("❌ Błąd: nie można wczytać obrazu!")
else:
    print("✅ Obraz wczytano poprawnie.")
    cv2.imshow("Wyświetlony obraz", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
