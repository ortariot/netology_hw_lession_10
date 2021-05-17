from stak_owf_getter import StakOwerFlowSimpleClient
from ya_drive_uploader import YaDrive
from super_hero import SuperHero

# token:
token = ''

def main():
    cloud = YaDrive(token, '/test_app/') 
    with open('smartest_super_hero.txt', 'w', encoding='utf-8') as f:
        sh = SuperHero()
        f.write(sh.max_intelligence_character(['hulk', 'Captain America', 'Thanos']))
    cloud.upload('smartest_super_hero.txt')
    with open('sowf_last_questions.txt', 'w', encoding='utf-8') as f:
        sowf = StakOwerFlowSimpleClient()
        request = sowf.get_two_day_last_question('python')
        q_list = [line['title'] + '\n' for line in request]
        f.writelines(q_list)   
    cloud.upload('sowf_last_questions.txt')    


if __name__ == '__main__':
    main()