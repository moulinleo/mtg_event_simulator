import random
import matplotlib.pyplot as plt
import numpy as np

# Rewards for each number of wins
rewards = {
    'gold':[0,0,0,0,0,0],
    'gems':[50,100,150,600,800,1000],
}

rewards_std = {
    'gold':[0,0,0,0,0,0],
    'gems':[25,50,75,200,300,400,450, 500],
}

rewards_quick = {
    'gold':[0,0,0,0,0,0],
    'gems':[50,100,200,300,450,650,850,950],
}

rewards_trad_draft = {
    'gold':[0,0,0,0,0,0],
    'gems':[100,250,1000,2500],
}

rewards_prem = {
    'gold':[0,0,0,0,0,0],
    'gems':[50,100,250,1000,1400,1600,1800,2200],
}

def generate_result(winrate):
    # Outputs 1 if the match is one, 0 if lost
    if random.random() < winrate:
        return 1
    else:
        return 0
    
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
        
    def run_matches(self, nb_exps, winrate):
        gain_gem_tot = 0
        list_nb_wins = []
        list_gain_gems = []
        list_avg_gems = []
        
        for exp in range(1, nb_exps):
            nb_wins = 0
            
            for game in range(self.nb_games):
                if self.bo == 'bo1':
                    win = self.generate_result(winrate)
                elif self.bo == 'bo3':
                    win = self.generate_result_bo3(winrate)
                else:
                    raise('Error')
                
                nb_wins += win
                
            gain_gem = self.rewards['gems'][nb_wins]
            list_gain_gems.append(gain_gem)
            list_nb_wins.append(nb_wins)
            gain_gem_tot += gain_gem
            avg_gem = gain_gem_tot / exp
            list_avg_gems.append(avg_gem)
        
        return avg_gem, list_avg_gems
    
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
                    win = self.generate_result(winrate)
                elif self.bo == 'bo3':
                    win = self.generate_result_bo3(winrate)
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
            
        return avg_gem, list_avg_gems
            
            
    def generate_result_bo3(self, winrate):
        # Result of the BO3 match. Outputs 0, 1, 2, 3 for 0, 1, 2, 3 wins respectively.
        # Outputs 1 if the match is won (2 or 3 wins), 0 otherwise
        match1 = int(random.random() < winrate)
        match2 = int(random.random() < winrate)
        match3 = int(random.random() < winrate)
        if (match1 + match2 + match3) > 1.5:
            return 1
        else:
            return 0
        
    def generate_result(self, winrate):
        # Outputs 1 if the match is one, 0 if lost
        if random.random() < winrate:
            return 1
        else:
            return 0            
            

def show_avg_gem_over_drafts(nb_exps, list_events, list_names):
    
    fig, axes = plt.subplots(nrows=3, ncols=2)
    axes = axes.ravel()
    
    for jj,event in enumerate(list_events):
        
        axes[jj].axhline(y=event.entry_cost, label='ENTRY COST', linestyle='--')

        for winrate in [0.5, 0.6, 0.7, 0.8]:
            avg_gem, list_avg_gems = event.run(nb_exps, winrate)
            axes[jj].set_ylabel('Gems gained')
            axes[jj].set_xlabel('Number of drafts')
            axes[jj].plot(list_avg_gems, label = f'winrate = {winrate}')
            axes[jj].set_title(list_names[jj])
    plt.tight_layout()

    plt.show()



def plot_winrate_avggaingem(nb_exps, list_events, list_names):

    plt.figure()
    winrates = np.linspace(0.4,0.8,2000)
    for jj,event in enumerate(list_events):
        list_ratios = []
        ff = False
        for winrate_jj in winrates:
            avg_gem, list_avg_gems = event.run(nb_exps, winrate_jj)
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
    

# CREATE HERE EVENTS
StandardEvent = DraftSimulator(rewards=rewards_std, entry_cost=375, bo='bo1', nb_games=100, until_3_lose=True)
QuickDraft = DraftSimulator(rewards=rewards_quick, entry_cost=750, bo='bo1', nb_games=100, until_3_lose=True)
TradDraft = DraftSimulator(rewards=rewards_trad_draft, entry_cost=1500, bo='bo3', nb_games=3, until_3_lose=False)
TradEvent = DraftSimulator(rewards=rewards, entry_cost=750, bo='bo3', nb_games=5, until_3_lose=False)
PremiumDraft = DraftSimulator(rewards=rewards_prem, entry_cost=1500, bo='bo1', nb_games=100, until_3_lose=True)

# Number of simulated drafts
nb_exps = 3000 

list_events = [TradEvent, StandardEvent, QuickDraft, TradDraft, PremiumDraft]
list_names = ['TradEvent','StandardEvent', 'QuickDraft', 'TradDraft', 'PremiumDraft']

## ACTUAL PLOTTING 
# Show the subplots with the average gem over the number of drafts
show_avg_gem_over_drafts(nb_exps, list_events, list_names)
# Show the AvgGemGainCost vs Winrate graph
plot_winrate_avggaingem(nb_exps, list_events, list_names)
