import glob
import os
import sys
import select
import cv2
import hardware
import config
import face



POSITIVE_FILE_PREFIX = 'positive_'


def is_letter_input(letter):
	if select.select([sys.stdin,],[],[],0.0)[0]:
		input_char = sys.stdin.read(1)
		return input_char.lower() == letter.lower()
	return False


if __name__ == '__main__':
	camera = config.get_camera()
	box = hardware.Box()
	if not os.path.exists(config.POSITIVE_DIR):
		os.makedirs(config.POSITIVE_DIR)
	
	files = sorted(glob.glob(os.path.join(config.POSITIVE_DIR, 
		POSITIVE_FILE_PREFIX + '[0-9][0-9][0-9].pgm')))
	count = 0
	if len(files) > 0:
		count = int(files[-1][-7:-4])+1
	print 'Capturing positive training images.'
	print 'Press button or type c (and press enter) to capture an image.'
	print 'Press Ctrl-C to quit.'
	while True:
		
		if box.is_button_up() or is_letter_input('c'):
			print 'Capturing image...'
			image = camera.read()
			image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
			result = face.detect_single(image)
			if result is None:
				print 'Could not detect single face!  Check the image in capture.pgm' \
					  ' to see what was captured and try again with only one face visible.'
				continue
			x, y, w, h = result
			
			crop = face.crop(image, x, y, w, h)
			# Save image to file.
			filename = os.path.join(config.POSITIVE_DIR, POSITIVE_FILE_PREFIX + '%03d.pgm' % count)
			cv2.imwrite(filename, crop)
			print 'Found face and wrote training image', filename
			count += 1
