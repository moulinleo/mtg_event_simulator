import random

import matplotlib.pyplot as plt
import numpy as np




winrate = 0.5

rewards = {
    'gold':[0,0,0,0,0,0],
    'gems':[50,100,150,600,800,1000],
}

def generate_result(winrate=winrate):
    if random.random() < winrate:
        return 1
    else:
        return 0


nb_exps = 10000

def run(nb_exps, winrate=winrate, rewards = rewards):
    gain_gem_tot = 0 
    list_nb_wins = []
    list_gain_gems = []
    list_avg_gems = []
    nb_games = 5
    for exp in range(1,nb_exps):
        nb_wins = 0
        for game in range(nb_games):
            nb_wins = nb_wins + generate_result(winrate=winrate)
        gain_gem = rewards['gems'][nb_wins]
        
        list_gain_gems.append(gain_gem)
        list_nb_wins.append(nb_wins)
        gain_gem_tot = gain_gem_tot + gain_gem
        avg_gem = gain_gem_tot/exp
        list_avg_gems.append(avg_gem)
    return list_gain_gems, list_nb_wins, list_avg_gems, avg_gem



rewards_std = {
    'gold':[0,0,0,0,0,0],
    'gems':[25,50,75,200,300,400,450, 500],
}

def run_std_event(nb_exps, winrate=winrate, rewards=rewards_std):
    gain_gem_tot = 0 
    list_nb_wins = []
    list_gain_gems = []
    list_avg_gems = []
    for exp in range(1,nb_exps):
        nb_wins = 0
        nb_loses = 0
        for game in range(1000):
            win = generate_result(winrate=winrate)
            if win == 0:
                nb_loses = nb_loses + 1
            nb_wins = nb_wins + win
            if (nb_wins == 7) or (nb_loses == 3):
                gain_gem = rewards['gems'][nb_wins]
                break
        
        list_gain_gems.append(gain_gem)
        list_nb_wins.append(nb_wins)
        gain_gem_tot = gain_gem_tot + gain_gem
        avg_gem = gain_gem_tot/exp
        list_avg_gems.append(avg_gem)
    return list_gain_gems, list_nb_wins, list_avg_gems, avg_gem




rewards_trad_draft = {
    'gold':[0,0,0,0,0,0],
    'gems':[100,250,1000,2500],
}

def run_trad_draft(nb_exps, winrate=winrate, rewards=rewards_trad_draft):
    gain_gem_tot = 0 
    list_nb_wins = []
    list_gain_gems = []
    list_avg_gems = []
    for exp in range(1,nb_exps):
        nb_wins = 0
        nb_games = 3
        for game in range(nb_games):
            nb_wins = nb_wins + generate_result(winrate=winrate)
        gain_gem = rewards['gems'][nb_wins]
        
        list_gain_gems.append(gain_gem)
        list_nb_wins.append(nb_wins)
        gain_gem_tot = gain_gem_tot + gain_gem
        avg_gem = gain_gem_tot/exp
        list_avg_gems.append(avg_gem)
    return list_gain_gems, list_nb_wins, list_avg_gems, avg_gem

ratio_gold_gem_quick = 0 
ratio_gold_gem_prem = 0

rewards_quick = {
    'gold':[0,0,0,0,0,0],
    'gems':[50,100,200,300,450,650,850,950],
}

def run_quick_draft(nb_exps, winrate=winrate, rewards=rewards_quick):
    gain_gem_tot = 0 
    list_nb_wins = []
    list_gain_gems = []
    list_avg_gems = []
    for exp in range(1,nb_exps):
        nb_wins = 0
        nb_loses = 0
        for game in range(1000):
            win = generate_result(winrate=winrate)
            if win == 0:
                nb_loses = nb_loses + 1
            nb_wins = nb_wins + win
            if (nb_wins == 7) or (nb_loses == 3):
                gain_gem = rewards['gems'][nb_wins]
                break
        
        list_gain_gems.append(gain_gem)
        list_nb_wins.append(nb_wins)
        gain_gem_tot = gain_gem_tot + gain_gem
        avg_gem = gain_gem_tot/exp
        list_avg_gems.append(avg_gem)
    return list_gain_gems, list_nb_wins, list_avg_gems, avg_gem


rewards_prem = {
    'gold':[0,0,0,0,0,0],
    'gems':[50,100,250,1000,1400,1600,1800,2200],
}

def run_prem_draft(nb_exps, winrate=winrate, rewards=rewards_prem):
    gain_gem_tot = 0 
    list_nb_wins = []
    list_gain_gems = []
    list_avg_gems = []
    for exp in range(1,nb_exps):
        nb_wins = 0
        nb_loses = 0
        for game in range(1000):
            win = generate_result(winrate=winrate)
            if win == 0:
                nb_loses = nb_loses + 1
            nb_wins = nb_wins + win
            if (nb_wins == 7) or (nb_loses == 3):
                gain_gem = rewards['gems'][nb_wins]
                break
        
        list_gain_gems.append(gain_gem)
        list_nb_wins.append(nb_wins)
        gain_gem_tot = gain_gem_tot + gain_gem
        avg_gem = gain_gem_tot/exp
        list_avg_gems.append(avg_gem)
    return list_gain_gems, list_nb_wins, list_avg_gems, avg_gem






nb_exps = 100

if 0:

    fig, axes = plt.subplots(nrows=3, ncols=2)
    axes[0, 0].axhline(y=750, label='ENTRY COST', linestyle='--')
    axes[0, 1].axhline(y=375, label='ENTRY COST', linestyle='--')
    axes[1, 0].axhline(y=750, label='ENTRY COST', linestyle='--')
    axes[1, 1].axhline(y=1500, label='ENTRY COST', linestyle='--')
    axes[2, 0].axhline(y=1500, label='ENTRY COST', linestyle='--')

    for winrate in [0.5, 0.6, 0.7, 0.8]:
        list_gain_gems, list_nb_wins, list_avg_gems, avg_gem = run(nb_exps, winrate=winrate)
        axes[0, 0].set_ylabel('Gems gained')
        axes[0, 0].set_xlabel('Number of drafts')
        axes[0, 0].plot(list_avg_gems, label = f'winrate = {winrate}')
        axes[0, 0].set_title('trad_std_event')
        axes[0, 0].legend(fontsize='small')
        
        # SECOND    
        list_gain_gems, list_nb_wins, list_avg_gems, avg_gem = run_std_event(nb_exps, winrate=winrate)
        axes[0, 1].set_ylabel('Gems gained')
        axes[0, 1].set_xlabel('Number of drafts')
        axes[0, 1].plot(list_avg_gems, label = f'winrate = {winrate}')
        axes[0, 1].set_title('std_event')
        axes[0, 1].legend(fontsize='small')
        
        # TRAD DRAFT
        list_gain_gems, list_nb_wins, list_avg_gems, avg_gem = run_trad_draft(nb_exps, winrate=winrate)
        axes[1, 1].set_ylabel('Gems gained')
        axes[1, 1].set_xlabel('Number of drafts')
        axes[1, 1].plot(list_avg_gems, label = f'winrate = {winrate}')
        axes[1, 1].set_title('trad_draft')
        axes[1, 1].legend(fontsize='small')
        
        # QUICK DRAFT
        list_gain_gems, list_nb_wins, list_avg_gems, avg_gem = run_quick_draft(nb_exps, winrate=winrate)
        axes[1, 0].set_ylabel('Gems gained')
        axes[1, 0].set_xlabel('Number of drafts')
        axes[1, 0].plot(list_avg_gems, label = f'winrate = {winrate}')
        axes[1, 0].set_title('quick_draft')
        axes[1, 0].legend(fontsize='small')
        
        # PREMIER DRAFT
        list_gain_gems, list_nb_wins, list_avg_gems, avg_gem = run_prem_draft(nb_exps, winrate=winrate)
        axes[2, 0].set_ylabel('Gems gained')
        axes[2, 0].set_xlabel('Number of drafts')
        axes[2, 0].plot(list_avg_gems, label = f'winrate = {winrate}')
        axes[2, 0].set_title('prem_draft')
        axes[2, 0].legend(fontsize='small')
        
    

    plt.tight_layout()

    plt.show()





class DraftSimulator:
    def __init__(self, rewards, entry_cost, bo, nb_games, until_3_lose) -> None:
        self.rewards = rewards
        self.entry_cost = entry_cost
        self.bo = bo
        self.nb_games = nb_games
        self.until_3_lose = until_3_lose
        
    def run(self, nb_exps, winrate):
        if self.until_3_lose:
            return self.run_until_3_loses(nb_exps, winrate)
        else:
            return self.run_matches(nb_exps,  winrate)
        
    def run_matches(self, nb_exps,  winrate):
        gain_gem_tot = 0
        list_nb_wins = []
        list_gain_gems = []
        list_avg_gems = []
        
        for exp in range(1, nb_exps):
            nb_wins = 0
            
            for game in range(self.nb_games):
                if self.bo == 'bo1':
                    win = self.generate_result(winrate=winrate)
                elif self.bo == 'bo3':
                    win = self.generate_result_bo3(winrate=winrate)
                else:
                    raise('Error')
                
                nb_wins += win
                
            gain_gem = self.rewards['gems'][nb_wins]
            list_gain_gems.append(gain_gem)
            list_nb_wins.append(nb_wins)
            gain_gem_tot += gain_gem
            avg_gem = gain_gem_tot / exp
            list_avg_gems.append(avg_gem)
        
        return avg_gem
    
    def run_until_3_loses(self, nb_exps, winrate):
        gain_gem_tot = 0 
        list_nb_wins = []
        list_gain_gems = []
        list_avg_gems = []
        for exp in range(1,nb_exps):
            nb_wins = 0
            nb_loses = 0
            for game in range(1000):
                if self.bo == 'bo1':
                    win = self.generate_result(winrate=winrate)
                elif self.bo == 'bo3':
                    win = self.generate_result_bo3(winrate=winrate)
                else:
                    raise('Error')
                    
                if win == 0:
                    nb_loses = nb_loses + 1
                nb_wins = nb_wins + win
                if (nb_wins == 7) or (nb_loses == 3):
                    gain_gem = self.rewards['gems'][nb_wins]
                    break
            
            list_gain_gems.append(gain_gem)
            list_nb_wins.append(nb_wins)
            gain_gem_tot = gain_gem_tot + gain_gem
            avg_gem = gain_gem_tot/exp
            list_avg_gems.append(avg_gem)
            
        return avg_gem
            
    def generate_result_bo3(self, winrate=winrate):
        match1 = int(random.random() < winrate)
        match2 = int(random.random() < winrate)
        match3 = int(random.random() < winrate)
        if (match1 + match2 + match3) > 1.5:
            return 1
        else:
            return 0
        
    def generate_result(self, winrate=winrate):
        if random.random() < winrate:
            return 1
        else:
            return 0
        
    
    
StandardEvent = DraftSimulator(rewards=rewards_std, entry_cost=375, bo='bo1', nb_games=100, until_3_lose=True)
QuickDraft = DraftSimulator(rewards=rewards_quick, entry_cost=750, bo='bo1', nb_games=100, until_3_lose=True)
TradDraft = DraftSimulator(rewards=rewards_trad_draft, entry_cost=1500, bo='bo3', nb_games=3, until_3_lose=False)
TradEvent = DraftSimulator(rewards=rewards, entry_cost=750, bo='bo3', nb_games=5, until_3_lose=False)
PremiumDraft = DraftSimulator(rewards=rewards_prem, entry_cost=1500, bo='bo1', nb_games=100, until_3_lose=True)

# ALL
nb_exps = 15000
list_events = [TradEvent, StandardEvent, QuickDraft, TradDraft, PremiumDraft]
list_names = ['TradEvent','StandardEvent', 'QuickDraft', 'TradDraft', 'PremiumDraft']


def plot_winrate_avggaingem(nb_exps, list_events, list_names):
    

    plt.figure()
    winrates = np.linspace(0.4,0.8,2000)
    for jj,event in enumerate(list_events):
        list_ratios = []
        ff = False
        for winrate_jj in winrates:
            avg_gem = event.run(nb_exps, winrate_jj)
            ratio = avg_gem/event.entry_cost
            list_ratios.append(ratio)
            if (winrate_jj > 0.5) and ff == False:
                print(f'{list_names[jj]} : avg_gem {avg_gem}, cost : {event.entry_cost}')
                ff = True
        plt.plot(winrates,list_ratios,label=list_names[jj])
    plt.legend()
    plt.grid(alpha=0.3)
    plt.xlabel('Game Winrate')
    plt.ylabel('Ratio AvgGemGain/Cost')
    plt.tight_layout()
    plt.show()
    


plot_winrate_avggaingem(nb_exps, list_events, list_names)
