from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#my modules
import os


mod = "mod4"
terminal = guess_terminal()



keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("dmenu_run -l 13 -h 73 -x 1700 -y 32 -fn 'Ubuntu Mono Nerd Font'"),
        desc="Spawn a command using a prompt widget"),
]

__groups={
    1:Group(' Dev '),
    2:Group(' Net '),
    3:Group(' Test '),
    4:Group(' Rel  '),
    5:Group(' Rdm '),
}

groups = [__groups[i] for i in __groups]

def get_key(name):
    return [k for k, g in __groups.items() if g.name==name][0]

for i in groups:
    keys.extend([
        # mod1 + ltter of group = switch to group
        Key([mod], str(get_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_key(i.name)), lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        Key([mod, 'control'], 'Left', lazy.screen.prev_group()),
        Key([mod, 'control'], 'Right', lazy.screen.next_group())
        
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    # layout.Columns(border_focus_stack='#d75f5f',),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),

    layout.MonadTall(
        align=1,
        borde_width=2,
        margin=15,
        border_focus='#75758f',
        border_normal='000000',
    ),

    #layout.MonadWide(),

    layout.Max(),

    #layout.RatioTile(),
    #layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=14,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            
            [

                widget.TextBox(
                    text='a',
                    foreground='#262525',
                    margin_left=3,
                ),

                widget.GroupBox(
                    font='Ubuntu Mono Nerd Font',
                    fontsize=16,
                    margin_y=3,
                    margin_x=3,
                    block_highlight_text_color='9112e0',
                    inactive='ffffff',
                    active='ffffff',
                    borderwidth=0,
                    spacing=35,

                ),
               
                widget.TextBox(
                    text='a',
                    foreground='#262525',
                    padding=275
                ),

                widget.CheckUpdates(
                    font='Ubuntu Mono Nerd Font',
                    display_format='{updates} updates',
                    padding=7
                ),

                widget.TextBox(
                    text='║',
                    foreground='9112e0',
                    fontsize=20
                ),

                widget.Net(
                    font='Ubuntu Mono Nerd Font',
                    format='⇑{down}⇓{up}',
                    padding=7
                ),

                widget.TextBox(
                    text='║',
                    foreground='9112e0',
                    fontsize=20
                ),

                widget.CPU(
                    font='Ubuntu Mono Nerd Font',
                    format='CPU {freq_current}ghz',
                    padding=7,
                ),

                widget.TextBox(
                    text='║',
                    foreground='9112e0',
                    fontsize=20
                ),

                widget.ThermalSensor(
                    font='Ubuntu Mono Nerd Font',
                    padding=7,
                    foreground='#ffffff',
                    margin_x=0,
                ),

                widget.TextBox(
                    text='║',
                    foreground='9112e0',
                    fontsize=20
                ),

                widget.Memory(
                    font='Ubuntu Mono Nerd Font',
                    padding=7,
                    foreground='ffffff',
                    format= 'ram {MemTotal: .0f}{mm} ({MemPercent:.0f}%)'
                ),

                widget.TextBox(
                    text='║',
                    foreground='9112e0',
                    fontsize=20
                ),

                widget.DF(
                    font='Ubuntu Mono Nerd Font',
                    visible_on_warn=False,
                    format='hdd ({uf}{m}) Free',
                    margin_y=0,
                    padding=7
                ),

                widget.TextBox(
                    text='║',
                    foreground='9112e0',
                    fontsize=20
                ),

                widget.Clock(
                    font='Ubuntu Mono Nerd Font',
                    padding=7,
                    margin_y=0,
                    format='%A - %d %B, %H:%M',
                    foreground= 'ffffff',
                ),

            ],
            20,
            background='#262525',
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position(), focus=None),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size(), focus=None),
    Click([mod], "Button2", lazy.window.bring_to_front(), focus=None),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
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
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

automatic = [
    'setxkbmap -model pc105 -layout latam',
    'feh --randomize --bg-scale /home/kaizuser/Imágenes/',
    'picom &',
]

for x in automatic:
    os.system(x)
