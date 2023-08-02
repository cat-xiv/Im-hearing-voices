import shared
from type import *

shared.mod_name = "Emote Changer"

def mods_data() -> Mods:
    return {(race,sex,voice): mod_data(race,sex,voice)  
            for race in shared.voice_ids.keys()  
            for sex in shared.voice_ids[race].keys() 
            for voice in range(0, len(shared.voice_ids[race][sex]))}

def mod_data(race:Race, sex:Sex, voice:Voice)-> Groups:
    return {f"{to_race} {shared.emote_names[to_emote]}":group_data(race, sex, voice, to_race, to_emote) 
                for to_race in shared.voice_ids.keys() 
                for to_emote in range(0, len(shared.emote_names))
                }

def group_data(race:Race, sex:Sex, voice:Voice, to_race:Race, to_emote:int) -> Options: 
    return {(to_race, to_sex,to_voice):option_data(race,sex,voice, to_race,to_sex,to_voice, to_emote) 
            for to_sex in shared.voice_ids[to_race].keys() 
            for to_voice in range(0,len(shared.voice_ids[to_race][to_sex]))
            }

def option_data(race:Race, sex:Sex, voice:Voice, to_race:Race,to_sex:Sex,to_voice:Voice, to_emote:int) -> FileSwaps:
    return dict([swaps_data(race,sex,voice,to_race,to_sex,to_voice,to_emote)])

def swaps_data(race:Race, sex:Sex, voice:Voice,to_race:Race,to_sex:Sex,to_voice:Voice,to_emote:int) -> Swap:
    return (from_file_id(race,sex,voice, to_race)+to_emote, to_file_id(to_race,to_sex,to_voice)+to_emote)

def from_file_id(race:Race, sex:Sex, voice:Voice, to_race:Race) -> int:
    offset_a = (voice % 3) * 1000
    offset_b = (shared.offsets[race] - shared.offsets[to_race])*6000
    from_id = shared.voice_ids[race][sex][voice] + offset_a - offset_b
    if race == to_race:
        from_id = shared.voice_ids[race][sex][voice]
    # TODO: Find all voices that are duplicated and add exceptions eg.: midlander f 1 and roegadyn f 2
    return from_id

def to_file_id(to_race:Race,to_sex:Sex,to_voice:Voice) -> int:
    return  shared.voice_ids[to_race][to_sex][to_voice]


if __name__ == "__main__":
    shared.make_mods(mods_data(), "./Emote")
