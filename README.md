# Card Game Simulation

A card game built with Python and Pygame, featuring a full game engine, AI opponents, and an interactive UI.

---

## Folder Structure

```
ard-Game-Simulation/
├── main.py              # Entry point — run this to start the game
├── core/                # Core game logic
│   ├── card.py
│   ├── deck.py
│   ├── game.py
│   ├── groups.py
│   ├── player.py
│   └── turn.py
├── ui/                  # Pygame UI components
│   ├── buttons.py
│   ├── events.py
│   ├── menu.py
│   ├── renderer.py
│   └── screen.py
├── ai/                  # AI opponent strategies
│   ├── strat1.py
│   └── strat2.py
└──

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
