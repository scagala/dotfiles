from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import (
    Click,
    Drag,
    Group,
    Key,
    Match,
    Screen,
    Rule,
    ScratchPad,
    DropDown,
)
from libqtile.command import interface, lazy
from custom.colorscheme import palette
import subprocess
import os

mod = "mod4"
alt = "mod1"

terminal = "kitty"
browser = "firefox"
media = "vlc"
music = "spotify"

regfont = "JetBrainsMono Nerd Font Mono"
boldfont = "JetBrainsMono Nerd Font Bold"
italicfont = "JetBrainsMono Nerd Font Italic"

# catppuccin colorscheme
# cs = Flavour.macchiato()


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])


keys = [
    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    # MOVE WINDOWS IN CURRENT GROUP
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # WINDOW RESIZING
    Key([mod, "control"], "h", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "Up", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "l", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, "control"], "Down", lazy.layout.shrink(), desc="Shring window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # LAYOUT SETTING
    Key(["Lock"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    # GENERAL SETTINGS
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # LAUNCHERS
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod],
        "p",
        lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu/type-1/powermenu.sh")),
        desc="Spawn powemenu",
    ),
    Key(
        [mod],
        "r",
        lazy.spawn(os.path.expanduser("~/.config/rofi/launchers/type-3/launcher.sh")),
        desc="Spawn app menu",
    ),
    Key([mod], "w", lazy.spawn(browser)),
    Key([mod], "m", lazy.spawn(music)),
    Key(
        [mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    # MEDIA / BRIGHTNESS CONTROL
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
]

groups = [
    Group("1", screen_affinity=1),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8", layout="verticaltile", screen_affinity=2),
    Group("9", matches=[Match(wm_class=["Kodi"])], layout="max", screen_affinity=3),
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="Move focused window to group {}".format(i.name),
            ),
        ]
    )

layout_defaults = dict(
    margin=8,
    border_focus=palette.pink,
    border_normal=palette.surface0,
    border_width=2,
)

layouts = [
    layout.MonadTall(**layout_defaults),
    layout.Max(**layout_defaults),
    layout.VerticalTile(**layout_defaults),
    layout.MonadThreeCol(**layout_defaults),
    layout.MonadWide(**layout_defaults),
    layout.Zoomy(**layout_defaults),
]


floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),
    ],
    border_focus=palette.mauve,
    border_normal=palette.surface0,
    border_width=2,
)

mouse = [
    Click([mod], "Button1", lazy.window.bring_to_front()),
    Click([mod, "shift"], "Button1", lazy.window.toggle_floating()),
    Drag(
        [mod],
        "Button2",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
]


def get_widgets(primary=False):
    widgets = [
        # widget.Image(
        #     filename='~/.local/share/assets/icons/itsv_logo.svg',
        #     margin = 1,
        #     mouse_callbacks= {
        #         'Button1':
        #             lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/launchers/type-3/launcher.sh'))
        #     },
        # ),
    ]

    return widgets


screens = [
    # order according to xrandr --listmonitors
    # ASUS 27inch
    Screen(
        top=bar.Bar(
            [
                # widget.TextBox(
                #     font=regfont,
                #     fontsize=25,
                #     text="",
                #     foreground=cs.yellow.hex,
                #     padding=0
                # ),
                widget.GroupBox(
                    font=boldfont,
                    disable_drag=True,
                    # highlight_method='block',
                    this_screen_border=palette.lavender,
                    this_current_screen_border=palette.lavender,
                    other_screen_border=palette.overlay0,
                    other_current_screen_border=palette.overlay0,
                    active=palette.lavender,
                    inactive=palette.overlay0,
                    # background=cs.yellow.hex,
                    fontsize=14,
                ),
                # widget.TextBox(
                #     font=regfont,
                #     fontsize=25,
                #     text="",
                #     foreground=cs.yellow.hex,
                #     padding=0
                # ),
                widget.CurrentLayout(
                    font=boldfont,
                    fontsize=14,
                ),
                # widget.Prompt(
                #     background=colors["base"],
                #     bell_style=None,
                #     cursor_color=palette.text,
                #     prompt=f"  {fa.icons['terminal']}  ",
                # ),
                widget.Spacer(),
                widget.WindowName(
                    font=italicfont,
                    fontsize=14,
                    foreground=palette.text,
                    fmt="{}",
                    for_current_screen=True,
                ),
                widget.Spacer(),
                # widget.ThermalZone(
                #     fmt="{}",
                #     zone="/sys/class/thermal/thermal_zone0/temp"
                # ),
                widget.Net(
                    # interface="wlan0",
                    use_bits=True,
                    format=" {down}",
                    foreground=palette.blue,
                    font=boldfont,
                    fontsize=14,
                    prefix='M',
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            os.path.expanduser(
                                "~/.config/rofi/applets/bin/wifi.sh"
                            )
                        )
                    },
                ),
                widget.Sep(
                        padding=5,
                        foreground=palette.subtext0,
                        background=palette.mantle,
                        ),
                widget.Backlight(
                    backlight_name="nvidia_wmi_ec_backlight",
                    change_command="brightnessctl set {0}%",
                    font=boldfont,
                    fontsize=14,
                    foreground=palette.lavender,
                    step=5,
                    fmt="󰃟 {}"
                ),
                widget.Sep(
                        padding=5,
                        foreground=palette.subtext0,
                        background=palette.mantle,
                        ),
                widget.CPU(
                    format="󰘚 {load_percent}%",
                    font=boldfont,
                    fontsize=14,
                    foreground=palette.maroon,
                    background=palette.mantle,
                ),
                # widget.Spacer(length=5),
                widget.Sep(
                    padding=5,
                    foreground=palette.subtext0,
                    background=palette.mantle,

                    ),

                widget.Memory(
                    background=palette.mantle,
                    font=boldfont,
                    fontsize=14,
                    foreground=palette.sky,
                    format="󰍛 {MemUsed:.1f}{mm}",
                    measure_mem="G",
                ),
                # widget.Spacer(length=5),
                widget.Sep(
                    background=palette.mantle,
                    padding=5,
                    foreground=palette.subtext0
                    ),

                widget.ThermalSensor(
                    background=palette.mantle,
                    font=boldfont,
                    fontsize=14,
                    foreground=palette.rosewater,
                    foreground_alert=palette.red,
                    threshold=65,
                    tag_sensor="Tdie",
                    format=" {temp:.1f} {unit}",
                ),
                widget.Sep(
                    padding=5,
                    foreground=palette.subtext0,
                    background=palette.mantle,

                    
                    ),
                widget.Battery(
                    background=palette.mantle,
                    font=boldfont,
                    fontsize=14,
                    charge_char="󰂄",
                    discharge_char="󱟤",
                    empty_char="󰂎",
                    full_char="󰁹",
                    format="{char} {percent:2.0%}",
                    foreground=palette.green,
                    low_foreground=palette.red,
                    low_percentage=0.15,
                    update_interval=30,
                ),
                widget.Sep(
                    padding=5,
                    foreground=palette.subtext0,
                    background=palette.mantle,
                    ),  

                # widget.Spacer(length=5),
                # widget.Systray(
                #     icon_size = 20,
                #     background = colors["base"]
                # ),
                widget.Spacer(length=5, background=palette.mantle),
                widget.Clock(
                    # fmt = f"{fa.icons['clock']} " + "{}",
                    # format = "%Y-%m-%d %a %I:%M %p",
                    format="  %H:%M",
                    background=palette.mantle,
                    foreground=palette.yellow,
                    fontsize=14,
                    font=boldfont,

                ),
                # widget.Spacer(
                #     length=10,
                #     background=palette.mantle,
                # ),
                widget.Sep(
                        padding=5,
                        foreground=palette.subtext0,
                        background=palette.mantle,
                        ),

                widget.TextBox(
                    text="",
                    fontsize=16,
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            os.path.expanduser(
                                "~/.config/rofi/powermenu/type-1/powermenu.sh"
                            )
                        )
                    },
                    foreground=palette.maroon,
                    background=palette.mantle,
                    font=boldfont,
                    padding=10,
                ),
                widget.Spacer(length=15, background=palette.mantle),
            ],
            24,  # height in px
            margin=[5, 3, 0, 3],
            background=palette.base,  # background color
        ),
    ),
    # vertical samsung
    # Screen(
    #     top=bar.Bar(
    #         [
    #             widget.GroupBox(
    #                 disable_drag=True,
    #                 # highlight_method='line',
    #                 this_screen_border=colors["lavender"],
    #                 this_current_screen_border=colors["lavender"],
    #                 active=colors["lavender"],
    #                 inactive=palette.overlay0,
    #                 background=colors["base"],
    #             ),
    #         ],
    #         25,
    #         margin=[5, 5, 5, 5],
    #     ),
    # ),
    # # laptop builtin
    # Screen(
    #     top=bar.Bar(
    #         [
    #             widget.GroupBox(
    #                 disable_drag=True,
    #                 # highlight_method='line',
    #                 this_screen_border=colors["lavender"],
    #                 this_current_screen_border=colors["lavender"],
    #                 active=colors["lavender"],
    #                 inactive=palette.overlay0,
    #                 background=colors["base"],
    #             ),
    #         ],
    #         25,
    #         margin=[5, 5, 5, 5],
    #     ),
    # ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"
