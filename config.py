
LOCK_SERVO_PIN = 18

LOCK_SERVO_UNLOCKED = 2000
LOCK_SERVO_LOCKED   = 1100

# Pi GPIO port which is connected to the button.
BUTTON_PIN = 25

BUTTON_DOWN = False  # Low signal
BUTTON_UP   = True   # High signal


POSITIVE_THRESHOLD = 2000.0

# File to save and load face recognizer model.
TRAINING_FILE = 'training.xml'

# Directories which contain the positive and negative training image data.
POSITIVE_DIR = './training/positive'
NEGATIVE_DIR = './training/negative'


POSITIVE_LABEL = 1
NEGATIVE_LABEL = 2


FACE_WIDTH  = 92
FACE_HEIGHT = 112

HAAR_FACES         = 'haarcascade_frontalface_alt.xml'
HAAR_SCALE_FACTOR  = 1.3
HAAR_MIN_NEIGHBORS = 4
HAAR_MIN_SIZE      = (30, 30)

# Filename to use when saving the most recently captured image for debugging.
DEBUG_IMAGE = 'capture.pgm'

def get_camera():	
	# Camera to use for capturing images.
	# Use this code for capturing from the Pi camera:
	import picam
	return picam.OpenCVCapture()
	# Use this code for capturing from a webcam:
	# import webcam
	# return webcam.OpenCVCapture(device_id=0)
