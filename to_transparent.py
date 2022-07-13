import os
from PIL import Image


def img_to_transparent(img_file):

	img = Image.open(img_file)
	img = img.convert("RGBA")
	channels = img.getdata()
	
	rgb_threshold = 250

	new_channels = []
	for item in channels:
		if item[0] > rgb_threshold and \
		   item[1] > rgb_threshold and \
		   item[2] > rgb_threshold:
			new_channels.append((255, 255, 255, 0))
		else:
			new_channels.append(item)

	img.putdata(new_channels)
	return img


def dir_to_transparent(input_dir, output_dir):

	for img_file in os.listdir(input_dir):
		print(img_file)
		if ('.png' in img_file) or ('.jpeg' in img_file):
			img = img_to_transparent(input_dir + img_file)
			img.save(output_dir + img_file, "PNG")

	return


def main():
	input_dir = './samples/to_transparent/input/'
	output_dir = './samples/to_transparent/output/'
	dir_to_transparent(input_dir, output_dir)


if __name__ == "__main__":
	main()







