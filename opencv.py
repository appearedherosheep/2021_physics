import cv2

src = cv2.imread('src/img_process_lower.png')
src_2 = cv2.imread('src/img_process.png')

dst = src.copy()
cv2.imshow('img_color', dst)
cv2.waitKey(0)

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)


ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('img_binary', binary)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in contours[1:]:
    M = cv2.moments(i)
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])

    print(cX,cY)
    # cv2.circle(dst, (cX, cY), 3, (255, 0, 0), 3)
    # cv2.drawContours(dst, [i], 0, (0, 0, 255), 2)
    cv2.circle(src_2, (cX, cY), 3, (255, 0, 0), 3)
    cv2.drawContours(src_2, [i], 0, (0, 0, 255), 2)

    
cv2.imshow("dst", dst)
cv2.imshow('src_2',src_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
