
from typing import TypeAlias

Race: TypeAlias  = str
Sex: TypeAlias  = str
Voice: TypeAlias  = int
Swap: TypeAlias  = tuple[int,int]
FileSwaps: TypeAlias  = dict[int, int]
SexVoice: TypeAlias  = tuple[Sex, Voice]
RaceSexVoice: TypeAlias  = tuple[Race,Sex,Voice]
Options: TypeAlias  = dict[SexVoice, FileSwaps]
Groups: TypeAlias  = dict[str, Options]
Mods: TypeAlias  = dict[RaceSexVoice, Groups]
VoiceDict: TypeAlias = dict[Race, dict[Sex, int]]