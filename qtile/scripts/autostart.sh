#!/bin/sh
nitrogen --restore &
picom &

# For reverse scrolling and tap to touch
xinput set-prop 'ELAN1203:00 04F3:307A Touchpad' 'libinput Tapping Enabled' 1 &
xinput set-prop 'ELAN1203:00 04F3:307A Touchpad' 'libinput Natural Scrolling Enabled' 1 &
