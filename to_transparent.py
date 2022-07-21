import os
from PIL import Image

# add google style docstrings
# add comments


def img_bg_to_transparent(img_filepath, output_dir, output_filename=None, rgb_threshold=250, compare_sign=">"):
	'''
	Load a png or jpeg image given it's filepath and convert background pixels
	(threshold based, white-ish pixels by default) into transparent pixels.
	
	Args:
		+
	Returns:
		+
 	'''

	# load image
	img = Image.open(img_filepath)
	img = img.convert("RGBA")

	# get RGBA channels
	channels = img.getdata()

	# using chosen comparison sign and RGB threshold,
	# replace valid pixels alpha channel value to 0
	new_channels = []
	for item in channels:
		if compare_sign == ">":
			if item[0] > rgb_threshold and \
			   item[1] > rgb_threshold and \
			   item[2] > rgb_threshold:
				new_channels.append((255, 255, 255, 0))
			else:
				new_channels.append(item)
		elif compare_sign == "<":
			if item[0] < rgb_threshold and \
			   item[1] < rgb_threshold and \
			   item[2] < rgb_threshold:
				new_channels.append((255, 255, 255, 0))
			else:
				new_channels.append(item)
		else:
				print('compare sign is invalid, use ">" or "<"')
				return

	# update RGBA channels
	img.putdata(new_channels)

	# get image filename from filepath
	img_file = img_filepath.split('/')[-1].split('.')[0]

	# get output image filepath depending on parameters
	if output_filename is None:
		output_img_filepath = output_dir + img_file + '.png'
	else:
		output_img_filepath = output_dir + output_filename + '.png'

	# save output image
	img.save(output_img_filepath, "PNG")
	
	# return output image filepath
	return output_img_filepath


def dir_to_transparent(input_dir, output_dir, file_type=None, verbose=True):

	# add parameter regex string for filename using re.search()

	# iterate through each file in input directory
	for img_file in os.listdir(input_dir):
		
		# check if file type is valid
		flag_process_file = False
		if file_type is None:
			if ('.png' in img_file) or ('.jpeg' in img_file):
				flag_process_file = True
		elif file_type == 'png':
			if ('.png' in img_file):
				flag_process_file = True
		elif file_type == 'jpeg':
			if ('.jpeg' in img_file):
				flag_process_file = True

		# if file type is valid, process with img_bg_to_transparent
		if flag_process_file:
			img_filepath = input_dir + img_file
			new_img_filepath = img_bg_to_transparent(img_filepath, output_dir)
			if verbose:
				print("saved new image: {}".format(new_img_filepath))
	return


def main():
	input_dir = './samples/to_transparent/input/'
	output_dir = './samples/to_transparent/output/'
	dir_to_transparent(input_dir, output_dir)


if __name__ == "__main__":
	main()







