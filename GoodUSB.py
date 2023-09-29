from colorama import Fore, Back, Style
import packaging
import requests

version = "0.0.1"
update_avaliable = "No update"

def check_update():
    if packaging.version(version) > packaging.version(requests.get("https://raw.githubusercontent.com/tspstudio/GoodUSD/master/version.txt").text):
        update_avaliable == "Avaliable"

def main():
    print(Fore.RED+"""
 ██████╗  ██████╗  ██████╗ ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║   ██║██║  ██║██║   ██║███████╗██████╔╝
██║   ██║██║   ██║██║   ██║██║  ██║██║   ██║╚════██║██╔══██╗
╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝╚██████╔╝███████║██████╔╝
 ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ 
"""+Fore.WHIRE)

    check_update()

    print(f"""
                        --- > Made by tspstudio
                        --- > Version: {version}
                        --- > Update: {update_avaliable}
""")


if __name__ == "__main__":
    main()