from game import Game

NUM_PLAYERS = 2

def main():
    game = Game(NUM_PLAYERS)
    game.initialize_from_file("castle.txt")

    turn = 0
    game.set_turn(turn)

    while not game.is_finished():
        if not game.finished[turn]:
            game.move()
        turn = (turn + 1) % NUM_PLAYERS
        game.set_turn(turn)

    print("\nGame Finished successfully, all players exited\n")

    for idx, player in enumerate(game.players, start=1):
        print(f"Path Travelled by Player {idx}:")
        player.print_path()
        print()
        print(f"Number of diamonds collected by Player {idx}: {player.get_diamonds()}\n")

if __name__ == "__main__":
    main()
