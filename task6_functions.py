#a
def calculate_total_sales(game):

    return game[3] + game[4] + game[5]

data = [
    ["Wii Sports", "Sports", 2006, 41.49, 29.02, 3.77],
    ["Super Mario Bros.", "Platform", 1985, 29.08, 3.58, 6.81],
]

print(calculate_total_sales(data[0]))
#b
def filter_by_genre(data, genre="Platform"):
    return [game for game in data if game[1] == genre]

print(filter_by_genre(data))

print(filter_by_genre(data, "Sports"))
#c
def get_summary(game):
    name = game[0]
    genre = game[1]
    year = game[2]
    total_sales = calculate_total_sales(game)
    return f"{name} ({year}) - {genre} - ${total_sales:.2f}M"
