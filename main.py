from dataclasses import dataclass
import math
import random


@dataclass
class SimulationStatistic: # Naming Conveniton (PEP8)
    clone_winrate:float
    droids_winrate:float
    medium_round_count:float
    clone_survivale:float
    droids_survivale:float

    def __str__(self)->str:
        return (f'Clone winrate: {battle_list.clone_winrate}\n'
        f'Droids winrate: {battle_list.droids_winrate}\n'
        f'Medium rounds: {battle_list.medium_round_count}\n' 
        f'Clone survability: {battle_list.clone_survivale}\n'
        f'Droids survability: {battle_list.droids_survivale}')

@dataclass 
class RoundStatistics:
    round_count:int=0
    clone_wins:int=0
    droids_wins:int=0
    clone_survivale:int=0
    droids_survivale:int=0    

#random.seed(100)

def simulate_single_battle(clone_count: int ,droid_count: int, droid_attack_power:int=1,hit_threshold:int=30,verbose_output:bool=True)->tuple[int ,int,int]:
    round_count=1
    while clone_count>0 and droid_count>0:
        clone_count-=droid_count//droid_attack_power
        clone_count=max(clone_count,0)
        for chance_to_hit in range(clone_count):
            chance_to_hit=random.randint(1,100)
            if chance_to_hit>hit_threshold:
                    droid_count-=1

        if verbose_output==True:
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



    return (clone_count,droid_count,round_count)




def simulate_battles(clone_count: int ,droid_count: int, droid_attack_power:int=1,hit_threshold:int=25,number_of_fights:int=1,verbose:bool=False)->SimulationStatistic:

    stats=RoundStatistics()


    for _ in range(number_of_fights):

        clone_left,droids_left,rounds_in_battle=simulate_single_battle(clone_count,droid_count,droid_attack_power,hit_threshold,verbose_output=verbose)

        if droids_left<=0:
            stats.clone_survivale+=clone_left
            stats.clone_wins+=1

        elif clone_left<=0:
            stats.droids_survivale+=droids_left
            stats.droids_wins+=1


        stats.round_count+=rounds_in_battle


    return SimulationStatistic(clone_winrate=stats.clone_wins/number_of_fights
                            ,droids_winrate=stats.droids_wins/number_of_fights
                            ,medium_round_count=stats.round_count/number_of_fights
                            ,clone_survivale=stats.clone_survivale/number_of_fights
                            ,droids_survivale=stats.droids_survivale/number_of_fights)




if __name__=='__main__':

    print('Try 1')
    simulate_single_battle(15,20,droid_attack_power=5)

    print('Try 2')
    simulate_single_battle(10,20,droid_attack_power=10)

    print('Try 3')
    simulate_single_battle(15,100,droid_attack_power=1)

    print("Simulation")

    battle_list=simulate_battles(clone_count=8,droid_count=10,droid_attack_power=3,hit_threshold=30,number_of_fights=1000,verbose=False)
    print(battle_list)




