from PIL import ImageGrab, ImageOps
from pynput.keyboard import Key, Controller
import time
from numpy import *
import keyboard as kb

keyboard = Controller()

class Coordinates():
	hitZone = (530, 390,
	640, 500)


class Vars():
	donNum = 0
	katsuNum = 0
	awaitInput = True
	canPlay = False
	timeToWait = 0.05

def hitDon():
	print("Don!")
	if (Vars.donNum == 0):
		keyboard.press('f')
		time.sleep(Vars.timeToWait)
		keyboard.release('f')
		Vars.donNum += 1
	else:
		keyboard.press('j')
		time.sleep(Vars.timeToWait)
		keyboard.release('j')
		Vars.donNum -= 1

	# print("Done")


def hitKatsu():
	print("Katsu!")
	if (Vars.katsuNum == 0):
		keyboard.press('d')
		time.sleep(Vars.timeToWait)
		keyboard.release('d')
		Vars.katsuNum += 1
	else:
		keyboard.press('k')
		time.sleep(Vars.timeToWait)
		keyboard.release('k')
		Vars.katsuNum -= 1

	# print("Done")


def play():

	image = ImageGrab.grab(Coordinates.hitZone)
	image.mode = "RGB"
	opImage = ImageOps.solarize(image, 8)

	ar = array(opImage.getcolors(10000))

	pixel = opImage.getpixel((1, 5))
	pixel2 = opImage.getpixel((5, 5))
	pixel3 = opImage.getpixel((10, 5))

	# print(pixel)

	if ((pixel[0] < 50 and pixel[1] > 150 and pixel[2] > 150)
	or (pixel2[0] < 50 and pixel2[1] > 150 and pixel2[2] > 150)
	or (pixel3[0] < 50 and pixel3[1] > 150 and pixel3[2] > 150)):
		hitDon()
	elif ((pixel[0] > 150 and pixel[1] > 100 and pixel[2] < 100)
	or (pixel2[0] > 150 and pixel2[1] > 100 and pixel2[2] < 100)
	or (pixel3[0] > 150 and pixel3[1] > 100 and pixel3[2] < 100)):
		hitKatsu()

	if (kb.is_pressed('1')):
		exit()

def main():
	while (Vars.awaitInput):
		print("Waiting for input...")
		if (kb.is_pressed('0')):
			Vars.awaitInput = False
			while (True):
				play()

	# image = ImageGrab.grab(Coordinates.hitZone)
	# image.mode = "RGB"
	# opImage = ImageOps.solarize(image, 8)

	# opImage.show()


main()