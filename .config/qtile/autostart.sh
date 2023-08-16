#!/bin/sh

# MONITORS_N=$(xrandr --listmonitors | grep "Monitors: " | awk '{print $2}')
# if [[ MONITORS_N -eq 3 ]]; then
    	# .screenlayout/tripleMon.sh
# else
		# .screenlayout/singleMon.sh
# fi

feh --bg-fill /home/en1qc/Pictures/leap_of_faith.png --bg-fill /home/en1qc/Pictures/leap_of_faith.png --bg-fill /home/en1qc/Pictures/leap_of_faith.png2
#picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed
picom --config ~/.config/picom/picom.conf --experimental-backends & disown

21/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
# SYSTRAY
nm-applet 	 & disown # Network Manager
pasystray 	 & disown # Volume control
cbatticon 	 & disown # Battery indicator
blueman-applet   	 & disown # Bluetooth manager
udiskie -atn & disown
