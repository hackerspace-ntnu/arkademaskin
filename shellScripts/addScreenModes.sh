R1X1WIDTH=1200
R1X1HEIGHT=1200
R1X1NAME='1:1'

SCREENNAME=$(xrandr | grep -e " connected" | sed 's/ .*//')

R1X1DATA=$(cvt $R1X1WIDTH $R1X1HEIGHT | tail -n1 | sed -e 's/.*"//')
sudo xrandr --newmode "$R1X1NAME" $R1X1DATA
sudo xrandr --addmode $SCREENNAME $R1X1NAME
