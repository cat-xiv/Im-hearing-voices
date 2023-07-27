import os

offsets = {
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


default_ids = {
    "Midlander": {"Masculine": 7453000, "Feminine": 7456000},
    "Lalafell": {"Masculine": 7459000, "Feminine": 7462000},
    "Elezen": {"Masculine": 7465000, "Feminine": 7468000},
    "Highlander": {"Masculine": 7471000, "Feminine": 7474000},
    "Miqo'te": {"Masculine": 7477000, "Feminine": 7480000},
    "Roegadyn": {"Masculine": 7483000, "Feminine": 7486000},
    "AuRa": {"Masculine": 7489000, "Feminine": 7492000},
    "Hrothgar": {"Masculine": 7495000, "Feminine": 7498000},
    "Viera": {"Masculine": 7501000, "Feminine": 7504000},
}











default_ids_hroth = {
    "Midlander": {"Masculine": 17361000,    "Feminine": 17364000},
    "Lalafell": {"Masculine": 17367000,     "Feminine": 17370000},
    "Elezen": {"Masculine": 17373000,       "Feminine": 17376000},
    "Highlander": {"Masculine": 17379000,   "Feminine": 17382000},
    "Miqo'te": {"Masculine": 17385000,      "Feminine": 17388000},
    "Roegadyn": {"Masculine": 17391000,     "Feminine": 17394000},
    "AuRa": {"Masculine": 17397000,         "Feminine": 17400000},
    "Hrothgar": {"Masculine": 17401000,     "Feminine": 17404000},
    "Viera": {"Masculine": 17409000,        "Feminine": 17412000},
}




prio = 0
mod_directory = "./MODS"
voice_ids = {
    "Midlander": {
        "Masculine": [
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
        "Feminine": [
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
        "Masculine": [
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
        "Feminine": [
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
        "Masculine": [
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
        "Feminine": [
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
        "Masculine": [
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
        "Feminine": [
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
        "Masculine": [
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
        "Feminine": [
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
        "Masculine": [
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
        "Feminine": [
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
        "Masculine": [
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
        "Feminine": [
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
        "Masculine": [
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
        "Feminine": [
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
        "Masculine": [
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
        "Feminine": [
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


def mods_gen():
    print("generating mods")
    for from_race in voice_ids.keys():
        for from_gender in voice_ids[from_race].keys():
            for from_voice in range(0, len(voice_ids[from_race][from_gender])):
                mod_gen(from_race, from_gender, from_voice)


def mod_gen(from_race, from_gender, from_voice):
    print(f"### generating mod {from_race} {from_gender} {from_voice+1} ###")
    global mod_directory
    mod_directory = f"./MODS/Voice Fix {from_race} {from_gender} Voice {from_voice +1}"
    meta_filename = mod_directory + "/meta.json"
    meta_file = (
        """{
  "FileVersion": 1,
  "Name": "Glamourer Voice fix for """
        + f"{from_race} {from_gender} voice {from_voice+1}"
        + """\",
  "Author": "Cat",
  "Description": "Fixes broken voices when changing races with Glamourer",
  "Version": "1.0.0",
  "Website": "",
  "ModTags": []
}"""
    )
    default_file = """{
  "Name": "",
  "Priority": 0,
  "Files": { },
  "FileSwaps": { },
  "Manipulations": []
}"""
    default_filename = mod_directory + "/default_mod.json"
    os.makedirs(os.path.dirname(meta_filename), exist_ok=True)
    with open(meta_filename, "w") as mf:
        mf.write(meta_file)
    with open(default_filename, "w") as df:
        df.write(default_file)
    groups_gen(from_race, from_gender, from_voice)


def groups_gen(from_race, from_gender, from_voice):
    global mod_directory
    group = 0
    print(
        f"creating groups for {from_race}, {from_gender}, {from_voice+1}: {voice_ids[from_race][from_gender][from_voice]}"
    )
    for to_race in voice_ids.keys():
        group += 1
        filename = mod_directory + f"/group_{group:03d}_{to_race}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as file:
            file.write(group_gen(from_race, from_gender, from_voice, to_race))
    pass


def group_gen(from_race, from_gender, from_voice, to_race):
    global prio
    prio += 1
    offset_a = (from_voice % 3) * 1000
    offset_b = (offsets[from_race] - offsets[to_race])*6000
    from_id = voice_ids[from_race][from_gender][from_voice] + offset_a - offset_b
    if from_race == to_race:
        from_id = voice_ids[from_race][from_gender][from_voice]
    #elif from_race == "Hrothgar" or from_race == "Viera":
    #    from_id = default_ids_hroth[to_race][from_gender]



    print(f"creating group {to_race} from_id: {from_id} offsets {offset_a} {offset_b}")
    return (
        """ {
    "Name": \""""
        + to_race
        + """ emote voice\",
    "Description": "The emote voice you are replacing",
    "Priority": """
        + str(prio)
        + """,
    "Type": "Single",
    "DefaultSettings": 0,
    "Options": ["""
        + options_gen(to_race, from_id)
        + """]
    }"""
    )


def options_gen(race, from_id):
    global prio
    tmp = [
        """{
      "Name": "None",
      "Description": "",
      "Files": {},
      "FileSwaps": {},
      "Manipulations": []
    }"""
    ]

    # print(f"generating options for {race}")
    for gender in voice_ids[race].keys():
        for voice in range(0, len(voice_ids[race][gender])):
            tmp.append(option_gen(race, gender, voice, from_id))
    return ",\n".join(tmp)


def option_gen(race, gender, voice, from_id):
    global prio
    prio += 1
    # print(f"{from_id}, voice_ids[{race}][{gender}][{voice}]")

    # print(f"generating option for {race}, {gender}, {voice} ,{from_id}")
    tmp = file_swaps(from_id, voice_ids[race][gender][voice])

    return (
        """{"Name": \""""
        + race
        + " "
        + gender
        + " "
        + str(voice + 1)
        + """\",
            "Description": "",
            "Priority": """
        + str(prio)
        + """,
            "Files": {},
            "FileSwaps": {
                """
        + tmp
        + """
            },
            "Manipulations": []
        }"""
    )


def file_swaps(from_id, to_id):
    tmp = []
    for i in range(0, 16):
        tmp.append(file_swap(from_id + i, to_id + i))
    return ",\n".join(tmp)


def file_swap(from_id, to_id):
    return f'"sound/voice/vo_emote/{from_id}.scd": "sound\\\\voice\\\\vo_emote\\\\{to_id}.scd"'


if __name__ == "__main__":
    mods_gen()
    # groups_gen("Hrothgar", "Masculine", 5)
    # from_race, from_gender, from_voice, to_race
