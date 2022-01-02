import cv2
img = cv2.imread('img_process.png')
# img2 = cv2.imread('images/ahffk.PNG')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thr1 = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
_, contours = cv2.findContours(thr1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0] 

mmt = cv2.moments(cnt)

for key, value in mmt.items():
    print(key, " : ", value) 
    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])
    print('x 무게중심', cx, 'y 무게중심', cy)
