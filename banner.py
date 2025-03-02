import os

def install_banner():
    banner_script = """clear
figlet -f slant "Arch Linux" | lolcat
echo -e "\\e[1;32mCreated by: @Hitesh.s.h" | lolcat
echo -e "\\e[1;36mInstagram: instagram.com/hitesh.s.h" | lolcat
neofetch --ascii_distro arch"""

    with open(os.path.expanduser("~/.bashrc"), "a") as bashrc:
        bashrc.write("\n" + banner_script + "\n")

    print("✅ Banner Installed Successfully! Restart Termux to See Changes.")

if __name__ == "__main__":
    install_banner()
