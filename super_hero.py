import requests
  
def get_intelligence(name):
    url = 'https://superheroapi.com/api/2619421814940190/search/' + name
    resp = requests.get(url)
    if resp.status_code == 200:
        if resp.json()['response'] == 'success':
            return resp.json()['results'][0]['powerstats']['intelligence']
        else: return 0   
    else:
        print(f'Error {resp.status_code}')
        return None     

def max_intelligence_character(hero_list):
    name = None
    max_intelligence = 0
    for hero in hero_list:
        intelligence = get_intelligence(hero)
        if intelligence is not None:
            int_intelligence = int(intelligence)
            if int_intelligence > max_intelligence:
                max_intelligence = int_intelligence
                name = hero
        else:
            name = None
    return name


if __name__ == '__main__':
    super_hero = ['hulk', 'Captain America', 'Thanos']
    print(max_intelligence_character(super_hero))