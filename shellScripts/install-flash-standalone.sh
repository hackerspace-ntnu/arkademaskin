wget https://fpdownload.macromedia.com/pub/flashplayer/updaters/32/flash_player_sa_linux.x86_64.tar.gz
mkdir flash-temp
tar xvzf flash_player_sa_linux.x86_64.tar.gz -C flash-temp
sudo mv flash-temp/flashplayer /usr/local/bin
rm -r flash-temp
rm flash_player_sa_linux.x86_64.tar.gz
