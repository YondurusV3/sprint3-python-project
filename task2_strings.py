# a)
game_name = video_game_sales[4][NAME]
print(game_name[:7])
# b)
messy_names = [' Wii Sports ', 'TETRIS', ' mario kart WII']
for name in messy_names:
    print(name.strip().lower())
# c)
print(f"#{video_game_sales[0][RANK]} Best Seller: {video_game_sales[0][NAME]} ({video_game_sales[0][YEAR]}) - ${video_game_sales[0][GLOBAL_SALES]}M global sales")
