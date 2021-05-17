import requests
  

class SuperHero:

    def get_intelligence(self, name):
        url = 'https://superheroapi.com/api/2619421814940190/search/' + name
        resp = requests.get(url)
        if resp.status_code == 200:
            if resp.json()['response'] == 'success':
                return resp.json()['results'][0]['powerstats']['intelligence']
            else: return 0   
        else:
            print(f'Error {resp.status_code}')
            return None     

    def max_intelligence_character(self, hero_list):
        name = None
        max_intelligence = 0
        for hero in hero_list:
            intelligence = self.get_intelligence(hero)
            if intelligence is not None:
                int_intelligence = int(intelligence)
                if int_intelligence > max_intelligence:
                    max_intelligence = int_intelligence
                    name = hero
            else:
                name = None
        return name


if __name__ == '__main__':
    super_heroes = ['hulk', 'Captain America', 'Thanos']
    sh = SuperHero()
    print(sh.max_intelligence_character(super_heroes))