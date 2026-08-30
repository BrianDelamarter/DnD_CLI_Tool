from terminaltexteffects.effects.effect_burn import Burn
from terminaltexteffects.effects.effect_print import Print
from terminaltexteffects.effects import Thunderstorm
from terminaltexteffects.effects.effect_wipe import Wipe
import pyfiglet


def burn(text: str):
    effect = Burn(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def printer(text: str):
    effect = Print(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def thunderstorm(text: str):
    effect = Thunderstorm(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def wipe(text: str):
    effect = Wipe(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def figlet_format(text: str, font: str):
    return pyfiglet.figlet_format(text, font=font)