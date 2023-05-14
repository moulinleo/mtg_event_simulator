# Draft Simulator

This code simulates different drafting scenarios in a card game and compares the average number of gems gained per draft. The simulations are based on a given win rate and rewards structure.

## Prerequisites

- Python 3.x
- Matplotlib

## Usage

1. Run the script using the following command:

``python draft_simulator.py``

## Description

The code consists of several functions and classes:

- `generate_result(winrate)`: This function generates a win or loss result based on the given win rate.

- `run(nb_exps, winrate, rewards)`: This function simulates drafting scenarios and returns lists of gained gems, number of wins, average gems, and average gems per entry cost.

- `run_std_event(nb_exps, winrate, rewards)`: This function simulates standard event drafting scenarios, where players continue until they lose three times or win seven times.

- `run_trad_draft(nb_exps, winrate, rewards)`: This function simulates traditional draft scenarios, where players play three games and gain gems based on the number of wins.

- `run_quick_draft(nb_exps, winrate, rewards)`: This function simulates quick draft scenarios, where players continue until they lose three times or win seven times.

- `run_prem_draft(nb_exps, winrate, rewards)`: This function simulates premier draft scenarios, where players continue until they lose three times or win seven times.

- `DraftSimulator(rewards, entry_cost, bo, nb_games, until_3_lose)`: This class represents a drafting simulator with customizable rewards, entry cost, best-of format, number of games, and stopping condition.

- `plot_winrate_avggaingem(nb_exps, list_events, list_names)`: This function plots the average gems gained per entry cost for different win rates.

## Results

The script generates plots showing the average gems gained per entry cost for different drafting scenarios and win rates. It compares the results for standard event, quick draft, traditional draft, and premium draft.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

