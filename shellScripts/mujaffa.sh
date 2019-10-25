SCREENNAME=$(xrandr | grep -e " connected" | sed 's/ .*//')
xrandr --output $SCREENNAME --mode 1:1
{
./flashplayer mujaffa_spillet.swf
xrandr -s 0
} &
sleep 0.6
xdotool search --name "Adobe Flash Player" set_window --name "Mujaffa Spillet"
xdotool key ctrl+f