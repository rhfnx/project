import stf,os
from stf import ColoringText,InstagramFeature,YoutubeFeature

R = ColoringText.ColorRed()
Y = ColoringText.ColorYellow()
G = ColoringText.ColorGreen()
C = ColoringText.ColorCyan()
W = ColoringText.ColorWhite()

class MAIN:
    def __init__(self,UserInputInput):
        self.UserInputInput = UserInputInput
    
    def MainMenu():
        with open('text-file/logo.txt') as Logo,open('text-file/desc.txt','r') as Description,open('text-file/menu.txt','r') as Menu:
            DrawLogo = Logo.readlines()
            WriteMenu = Menu.readlines()
            WriteDesc = Description.readlines()

            print(
                f"{R+DrawLogo[0]+DrawLogo[1]+DrawLogo[2]+DrawLogo[3]+DrawLogo[4]}"+
                f"{R+DrawLogo[5]+DrawLogo[6]+Y+DrawLogo[7]+Y+DrawLogo[8]+W+DrawLogo[9]}"
            )
            print(
                f"{W+WriteDesc[0]+WriteDesc[1]+WriteDesc[2]+DrawLogo[9]}\n"
            )
            print(
                f"{R+WriteMenu[0]+W+'['+Y+'1'+W+']'+WriteMenu[1]+'['+Y+'2'+W+']'+WriteMenu[2]+'['+Y+'3'+W+']'+WriteMenu[3]+'['+Y+'4'+W+']'+WriteMenu[4]}"
            )

    def ExitFucntion():
        print(R+'\n[Exit Socio Tools]')
        exit()

    def MainBody():
        while True:
            os.system('clear')
            MAIN.MainMenu()
            print(R+'[Other Options]'+W+'\n['+Y+'E'+W+']'+W+'Press E for Exit')
            UserInput = input(W+'[Choose an option]: ')
            if UserInput == '1':
                InstagramFeature.DownloadInstagramProfile()
                print(G+'\n[?]'+W+'[Continue to menu][y/n]')
                UserInput = input(W+'[Enter(y/n)]: ')
                if UserInput == 'y':
                    return MAIN.MainBody()
                else:
                    MAIN.ExitFucntion()
            elif UserInput == '2':
                InstagramFeature.SearchInstagramAccountInformation()
                print(G+'\n[?]'+W+'[Continue to menu][y/n]')
                UserInput = input(W+'[Enter(y/n)]: ')
                if UserInput == 'y':
                    return MAIN.MainBody()
                else:
                    MAIN.ExitFucntion()
            elif UserInput == '3':
                InstagramFeature.PrintAccountFollowers()
                print(G+'\n[?]'+W+'[Continue to menu][y/n]')
                UserInput = input(W+'[Enter(y/n)]: ')
                if UserInput == 'y':
                    return MAIN.MainBody()
                else:
                    MAIN.ExitFucntion()
            elif UserInput == '4':
                YoutubeFeature.DownloadYotubeVideo()
                print(G+'\n[?]'+W+'[Continue to menu][y/n]')
                UserInput = input(W+'[Enter(y/n)]: ')
                if UserInput == 'y':
                    return MAIN.MainBody()
                else:
                    MAIN.ExitFucntion()
            elif UserInput == 'e':
                MAIN.ExitFucntion()


