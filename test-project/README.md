# Chuck Norris Joke Script

A Python CLI script that fetches random Chuck Norris jokes from api.chucknorris.io using only built-in modules (`urllib`, `json`).

## Features

- **Menu-driven interface** with 4 options: random joke, search, category picker, exit
- **Category support** - fetches available categories from API, lets user pick one
- **Search functionality** - search jokes by keyword
- **Colored output** - ANSI colors (yellow for jokes, cyan/green for UI elements)
- **ASCII art header** on startup
- **Joke counter** - tracks how many jokes shown this session
- **Varied prompts** - rotates through 5 different "want another?" messages
- **Shorter yes/no** - accepts "y", "yes", "n", "no"
- **Error handling** - handles EOFError and KeyboardInterrupt gracefully

## Dependencies

- Only Python standard library (no 3rd party packages)

## Usage

```bash
python chuck_norris_joke.py
```

## Menu Options

1. **Random joke** - Get a random Chuck Norris joke
2. **Search jokes** - Search for jokes by keyword
3. **Pick a category** - Choose from available categories (animal, career, celebrity, etc.)
4. **Exit** - Quit the program

## Key Functions

- `fetch_json(url)` - generic JSON fetcher with User-Agent header
- `get_categories()` - fetches available joke categories
- `get_random_joke(category=None)` - fetches random joke, optionally filtered by category
- `search_jokes(term)` - searches jokes by keyword
- `print_joke(joke, count)` - prints joke with color and counter
- `main()` - main loop with menu and interaction flow
