from colorama import Fore, Back, Style
import packaging

version = "0.0.1"
update_avaliable = "No update"

def check_update():
    if packaging.version(version):
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

    print(f"""
                        --- > Made by tspstudio
                        --- > Version: {version}
                        --- > Update: {update_avaliable}
""")


if __name__ == "__main__":
    main()