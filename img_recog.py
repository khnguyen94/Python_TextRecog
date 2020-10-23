# Import all necessary packages and dependeencies
import io
import json
import cv2
import numpy as np
import requests

# Load in the image
img = cv2.imread("screenshots/medicare_ID.jpg")
height, width, _ = img.shape

# print(img)
# openCV opens img as a numpy array, will later need to compress and convert img file into bytes in order to use eit with OCR
# print("Image Dimensions: " + img.shape)

# Show the image
cv2.imshow("Img", img)

# Not necessary to cut the image to show only the text, because ID card is ususally info/text dense

# Set up OCR server to accept and process img
# Define API URL
api_url = "https://api.ocr.space/parse/image"

# Compress image
_, compressedImg = cv2.imencode(".jpg", img, [1, 90])

# Convert image into bytes with io library
file_bytes = io.BytesIO(compressedImg)

# Send the POST request and store it into a result variable
result = requests.post(api_url,
              files={"screenshots/medicare_ID.jpg": file_bytes},
              data={"apikey": "1d2029041b88957", "language": "eng"}
              )

# Interpret the Response 200 sent back from OCR
result = result.content.decode()

# print(result)
# print(type(result))

# Convert the response into a JSON dictionary so contents can be accessed
result = json.loads(result)
# print(type(result))

text_detected = result.get("ParsedResults")[0].get("ParsedText")
print("Text Detected")
print(text_detected)

# Keep the img open until we press some key,
cv2.waitKey(0)
cv2.destroyAllWindows()
