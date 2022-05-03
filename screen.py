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
            mainScreen.blit(playButton.image, (x*(2/10), y*(7/10)))
            mainScreen.blit(mpButton.image, (x*(2/10), y*(8.5/10)))
            mainScreen.blit(settingButton.image, (x*(6/10), y*(7/10)))
            mainScreen.blit(exitButton.image, (x*(6/10), y*(8.5/10)))
            pygame.display.update()
