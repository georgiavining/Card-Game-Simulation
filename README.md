# Card Game Simulation

A card game built with Python and Pygame, featuring a full game engine, AI opponents, and an interactive UI.

---

## Folder Structure

```
Card-Game-Simulation/
├── main.py              # Entry point — run this to start the game
├── core/                # Core game logic
│   ├── card.py
│   ├── deck.py
│   ├── hand.py
│   ├── player.py
│   ├── rules.py
│   ├── turn_manager.py
│   └── state.py
├── ui/                  # Pygame UI components
│   ├── screen.py
│   ├── main_screen.py
│   ├── game_over_screen.py
│   ├── layout.py
│   └── visual_objects.py
├── ai/                  # AI opponent logic
└── assets/              # Images for cards, deck, background
```

---

## How to Run

1. **Clone the repo**
```bash
git clone https://github.com/georgiavining/Card-Game-Simulation.git
```

2. **Navigate to the project folder**
```bash
cd Card-Game-Simulation
```

3. **Install dependencies**
```bash
python -m pip install pygame
```

4. **Run the game**
```bash
python main.py
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `pygame` | Game window, rendering, input handling |
| `python 3.x` | Language runtime |
