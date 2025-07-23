def test_agent(agent_x, num_games=5):
    env = TicTacToe()
    results = {'X_wins': 0, 'O_wins': 0, 'Draws': 0}
    
    for game in range(num_games):
        print(f"\nGame {game + 1}")
        state = env.reset()
        env.print_board()
        
        while True:
            if env.current_player == 1:  # Agent's turn (X)
                available_moves = env.available_moves()
                action = agent_x.choose_action(state, available_moves)
                env.make_move(action)
                print(f"Agent (X) moves to {action}")
                env.print_board()
            else:  # Human's turn (O)
                print("Your turn (O). Enter move as 'row col' (e.g., '0 0' for top-left):")
                while True:
                    try:
                        row, col = map(int, input().split())
                        move = (row, col)
                        if move in env.available_moves():
                            env.make_move(move)
                            print(f"Human (O) moves to {move}")
                            env.print_board()
                            break
                        else:
                            print("Invalid move. Try again.")
                    except (ValueError, IndexError):
                        print("Invalid input. Use format 'row col' (e.g., '0 0').")
            
            state = env.get_state()
            winner = env.check_winner()
            if winner is not None:
                if winner == 1:
                    print("Agent (X) wins!")
                    results['X_wins'] += 1
                elif winner == -1:
                    print("Human (O) wins!")
                    results['O_wins'] += 1
                else:
                    print("It's a draw!")
                    results['Draws'] += 1
                break
    time.sleep(0.5)
    
    print("\nTest Results:")
    print(f"Agent (X) wins: {results['X_wins']}")
    print(f"Human (O) wins: {results['O_wins']}")
    print(f"Draws: {results['Draws']}")
    return results

if __name__ == "__main__":
    print("Training agents...")
    agent, rewards = train_agent(episodes=10000)
    print("Training complete. Starting test against human...")
    test_agent(agent, num_games=5)
