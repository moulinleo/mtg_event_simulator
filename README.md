# Draft Simulator

This code simulates different draft scenarios in a game and calculates the average gem gain based on the win rate. It can simulate various draft modes, including BO1 (Best of 1) and BO3 (Best of 3), and provides insights into the gem rewards for different numbers of wins.

## Requirements

To run this code, you need the following dependencies:

- Python 3.x
- matplotlib
- numpy

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:
3. Run the `draft_simulator.py` file
4. The script will generate plots showing the average gem gain over the number of drafts and the AvgGemGainCost vs Winrate for different draft scenarios.

## Configuration

You can customize the draft scenarios by modifying the following variables in the code:

- `rewards`: Defines the gem rewards for each number of wins in different draft modes.
- `rewards_std`: Rewards for Standard draft mode.
- `rewards_quick`: Rewards for Quick draft mode.
- `rewards_trad_draft`: Rewards for Traditional Draft mode.
- `rewards_prem`: Rewards for Premium draft mode.
- `nb_exps`: Number of simulated drafts.
- `list_events`: List of draft events to simulate.
- `list_names`: Names of the draft events.

## Results

The script generates visualizations that provide insights into the average gem gain and the gem gain-to-cost ratio for different win rates and draft modes. These visualizations can help players make informed decisions about participating in different draft scenarios.
