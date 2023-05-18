import itertools
import pandas as pd
import numpy as np

num_cells = 12
last_cell_num = 12
nums_dice = [3, 6, 12]

answer = pd.DataFrame(
    np.zeros((12, 3)),
    index=[f'Cell 0{i}' for i in range(1, 13)],
    columns=[f'{j} Cubes' for j in nums_dice]
)

def throw_dice(n):
    return itertools.product(range(1, 7), repeat=n)

def last_cell(dice_roll, start_cell):
    end_cell = start_cell
    for roll in dice_roll:
        end_cell += roll
        if end_cell > last_cell_num:
            end_cell -= last_cell_num
    return end_cell

for i, num_dice in enumerate(nums_dice):
  cell_counts = [0] * num_cells

  for dice_roll in throw_dice(num_dice):
      end_cell = last_cell(dice_roll, last_cell_num)
      cell_counts[end_cell-1] += 1

  total_combinations = 6 ** num_dice
  cell_probabilities = [count / total_combinations for count in cell_counts]

  answer[answer.columns[i]] = cell_probabilities

answer.to_csv('answer.csv')
