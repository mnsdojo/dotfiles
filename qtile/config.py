from libqtile import bar, layout, widget
import os 
import subprocess
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile import hook
from libqtile.lazy import lazy

# Nord color scheme
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

keys = [
    # Window focus movement
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus"),

    # Custom 
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
    Key([mod], "s", lazy.spawn("code"), desc='Vscode'),
    
    # Window movement
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Window resizing
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

# Group definitions for workspaces (1-9)
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Move window to group {i.name}"),
    ])

# Layout theming
layout_theme = {
    "border_width": 2,
    "margin": 9,
    "border_focus": colors["frost"]["blue"],
    "border_normal": colors["polar-night"]["light"],
    "grow_amount": 2,
    "border_on_single": True,
}

# Layouts
layouts = [
    layout.Columns(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(),
]

# Widget defaults
widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=3,
    background=colors["polar-night"]["darkest"],
)
extension_defaults = widget_defaults.copy()

# Screen setup with bar and widgets
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=colors["snow-storm"]["light"],
                    inactive=colors["polar-night"]["light"],
                    highlight_method="line",
                    highlight_color=[colors["polar-night"]["darkest"]],
                    this_current_screen_border=colors["frost"]["blue"],
                    padding=5,
                    margin_x=0,
                    margin_y=3,
                    borderwidth=3,
                    fontsize=14,
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
                widget.WindowName(
                    format="{name}",
                    max_chars=50,
                    foreground=colors["frost"]["cyan"],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
                widget.CPU(
                    format=' CPU {load_percent}%',
                    foreground=colors["aurora"]["yellow"],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
                widget.Memory(
                    format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                    foreground=colors["aurora"]["green"],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
                widget.Net(
                    interface="enp4s0",
                    format=' {down} ↓↑ {up}',
                    foreground=colors["frost"]["ocean"],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
                widget.Volume(
                    fmt=' {}',
                    foreground=colors["aurora"]["purple"],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
                widget.Battery(
                    format=' {char} {percent:2.0%} {hour:d}:{min:02d}',
                    charge_char='⚡',
                    discharge_char='',
                    full_char='',      # Icon for full battery
                    empty_char='',
                    unknown_char='',
                    low_percentage=0.2,
                    low_foreground=colors["aurora"]["red"],
                    foreground=colors["frost"]["cyan"],
                    show_short_text=False,
                    notify_below=20,
                ),
                widget.Clock(
                    format=' %Y-%m-%d %a %I:%M %p',
                    foreground=colors["frost"]["mint"],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
                widget.Systray(
                    padding=6,
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
                widget.QuickExit(
                    default_text=' ',
                    countdown_format='{}',
                    foreground=colors["aurora"]["red"],
                    fontsize=14,
                ),
            ],
            28,  # Bar height
            background=colors["polar-night"]["darkest"],
            margin=[4, 6, 0, 6],  # [top, right, bottom, left]
            opacity=0.95,
        ),
    ),
]

# Mouse bindings
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Floating layout rules
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
)

# Other settings
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
