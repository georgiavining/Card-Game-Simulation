# PyGame_Project

## How to Run

1. **Clone the repo**  
```bash
git clone <repo_url>
```

2. **Navigate to the project folder**  
```bash
cd Pygame_Project
```

3. **Install depedencies**  
```bash
python -m pip install pygame
```

4. **Run the game**  
```bash
python main.py
```

## Team Workflow

To keep the project organized, everyone should work on their own branch and only merge into `main` via pull requests 

### 1. Make sure your local `main` is up-to-date
```bash
git checkout main
git pull origin main
```

### 2. Create a new branch for your feature
Use a descriptive branch name instead of the placeholder `feature-name`:
```bash
git checkout -b <feature-name>
```

### 3. Work on your branch
- Make changes locally
- Commit changes
- Push the branch to GitHub
```bash
git add .
git commit -m " ..."
git push -u origin <feature-name>
```

### 4. Create a pull request
- Go to GitHub and open a PR from your branch → main.
- Add a short description of your changes
- Wait for review/approval before merging

### 5. Merge PR into 'main'
- Merge PR
- Pull updated main branch locally
```bash
git checkout main
git pull origin main
```


## Folder Structure

```
PyGame Project/
├─ main.py              # Entry point to run the game
├─ config.py              # Constants
├─ game/                  # Core game logic
│  ├─ card.py
│  ├─ deck.py
│  ├─ hand.py
│  ├─ player.py
│  ├─ rules.py
│  ├─ turn_manager.py
│  └─ state.py
├─ ui/                    # Pygame UI components
│  ├─ screen.py
│  ├─ main_screen.py
|  ├─ game_over_screen.py
│  ├─ layout.py             # Layout function for player's hands
│  └─ visual_objects.py
├─ asets/          # Images for cards, deck, background
└─ README.md
```