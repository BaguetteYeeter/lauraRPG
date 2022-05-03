class screen:
    class menu:
        class button:
            def __init__(self, x=0, y=0, w=1, h=1, image="images/playButton.png"):
                self.x = x
                self.y = y
                self.image = pygame.transform.scale(pygame.image.load(image), (w, h))
                self.pressed = False
                self.rect = pygame.Rect(x, y, w, h)
        class title:
            def __init__(self, x=0, y=0, w=1, h=1, image="images/title.png"):
                self.x = x
                self.y = y
                self.image = pygame.transform.scale(pygame.image.load(image), (w, h))
                self.rect = pygame.Rect(x, y, w, h)
        def showButtons():
            mainScreen.blit(title.image, (x/10, y/20))
            mainScreen.blit(playButton.image, (playButton.x, playButton.y))
            mainScreen.blit(mpButton.image, (mpButton.x, mpButton.y))
            mainScreen.blit(settingButton.image, (settingButton.x, settingButton.y))
            mainScreen.blit(exitButton.image, (exitButton.x, exitButton.y))
            mainScreen.blit(discordButton.image, (discordButton.x, discordButton.y))
            mainScreen.blit(redditButton.image, (redditButton.x, redditButton.y))
            pygame.display.update()
        def buttonClick(events, *args):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in args:
                        if i.rect.collidepoint(event.pos):
                            i.pressed = True
                        else:
                            i.pressed = False
