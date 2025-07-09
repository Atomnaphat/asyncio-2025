import time
from datetime import timedelta


def game():
    """
    Simulates a synchronous chess exhibition with Judit and multiple opponents.
    Calculates and prints time spent for each move, game, and the entire exhibition.
    """

    # --- Configuration Parameters ---
    # Simulation speed factor (1 for real time, lower for faster simulation)
    # For example, speed = 0.1 means the simulation runs 10 times slower.
    # speed = 10 means the simulation runs 10 times faster.
    speed = 100
    judit_move_time_secs = 5  # Time Judit takes for a move in seconds
    opponent_move_time_secs = 55  # Time Opponent takes for a move in seconds
    num_opponents = 24  # Total number of opponents Judit plays against (SET TO 1 FOR THIS EXAMPLE)
    num_move_pairs_per_game = 30  # Number of move pairs (Judit + Opponent) per game

    print("Results 1 board")
    print(f"Number of games: {num_opponents}game.")
    print(f"Number of move: {num_move_pairs_per_game} pairs.")

    # Initialize overall exhibition timers
    total_exhibition_start_time = time.perf_counter() # Real time counter for the entire exhibition
    total_exhibition_calculated_time = timedelta(seconds=0) # Calculated time for the entire exhibition

    # --- Simulate Each Game ---
    for game_number in range(1, num_opponents + 1):
        game_start_time = time.perf_counter() # Real time counter for the current game
        game_calculated_time = timedelta(seconds=0) # Calculated time for the current game

        # --- Simulate Moves within Each Game ---
        for move_pair_number in range(1, num_move_pairs_per_game + 1):
            # Judit's move
            print(f"BOARD-{game_number} {move_pair_number} Judit made a move with {judit_move_time_secs} secs.")
            time.sleep(judit_move_time_secs / speed) # Pause to simulate time passing
            game_calculated_time += timedelta(seconds=judit_move_time_secs) # Add to calculated game time

            # Opponent's move
            print(f"BOARD-{game_number} {move_pair_number} Opponent made move with {opponent_move_time_secs} secs.")
            time.sleep(opponent_move_time_secs / speed) # Pause to simulate time passing
            game_calculated_time += timedelta(seconds=opponent_move_time_secs) # Add to calculated game time

        # --- Game Summary ---
        game_end_time = time.perf_counter() # End real time counter for the current game
        real_game_duration = game_end_time - game_start_time # Calculate real duration of the game

        print(f"BOARD-{game_number} ->>>>>>>>>>>>>>> Finished move in {real_game_duration:.1f} secs")
        print(f"BOARD-{game_number} ->>>>>>>>>>>>>>> Finished move in {game_calculated_time.total_seconds():.1f} secs (calculated)")

        # Add current game's calculated time to the total exhibition calculated time
        total_exhibition_calculated_time += game_calculated_time

    # --- Exhibition Summary ---
    total_exhibition_end_time = time.perf_counter() # End real time counter for the entire exhibition
    real_exhibition_duration = total_exhibition_end_time - total_exhibition_start_time # Calculate real duration of the exhibition

    # Convert total real duration to timedelta object for easy formatting
    real_exhibition_td = timedelta(seconds=real_exhibition_duration)
    # The calculated exhibition time is already a timedelta object

    # Print final exhibition summary, formatting timedelta to HH:MM:SS
    # .split('.')[0] is used to remove milliseconds from the string representation
    print(f"\nBoard exhibition finished for {num_opponents} opponents in {str(real_exhibition_td).split('.')[0]} hr.")
    print(f"Board exhibition finished for {num_opponents} opponents in {str(total_exhibition_calculated_time).split('.')[0]} hr. (calculated)")

# --- Run the simulation ---
# This ensures that game() is called only when the script is executed directly
if __name__ == "__main__":
    game()
