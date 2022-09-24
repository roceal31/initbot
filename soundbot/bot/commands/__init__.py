from typing import FrozenSet, Any
from .commands import soundboard, shush, sounds, sound

commands: FrozenSet[Any] = frozenset((soundboard, shush, sounds, sound))
