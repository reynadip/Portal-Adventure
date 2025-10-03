# Portal Adventurer

**Portal Adventurer** is a 2D game built using **PyOpenGL** and **GLFW** for a Computer Graphics assignment (**CSL7450**). The game follows Rick, who is suddenly teleported to an unknown world and must navigate moving platforms, collect keys, and avoid enemies to find a way back home.

## 📜 Features
- **Three Levels** with unique biomes (e.g., river, jungle).
- **Moving Platforms** that require careful timing.
- **Enemies** with randomized movement.
- **Key Collection System** to unlock exit portals.
- **Teleportation between levels** via exit portals.
- **Health & Lives System** displayed via a HUD.
- **Save/Load Game Functionality** to track progress.

---

## 🔧 Installation & Setup
### Prerequisites
Make sure you have the following installed:
- Python 3.8+
- OpenGL
- GLFW
- imgui
- NumPy

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Game
```bash
python main.py
```

---

## 🎮 Controls
| Key | Action |
|-----|--------|
| W   | Move Up |
| A   | Move Left |
| S   | Move Down |
| D   | Move Right |
| SPACE | Jump |

---

## 🖥️ Heads-Up Display (HUD)
The HUD displays:
- **Player Lives** (Starts with 3 lives)
- **Health** (Decreases when touching enemies)
- **Keys Collected** (Needed to unlock portals)

---

## 📁 File Structure
```
├── assets/
│   ├── shaders/  # Shader programs
│   ├── objects/  # Game object properties
├── utils/
│   ├── window_manager.py  # GLFW window handling
│   ├── graphics.py  # Object rendering logic
├── game.py  # Main game logic
├── main.py  # Entry point
├── README.md  # Project documentation
```

---

## ❌ Game Over Conditions
- If health reaches **0**, the player loses a life.
- If all lives are lost, **Game Over**.
- Successfully reaching the final portal wins the game!

---

## 🚀 Future Enhancements
- Sound effects and background music 🎵
- More enemy types and mechanics 🕷️
- Advanced AI for enemies 🤖

### 🏆 Enjoy playing **Portal Adventurer**! 🎮

