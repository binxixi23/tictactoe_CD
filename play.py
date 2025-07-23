def play_game(agent):
    env = TicTacToe()
    state = env.reset()
    done = False

    print("Initial Board:")
    print_board(env.board)

    while not done:
        # Agent's turn (X)
        available_actions = env.available_actions()
        if not available_actions:
            break

        action = agent.get_action(state, available_actions)
        state, reward, done = env.step(action, player=1)
        print(f"Agent plays X at {action}:")
        print_board(env.board)

        if done:
            break

        # Human/Opponent's turn (O)
        print("Your turn (O). Enter row (0-2) and column (0-2):")
        try:
            row, col = map(int, input().split())
            if (row, col) not in env.available_actions():
                print("Invalid move! Try again.")
                continue
        except:
            print("Invalid input! Try again.")
            continue

        state, reward, done = env.step((row, col), player=2)
        print("Board after your move:")
        print_board(env.board)

    if env.winner == 1:
        print("Agent (X) wins!")
    elif env.winner == 2:
        print("You (O) win!")
    else:
        print("It's a draw!")
    

    

def print_board(board):
    symbols = {0: '.', 1: 'X', 2: 'O'}
    for row in board:
        print(' '.join(symbols[cell] for cell in row))
    print()

    with open('q_table.pkl', 'rb') as f:
     q_table = pickle.load(f)
     print("Loaded Q-table size:", len(q_table))

    if __name__ == "__main__":
     print("Training agent...")
     agent = train_agent(num_episodes=10000)
    
    
     print("Training complete! Let's play a game.")
     play_game(agent)
