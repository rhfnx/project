import instaloader,colorama,os,pytube,bullet

from colorama import Fore,Back,Style
from time import sleep
from instaloader import Instaloader
from pytube import YouTube
from bullet import Password

colorama.init(autoreset=True)

class InstagramFeature:

    def __init__(self,Username,UserInput,Pw):
        self.Username = Username
        self.UserInput = UserInput
        self.Pw = Pw

    def DownloadInstagramProfile():
        IG = instaloader.Instaloader()
        os.system('clear')
        print(R+'\n[Option 1]\n')
    
        Username = input(W+'[Enter the Username]: ')
        try:
            print(C+'\n[Processing]')
            IG.download_profile(Username,profile_pic_only=True)
            print(
                C+'[Download Complete]\n'+Y+'\n[File Downloaded]:'
                +W+'\n  - [Profile Image]\n  - [Username] Id\n  - [File.xz] (Open to see Profile Metadata[JSON])'
            )
            print(G+'\n[?]'+W+'[Continue Download Another Profile][y/n]')
            UserInput = input(W+'[Enter (y/n)]: ')
            if UserInput == 'y':
                return InstagramFeature.DownloadInstagramProfile()
            else:
                os.system('clear')
                return
        except:
            os.system('clear')
            print(
                R+'\n[Username Unknown or Connection Eror]\n'+Y+'[Please Check your Username Iput or Internet Connection Properly]\n'
                +G+'[?]'+W+'[Continue Download Another Profile][y/n]'
            )
            UserInput = input(W+'[Enter(y/n)]: ')
            if UserInput == 'y':
                return InstagramFeature.DownloadInstagramProfile()
            else:
                os.system('clear')
                return

    def SearchInstagramAccountInformation():
        IG = instaloader.Instaloader()
        def Searching(username):
            UserProfile = instaloader.Profile.from_username(IG.context, username)
            print(
                R+'[Username]          '+W+': '+UserProfile.username+'\n'+
                C+'[User Surename]     '+W+': '+UserProfile.full_name+'\n'+
                G+'[User Id]           '+W+': '+str(UserProfile.userid)+'\n'+
                W+'[Posted]            '+W+': '+str(UserProfile.mediacount)+'\n'+
                W+'[Followers]         '+W+': '+str(UserProfile.followers)+'\n'+
                W+'[Following]         '+W+': '+str(UserProfile.followees)+'\n'+
                Y+'[Private Acc]       '+W+': '+str(UserProfile.is_private)+'\n'+
                Y+'[Business Acc]      '+W+': '+str(UserProfile.is_business_account)+'\n'+
                C+'[Verified Acc]      '+W+': '+R+str(UserProfile.is_verified)+'\n'+
                Y+'[Business Category] '+W+': '+str(UserProfile.business_category_name)+'\n'+
                G+'[Biography]         '+W+':'+'\n'+str(UserProfile.biography)
            )
        os.system('clear')
        IG = instaloader.Instaloader()
        print(R+'\n[Option 2]\n')
        
        Username = input(W+'[Enter Target Username]: ')
        try:
            print(C+'[Processing]\n')
            sleep(2)
            os.system('clear')
            print(G+'[Complete]\n')
            Searching(Username)
            print(G+'\n[?]'+W+'[Continue Search Another Profile][y/n]')
            UserInput = input(W+'[Enter (y/n)]: ')
            if UserInput == 'y':
                return InstagramFeature.SearchInstagramAccountInformation()
            else:
                os.system('clear')
                return
        except:
            print(
                R+'\n[Username Unknown or Connection Error]\n'+Y+'[Please Check your Username Input or Internet Connection Properly]\n'
                +G+'[?]'+W+'[Continue Search Another Profile][y/n]'
            )
            UserInput = input(W+'[Enter (y/n)]: ')
            if UserInput == 'y':
                return InstagramFeature.SearchInstagramAccountInformation()
            else:
                os.system('clear')
                return
    
    def PrintAccountFollowers():
        os.system('clear')
        IG = instaloader.Instaloader()
        print(R+'\n[Option 3]\n')
        
        print(W+'['+Y+'Required User Login'+W+']')
        UserInput = input(W+'[Enter Your Username]: ')
        Pw = Password(prompt=W+"[Enter Your Password]: ",hidden=W+"*")
        Pw = Pw.launch()
        IG.login(UserInput, Pw)
        Username = input(W+'[Enter Target Username]: ')
        UserProfile = instaloader.Profile.from_username(IG.context, Username)
        try:
            Followers = UserProfile.get_followers()
            for Follower in Followers:
                print('\n'+W+Follower)

            print(G+'\n[?]'+W+'[Continue Print Another Account Followers][y/n]')
            UserInput = input(W+'[Enter (y/n)]: ')
            if UserInput == 'y':
                return InstagramFeature.PrintAccountFollowers()
            else:
                os.system('clear')
                return
        except:
            print(
                R+'\n[Username Unknown or Connection Error]\n'+Y+'[Please Check your Username Input or Internet Connection Properly]\n'
                +G+'[?]'+W+'[Continue Search Another Profile][y/n]'
            )
            UserInput = input(W+'[Enter (y/n)]: ')
            if UserInput == 'y':
                return InstagramFeature.PrintAccountFollowers()
            else:
                os.system('clear')
                return

class YoutubeFeature:
    def __init__(self,Link,Account,UserInput):
        self.Link = Link
        self.Account = Account
        self.UserInput = UserInput

    def DownloadYotubeVideo():
        def Function(link):
            YoutubeLink = YouTube(link)
            print(
                R+'\n[Youtube Quality Option]'+
                W+'\n['+Y+'1'+W+']'+'Highest Resolution\n'+
                W+'['+Y+'2'+W+']'+'Lowest Resolution\n'
            )

            VideoQuality = int(input(W+'[Enter Option]: '))
            StreamYoutube = YoutubeLink.streams.filter(file_extension='mp4',progressive=True)
            if VideoQuality == 1:
                try:
                    os.system('clear')
                    print(C+'[Processing]')
                    StreamYoutube.get_highest_resolution().download()
                    print(C+'[Download Complete]\n')
                except:
                    print(R+'[an Error has occurred]')

            elif VideoQuality == 2:
                try:
                    os.system('clear')
                    print(C+'[Processing]')
                    StreamYoutube.get_lowest_resolution().download()
                    sleep(2)
                    print(C+'[Download Complete]\n')
                except:
                    print(R+'[an Error has occurred]')

        os.system('clear')
        print(R+'\n[Option 4]\n'+W+'[Enter Youtbe Link]')
        Link= input(W+'[Type Here]: ')
        
        try:
            Function(Link)
            print(G+'[?]'+W+'[Continue Download Another Video][y/n]')
            UserInput = input(W+'[Enter (y/n)]: ')
            if UserInput == 'y':
                return YoutubeFeature.DownloadYotubeVideo()
            else:
                os.system('clear')
                return
        except:
            print(R+'\n[Incorrect Link or Connection Error]\n'+Y+'[Please Check your Link or Internet Connection Properly]\n'
                +G+'[?]'+W+'[Continue Download Another Video][y/n]'
            )
            UserInput = input(W+'[Enter (y/n)]: ')
            if UserInput == 'y':
                return YoutubeFeature.DownloadYotubeVideo()
            else:
                os.system('clear')
                return
            
class ColoringText:
    def __init__(self,Red,Yellow,Green,Cyan,White,Magenta):
        self.Red = Red
        self.Yellow = Yellow
        self.Green = Green
        self.Cyan = Cyan
        self.White = White

    def ColorRed():
        Red = Fore.RED+Style.BRIGHT
        return Red

    def ColorYellow():
        Yellow = Fore.YELLOW+Style.BRIGHT
        return Yellow

    def ColorGreen():
        Green = Fore.GREEN+Style.BRIGHT
        return Green

    def ColorCyan():
        Cyan = Fore.CYAN+Style.BRIGHT
        return Cyan

    def ColorMagenta():
        Magenta = Fore.MAGENTA+Style.BRIGHT
        return Magenta

    def ColorWhite():
        White = Fore.WHITE+Style.BRIGHT
        return White

R = ColoringText.ColorRed()
Y = ColoringText.ColorYellow()
G = ColoringText.ColorGreen()
C = ColoringText.ColorCyan()
W = ColoringText.ColorWhite()
M = ColoringText.ColorMagenta()

