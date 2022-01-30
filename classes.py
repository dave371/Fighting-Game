import pygame
from os import path
from settings import *

"""
Defining Sprite Classes
"""

class Character(pygame.sprite.Sprite):
    """
    This is the character class.
    """

    def __init__(self, ground, character_choice, height):

        """
        This is the constructor for the class
        """

        # Initiziling the spirte
        pygame.sprite.Sprite.__init__(self)

        # Initializing the character choice variable
        self.character_choice = character_choice

        # Initializing character health
        self.character_health = 100

        # Setting the ground object
        self.ground = ground

        # Setting the ground height
        self.ground_height = height

        # Setting a direction of the sprite
        if self.character_choice == 1:
            self.facing_right = True
        elif self.character_choice == 2:
            self.facing_right = False

        # Setting our walking state
        self.walking = False

        # Setting our jumping state
        self.jumping = False

        # Setting the current frame the program is on
        self.current_frame = 0

        # Setting attack frame
        self.attacking_frame = 0

        # Setting the light attack animation flag
        self.light_attack_animation = 0

        # Setting the heavy attack animation flag
        self.heavy_attack_animation = 0

        # Setting the last updated frame
        self.last_update = 0

        # Setting the last time attack frame was updates
        self.attack_last = 0

        # Setting up a jumping flag
        self.jumping_flag = 0

        # Loading our images
        if self.character_choice == 1:
            self.load_images_character_one()
        elif self.character_choice == 2:
            self.load_images_character_two()

        # Getting an image from the sprite sheet
        self.image = self.idle_frames_right[0]

        # Converting the initial image into a rectangle
        self.rect = self.image.get_rect()

        # Setting the object to the middle of screen
        if self.character_choice == 1:
            self.rect.center = (int(WIDTH / 2) - 100, int(self.ground_height))
            # Setting the vector for the position for character one
            self.pos = vec(int(WIDTH / 2) - 100, int(self.ground_height))
        elif self.character_choice == 2:
            self.rect.center = (int(WIDTH / 2) + 100, int(self.ground_height))
            # Setting the vector for the position for charcter two
            self.pos = vec(int(WIDTH / 2) + 100, int(self.ground_height))

        # Setting the velocity and the acceleration vectors
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        """
        This method makes the player jump once
        """
        # Checking to see if we are standing on something, then we can jump if we are standing on something

        # Going below to the player to see if it is standing on something 
        self.rect.x += 1

        # Checking to see if the player is colliding with the ground
        hits = pygame.sprite.spritecollide(self, self.ground, False)

        # The goes back to current x position
        self.rect.x -= 1

        # If the player is standing on something then we can jump
        if hits:
            self.jumping_flag = 1

    def light(self, now):
        """
        This method will handle the light attack animation
        """
        # Implementing a cool down timer
        if now - self.attack_last > 750:
            # Update the last time the attack animation went through
            self.attack_last = now
            # Checks to see if the heavy attack animation is going
            if self.heavy_attack_animation == False:
                # Set the light attack animation to true
                self.light_attack_animation = True

    def heavy(self, now):
        """
        This method will handle the heavy attack
        """
        # Implementing a cool down timer
        if now - self.attack_last > 1000:
            # Update the last time the attack animation went through
            self.attack_last = now
            # Checks to see if the light attack animation is going
            if self.light_attack_animation == False:
                # Sets heavy attack animation to true
                self.heavy_attack_animation = True

    def load_images_character_one(self):
        """
        This method will load in the the images used as frames for character one
        """

        # Setting up main path, the image path, and character path
        self.main_dir = path.dirname(__file__)
        self.img_dir = path.join(self.main_dir, "images")
        self.character = path.join(self.img_dir, "character_one")

        # Setting idle frame folder path
        self.idle_path = path.join(self.character, "idle_frames")
        
        # Loading in idle frames
        self.idle_frame_one = pygame.image.load(path.join(self.idle_path, "0.png")).convert()
        self.idle_frame_two = pygame.image.load(path.join(self.idle_path, "1.png")).convert()
        self.idle_frame_three = pygame.image.load(path.join(self.idle_path, "2.png")).convert()
        self.idle_frame_four = pygame.image.load(path.join(self.idle_path, "3.png")).convert()

        # Setting walking/runnning folder path
        self.run_path = path.join(self.character, "running_frames")

        # Loading in walking/running frames
        self.running_frame_right_one = pygame.image.load(path.join(self.run_path, "0.png")).convert()
        self.running_frame_right_two = pygame.image.load(path.join(self.run_path, "1.png")).convert()
        self.running_frame_right_three = pygame.image.load(path.join(self.run_path, "2.png")).convert()
        self.running_frame_right_four = pygame.image.load(path.join(self.run_path, "3.png")).convert()
        self.running_frame_right_five = pygame.image.load(path.join(self.run_path, "4.png")).convert()
        self.running_frame_right_six = pygame.image.load(path.join(self.run_path, "5.png")).convert()
        self.running_frame_right_seven = pygame.image.load(path.join(self.run_path, "6.png")).convert()
        self.running_frame_right_eight = pygame.image.load(path.join(self.run_path, "7.png")).convert()

        # Setting the jump folder path
        self.jump_path = path.join(self.character, "jump_frames")

        # Loading in the jumping frames
        self.jump_frame_one = pygame.image.load(path.join(self.jump_path, "0.png")).convert()
        self.jump_frame_two = pygame.image.load(path.join(self.jump_path, "1.png")).convert()

        # Setting the falling folder path
        self.fall_path = path.join(self.character, "falling_frames")

        # Loading in the falling frames
        self.fall_frame_one = pygame.image.load(path.join(self.fall_path, "0.png")).convert()
        self.fall_frame_two = pygame.image.load(path.join(self.fall_path, "1.png")).convert()

        # Setting the light attack folder path
        self.l_attack_path = path.join(self.character, "light_attack_frames")

        # Loading in right light attack attack frames
        self.l_attack_frame_right_one = pygame.image.load(path.join(self.l_attack_path, "0.png")).convert()
        self.l_attack_frame_right_two = pygame.image.load(path.join(self.l_attack_path, "1.png")).convert()
        self.l_attack_frame_right_three = pygame.image.load(path.join(self.l_attack_path, "2.png")).convert()
        self.l_attack_frame_right_four = pygame.image.load(path.join(self.l_attack_path, "3.png")).convert()

        # Setting the heavy attack folder path
        self.h_attack_path = path.join(self.character, "heavy_attack_frames")

        # Loading in the right heavy attack frames
        self.h_attack_frame_right_one = pygame.image.load(path.join(self.h_attack_path, "0.png")).convert()
        self.h_attack_frame_right_two = pygame.image.load(path.join(self.h_attack_path, "1.png")).convert()
        self.h_attack_frame_right_three = pygame.image.load(path.join(self.h_attack_path, "2.png")).convert()
        self.h_attack_frame_right_four = pygame.image.load(path.join(self.h_attack_path, "3.png")).convert()

        """
        Idle frames
        """

        # Loading the right idle frames into a list
        self.idle_frames_right = [self.idle_frame_one,
                            self.idle_frame_two,
                            self.idle_frame_three,
                            self.idle_frame_four]

        # Setting color key for the all idle frames
        for frame in self.idle_frames_right:
            frame.set_colorkey(BLACK)

        # Loading the left idle frames into a list
        # Initializing the left idle frames list
        self.idle_frames_left = []

        # Looping through the right idle frames and flipping to the make them face left, then adding the color key to them
        for frame in self.idle_frames_right:
            self.idle_frames_left.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)

        """
        Walking/Running frames
        """

        # Loading the walking/running right frames into a list
        self.running_frames_right = [self.running_frame_right_one,
                               self.running_frame_right_two,
                               self.running_frame_right_three,
                               self.running_frame_right_four,
                               self.running_frame_right_five,
                               self.running_frame_right_six,
                               self.running_frame_right_seven,
                               self.running_frame_right_eight]
        
        # Setting the color key for all the walking/running frames
        for frame in self.running_frames_right:
            frame.set_colorkey(BLACK)

        # Loading the walking/running left frames into a list
        # Initializing a list for the left walking/running frames
        self.running_frames_left = []

        # Looping through the right running frames and fliping them to face right, and adding a color key
        for frame in self.running_frames_right:
            self.running_frames_left.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)


        """
        Jumping frames
        """

        # Loading the right jump frames into a list
        self.jump_frames_right = [self.jump_frame_one,
                                  self.jump_frame_two]

        # Setting the color key for all the right jump frames
        for frame in self.jump_frames_right:
            frame.set_colorkey(BLACK)

        # Loading the left jump frames into a list
        # Initializing the left jump frame list
        self.jump_frames_left = []

        # Looping through the right jump frames and flipping them, then we are adding it to the left jump frame list
        for frame in self.jump_frames_right:
            self.jump_frames_left.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)

        """
        Fall frames
        """

        # Loading the right fall frames into a list
        self.fall_frames_right = [self.fall_frame_one,
                                  self.fall_frame_two]
        
        # Setting the color key for all the right fall frames
        for frame in self.fall_frames_right:
            frame.set_colorkey(BLACK)

        # Loading the left fall frames into a list
        # Initializing the left fall frame list
        self.fall_frames_left = []

        # Looping through the right fall frames and flipping them, then we are adding it to the left fall frame list
        for frame in self.fall_frames_right:
            self.fall_frames_left.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)

        """
        Light attack frames
        """

        # Loading in the right light attack frames into a list
        self.r_light_attack_frames = [self.l_attack_frame_right_one,
                                      self.l_attack_frame_right_two,
                                      self.l_attack_frame_right_three,
                                      self.l_attack_frame_right_four]

        # Setting the color key for the right light attack frames
        for frame in self.r_light_attack_frames:
            frame.set_colorkey(BLACK)

        # Loading the left light attack frames into a list
        # Initializing the left attack frames list
        self.l_light_attack_frames = []

        # Looping through the right light attack frames and flipping them to face the left side. Also changing the color key
        for frame in self.r_light_attack_frames:
            self.l_light_attack_frames.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)

        """
        Heavy attack frames
        """

        #Loading all the right heavy attack frames into a list
        self.r_heavy_attack_frames = [self.h_attack_frame_right_one,
                                      self.h_attack_frame_right_two,
                                      self.h_attack_frame_right_three,
                                      self.h_attack_frame_right_four]

        # Setting the color key for the right heavy attack frames
        for frame in self.r_heavy_attack_frames:
            frame.set_colorkey(BLACK)

        # Loading the left heavy attack frames into a list
        # Initialized the left heavy attack frames list
        self.l_heavy_attack_frames = []

        # Looping through the right heavy attack frames and then fliping them to turn left and adding it to the list
        # Also, setting the color key of the frames
        for frame in self.r_heavy_attack_frames:
            self.l_heavy_attack_frames.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)

    def load_images_character_two(self):
        """
        This method will load in the the images used as frames for character two
        """

        # Setting up main path, the image path, and character path
        self.main_dir = path.dirname(__file__)
        self.img_dir = path.join(self.main_dir, "images")
        self.character = path.join(self.img_dir, "character_two")

        # Setting idle frame folder path
        self.idle_path = path.join(self.character, "idle_frames")
        
        # Loading in idle frames
        self.idle_frame_one = pygame.image.load(path.join(self.idle_path, "0.png")).convert()
        self.idle_frame_two = pygame.image.load(path.join(self.idle_path, "1.png")).convert()
        self.idle_frame_three = pygame.image.load(path.join(self.idle_path, "2.png")).convert()
        self.idle_frame_four = pygame.image.load(path.join(self.idle_path, "3.png")).convert()
        self.idle_frame_five = pygame.image.load(path.join(self.idle_path, "4.png")).convert()
        self.idle_frame_six = pygame.image.load(path.join(self.idle_path, "5.png")).convert()
        self.idle_frame_seven = pygame.image.load(path.join(self.idle_path, "6.png")).convert()
        self.idle_frame_eight = pygame.image.load(path.join(self.idle_path, "7.png")).convert()

        # Setting walking/runnning folder path
        self.run_path = path.join(self.character, "running_frames")

        # Loading in walking/running frames
        self.running_frame_right_one = pygame.image.load(path.join(self.run_path, "0.png")).convert()
        self.running_frame_right_two = pygame.image.load(path.join(self.run_path, "1.png")).convert()
        self.running_frame_right_three = pygame.image.load(path.join(self.run_path, "2.png")).convert()
        self.running_frame_right_four = pygame.image.load(path.join(self.run_path, "3.png")).convert()
        self.running_frame_right_five = pygame.image.load(path.join(self.run_path, "4.png")).convert()
        self.running_frame_right_six = pygame.image.load(path.join(self.run_path, "5.png")).convert()
        self.running_frame_right_seven = pygame.image.load(path.join(self.run_path, "6.png")).convert()
        self.running_frame_right_eight = pygame.image.load(path.join(self.run_path, "7.png")).convert()

        # Setting the jump folder path
        self.jump_path = path.join(self.character, "jump_frames")

        # Loading in the jumping frames
        self.jump_frame_one = pygame.image.load(path.join(self.jump_path, "0.png")).convert()
        self.jump_frame_two = pygame.image.load(path.join(self.jump_path, "1.png")).convert()

        # Setting the falling folder path
        self.fall_path = path.join(self.character, "falling_frames")

        # Loading in the falling frames
        self.fall_frame_one = pygame.image.load(path.join(self.fall_path, "0.png")).convert()
        self.fall_frame_two = pygame.image.load(path.join(self.fall_path, "1.png")).convert()

        # Setting the light attack folder path
        self.l_attack_path = path.join(self.character, "light_attack_frames")

        # Loading in right light attack attack frames
        self.l_attack_frame_right_one = pygame.image.load(path.join(self.l_attack_path, "0.png")).convert()
        self.l_attack_frame_right_two = pygame.image.load(path.join(self.l_attack_path, "1.png")).convert()
        self.l_attack_frame_right_three = pygame.image.load(path.join(self.l_attack_path, "2.png")).convert()
        self.l_attack_frame_right_four = pygame.image.load(path.join(self.l_attack_path, "3.png")).convert()
        self.l_attack_frame_right_five = pygame.image.load(path.join(self.l_attack_path, "4.png")).convert()
        self.l_attack_frame_right_six = pygame.image.load(path.join(self.l_attack_path, "5.png")).convert()

        # Setting the heavy attack folder path
        self.h_attack_path = path.join(self.character, "heavy_attack_frames")

        # Loading in the right heavy attack frames
        self.h_attack_frame_right_one = pygame.image.load(path.join(self.h_attack_path, "0.png")).convert()
        self.h_attack_frame_right_two = pygame.image.load(path.join(self.h_attack_path, "1.png")).convert()
        self.h_attack_frame_right_three = pygame.image.load(path.join(self.h_attack_path, "2.png")).convert()
        self.h_attack_frame_right_four = pygame.image.load(path.join(self.h_attack_path, "3.png")).convert()
        self.h_attack_frame_right_five = pygame.image.load(path.join(self.h_attack_path, "4.png")).convert()
        self.h_attack_frame_right_six = pygame.image.load(path.join(self.h_attack_path, "5.png")).convert()

        """
        Idle frames
        """

        # Loading the right idle frames into a list
        self.idle_frames_right = [self.idle_frame_one,
                            self.idle_frame_two,
                            self.idle_frame_three,
                            self.idle_frame_four,
                            self.idle_frame_five,
                            self.idle_frame_six,
                            self.idle_frame_seven,
                            self.idle_frame_eight]

        # Setting color key for the all idle frames
        for frame in self.idle_frames_right:
            frame.set_colorkey(BLACK)

        # Loading the left idle frames into a list
        # Initializing the left idle frames list
        self.idle_frames_left = []

        # Looping through the right idle frames and flipping to the make them face left, then adding the color key to them
        for frame in self.idle_frames_right:
            self.idle_frames_left.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)

        """
        Walking/Running frames
        """

        # Loading the walking/running right frames into a list
        self.running_frames_right = [self.running_frame_right_one,
                               self.running_frame_right_two,
                               self.running_frame_right_three,
                               self.running_frame_right_four,
                               self.running_frame_right_five,
                               self.running_frame_right_six,
                               self.running_frame_right_seven,
                               self.running_frame_right_eight]
        
        # Setting the color key for all the walking/running frames
        for frame in self.running_frames_right:
            frame.set_colorkey(BLACK)

        # Loading the walking/running left frames into a list
        # Initializing a list for the left walking/running frames
        self.running_frames_left = []

        # Looping through the right running frames and fliping them to face right, and adding a color key
        for frame in self.running_frames_right:
            self.running_frames_left.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)

        """
        Jump frames
        """

        # Loading the right jump frames into a list
        self.jump_frames_right = [self.jump_frame_one,
                                  self.jump_frame_two]

        # Setting the color key for all the right jump frames
        for frame in self.jump_frames_right:
            frame.set_colorkey(BLACK)

        # Loading the left jump frames into a list
        # Initializing the left jump frame list
        self.jump_frames_left = []

        # Looping through the right jump frames and flipping them, then we are adding it to the left jump frame list
        for frame in self.jump_frames_right:
            self.jump_frames_left.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)

        """
        Fall frames
        """

        # Loading the right fall frames into a list
        self.fall_frames_right = [self.fall_frame_one,
                                  self.fall_frame_two]
        
        # Setting the color key for all the right fall frames
        for frame in self.fall_frames_right:
            frame.set_colorkey(BLACK)

        # Loading the left fall frames into a list
        # Initializing the left fall frame list
        self.fall_frames_left = []

        # Looping through the right fall frames and flipping them, then we are adding it to the left fall frame list
        for frame in self.fall_frames_right:
            self.fall_frames_left.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)

        """
        Light attack frames
        """

        # Loading in the right light attack frames into a list
        self.r_light_attack_frames = [self.l_attack_frame_right_one,
                                      self.l_attack_frame_right_two,
                                      self.l_attack_frame_right_three,
                                      self.l_attack_frame_right_four,
                                      self.l_attack_frame_right_five,
                                      self.l_attack_frame_right_six]

        # Setting the color key for the right light attack frames
        for frame in self.r_light_attack_frames:
            frame.set_colorkey(BLACK)

        # Loading the left light attack frames into a list
        # Initializing the left attack frames list
        self.l_light_attack_frames = []

        # Looping through the right light attack frames and flipping them to face the left side. Also changing the color key
        for frame in self.r_light_attack_frames:
            self.l_light_attack_frames.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)

        """
        Heavy attack frames
        """

        #Loading all the right heavy attack frames into a list
        self.r_heavy_attack_frames = [self.h_attack_frame_right_one,
                                      self.h_attack_frame_right_two,
                                      self.h_attack_frame_right_three,
                                      self.h_attack_frame_right_four,
                                      self.h_attack_frame_right_five,
                                      self.h_attack_frame_right_six]

        # Setting the color key for the right heavy attack frames
        for frame in self.r_heavy_attack_frames:
            frame.set_colorkey(BLACK)

        # Loading the left heavy attack frames into a list
        # Initialized the left heavy attack frames list
        self.l_heavy_attack_frames = []

        # Looping through the right heavy attack frames and then fliping them to turn left and adding it to the list
        # Also, setting the color key of the frames
        for frame in self.r_heavy_attack_frames:
            self.l_heavy_attack_frames.append(pygame.transform.flip(frame, True, False))
            frame.set_colorkey(BLACK)

    def update(self):

        """
        This method controls the actions of player one
        """

        # If the jumping flag was triggered, set the y velocity
        if self.jumping_flag == 1:
            self.vel.y = -15
            self.jumping_flag = 0

        # Calling the animation method
        self.animate()

        # Setting the base velocity for player one
        self.acc = vec(0, .5)

        # Setting the players friction
        player_friction = -.11

        # Getting the keys that are pressed
        keys = pygame.key.get_pressed() 

        if self.character_choice == 1:
            # Controlling what happens when the left arrow key is pressed
            if keys[pygame.K_a]:
                self.acc.x = -0.5
                self.facing_right = False

            # Controlling what heppens when the right arrow key is pressed
            if keys[pygame.K_d]:
                self.acc.x = 0.5
                self.facing_right = True
        elif self.character_choice == 2:
            # Controlling what happens when the left arrow key is pressed
            if keys[pygame.K_j]:
                self.acc.x = -0.5
                self.facing_right = False

            # Controlling what heppens when the right arrow key is pressed
            if keys[pygame.K_l]:
                self.acc.x = 0.5
                self.facing_right = True

        # Setting the accleration with respect to friction
        self.acc.x += self.vel.x * player_friction

        # Setting the velocity
        self.vel += self.acc

        # Setting our velocity to zero
        if abs(self.vel.x) < .1:
            self.vel.x = 0

        # Setting the position (this is an equation for motion)
        self.pos += self.vel + 0.5 * self.acc

        # Setting the postion of the player
        self.rect.midbottom = self.pos
    
    def animate(self):

        """
        This method controls the animation of player one
        """

        # Getting the how many ticks since the program started
        now = pygame.time.get_ticks()

        # Seeing if the player is walking/running
        if self.vel.x != 0 and self.vel.y == 0:
            self.walking = True
        else:
            self.walking = False

        # Seeing if the player is jump
        if self.vel.y != 0:
            self.jumping = True
        else:
            self.jumping = False

        """
        Idle animation
        """

        # If the player is idle then start the idle animation
        if not self.walking and not self.walking:

            # Checks to see if its time to update the frame
            if now - self.last_update > 100:

                # Updates the last update variable
                self.last_update = now

                # Gets the current frame
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_right)

                # Gets the bottom position of the current frame
                bottom = self.rect.bottom

                # Deciding which idle frame to display left or right
                if self.facing_right:
                    # Sets the new frame
                    self.image = self.idle_frames_right[self.current_frame]
                else:
                    # Sets the new frame
                    self.image = self.idle_frames_left[self.current_frame]

                # Gets the new dimension of the new image
                self.rect = self.image.get_rect()

                # Sets the bottom position to the same position of the last frame
                self.rect.bottom = bottom

        """
        Walking/Running animation
        """

        # If the player is walking/running then start the running animation
        if self.walking:

            # Checks to see if it is time to update the frame
            if now - self.last_update > 100:

                # Update the last update variable
                self.last_update = now

                # Gets the current frame
                self.current_frame = (self.current_frame + 1) % (len(self.running_frames_left) - 1)

                # Gets the bottom position of the current frame
                bottom = self.rect.bottom

                # Deciding whether the player is walking left or right
                if self.vel.x > 0:
                    # Sets the frame to running right frame
                    self.image = self.running_frames_right[self.current_frame]
                else:

                    # Sets the frame to the running right frame
                    self.image = self.running_frames_left[self.current_frame]

                # Gets the dimension of the new frame
                self.rect = self.image.get_rect()

                # Sets the bottom position to the same position as the last frame
                self.rect.bottom = bottom

        """
        Jumping animation
        """

        # If the player is jumping then start the jumping animation or the falling animation
        if self.jumping:

            # Checks to see if the frame need to be updated
            if now - self.last_update > 50:

                # Updates the last updated variable
                self.last_update = now

                # Gets the current frame
                self.current_frame = (self.current_frame + 1) % (len(self.jump_frames_right))

                # Saves the bottom postion of the current frame
                bottom = self.rect.bottom


                # Deciding whether the player is jumping left or right
                if self.vel.x > 0:

                    # Checks to see if the player if falling
                    if self.vel.y > 0:
                        # Sets frame to the falling right frame
                        self.image = self.fall_frames_right[self.current_frame]
                    else:
                        # Set frame to the jumping right frame
                        self.image = self.jump_frames_right[self.current_frame]
                elif self.vel.x < 0:

                    # Checks to see if the player is falling
                    if self.vel.y > 0:
                        # Set frame to the falling left frame
                        self.image = self.fall_frames_left[self.current_frame]
                    else:
                        # Sets frame to the jump left frame
                        self.image = self.jump_frames_left[self.current_frame]

                # Gets the new dimension of the new frame
                self.rect = self.image.get_rect()

                # Set the position of the new frame to the same position as the last frame
                self.rect.bottom = bottom

        """
        Light attack animation
        """

        # Players light attack animation
        if self.light_attack_animation:

            # Checks to see if frame need to be updated
            if now - self.last_update > 75:

                # Updates the last update variable
                self.last_update = now

                # Increments the attacking frame
                self.attacking_frame += 1

            # Checks to see if we are going to finish the attacking animation
            if self.attacking_frame >= len(self.r_light_attack_frames):

                # Sets the attacking frame back to zero
                self.attacking_frame = 0

                # Updates the light attack animation flag
                self.light_attack_animation = False

            # Getting the bottom position of the last frame
            bottom = self.rect.bottom
            
            # Checks to see which way we are facing
            if self.facing_right:
                # If we are facing right, then pull the right attacking frames
                self.image = self.r_light_attack_frames[self.attacking_frame]
            else:
                # If we are facing left, then pull the left attacking frames
                self.image = self.l_light_attack_frames[self.attacking_frame]

            # Updates our rect object for the new frame
            self.rect = self.image.get_rect()

            # Sets the new frame to the position of the previos frame
            self.rect.bottom = bottom
    
        """
        Heavy attack animation
        """

        # Players heavy attack animation
        if self.heavy_attack_animation:

            # Checks to see if frame need to be updated
            if now - self.last_update > 95:

                # Updates the last update variable
                self.last_update = now

                # Increments the attacking frame
                self.attacking_frame += 1

            # Checks to see if we are going to finish the attacking animation
            if self.attacking_frame >= len(self.r_heavy_attack_frames):

                # Sets the attacking frame back to zero
                self.attacking_frame = 0

                # Updates the light attack animation flag
                self.heavy_attack_animation = False

            # Getting the bottom position of the last frame
            bottom = self.rect.bottom
            
            # Checks to see which way we are facing
            if self.facing_right:
                # If we are facing right, then pull the right attacking frames
                self.image = self.r_heavy_attack_frames[self.attacking_frame]
            else:
                # If we are facing left, then pull the left attacking frames
                self.image = self.l_heavy_attack_frames[self.attacking_frame]

            # Updates our rect object for the new frame
            self.rect = self.image.get_rect()

            # Sets the new frame to the position of the previos frame
            self.rect.bottom = bottom

class Ground(pygame.sprite.Sprite):
    """
    This calls is going to make a ground platform
    """
    # Constructor
    def __init__(self, height):

        # Initializing the object as a sprite
        pygame.sprite.Sprite.__init__(self)

        # Initializing height variables
        self.height = height

        # Creating the ground dimensions
        self.image = pygame.Surface((10000, 1))

        # Giving it a color
        self.image.fill(GREEN)

        # Turing it to a rectange
        self.rect = self.image.get_rect()

        # Setting it on the screen
        self.rect.center = (int(WIDTH / 2), self.height)

class Boundries(pygame.sprite.Sprite):

    def __init__(self, width, height, positionx, positiony):
        # Making a sprite class
        pygame.sprite.Sprite.__init__(self)
        # Making an image
        self.image = pygame.Surface((width, height))
        # Making it the color green
        self.image.fill(GREEN)
        # Getting a rect of our image
        self.rect = self.image.get_rect()
        # Setting the position of the boundry
        self.rect.center = (positionx, positiony)

"""
Defining Regular Classes
"""

class Button():
    """
    This class will make buttons
    """
    
    # Constructor
    def __init__(self, color, x, y, width, height, text=''):
        # Setting the button color
        self.color = color
        # Setting the x vaule
        self.x = x
        # Setting the y vaule
        self.y = y
        # Setting the width
        self.width = width
        # Setting the height
        self.height = height
        # Setting the text, if there is any
        self.text = text

    def draw(self, win):
        # Call this method to draw the button on the screen
        pygame.draw.rect(win, self.color, (int(self.x), int(self.y), self.width, self.height), 0)

        # Checks to see if there is suppose to be text on the button
        if self.text != '':
            # Setting the font for the buttons
            font = pygame.font.SysFont('comicsans', 30)
            # Rendering the text
            text = font.render(self.text, 1, (0, 0, 0))
            # Setting the text on the button
            win.blit(text, (
                int(self.x + (self.width / 2 - text.get_width() / 2)),
                int(self.y + (self.height / 2 - text.get_height() / 2))))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        # Checks to see if the mouse position is within the width of the button
        if self.x < pos[0] < self.x + self.width:
            # Checks to see if the mouse position is with the height of the button
            if self.y < pos[1] < self.y + self.height:
                # Return true
                return True
        # Else return
        return False