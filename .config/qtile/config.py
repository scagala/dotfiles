from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule, ScratchPad, DropDown
from libqtile.command import lazy

from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText,
    PopupWidget
)
from catppuccin import Flavour
import fontawesome as fa
import subprocess
import os



mod = "mod4"
terminal = "kitty"
cs = Flavour.macchiato()
regfont = 'JetBrainsMono Nerd Font Mono'
boldfont = 'JetBrainsMono Nerd Font Bold'
italicfont = 'JetBrainsMono Nerd Font Italic'

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
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
    Key([mod], "r", lazy.spawn(os.path.expanduser('~/.config/rofi/launchers/type-3/launcher.sh')),desc="Spawn app menu"),


    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),  desc="Move window to the left"),

    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),

    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),

    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(), 
        desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h",
        lazy.layout.grow(),
        desc="Grow window"),
    Key([mod, "control"], "Up", 
        lazy.layout.grow(),
        desc="Grow window"),
    Key([mod, "control"], "l",
        lazy.layout.shrink(),
        desc="Shrink window"),
    Key([mod, "control"], "Down",
        lazy.layout.shrink(),
        desc="Shring window"),
    Key([mod], "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),

    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),

    Key([mod, "shift"], "space", lazy.layout.flip()),

    Key([mod], "p", lazy.spawn(os.path.expanduser('~/.config/rofi/powermenu/type-1/powermenu.sh'))),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),

    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod, "shift"], "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 5%+")),
    
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 5%-")),
    
    Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),
    
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
    keys.extend([
        
        # mod1 + letter of group = switch to group
        Key( [mod], i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)
        ),
        
        # mod1 + shift + letter of group = switch to & move focused window to group
        Key( [mod, "shift"], i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)
        ),
    ])

layout_defaults = dict(
    margin=8,
    border_focus=cs.sapphire.hex,
    border_normal=cs.surface2.hex,
    border_width=2
)

layouts = [
    layout.MonadTall(**layout_defaults),
    #layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    layout.VerticalTile(**layout_defaults),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])


mouse = [
    Click([mod], "Button1", lazy.window.bring_to_front()),
    Click([mod, "shift"], "Button1", lazy.window.toggle_floating()),
    Drag([mod], "Button2", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size())
]


screens = [
    # order according to xrandr --listmonitors
    # ASUS 27inch
    Screen(
        top=bar.Bar(
            [   widget.Sep(
                    padding=3, 
                    linewidth=0, 
                    background=cs.base.hex
                ),
                widget.Image(
                    filename='~/Pictures/itsv_logo.svg',
                    margin = 1,
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/launchers/type-3/launcher.sh'))
                    },
                ),
                widget.Spacer(
                    length = 8,

                ),
                widget.GroupBox(
                    font = boldfont,
                    disable_drag=True,
                    # highlight_method='block',
                    this_screen_border=cs.lavender.hex,
                    this_current_screen_border=cs.lavender.hex,
                    other_screen_border = cs.overlay0.hex,
                    other_current_screen_border = cs.overlay0.hex,
                    active=cs.lavender.hex,
                    inactive=cs.overlay0.hex,
                    background=cs.base.hex,
                    fontsize = 14
                ),
                widget.Prompt(
                    background=cs.base.hex,
                    bell_style=None,
                    cursor_color=cs.text.hex,
                    prompt=f"  {fa.icons['terminal']}  ",
                ),
                widget.Spacer(),
                widget.WindowName(    
                    font = italicfont,
                    fontsize = 14,                    
                    foreground=cs.text.hex,
                    fmt='{}',
                    for_current_screen = True,
                ),
                widget.Spacer(),
                
                widget.Systray(
                    icon_size = 20,
                    background = cs.base.hex
                ),
                widget.Spacer(
                    length=5,
                    background=cs.base.hex
                ),
                widget.Clock(
                    fmt = f"{fa.icons['clock']} " + "{}",
                    format = "%Y-%m-%d %a %I:%M %p",
                    background = cs.base.hex,
                    foreground = cs.green.hex,
                    fontsize = 14,
                    font = boldfont
                ),
                widget.Spacer(
                    length=10,
                    background=cs.base.hex
                ),
                widget.TextBox(
                    text=f"{fa.icons['power-off']} ",
                    fontsize=17,
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu/type-1/powermenu.sh'))
                    },
                    foreground=cs.maroon.hex,
                    background=cs.base.hex,
                    font = boldfont
                ),
                widget.Spacer(
                    length=10,
                    background=cs.base.hex
                )

                
            ],
            25,  # height in px
            margin=[5,5,5,5],
            background=cs.base.hex  # background color
        ),
    ),
    
    # vertical samsung
    Screen(

        top=bar.Bar(
            [
                widget.GroupBox(
                    disable_drag=True,
                    # highlight_method='line',
                    this_screen_border=cs.lavender.hex,
                    this_current_screen_border=cs.lavender.hex,
                    active=cs.lavender.hex,
                    inactive=cs.overlay0.hex,
                    background=cs.base.hex,
                ),
            ],
            25,
            margin=[5,5,5,5],
        ),
    ),

    # laptop builtin
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    disable_drag=True,
                    # highlight_method='line',
                    this_screen_border=cs.lavender.hex,
                    this_current_screen_border=cs.lavender.hex,
                    active=cs.lavender.hex,
                    inactive=cs.overlay0.hex,
                    background=cs.base.hex,
                ),
            ],
            25,
            margin=[5,5,5,5],
        ),
    ),

]
  

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"
