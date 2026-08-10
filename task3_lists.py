# a) Create a list containing only the game names
game_names = []
for game in video_game_sales:
    game_names.append(game[NAME])
print(game_names)
# b) Add a new game to the dataset
video_game_sales.append(
[21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18]
)
print(len(video_game_sales))
# c) Create a tuple with dataset metadata
# A tuple is appropriate because dataset metadata should not change after it is created.
dataset_info = (len(video_game_sales), 10, 'Video Game Sales')
print(dataset_info)
