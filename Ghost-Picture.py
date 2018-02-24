import pygame

#Initialize pygame
pygame.init()

#Asks the user if they need instructions and if they do provide them
instructions = input("Do you require instructions? ").upper()

if instructions == "YES":

	print ("First, provide the name of the ghost image, next provide the name of the background image, then provide the the x and y co-ordinates at which the ghost will be centered.")

#Gets name of ghost image
ghost_image_name = input("Please enter the name of the ghost image: ")

#Error checks name of ghost image

if ghost_image_name != "ghost_with_broom.bmp" and ghost_image_name !="ghost_with_crutches.bmp" and ghost_image_name != "ghost_with_frame.bmp":

	print ("First, provide the name of the ghost image, next provide the name of the background image, then provide the the x and y co-ordinates at which the ghost will be centered.")

	pygame.quit()

	quit()

else:
#Loads ghost image 
	ghost_image = pygame.image.load(ghost_image_name)

#Gets name of background image
	background_image_name = input("Please enter the name of the background image: ")

#Error checks name of background image

	if background_image_name != "abandoned_circus.bmp" and background_image_name !="abandoned_homestead.bmp" and background_image_name != "abandoned_plant.bmp":

		print ("First, provide the name of the ghost image, next provide the name of the background image, then provide the the x and y co-ordinates at which the ghost will be centered.")

		pygame.quit()

		quit()

	else:
	
#Loads background image
		background_image = pygame.image.load(background_image_name)

#Gets dimensions of background image
		(width, height) = background_image.get_rect().size

#Gets dimensions of ghost image	
		(Gwidth, Gheight) = ghost_image.get_rect().size


#Gets x-coordinate to centre the ghost image at
		x_coordinate = int(input("Please enter the x-coordinate at which the ghost will be centered: "))

#Error checks x-coordinate
		while x_coordinate < 0 or x_coordinate > width:
			print("Please enter a valid x coordinate (greater than zero and less than image width): ", end = '')
			x_coordinate = int(input())

#Gets y-coordinate to centre the ghost image at
		y_coordinate = int(input("Please enter the y-coordinate at which the ghost will be centered: "))
#Error checks y-coordinate
		while y_coordinate < 0 or y_coordinate > height:
			print("Please enter a valid y coordinate (greater than zero and less than image height): ", end = '')
			y_coordinate = int(input())



#Sets display window to the dimensions of the background image
		window = pygame.display.set_mode((width, height))

#Displays background image in the display window 
		window.blit(background_image, (0,0))

#Gives x-coordinate and y-coordiante new values so that the ghost will be at the centre of the specified coordinates 

		x_coordinate = int(x_coordinate - (Gwidth/2))

		y_coordinate = int(y_coordinate - (Gheight/2))

#Goes through every vertical pixel of the ghost
		for i in range (Gheight):

#Goes through every horizontal pixel of the ghost

			for j in range (Gwidth):

#Makes sure x-coordinate and y-coordinate are greater than zero and less than the respective width and height of the ghost image

				if (x_coordinate + j > 0) and (x_coordinate + j < width) and (y_coordinate + i > 0) and (y_coordinate + i < height):

#Gets RGB values of each pixel in the ghost image
					(Gred,Ggreen,Gblue,_) = ghost_image.get_at ((j,i))

#Gets RGB values of each pixel in the background image
					(Bred, Bgreen, Bblue, _) = background_image.get_at ((j+ x_coordinate, i + y_coordinate ))

#Averages the RGB values of every non pure green pixel in the ghost image to make ghost translucent
					if (Gred != 0) and (Ggreen != 255) and (Gblue != 0):

						GredAverage = (Gred + Bred) /2

						GgreenAverage = (Ggreen + Bgreen) /2

						GblueAverage = (Gblue + Bblue) /2

#Sets the color of all the ghost image pixels to the RGB  average and displays the ghost over the background image 

						window.set_at((x_coordinate + j, y_coordinate + i), (GredAverage, GgreenAverage, GblueAverage))


#Keeps display window open until user manually exits the window	   
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	pygame.display.update()
