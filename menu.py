class menu:
    def init():
        global title, playButton, mpButton, settingButton, exitButton

        titleWidth = x*(4/5)
        titleHeight = y*(3/5)
        buttonWidth = x*(1/5)
        buttonHeight = y*(1/10)

        title = pygame.image.load("images/title.png")
        playButton = pygame.image.load("images/playButton.png")
        mpButton = pygame.image.load("images/mpButton.png")
        settingButton = pygame.image.load("images/settingButton.png")
        exitButton = pygame.image.load("images/exitButton.png")

        title = pygame.transform.scale(title, (titleWidth, titleHeight))
        playButton = pygame.transform.scale(playButton, (buttonWidth, buttonHeight))
        mpButton = pygame.transform.scale(mpButton, (buttonWidth, buttonHeight))
        settingButton = pygame.transform.scale(settingButton, (buttonWidth, buttonHeight))
        exitButton = pygame.transform.scale(exitButton, (buttonWidth, buttonHeight))
        
    def showButtons():
        mainScreen.blit(title, (x/10, y/20))
        mainScreen.blit(playButton, (x*(2/10), y*(7/10)))
        mainScreen.blit(mpButton, (x*(2/10), y*(8.5/10)))
        mainScreen.blit(settingButton, (x*(6/10), y*(7/10)))
        mainScreen.blit(exitButton, (x*(6/10), y*(8.5/10)))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
