import pygame
import os
from settings import *
from classes import *


"""
Initializing pygame and creating the window for the game
"""
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shubh Vs. David")
clock = pygame.time.Clock()

def draw_text(surf, text, size, x, y, color = WHITE):
    # Getting font
    font = pygame.font.Font(font_name, size)
    # Rendering the text
    text_surface = font.render(text, True, color)
    # Getting a rect of our text
    text_rect = text_surface.get_rect()
    # Positioning our text
    text_rect.midtop = (int(x), int(y))
    # Display the text on the screen
    surf.blit(text_surface, text_rect)

def main_menu():
    """
    This function will control what is drawn on the screen for the main menu.
    """

    # Making the start button
    start_button = Button(WHITE, 350, 300, BUTTON_WIDTH, BUTTON_HEIGHT, "Play")
    # Making the controls button
    controls_button = Button(WHITE, 350, 345, BUTTON_WIDTH, BUTTON_HEIGHT, "Controls")
    # Making the exit button
    exit_button = Button(WHITE, 350, 390, BUTTON_WIDTH, BUTTON_HEIGHT, "Exit")

    # Setting our looping condition
    running = True

    # Screen loop
    while running:
        # Stetting our tick rate
        clock.tick(FPS)

        # Checking for user input (Event Listener)
        for event in pygame.event.get():

            # Getting mouse point position
            pos = pygame.mouse.get_pos()
            
            # Checking to see if the user hits the X-button on the game window
            if event.type == pygame.QUIT:
                # Set our loop condition to false
                running = False
                # Closes program
                pygame.quit()
                quit()
            
            # Checking to see if the user presses the mouse button down
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks to see if the click was on the start button
                if start_button.is_over(pos):
                    # Set the looping condition to false
                    running = False
                    # Calls the level selection function
                    level_selection()
                # Checks to see if the click was on the exit button
                if exit_button.is_over(pos):
                    # Closes program
                    pygame.quit()
                    quit()
                # Checks to see if the click was on the controls button  
                if controls_button.is_over(pos):
                    # Calls the controls screen function
                    controls_screen()

            # Checking mouse cursor motion
            if event.type == pygame.MOUSEMOTION:
                # Checks to see if the cursor is over the button 
                if start_button.is_over(pos):
                    # Set button color to grey
                    start_button.color = GREY
                else:
                    # Set button color to white
                    start_button.color = WHITE
                # Checks to see if the cursor is over the button 
                if exit_button.is_over(pos):
                    # Set button color to grey
                    exit_button.color = GREY
                else:
                    # Set button color to white
                    exit_button.color = WHITE
                # Checks to see if the cursor is over the button 
                if controls_button.is_over(pos):
                    # Set button color to grey
                    controls_button.color = GREY
                else:
                    # Set button color to white
                    controls_button.color = WHITE

        # Set the screen background to a black color           
        screen.fill(BLACK)
        # Print out the games name
        draw_text(screen, "Shubh Vs. David", 60, (WIDTH / 2), 150)
        # Draws the buttons
        start_button.draw(screen)
        controls_button.draw(screen)
        exit_button.draw(screen)
        # Updates the screen
        pygame.display.update()

def level_selection():
    """
    This function will control what is displayed on the level select screen. It will also handle
    logic of what map to load in for the players.
    """

    # Loading preview images for maps
    map_one_pre = pygame.image.load(os.path.join(previews, "map_one_pre.png"))
    map_two_pre = pygame.image.load(os.path.join(previews, "map_two_pre.png"))

    # Making the level one button
    level_one_button = Button(WHITE, 200, 345, BUTTON_WIDTH, BUTTON_HEIGHT, "Level 1")
    # Making the level two button
    level_two_button = Button(WHITE, 500, 345, BUTTON_WIDTH, BUTTON_HEIGHT, "Level 2")
    # Making the back button
    back_button = Button(WHITE, 20, 550, BUTTON_WIDTH, BUTTON_HEIGHT, "Back")

    # Setting the loop condition
    running = True

    # Screen loop
    while running:
        # Setting the screen tick rate
        clock.tick(FPS)

        # Checking for user input (Event Listener)
        for event in pygame.event.get():

            # Getting the mouse position
            pos = pygame.mouse.get_pos()

            # Checking to see if the user hits the X-button on the game window
            if event.type == pygame.QUIT:
                # Set loop condition to false
                running = False
                # Close program
                pygame.quit()
                quit()

            # Check if the mouse button was pressed down    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check to see if the user clicked on the level one button
                if level_one_button.is_over(pos):
                    # Set looping condition to false
                    running = False
                    # Load in the correct map for the background
                    background = pygame.image.load(os.path.join(maps_path, "map_one.png"))
                    # Call the main game function
                    main_game(background, 550)
                # Checks to see if the user clicked on the level two button
                elif level_two_button.is_over(pos):
                    # Set looping condition to false
                    running = False
                    # Load in the correct map for the background
                    background = pygame.image.load(os.path.join(maps_path, "map_two.png"))
                    # Call the main game function
                    main_game(background, 580)
                # Checks to see if the use clicked the back button
                elif back_button.is_over(pos):
                    # Set the loop condition to false
                    running = False
                    # Calls the main menu function
                    main_menu()

            # Checking mouse cursor motion
            if event.type == pygame.MOUSEMOTION:
                # Checks to see if the cursor is over the button 
                if level_one_button.is_over(pos):
                    # Set button color to grey
                    level_one_button.color = GREY
                else:
                    # Set button color to white
                    level_one_button.color = WHITE
                # Checks to see if the cursor is over the button 
                if level_two_button.is_over(pos):
                    # Set button color to grey
                    level_two_button.color = GREY
                else:
                    # Set button color to white
                    level_two_button.color = WHITE
                # Checks to see if the cursor is over the button 
                if back_button.is_over(pos):
                    # Set button color to grey
                    back_button.color = GREY
                else:
                    # Set button color to white
                    back_button.color = WHITE

        # Sets the background color to black for the screen
        screen.fill(BLACK)
        # Print out level select to the screen
        draw_text(screen, "Level Select", 60, (WIDTH / 2), 50)
        # Draws the buttons out
        level_one_button.draw(screen)
        level_two_button.draw(screen)
        back_button.draw(screen)
        # Displays the map previews
        screen.blit(map_one_pre, (175,180))
        screen.blit(map_two_pre, (475,180))
        # Updates the screen
        pygame.display.update()

def pause_screen():
    """
    This function will control what is displayed for the pause screen.
    """

    # Making the resume button
    resume_button = Button(WHITE, 350, 300, BUTTON_WIDTH, BUTTON_HEIGHT, "Resume")
    # Making the controls button
    controls_button = Button(WHITE, 350, 345, BUTTON_WIDTH, BUTTON_HEIGHT, "Controls")
    # Making the exit button
    exit_button = Button(WHITE, 350, 390, BUTTON_WIDTH, BUTTON_HEIGHT, "Exit")

    # Setting the looping condition
    running = True

    # Screen loop
    while running:

        # Setting the tick rate of the screen
        clock.tick(FPS)

        # Checking for user input (Event Listener)
        for event in pygame.event.get():

            # Getting the mouse position on the screen
            pos = pygame.mouse.get_pos()

            # Checking to see if the user hits the X-button on the game window
            if event.type == pygame.QUIT:
                # Setting the loop condition to false
                running = False
                # Close program
                pygame.quit()
                quit()

            # Checks to see if the mouse has been clicked on screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks to see if the resume button was clicked
                if resume_button.is_over(pos):
                    # Set looping condition to false
                    running = False
                # Checks to see if the exit button was clicked
                if exit_button.is_over(pos):
                    # Close program
                    pygame.quit()
                    quit()
                # Checks to see if the controls button was clicked
                if controls_button.is_over(pos):
                    # Calls the controls screen function
                    controls_screen()

            # Checking mouse cursor motion
            if event.type == pygame.MOUSEMOTION:
                # Checks to see if the cursor is over the button 
                if resume_button.is_over(pos):
                    # Set button color to grey
                    resume_button.color = GREY
                else:
                    # Set button color to white
                    resume_button.color = WHITE
                # Checks to see if the cursor is over the button 
                if controls_button.is_over(pos):
                    # Set button color to grey
                    controls_button.color = GREY
                else:
                    # Set button color to white
                    controls_button.color = WHITE
                # Checks to see if the cursor is over the button 
                if exit_button.is_over(pos):
                    # Set button color to grey
                    exit_button.color = GREY
                else:
                    # Set button color to white
                    exit_button.color = WHITE

        # Sets the background color to black for the screen
        screen.fill(BLACK)
        # Prints "Paused" on the screen
        draw_text(screen, "Pasued", 60, (WIDTH / 2), 150)
        # Draws buttons on the screen
        resume_button.draw(screen)
        controls_button.draw(screen)
        exit_button.draw(screen)
        # Updates the screen
        pygame.display.update()

def controls_screen():
    """
    This function will control what is displayed on the screen. In this case all the control for the
    players movement and attacks are shown.
    """

    # Loading in the keyboard key images
    a_key = pygame.image.load(os.path.join(keys, "a_key.png"))
    w_key = pygame.image.load(os.path.join(keys, "w_key.png"))
    d_key = pygame.image.load(os.path.join(keys, "d_key.png"))
    q_key = pygame.image.load(os.path.join(keys, "q_key.png"))
    e_key = pygame.image.load(os.path.join(keys, "e_key.png"))
    i_key = pygame.image.load(os.path.join(keys, "i_key.png"))
    j_key = pygame.image.load(os.path.join(keys, "j_key.png"))
    l_key = pygame.image.load(os.path.join(keys, "e_key.png"))
    u_key = pygame.image.load(os.path.join(keys, "u_key.png"))
    o_key = pygame.image.load(os.path.join(keys, "o_key.png"))

    # Making a back button
    back_button = Button(WHITE, 20, 550, BUTTON_WIDTH, BUTTON_HEIGHT, "Back")

    # Setting looping condition
    running = True

    # Screen loop
    while running:

        # Setting the tick rate for the screen
        clock.tick(FPS)

        # Checks for user input (Event Listener)
        for event in pygame.event.get():

            # Gets the mouse position on the screen
            pos = pygame.mouse.get_pos()

           # Checking to see if the user hits the X-button on the game window
            if event.type == pygame.QUIT:
                # Set the looping condition to false
                running = False
                # Close program
                pygame.quit()
                quit()
            
            # Checks to see if the mouse has been clicked on screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the back button is clicked on
                if back_button.is_over(pos):
                    # Set the loop condtition to false
                    running = False

            # Checking mouse cursor motion
            if event.type == pygame.MOUSEMOTION:
                # Checks to see if the cursor is over the button 
                if back_button.is_over(pos):
                    # Set button color to grey
                    back_button.color = GREY
                else:
                    # Set button color to white
                    back_button.color = WHITE
    
        # Sets the background color to black for the screen
        screen.fill(BLACK)
        # Draws the back button
        back_button.draw(screen)
        # Prints "Controls" on the screen
        draw_text(screen, "Controls", 45, (WIDTH / 2) - 20,20)

        """
        Drawing player one controls
        """

        # Drawing player one on the screen
        draw_text(screen, "Player One:", 35, (WIDTH * (1/9)), 75)
        #Drawing movement on the screen
        draw_text(screen, "Movement", 35, (WIDTH * (1/9.5)), 150)
        # Displaying the a key image and drawing the function of it
        screen.blit(a_key, ((WIDTH * (1/75)),200))
        draw_text(screen, "Backward", 30,(WIDTH * (1/7)),206)
        # Displaying the w key image and drawing the function of it
        screen.blit(w_key, ((WIDTH * (1/75)),240))
        draw_text(screen, "Jump", 30,(WIDTH * (1/9)),246)
        # Displaying the d key image and drawing the function of it
        screen.blit(d_key, ((WIDTH * (1/75)),280))
        draw_text(screen, "Forward", 30,(WIDTH * (1/7.5)),286)
        #Drawing Attacking on the screen
        draw_text(screen, "Attacking", 35, (WIDTH * (1/11)), 350)
        # Displaying the q key image and drawing the function of it
        screen.blit(q_key, ((WIDTH * (1/75)),400))
        draw_text(screen, "Light", 30,(WIDTH * (1/9)),406)
        # Displaying the e key image and drawing the function of it
        screen.blit(e_key, ((WIDTH * (1/75)),440))
        draw_text(screen, "Heavy", 30,(WIDTH * (1/8.5)),446)

        """
        Drawing player one controls
        """

        # Drawing player one on the screen
        draw_text(screen, "Player Two:", 35, (WIDTH * (7/9)), 75)
        #Drawing movement on the screen
        draw_text(screen, "Movement", 35, (WIDTH * (7.3/9.5)), 150)
        # Displaying the j key image and drawing the function of it
        screen.blit(j_key, ((WIDTH * (50.5/75)),200))
        draw_text(screen, "Backward", 30,(WIDTH * (5.6/7)),206)
        # Displaying the i key image and drawing the function of it
        screen.blit(i_key, ((WIDTH * (50.5/75)),240))
        draw_text(screen, "Jump", 30,(WIDTH * (6.9/9)),246)
        # Displaying the l key image and drawing the function of it
        screen.blit(l_key, ((WIDTH * (50.5/75)),280))
        draw_text(screen, "Forward", 30,(WIDTH * (5.9/7.5)),286)
        #Drawing Attacking on the screen
        draw_text(screen, "Attacking", 35, (WIDTH * (8.4/11)), 350)
        # Displaying the u key image and drawing the function of it
        screen.blit(u_key, ((WIDTH * (50.5/75)),400))
        draw_text(screen, "Light", 30,(WIDTH * (6.9/9)),406)
        # Displaying the o key image and drawing the function of it
        screen.blit(o_key, ((WIDTH * (50.5/75)),440))
        draw_text(screen, "Heavy", 30,(WIDTH * (6.6/8.5)),446)

        # Updating the screen
        pygame.display.update()
    
def results_screen(character, background, height):
    # Making the rematch button
    rematch_button = Button(WHITE, 350, 300, BUTTON_WIDTH, BUTTON_HEIGHT, "Rematch")
    # Making the main menu button
    main_menu_button = Button(WHITE, 350, 345, BUTTON_WIDTH, BUTTON_HEIGHT, "Menu")
    # Making the exit button
    exit_button = Button(WHITE, 350, 390, BUTTON_WIDTH, BUTTON_HEIGHT, "Exit")

    # Setting loop condition
    running = True

    # Screen loop
    while running:

        # Setting the tick rate of the screen
        clock.tick(FPS)

        # Checks for user input (Event Listener)
        for event in pygame.event.get():

            # Get the mouse position on screen
            pos = pygame.mouse.get_pos()

            # Checking to see if the user hits the X-button on the game window
            if event.type == pygame.QUIT:
                # Sets the loop condition to false
                running = False
                # Close program
                pygame.quit()
                quit()

            # Checks if the user clicks on the screen
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Checks to see if player clicked the rematch button
                if rematch_button.is_over(pos):
                    # Sets the looping condition to false
                    running = False
                    # Calls the main menu function
                    main_game(background, height)
                # Checks to see if the player clicked the exit button
                if exit_button.is_over(pos):
                    # Close program
                    pygame.quit()
                    quit()
                # Check to see if the player clicked the main menu button
                if main_menu_button.is_over(pos):
                    # Call the main menu function
                    main_menu()

            
            # Checking mouse cursor motion
            if event.type == pygame.MOUSEMOTION:
                # Checks to see if the cursor is over the button 
                if rematch_button.is_over(pos):
                    # Set button color to grey
                    rematch_button.color = GREY
                else:
                    # Set button color to white
                    rematch_button.color = WHITE
                # Checks to see if the cursor is over the button 
                if main_menu_button.is_over(pos):
                    # Set button color to grey
                    main_menu_button.color = GREY
                else:
                    # Set button color to white
                    main_menu_button.color = WHITE
                # Checks to see if the cursor is over the button 
                if exit_button.is_over(pos):
                    # Set button color to grey
                    exit_button.color = GREY
                else:
                    # Set button color to white
                    exit_button.color = WHITE

        # Set the background color to black for the screen
        screen.fill(BLACK)

        # Checks if see if player one won
        if character == 1:
            # Print out p1 wne
            draw_text(screen, "Player 1 Won!", 60, (WIDTH / 2), 150)
        # Checks to see if p2 won
        elif character == 2:
            # Print out p2 won
            draw_text(screen, "Player 2 Won!", 60, (WIDTH / 2), 150)
        # Checks to see if p1 and p2 won
        elif character == 3:
            # Print out "Draw" on screen
            draw_text(screen, "Draw", 60, (WIDTH / 2), 150)
        # Draw buttons
        rematch_button.draw(screen)
        main_menu_button.draw(screen)
        exit_button.draw(screen)
        # Update screen
        pygame.display.update()

def main_game(background, height):
    """
    This is where the main game will be located
    """

    # Making the ground sprite groups
    ground_sprite = pygame.sprite.Group()
    # Making a ground object
    ground = Ground(height)
    # Add ground object to the groud sprite group
    ground_sprite.add(ground)

    # Making player one sprite group
    player_one_sprite = pygame.sprite.Group()
    # Making player one object
    player_one = Character(ground_sprite, 1, height)
    # Adding the player one object to the player one sprite group
    player_one_sprite.add(player_one)

    # Making second player two sprite group
    player_two_sprite = pygame.sprite.Group()
    # Making player two object
    player_two = Character(ground_sprite, 2, height)
    # Adding the player two object to the player two sprite group
    player_two_sprite.add(player_two)

    # Making the boundry left sprite group
    bound_left = pygame.sprite.Group()
    # Making the boundry right sprite group
    bound_right = pygame.sprite.Group()
    # Making the boundry left object
    boundry_left = Boundries(1, 10000, 0, 0)
    # Making the boundry right object
    boundry_right = Boundries(1, 10000, WIDTH - 1, HEIGHT - 1)
    # Adding the boundry left object to the boundry left sprite group
    bound_left.add(boundry_left)
    # Adding the boundry right object to the boundry right sprite group
    bound_right.add(boundry_right)

    # Setting looping condition
    running = True

    # Setting the p1 attack flag
    player_one_attack_flag = 0

    # Setting the p2 attack flag
    player_two_attack_flag = 0

    # Main game loop
    while running:

        # Getting how much time has passed in the game
        now = pygame.time.get_ticks()

        #Setting up the speed for the program to run at
        clock.tick(FPS)

        #Checking all events
        for event in pygame.event.get():
            # Checking to see if the user hits the X-button on the game window
            if event.type == pygame.QUIT:
                # Set the looping condition for false
                running = False
                # Close program
                pygame.quit()
                quit()

            # Check the users keypresses 
            if event.type == pygame.KEYDOWN:
                # Checks to see if the w key has been pressed
                if event.key == pygame.K_w:
                    # Calls the player one jump method
                    player_one.jump()
                # Checkse to see if the q key has been pressed
                if event.key == pygame.K_q:
                    # Calls the player one light attack method
                    player_one.light(now)
                    # Set the p1 attack flag to 1
                    player_one_attack_flag = 1
                # Checks to see if the e key has been pressed
                if event.key == pygame.K_e:
                    # Calls the player one heavy attack method
                    player_one.heavy(now)
                    # Sets the p2 attack flag to 2
                    player_one_attack_flag = 2
                # Checks to see if the i key has been pressed
                if event.key == pygame.K_i:
                    # Calls the p2 jump method
                    player_two.jump()
                # Checks to see if the u key has been pressed
                if event.key == pygame.K_u:
                    # Calls the p2 light attack method
                    player_two.light(now)
                    # Turns the p2 attack flag to 1
                    player_two_attack_flag = 1
                # Checks to see if the o key has been pressed
                if event.key == pygame.K_o:
                    # Calls the p2 heavy attack method
                    player_two.heavy(now)
                    # Turns the p2 attack flag to 2
                    player_two_attack_flag = 2
                # Checks to see if the escape key have been pressed
                if event.key == pygame.K_ESCAPE:
                    # Calls the pause screen function
                    pause_screen()
                    

        """
        Check to make sure player one is within the bounds
        """

        # This makes sure that when we collide with the ground we stay on the ground
        # Checks the sprite collision between player one and the ground and return a boolean
        hits_ground_1 = pygame.sprite.spritecollide(player_one, ground_sprite, False)
        # Checks if there was a collision
        if hits_ground_1:
            # Set the player y position to the top of the ground
            player_one.pos.y = hits_ground_1[0].rect.top + 1
            # Stop the y velocity of the player
            player_one.vel.y = 0

        # This makes sure that when we collide with the left border we stay on screen
        # Checks the sprite collision between player one and the left boundry and return a boolean
        hits_bound_left_1 = pygame.sprite.spritecollide(player_one, bound_left, False)
        # Checks to see if there was a collision
        if hits_bound_left_1:
            # Changes the position of the player to the right of the boundry
            player_one.pos.x = hits_bound_left_1[0].rect.right + 16
            # Stops the players x velocity
            player_one.vel.x = 0

        # This makes sure that when we collide with the right border we stay on the screen
        # Checks the sprite collision between player one and the right boundry and return a boolean
        hits_bound_right_1 = pygame.sprite.spritecollide(player_one, bound_right, False)
        # Checks to see if there was a collision
        if hits_bound_right_1:
            # Set the players position to the left of the boundry
            player_one.pos.x = hits_bound_right_1[0].rect.left - 16
            # Stops the x velocity of the player
            player_one.vel.x = 0

        """
        Check to make sure player two is within the bounds
        """

        # This makes sure that when we collide with the ground we stay on the ground
        # Checks the sprite collision between player two and the ground and return a boolean
        hits_ground_2 = pygame.sprite.spritecollide(player_two, ground_sprite, False)
        # Checks to see if there was a collision
        if hits_ground_2:
            # Changes the position of the player to the top of the ground
            player_two.pos.y = hits_ground_2[0].rect.top + 1
            # Stop the y velocity of the player
            player_two.vel.y = 0

        # This makes sure that when we collide with the left border we stay on screen
        # Checks the sprite collision between player two and the left boundry and return a boolean
        hits_bound_left_2 = pygame.sprite.spritecollide(player_two, bound_left, False)
        # Checks to see if there was collison
        if hits_bound_left_2:
            # Changes the position of the player to the right of the boundry
            player_two.pos.x = hits_bound_left_2[0].rect.right + 18.5
            # Stops the x velocity of the player
            player_two.vel.x = 0

        # This makes sure that when we collide with the right border we stay on the screen
        # Checks the sprite collision between player two and the right boundry and return a boolean
        hits_bound_right_2 = pygame.sprite.spritecollide(player_two, bound_right, False)
        # Checks to see if there was a collision
        if hits_bound_right_2:
            # Changes the position of the player to the left of the boundry
            player_two.pos.x = hits_bound_right_2[0].rect.left - 18.5
            # Stops the players x velocity
            player_two.vel.x = 0

        """
        Checking the collision between player one and player two (attacks)
        """

        # This is going to make sure when player one hits player two it will register the damage
        # Checks to see if player one hit player two, then returns a boolean
        hits_player_one = pygame.sprite.spritecollide(player_one, player_two_sprite, False)
        # Checks to see if p1 hit player two with a ligth attack
        if hits_player_one and player_one_attack_flag == 1:
            # Player two loses 10 health
            player_two.character_health -= 10
            # Reset attack flag
            player_one_attack_flag = 0
        # Checks to see if player one hit player two with a heavy attack
        elif hits_player_one and player_one_attack_flag == 2:
            # Player two loses 20 health
            player_two.character_health -= 20
            # Reset the attack flag
            player_one_attack_flag = 0
        # Checks to see if player one light attack animation is done, when player one doesnt hit player two
        elif player_one.light_attack_animation == False and player_one_attack_flag == 1:
            # Reset attack flag
            player_one_attack_flag = 0
        # Checks to see if player one heavy attack animation is done, when player one doesnt hit player two
        elif player_one.heavy_attack_animation == False and player_one_attack_flag == 2:
            # Reset attack flag
            player_one_attack_flag = 0

        
        # This is going to make sure when player two hits player one it will register the damage
        # Checks to see if player two hit player one, then returns a boolean
        hits_player_two = pygame.sprite.spritecollide(player_two, player_one_sprite, False)
        # Checks to see if p2 hit p1 with a light attack
        if hits_player_two and player_two_attack_flag == 1:
            # Player one loses 10 health
            player_one.character_health -= 10
            # Resets p2 attack flag
            player_two_attack_flag = 0
        # Checks to see if p2 hit p1 with a heavy attack
        elif hits_player_two and player_two_attack_flag == 2:
            # Player one loses 20 health
            player_one.character_health -= 20
            # Resest p2 attack flag
            player_two_attack_flag = 0
        # Checks to see if p2 light attack animation is done, when p2 doesnt hit p1
        elif player_two.light_attack_animation == False and player_two_attack_flag == 1:
            # Reset p2 attack flag
            player_two_attack_flag = 0
        # Checks to see if p2 heavy attack animation is done, when p2 doesnt hit p1
        elif player_two.heavy_attack_animation == False and player_two_attack_flag == 2:
            # Reset p2 attack flag
            player_two_attack_flag = 0

        """
        Checking to see which player won
        """
        # Checks to see if p1 has run out of health
        if player_one.character_health <= 0:
            # Set loop condition to false
            running = False
            # Call the result screen function
            results_screen(2, background, height)
        # Checks to see if p2 has run out of health
        elif player_two.character_health <= 0:
            # Set loop condition to false
            running = False
            # Call the result screen functioin
            results_screen(1, background, height)
        # Checks to see if both player are knocked out at the same time
        elif player_one.character_health <= 0 and player_two.character_health <= 0:
            # Set looping condition to false
            running = False
            # Calls the result screen function
            results_screen(3, background, height)

        # Updating player sprites sprites
        player_one_sprite.update()
        player_two_sprite.update()

        
        # Displays background image
        screen.blit(background, (0,0))
        # Draws players
        player_one_sprite.draw(screen)
        player_two_sprite.draw(screen)
        # Displays health
        draw_text(screen,"P"+str(player_one.character_choice)+" Health: " + str(player_one.character_health), 30, 90, 10, RED)
        draw_text(screen,"P"+str(player_two.character_choice)+" Health: " + str(player_two.character_health), 30, 710, 10, RED)

        # Updates the screen
        pygame.display.update()

# Function Calls
main_menu()

# Ending the program
pygame.quit()
quit()
