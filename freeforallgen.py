import shared
from type import *

shared.mod_name = "Voice Changer FFA"

def mods_data() -> Mods:
    return {(race,sex,voice): mod_data(race,sex,voice)  
            for race in shared.voice_ids.keys()  
            for sex in shared.voice_ids[race].keys() 
            for voice in range(0, len(shared.voice_ids[race][sex]))}

def mod_data(race:Race, sex:Sex, voice:Voice)-> Groups:
    return {to_race:group_data(race, sex, voice, to_race) for to_race in shared.voice_ids.keys()  }

def group_data(race:Race, sex:Sex, voice:Voice, to_race:Race) -> Options: 
    return {(emote_race, to_sex,to_voice):option_data(race,sex,voice, to_race,to_sex,to_voice, emote_race) 
            for emote_race in shared.voice_ids.keys()  
            for to_sex in shared.voice_ids[emote_race].keys() 
            for to_voice in range(0,len(shared.voice_ids[emote_race][to_sex]))}

def option_data(race:Race, sex:Sex, voice:Voice, to_race:Race,to_sex:Sex,to_voice:Voice, emote_race: Race) -> FileSwaps:
    return dict([swaps_data(race,sex,voice,to_race,to_sex,to_voice,i, emote_race)  for i in range(0, 14)])

def swaps_data(race:Race, sex:Sex, voice:Voice,to_race:Race,to_sex:Sex,to_voice:Voice,offset:int, emote_race:Race) -> Swap:
    return (from_file_id(race,sex,voice, to_race)+offset, to_file_id(emote_race,to_sex,to_voice)+offset)

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
    shared.make_mods(mods_data(), "./FFA")
