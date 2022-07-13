import os
from PIL import Image


def img_to_transparent(img_filepath, output_dir):

	img = Image.open(img_filepath)
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
	img_file = img_filepath.split('/')[-1].split('.')[0]
	output_img_filepath = output_dir + img_file + '.png'
	img.save(output_img_filepath, "PNG")
	
	return output_img_filepath


def dir_to_transparent(input_dir, output_dir):

	for img_file in os.listdir(input_dir):
		if ('.png' in img_file) or ('.jpeg' in img_file):
			img_filepath = input_dir + img_file
			new_img_filepath = img_to_transparent(img_filepath, output_dir)
			print("saved new image: {}".format(new_img_filepath))
	return


def main():
	input_dir = './samples/to_transparent/input/'
	output_dir = './samples/to_transparent/output/'
	dir_to_transparent(input_dir, output_dir)


if __name__ == "__main__":
	main()







