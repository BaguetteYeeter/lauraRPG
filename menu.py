class menu:
    def init():
        global title, playButton, mpButton, settingButton, exitButton

        titleWidth = x*(4/5)
        titleHeight = y*(3/5)
        buttonWidth = x*(1/5)
        buttonHeight = y*(1/10)

        title = screen.menu.title(x=x/10, y=y/20, w=titleWidth, h=titleHeight, image="images/title.png")
        playButton = screen.menu.button(x=x*0.2, y=y*0.7, w=buttonWidth, h=buttonHeight, image="images/playButton.png")
        mpButton = screen.menu.button(x=x*0.2, y=y*0.85, w=buttonWidth, h=buttonHeight, image="images/mpButton.png")
        settingButton = screen.menu.button(x=x*0.6, y=y*0.7, w=buttonWidth, h=buttonHeight, image="images/settingButton.png")
        exitButton = screen.menu.button(x=x*0.6, y=y*0.85, w=buttonWidth, h=buttonHeight, image="images/exitButton.png")
