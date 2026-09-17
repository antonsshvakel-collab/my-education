from dataclasses import dataclass
import math
import random


@dataclass
class Simulation_Statistic:
    clone_winrate:float
    droids_winrate:float
    medium_round_count:float
    clone_survivale:float
    droids_survivale:float

@dataclass
class Stats:
    round_count:int=0
    clone_wins:int=0
    droids_wins:int=0
    clone_survivale:int=0
    droids_survivale:int=0    



def battle_simulation(clone_count: int ,droid_count: int, droid_attack_power:int=1,hit_threshold:int=30,verbose_battle:bool=True)->tuple[int ,int]:
    round_count=1
    while clone_count>0 and droid_count>0:
        clone_count-=1
        for chance_to_hit in range(clone_count):
            chance_to_hit=random.randint(1,100)
            if chance_to_hit>hit_threshold:
                    droid_count-=1

        if verbose_battle==True:
            if droid_count<=0:
                print(f'Победа за силами Галактической Республики!\nОсталось клонов: {clone_count};')
                break
        
            elif clone_count<=0:
                print(f'Победа за силами Торговой Федерации!\nОсталось дроидов: {droid_count};')
                break
        
            elif clone_count<=0 and droid_count <=0:
                print('Ничья! Все участники пали в бою!' )
                break
        
            print(f'Раунд {round_count}: осталось клонов — {clone_count}, осталось дроидов — {droid_count}')
            round_count+=1



    return clone_count,droid_count




def Simulation_of_battles(clone_count: int ,droid_count: int, droid_attack_power:int=1,hit_threshold:int=25,number_of_fights:int=1,verbose:bool=False)->Simulation_Statistic:

    stats=Stats()


    for _ in range(number_of_fights):

        clone_left,droids_left=battle_simulation(clone_count,droid_count,verbose_battle=verbose)

        if droids_left<=0:
            stats.clone_survivale+=clone_left
            stats.clone_wins+=1

        elif clone_left<=0:
            stats.droids_survivale+=droids_left
            stats.droids_wins+=1


        stats.round_count+=1


    return Simulation_Statistic(clone_winrate=stats.clone_wins/number_of_fights
                            ,droids_winrate=stats.droids_wins/number_of_fights
                            ,medium_round_count=stats.round_count/number_of_fights
                            ,clone_survivale=stats.clone_survivale/number_of_fights
                            ,droids_survivale=stats.droids_survivale/number_of_fights)




if __name__=='__main__':
    try:
        print('Try 1')
        battle_simulation(10,20)

        print('Try 2')
        battle_simulation(5,20)

        print('Try 3')
        battle_simulation(10,40)
    except ValueError as error:
        print(f'Error occur {error}')

    try:
        print("Simulation")

        battle_list=Simulation_of_battles(clone_count=5,droid_count=8,number_of_fights=1000,verbose=False)
        print(f'Clone winrate {battle_list.clone_winrate}', f'Droids winrate {battle_list.droids_winrate}', f'Medium rounds {battle_list.medium_round_count}' ,f'Clone survability {battle_list.clone_survivale}', f'Droids survability {battle_list.droids_survivale}',sep='\n')
    except ValueError as error:
        print(f'Error occur {error}')



