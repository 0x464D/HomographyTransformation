import cv2
import numpy as np

# Load the input image
# This should be a 400x400 px image of an 8x8 chessboard (or any other content)
img = cv2.imread('image.jpg')

# Check if the image loaded successfully
if img is None:
    print("❌ Error: Could not load the input image.")
    exit()

# === MODIFY THESE POINTS IF NEEDED ===

# Define the 4 corner points of the original image (top-left, top-right, bottom-right, bottom-left)
# These should match the full dimensions of the image you're loading
# If your image is NOT 400x400, update these values accordingly
src_points = np.array([
    [0, 0],          # Top-left
    [400, 0],        # Top-right
    [400, 400],      # Bottom-right
    [0, 400]         # Bottom-left
], dtype='float32')

# Define the 4 destination points (where you want the image to be "projected" or "warped" to)
# These points should be set according to the physical projection area (like a tabletop)
# You can measure these using pixels from a camera or estimate them manually
dst_points = np.array([
    [120, 80],       # New top-left
    [750, 60],       # New top-right
    [770, 280],      # New bottom-right
    [100, 600]       # New bottom-left
], dtype='float32')

# Calculate the perspective transformation matrix
H, _ = cv2.findHomography(src_points, dst_points)

# Create a blank canvas where the warped image will be placed
# This canvas should be big enough to hold the final projection
# You can increase or decrease the resolution if needed
output_size = (900, 700)  # (width, height)
output_canvas = np.zeros((output_size[1], output_size[0], 3), dtype=np.uint8)

# Apply the perspective transformation (warp the image)
warped = cv2.warpPerspective(img, H, output_size)

# Show the final projected image in a window
cv2.imwrite('output.jpg', warped)
cv2.imshow("Projected Image (Warped)", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
