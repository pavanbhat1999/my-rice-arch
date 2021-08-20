//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/	 	/*Update Interval*/	/*Update Signal*/
    {"", "netspeed",1,0},
    //{" 🐧 ", "$HOME/.config/dwm/dwmblocks/scripts/kernel",		    360,		        2},

	//{" 🔺 ", "$HOME/.config/dwm/dwmblocks/scripts/upt",		        60,		            2},

	{" 📦 ", "$HOME/.config/dwm/dwmblocks/scripts/pacupdate",		360,		        9},
    {"💾","$HOME/.config/dwm/dwmblocks/scripts/disk.sh",              60,                 1},
    {"🔥","$HOME/.config/dwm/dwmblocks/scripts/temp",5,1},
	
	{" 💻 ", "$HOME/.config/dwm/dwmblocks/scripts/memory",	        6,		            1},

	{" 🔊 ", "$HOME/.config/dwm/dwmblocks/scripts/volume",			1,		            10},

    {"🔋","cat /sys/class/power_supply/BAT0/capacity",2,0},
    {"🌞","$HOME/.config/dwm/dwmblocks/scripts/brightness",1,0},


	{" 🕑 ", "$HOME/.config/dwm/dwmblocks/scripts/clock",			5,		            0},
};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim = '|';
