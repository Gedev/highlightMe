from collections import defaultdict

import requests

report_id = 'n6rqwa7ZHjWvY84K'
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5OGEzYWZjMy1kZWUyLTQ5MDktOGY0Yy1lZmQ3ODdhZGVhNjEiLCJqdGkiOiJhNTcxZjU5ZWRjZGNhZDA1MDM1ZmY1NDc3NmVlOTE4MWNhZjJkMDlhNjg1MGE2NDVjZTc3NTBiOTdjZWZkMzc4ODM5MTRiZWJlNzhjMmM1NiIsImlhdCI6MTY3ODI4OTU0OC4xMjM1NiwibmJmIjoxNjc4Mjg5NTQ4LjEyMzU2MywiZXhwIjoxNzA5MzkzNTQ4LjExNzM3OCwic3ViIjoiIiwic2NvcGVzIjpbInZpZXctdXNlci1wcm9maWxlIiwidmlldy1wcml2YXRlLXJlcG9ydHMiXX0.xZ_mlnT-JAdAHdJVd1jJ5JjLzZ7UA9ifz86iHyjLnjr54XczYgvIAx8WE_7GgA1PuzQDy9oCzNLVfIA-8MbTnvQ6WlYYovhU7fWCQAPThvcWG7po6qBe0jG-L4NR9ox9lKGit1FuccSB32HYf22ejmt1Ke7viPKghUpr12UHb9UHjX7VITxBP5F2t9W6HCneErlo5EWX39TO6No72jpjDscygWHO9iA5XxQ6o1PjEzSxmiNVD8VF9jTgT40m-lak2h4okFzyfIG30rzMCwEcUbe06WgsadA69UGIPNJ_tf4kwI2gkAoZf1tjaUvro4xgzQHSL3E9zLn7rhYYxN26d6hGKkPiCwQiBttIyIgFCRBaEgR3nG7yxoGGhPwc-UmkW7_hA8rgQjsyZhIptFv6E7bc4B-dfraU_ED5QQ-C71HfXJZo7n9NhE0NSZQzypU3x41-R4u5DcLWWCiVru8SFbpaxUiRX4JBP779_Fvh_EaihBWg1Ct26SKpyGdfSofwD_Yye6r9if3Qezm-zjGWpkLrgc-3gFTH-VQgEnWKqojBSPdF4A1t3lnhWMihzr876heOrYzb2_oPif7LCaHnb9558r4RUIwcMoY4jW1sLpzBPdl5hdhqUlv2WcMKqo2RlJK9O-1RkpCTpXA2tzn9tjZUNqjSrBkvE0Z7MhOPdfU'

# Set up the API URL
api_url = f'https://www.warcraftlogs.com/api/v2'

# Set up the headers for the API request
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5OGEzYWZjMy1kZWUyLTQ5MDktOGY0Yy1lZmQ3ODdhZGVhNjEiLCJqdGkiOiJhNTcxZjU5ZWRjZGNhZDA1MDM1ZmY1NDc3NmVlOTE4MWNhZjJkMDlhNjg1MGE2NDVjZTc3NTBiOTdjZWZkMzc4ODM5MTRiZWJlNzhjMmM1NiIsImlhdCI6MTY3ODI4OTU0OC4xMjM1NiwibmJmIjoxNjc4Mjg5NTQ4LjEyMzU2MywiZXhwIjoxNzA5MzkzNTQ4LjExNzM3OCwic3ViIjoiIiwic2NvcGVzIjpbInZpZXctdXNlci1wcm9maWxlIiwidmlldy1wcml2YXRlLXJlcG9ydHMiXX0.xZ_mlnT-JAdAHdJVd1jJ5JjLzZ7UA9ifz86iHyjLnjr54XczYgvIAx8WE_7GgA1PuzQDy9oCzNLVfIA-8MbTnvQ6WlYYovhU7fWCQAPThvcWG7po6qBe0jG-L4NR9ox9lKGit1FuccSB32HYf22ejmt1Ke7viPKghUpr12UHb9UHjX7VITxBP5F2t9W6HCneErlo5EWX39TO6No72jpjDscygWHO9iA5XxQ6o1PjEzSxmiNVD8VF9jTgT40m-lak2h4okFzyfIG30rzMCwEcUbe06WgsadA69UGIPNJ_tf4kwI2gkAoZf1tjaUvro4xgzQHSL3E9zLn7rhYYxN26d6hGKkPiCwQiBttIyIgFCRBaEgR3nG7yxoGGhPwc-UmkW7_hA8rgQjsyZhIptFv6E7bc4B-dfraU_ED5QQ-C71HfXJZo7n9NhE0NSZQzypU3x41-R4u5DcLWWCiVru8SFbpaxUiRX4JBP779_Fvh_EaihBWg1Ct26SKpyGdfSofwD_Yye6r9if3Qezm-zjGWpkLrgc-3gFTH-VQgEnWKqojBSPdF4A1t3lnhWMihzr876heOrYzb2_oPif7LCaHnb9558r4RUIwcMoY4jW1sLpzBPdl5hdhqUlv2WcMKqo2RlJK9O-1RkpCTpXA2tzn9tjZUNqjSrBkvE0Z7MhOPdfU',
    'Content-Type': 'application/json',
}


code = input(("Enter report code: ")) # Example of code : n6rqwa7ZHjWvY84K

data = {'query': f'''{{ reportData {{
		report(code: "{code}") {{
			title
			table(startTime: 0, endTime: 99999999999)
			owner {{
				name
			}}
			healthStone: events(
				dataType: Healing
				startTime: 0
				endTime: 999999999
				abilityID: 6262
			) {{
				data
			}},
			death: events(
				dataType: Deaths
				startTime: 0
				endTime: 999999999
			) {{
				data
			}},
			playerDetails(startTime:0, endTime: 99999999)
		}}
	    }}}}
        '''}

# Make the API request
response = requests.post(api_url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("\033[1m Title : \033[0m" + data['data']['reportData']['report'].get('title'),
          ";\033[1m Uploaded By : \033[0m" + "\033[36m" + data['data']['reportData']['report']['owner'].get(
              'name') + "\033[0m")
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
else:
    print(f'Error fetching fight data: {response.status_code} - {response.text}')


playersMap = {}

for role in ['tanks', 'healers', 'dps']:
    for player in data['data']['reportData']['report']['playerDetails']['data']['playerDetails'][role]:
        playersMap[player['id']] = player
print(playersMap)



# countofDeaths = defaultdict(int)
# print("DEATHS RECAP :")
# # Print out the fight details
# for items in data['data']['reportData']['report']['table']['data']['deathEvents']:
#     countofDeaths[items.get('name')] += 1


print("-----------------------------------------------------------------")
print("---------------------- COUNT OF DEATHS --------------------------")
print("-----------------------------------------------------------------")
# Find the max amount of deaths
# max_deaths = max(countofDeaths.values())
#
# print(countofDeaths)
#
# # Print all players with max amount of deaths
# print("Players with max amount of deaths:")
# for player, deaths in countofDeaths.items():
#     if deaths == max_deaths:
#         print(player, max_deaths, "deaths")

deathByPlayer = {}

for event in data['data']['reportData']['report']['death']['data']:
    playerID = event['targetID']
    deathByPlayer.setdefault(playerID, 0)
    deathByPlayer[playerID] += 1

for playerID, death in deathByPlayer.items():
    print(playersMap[playerID]['name'], death, "deaths")


print("-----------------------------------------------------------------")
print("---------------------- HEALTHSTONE USE --------------------------")
print("-----------------------------------------------------------------")

healthStonesUsed = defaultdict(int)

playerDetails = data['data']['reportData']['report']['table']['data']['playerDetails']
print("Use of healthstone during the raid :")

for players in playerDetails['healers']:
    healthStonesUsed[players.get('name')] += players.get('healthstoneUse')

for players in playerDetails['dps']:
    healthStonesUsed[players.get('name')] += players.get('healthstoneUse')

for players in playerDetails['tanks']:
    healthStonesUsed[players.get('name')] += players.get('healthstoneUse')

healthStonesUsed = sorted(healthStonesUsed.items(), key=lambda x: x[1])

for items in healthStonesUsed:
    print(items)

print("-----------------------------------------------------------------")
print("---------------------- POTION USE --------------------------")
print("-----------------------------------------------------------------")

potionUsed = defaultdict(int)

playerDetails = data['data']['reportData']['report']['table']['data']['playerDetails']
print("Use of potions during the raid :")

for player in playerDetails['healers']:
    potionUsed[player.get('name')] = player.get('potionUse')

for player in playerDetails['dps']:
    potionUsed[player.get('name')] = player.get('potionUse')

for player in playerDetails['tanks']:
    potionUsed[player.get('name')] = player.get('potionUse')

potionUsed = sorted(potionUsed.items(), key=lambda x: x[1])

for items in potionUsed:
    print(items)
