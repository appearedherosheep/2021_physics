import cv2

src = cv2.imread('src/img_process_lower.png')
dst = src.copy()
cv2.imshow('img_color', dst)
cv2.waitKey(0)

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
cv2.imshow('img_gray', gray)
cv2.waitKey(0)

ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('img_binary', binary)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)


for i in range(len(contours)):
    cv2.drawContours(dst, contours, i, (0, 0, 255), 3)
    print(i)
    i += 1
    cv2.imshow("dst", dst)
    cv2.waitKey(0)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
