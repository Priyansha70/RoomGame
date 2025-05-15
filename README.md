# 🏰 Room Game

A modular, text-based adventure game where players explore a castle filled with rooms, portals, wormholes, and collectible diamonds.

This project is fully optimized for readability and maintainability, showcasing object-oriented design in Python. Ideal for demonstrating fundamental programming concepts, file-based configuration, and interactive user input.

---

## 🚀 Features

- 🔁 Turn-based multiplayer support
- 💎 Diamond collection and score tracking
- 🌀 Wormholes that teleport players randomly
- 🌀 Portals that return players to the entrance
- 🗺️ Castle loaded dynamically from a text file (`castle.txt`)
- 🧱 Modular architecture (Room, Player, Game, Castle, Diamond)

---

## 🧪 How to Run

Make sure you have **Python 3.7+** installed.

```bash
# Clone the repository
git clone https://github.com/Priyansha70/RoomGame.git
cd RoomGame

# Make sure you have a castle.txt file in the folder
# Run the game
python main.py
```

You will be prompted to input directions (e.g., `North`, `South`, `East`, `West`) as players explore the castle.

---

## 📁 Folder Structure

```
RoomGame/
├── main.py          # Game entry point
├── game.py          # Game engine logic
├── player.py        # Player class with inventory and position
├── room.py          # Room structure including portals and wormholes
├── castle.py        # Castle blueprint and room management
├── diamond.py       # Diamond tracking and scoring
└── castle.txt       # Input file defining the castle layout (you create this)
```

---

## 📚 Example Input (castle.txt)

```
RoomID, North, South, East, West, Object
...
```

This file should define rooms and their connections. Each line maps a room and any object (e.g., `D`, `W`, `P`) or special connection.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or enhance.

---

## 📜 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 👤 Author

**Priyansha Aggarwal**  
GitHub: [@Priyansha70](https://github.com/Priyansha70)  
LinkedIn: [linkedin.com/in/priyansha-aggarwal-520251352](https://linkedin.com/in/priyansha-aggarwal-520251352)
