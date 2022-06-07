from scrape_champion_points import *

#kevin_dict = get_mastery_point_dict('Nah latez')
kevin_dict = get_mastery_point_dict('dillusion8015')
vince_dict = get_mastery_point_dict('SalvatioÑ')

kevin_more_mastery = []
vince_more_master = []

champions = set(kevin_dict.keys()).union(set(vince_dict.keys()))
for champion in champions:
    if champion in vince_dict:
        if champion not in kevin_dict:
            kevin_dict[champion] = 0

        if vince_dict[champion] > kevin_dict[champion]:
            vince_more_master.append(
                f"Vince Has {str(vince_dict[champion] - kevin_dict[champion])} "
                f"More Points On {champion}"
            )

        else:
            kevin_more_mastery.append(
                f"Donny Has {str(kevin_dict[champion] - vince_dict[champion])} "
                f"More Points On {champion}"
            )

    else:

        if champion in kevin_dict:
            kevin_more_mastery.append(
                f"Donny Has {str(kevin_dict[champion])} "
                f"More Points On {champion}"
            )

        else:
            print(f'Neither Has Played {champion}')

print(f'Kevin Has More Points On {len(kevin_more_mastery)} Champions:')
[print(champion) for champion in kevin_more_mastery]

print(f'Vince Has More Points On {len(vince_more_master)} Champions:')
[print(champion) for champion in vince_more_master]