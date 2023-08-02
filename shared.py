import json
import os
from type import *

offsets: dict[Race, int] = {
    "Midlander": 0,
    "Lalafell": 1,
    "Elezen": 2,
    "Highlander": 3,
    "Miqo'te": 4,
    "Roegadyn": 5,
    "AuRa": 6,
    "Hrothgar": 7,
    "Viera": 8,
}


default_ids: VoiceDict = {
    "Midlander": {"Male": 7453000, "Female": 7456000},
    "Lalafell": {"Male": 7459000, "Female": 7462000},
    "Elezen": {"Male": 7465000, "Female": 7468000},
    "Highlander": {"Male": 7471000, "Female": 7474000},
    "Miqo'te": {"Male": 7477000, "Female": 7480000},
    "Roegadyn": {"Male": 7483000, "Female": 7486000},
    "AuRa": {"Male": 7489000, "Female": 7492000},
    "Hrothgar": {"Male": 7495000, "Female": 7498000},
    "Viera": {"Male": 7501000, "Female": 7504000},
}


emote_names: list[str] = ["Surprised",
"Angry",
"Furious",
"Cheer",
"Doze",
"Fume",
"Huh",
"Chuckle",
"Laugh",
"No",
"Stretch",
"Upset",
"Yes",
"Happy",
]


default_ids_hroth: VoiceDict = {
    "Midlander": {"Male": 17361000,    "Female": 17364000},
    "Lalafell": {"Male": 17367000,     "Female": 17370000},
    "Elezen": {"Male": 17373000,       "Female": 17376000},
    "Highlander": {"Male": 17379000,   "Female": 17382000},
    "Miqo'te": {"Male": 17385000,      "Female": 17388000},
    "Roegadyn": {"Male": 17391000,     "Female": 17394000},
    "AuRa": {"Male": 17397000,         "Female": 17400000},
    "Hrothgar": {"Male": 17401000,     "Female": 17404000},
    "Viera": {"Male": 17409000,        "Female": 17412000},
}

voice_ids: VoiceDict  = {
    "Midlander": {
        "Male": [
            7453000,
            7452000,
            7451000,
            7403000,
            7402000,
            7401000,
            7353000,
            7352000,
            7351000,
            7303000,
            7302000,
            7301000,
        ],
        "Female": [
            7456000,
            7455000,
            7454000,
            7406000,
            7405000,
            7404000,
            7356000,
            7355000,
            7354000,
            7306000,
            7305000,
            7304000,
        ],
    },
    "Lalafell": {
        "Male": [
            7459000,
            7458000,
            7457000,
            7409000,
            7408000,
            7407000,
            7359000,
            7358000,
            7357000,
            7309000,
            7308000,
            7307000,
        ],
        "Female": [
            7462000,
            7461000,
            7460000,
            7412000,
            7411000,
            7410000,
            7362000,
            7361000,
            7360000,
            7312000,
            7311000,
            7310000,
        ],
    },
    "Elezen": {
        "Male": [
            7465000,
            7464000,
            7463000,
            7415000,
            7414000,
            7413000,
            7365000,
            7364000,
            7363000,
            7315000,
            7314000,
            7313000,
        ],
        "Female": [
            7468000,
            7467000,
            7466000,
            7418000,
            7417000,
            7416000,
            7368000,
            7367000,
            7366000,
            7318000,
            7317000,
            7316000,
        ],
    },
    "Highlander": {
        "Male": [
            7471000,
            7470000,
            7469000,
            7421000,
            7420000,
            7419000,
            7371000,
            7370000,
            7369000,
            7321000,
            7320000,
            7319000,
        ],
        "Female": [
            7474000,
            7473000,
            7472000,
            7424000,
            7423000,
            7422000,
            7374000,
            7373000,
            7372000,
            7324000,
            7323000,
            7322000,
        ],
    },
    "Miqo'te": {
        "Male": [
            7477000,
            7476000,
            7475000,
            7427000,
            7426000,
            7425000,
            7377000,
            7376000,
            7375000,
            7327000,
            7326000,
            7325000,
        ],
        "Female": [
            7480000,
            7479000,
            7478000,
            7430000,
            7429000,
            7428000,
            7380000,
            7379000,
            7378000,
            7330000,
            7329000,
            7328000,
        ],
    },
    "Roegadyn": {
        "Male": [
            7483000,
            7482000,
            7481000,
            7433000,
            7432000,
            7431000,
            7383000,
            7382000,
            7381000,
            7333000,
            7332000,
            7331000,
        ],
        "Female": [
            7486000,
            7485000,
            7484000,
            7436000,
            7435000,
            7434000,
            7386000,
            7385000,
            7384000,
            7336000,
            7335000,
            7334000,
        ],
    },
    "AuRa": {
        "Male": [
            7489000,
            7488000,
            7487000,
            7439000,
            7438000,
            7437000,
            7389000,
            7388000,
            7387000,
            7339000,
            7338000,
            7337000,
        ],
        "Female": [
            7492000,
            7491000,
            7490000,
            7442000,
            7441000,
            7440000,
            7392000,
            7391000,
            7390000,
            7342000,
            7341000,
            7340000,
        ],
    },
    "Hrothgar": {
        "Male": [
            17453000,
            17452000,
            17451000,
            17403000,
            17402000,
            17401000,
            17353000,
            17352000,
            17351000,
            17303000,
            17302000,
            17301000,
        ],
        "Female": [
            17456000,
            17455000,
            17454000,
            17406000,
            17405000,
            17404000,
            17356000,
            17355000,
            17354000,
            17306000,
            17305000,
            17304000,
        ],
    },
    "Viera": {
        "Male": [
            17459000,
            17458000,
            17457000,
            17409000,
            17408000,
            17407000,
            17359000,
            17358000,
            17357000,
            17309000,
            17308000,
            17307000,
        ],
        "Female": [
            17462000,
            17461000,
            17460000,
            17412000,
            17411000,
            17410000,
            17362000,
            17361000,
            17360000,
            17312000,
            17311000,
            17310000,
        ],
    },
}

mod_name = "Voice Changer"
# create files with data
def make_mods(data: Mods, directory= "./MODS"):
    for key, value in data.items():
        make_mod(key, value, directory)

def make_mod(identifier: RaceSexVoice, groups: Groups, directory):
    directory = f"{directory}/{mod_name} for {modname(identifier)}"
    os.makedirs(os.path.dirname(f"{directory}/default.json"), exist_ok=True)
    with open(f"{directory}/default.json", 'w') as f:
        json.dump({
            "Name": "",
            "Priority": 0,
            "Files": { },
            "FileSwaps": { },
            "Manipulations": []
            }, f, indent=2)
    with open(f"{directory}/meta.json", 'w') as f:
        json.dump({
            "FileVersion": 1,
            "Name": f"{mod_name} for {modname(identifier)}",
            "Author": "Cat",
            "Description": "let's you cahnge voices when changing races with Glamourer",
            "Version": "1.0.0",
            "Website": "",
            "ModTags": []
            }, f, indent=2)
    group_no = 1
    for key, val in groups.items():
        with open(f"{directory}/group_{group_no:03d}_{key.lower()}.json", 'w') as f:
            json.dump(make_group(key, val), f, indent=2)


none_option = {
      "Name": "None",
      "Description": "",
      "Files": {},
      "FileSwaps": {},
      "Manipulations": []
    }

def make_group(key: str, options: Options):
    return  {
    "Name": key,
    "Description": "",
    "Priority": 0, # priority,
    "Type": "Single",
    "DefaultSettings": "0",
    "Options": [none_option, *make_options(options)]
 }

def make_options(options: Options):
    return [make_option(key, opt) for (key,opt) in options.items()]

def make_option(key:RaceSexVoice, file_swaps: FileSwaps ):
    return  {
      "Name": modname(key),
      "Description": "",
      "Files": {},
      "FileSwaps": make_fileswaps(file_swaps),
      "Manipulations": []
    }

def make_fileswaps(opt: FileSwaps):
    return {f"sound/voice/vo_emote/{k}.scd": f"sound/voice/vo_emote/{v}.scd" for k,v in opt.items()}

def modname(identifier: RaceSexVoice):
    return f"{identifier[0]} {identifier[1]} {identifier[2]+1}"