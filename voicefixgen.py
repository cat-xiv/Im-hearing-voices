import shared
from type import *

# for each race + sex + voice combination create a mod
def mods_data() -> Mods:
    return {(race,sex,voice): mod_data(race,sex,voice)  
            for race in shared.voice_ids.keys()  
            for sex in shared.voice_ids[race].keys() 
            for voice in range(0, len(shared.voice_ids[race][sex]))}

# for each mod create a group per race
def mod_data(race:Race, sex:Sex, voice:Voice)-> Groups:
    return {to_race:group_data(race, sex, voice, to_race) for to_race in shared.voice_ids.keys()  }

# for each group create a list of options
def group_data(race:Race, sex:Sex, voice:Voice, to_race:Race) -> Options: 
    return {(to_race, to_sex,to_voice):option_data(race,sex,voice, to_race,to_sex,to_voice) 
            for to_sex in shared.voice_ids[to_race].keys() 
            for to_voice in range(0,len(shared.voice_ids[to_race][to_sex]))}

# for each option create a list of file swaps
def option_data(race:Race, sex:Sex, voice:Voice, to_race:Race,to_sex:Sex,to_voice:Voice) -> FileSwaps:
    return dict([file_swap(race,sex,voice,to_race,to_sex,to_voice,i) for i in range(0, 14)])

# for each fileswap get the correct fileId (which file needs to be changed and which file has the chosen voice)
def file_swap(race:Race, sex:Sex, voice:Voice,to_race:Race,to_sex:Sex,to_voice:Voice,offset:int) -> Swap:
    return (from_file_id(race,sex,voice, to_race)+offset, to_file_id(to_race,to_sex,to_voice)+offset)


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
    shared.make_mods(mods_data())
