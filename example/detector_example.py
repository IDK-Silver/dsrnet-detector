import cv2

from dsrnet_detector.detector import DSRNetDetector, DSRNetINetType

model = DSRNetDetector()

# Note that you need to download weight file (dsrnet_l_epoch18.pt) to this folder
# You can download from https://drive.google.com/file/d/1hFZItZAzAt-LnfNj-2phBRwqplDUasQy
# More detail please see https://github.com/mingcv/DSRNet?tab=readme-ov-file#trained-weights
model.load_model('dsrnet_l_epoch18.pt', DSRNetINetType.dsrnet_l)

# in my case when the size of image is (640, 640), the detect process use more than 9 GB Video RAM
# ensure your GPU V-RAM can run with your input image
input_image = cv2.imread('input.jpg')
output_image = model.detect(input_image)
cv2.imwrite('output.jpg', output_image)

