from os import *
from os import geteuid


def validate_root():
    if not geteuid() == 0:
        print("-] Please run this script as root... [-]")
        exit()
    else:
        pass
#install go
#teste
def install_go():
    print('[+] Golang install Start... [+]')
    command_dowload_go = 'wget https://go.dev/dl/go1.19.4.linux-amd64.tar.gz'
    command_install_go = 'rm -rf /usr/local/go && tar -C /usr/local -xzf go1.19.4.linux-amd64.tar.gz'
    command_move_go_1 = 'cd /usr/local/go/bin'
    command_move_go_2 = 'mv * /usr/bin'
    command_go_version = 'go version'
    print('[+] Golang install finished... [+]')

#install tools
def install_amass():
    print('[+] Amass install Start... [+]')
    command_dowload = 'go install -v github.com/OWASP/Amass/v3/...@master'
    print('[+] Amass install Finished... [+]')

def install_anew():
    print('[+] Anew install Start... [+]')
    command_dowload = 'go install -v github.com/tomnomnom/anew@latest'
    print('[+] Anew install Finished... [+]')

def install_tomnonom():
    print('[+] Tomnonom hacks install Start... [+]')
    command_clone = 'git clonehttps://github.com/tomnomnom/hacks.git '
    command_install = 'cd hacks/'
    command_install_2 = 'cd assetfinder/'
    command_install_3 = 'go build'
    command_install_4 = 'mv assetfinder /usr/bin'
    command_install_4 = 'cd ..'
    print('[+] Tomnonom hacks install Finished... [+]')
 
