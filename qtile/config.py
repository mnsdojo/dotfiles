from libqtile import bar, layout, widget
import os 
import subprocess
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile import hook
from libqtile.lazy import lazy

# Enhanced Nord color scheme with additional colors for gradients
colors = {
    "polar-night": {
        "darkest": "#2E3440",
        "darker": "#3B4252",
        "dark": "#434C5E",
        "light": "#4C566A",
    },
    "snow-storm": {
        "dark": "#D8DEE9",
        "medium": "#E5E9F0",
        "light": "#ECEFF4",
    },
    "frost": {
        "mint": "#8FBCBB",
        "cyan": "#88C0D0",
        "ocean": "#81A1C1",
        "blue": "#5E81AC",
    },
    "aurora": {
        "red": "#BF616A",
        "orange": "#D08770",
        "yellow": "#EBCB8B",
        "green": "#A3BE8C",
        "purple": "#B48EAD",
    }
}

mod = "mod4"
terminal = "kitty"

# Key bindings
keys = [
    # Window focus movement
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus"),

    # Custom keybindings for media and brightness control
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='Volume Down'),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='Play/Pause'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='Previous Track'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='Next Track'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='Brightness Up'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='Brightness Down'),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
    Key([mod], "v", lazy.spawn("code"), desc='Launch VSCode'),

    # Window movement and resizing
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Window management
    Key([mod], "q", lazy.window.kill(), desc="Close focused window"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split/unsplit"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating window"),

    # System controls
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Quit Qtile"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
]

# Group definitions with icons
groups = [
    Group("1", label="一"),
    Group("2", label="二"),
    Group("3", label="三"),
    Group("4", label="四"),
    Group("5", label="五"),
    Group("6", label="六"),
    Group("7", label="七"),
    Group("8", label="八"),
    Group("9", label="九"),
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Move window to group {i.name}"),
    ])

# Layout theming
layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": colors["frost"]["blue"],
    "border_normal": colors["polar-night"]["light"],
    "border_on_single": True,
}

# Layouts
layouts = [
    layout.Columns(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(),
]

# Function to create a gradient effect
def create_separator():
    return widget.Sep(
        linewidth=0,
        padding=6,
        size_percent=60,
    )

# Powerline arrow functions
def create_left_arrow(bg_color, fg_color):
    return widget.TextBox(
        text="◀",  # Left-pointing triangle
        padding=0,
        fontsize=20,
        background=bg_color,
        foreground=fg_color,
    )

def create_right_arrow(bg_color, fg_color):
    return widget.TextBox(
        text="▶",  # Right-pointing triangle
        padding=0,
        fontsize=20,
        background=bg_color,
        foreground=fg_color,
    )

# Widget defaults
widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=5,
    background=colors["polar-night"]["darkest"],
)
extension_defaults = widget_defaults.copy()

# Screen setup with modernized bar and widgets
screens = [
    Screen(
        top=bar.Bar(
            [
                # Workspace groups with enhanced styling
                widget.GroupBox(
                    active=colors["snow-storm"]["light"],
                    inactive=colors["polar-night"]["light"],
                    highlight_method="line",
                    highlight_color=[colors["polar-night"]["darkest"]],
                    this_current_screen_border=colors["frost"]["blue"],
                    other_current_screen_border=colors["frost"]["ocean"],
                    other_screen_border=colors["frost"]["cyan"],
                    padding=6,
                    borderwidth=3,
                    fontsize=14,
                    rounded=True,
                    margin_y=4,
                    margin_x=4,
                    spacing=4,
                    disable_drag=True,
                ),
                create_separator(),
                
                # Window name with background
                widget.WindowName(
                    format="{name}",
                    max_chars=50,
                    foreground=colors["frost"]["cyan"],
                    background=colors["polar-night"]["darker"],
                    padding=10,
                    fontsize=14,
                ),
                
                create_right_arrow(colors["polar-night"]["darker"], colors["polar-night"]["dark"]),
                
                # System information section
                widget.CPU(
                    format=' {load_percent}%',
                    foreground=colors["aurora"]["yellow"],
                    background=colors["polar-night"]["dark"],
                    padding=10,
                ),
                
                create_right_arrow(colors["polar-night"]["dark"], colors["polar-night"]["darker"]),
                
                widget.Memory(
                    format='󰍛 {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
                    foreground=colors["aurora"]["green"],
                    background=colors["polar-night"]["darker"],
                    padding=10,
                ),
                
                create_right_arrow(colors["polar-night"]["darker"], colors["polar-night"]["dark"]),
                
                widget.Net(
                    interface="enp4s0",
                    format='󰈀 {down} ↓↑ {up}',
                    foreground=colors["frost"]["ocean"],
                    background=colors["polar-night"]["dark"],
                    padding=10,
                ),
                
                create_right_arrow(colors["polar-night"]["dark"], colors["polar-night"]["darker"]),
                
                # Volume widget with modern icon
                widget.Volume(
                    fmt='󰕾 {}',
                    foreground=colors["aurora"]["purple"],
                    background=colors["polar-night"]["darker"],
                    padding=10,
                ),
                
                create_right_arrow(colors["polar-night"]["darker"], colors["polar-night"]["dark"]),
                
                # Battery widget with enhanced formatting
                widget.Battery(
                    format='🔋 {percent:2.0%} {hour:d}:{min:02d}',
                    charge_char='⚡',
                    discharge_char='',
                    full_char='🔋',
                    empty_char='🔋',
                    unknown_char='❓',
                    low_percentage=0.2,
                    low_foreground=colors["aurora"]["red"],
                    foreground=colors["frost"]["cyan"],
                    background=colors["polar-night"]["darker"],
                    padding=10,
                    update_interval=10,
                ),
                
                create_right_arrow(colors["polar-night"]["dark"], colors["polar-night"]["darker"]),
                
                # Date and time widget with modern design
                widget.Clock(
                    format='📅 %Y-%m-%d %H:%M',
                    foreground=colors["snow-storm"]["light"],
                    background=colors["polar-night"]["darker"],
                    padding=10,
                ),
                
                # Systray for application icons
                widget.Systray(
                    background=colors["polar-night"]["dark"],
                    padding=10,
                ),
                
                create_right_arrow(colors["polar-night"]["darker"], colors["polar-night"]["dark"]),
                
                # Logout button with icon

                 widget.QuickExit(
                    default_text='⏻',
                    countdown_format='{}',
                    foreground=colors["aurora"]["red"],
                    background=colors["polar-night"]["dark"],
                    padding=10,
                ),
                
                create_separator(),
            ],
            size=30,
            background=colors["polar-night"]["darkest"],
        ),
    ),
]

# Floating layout configurations
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirm"),  # Confirm dialogs
        Match(wm_class="dialog"),  # Dialogs
        Match(wm_class="file_progress"),  # File progress dialogs
        Match(wm_class="notification"),  # Notifications
        Match(wm_class="pinentry"),  # Pin entry dialogs
        Match(title="branchdialog"),  # Git branch dialog
        Match(title="Open File"),  # Open file dialog
        Match(title="Save File"),  # Save file dialog
    ]
)

# Startup hook to launch applications
@hook.subscribe.startup_once
def startup():
    subprocess.call([os.path.expanduser("~/.config/qtile/scripts/autostart.sh")])

# Qtile configuration to include floating layout and other settings
auto_fullscreen = True
wmname = "Qtile"

