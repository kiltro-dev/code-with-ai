import json
import urllib.request


# ANSI color codes
YELLOW = "\033[93m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


ASCII_ART = f"""
{CYAN}{BOLD}
   _                               _         _                 _
  (_)                             (_)       | |               | |
   _  _ __   _   _  ___  ___ ___   _  _ __  | |__  _   _  ___ | |_
  | || '_ \\ | | | |/ _ \\/ __/ __| | || '_ \\ | '_ \\| | | |/ _ \\| __|
  | || | | || |_| |  __/\\__ \\__ \\ | || | | || |_) | |_| | (_) | |_
  |_||_| |_| \\__, |\\___||___/|___/ |_||_| |_||_.__/ \\__, |\\___/ \\__|
              __/ |                                   __/ |
             |___/                                   |___/
{RESET}
"""

JOKE_PROMPTS = [
    "Want another joke? (y/n): ",
    "Shall we continue? (y/n): ",
    "Another one? (y/n): ",
    "Keep going? (y/n): ",
    "More Chuck wisdom? (y/n): ",
]


def fetch_json(url, headers=None):
    request = urllib.request.Request(url, headers=headers or {"User-Agent": "Python/urllib"})
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode())


def get_categories():
    url = "https://api.chucknorris.io/jokes/categories"
    return fetch_json(url)


def get_random_joke(category=None):
    if category and category != "random":
        url = f"https://api.chucknorris.io/jokes/random?category={category}"
    else:
        url = "https://api.chucknorris.io/jokes/random"
    return fetch_json(url)["value"]


def search_jokes(term):
    url = f"https://api.chucknorris.io/jokes/search?query={term}"
    data = fetch_json(url)
    results = data.get("result", [])
    if not results:
        return None
    return results[0]["value"]


def print_joke(joke, count):
    print(f"\n{BOLD}{GREEN}[Joke #{count}]{RESET} {YELLOW}{joke}{RESET}\n")


def show_menu():
    print(f"{BOLD}Choose an option:{RESET}")
    print(f"  {CYAN}1{RESET} - Random joke")
    print(f"  {CYAN}2{RESET} - Search jokes by keyword")
    print(f"  {CYAN}3{RESET} - Pick a category")
    print(f"  {CYAN}4{RESET} - Exit")


def show_categories(categories):
    print(f"\n{BOLD}Available categories:{RESET}")
    print(f"  {CYAN}0{RESET} - random")
    for i, cat in enumerate(categories, 1):
        print(f"  {CYAN}{i}{RESET} - {cat}")


def yes_or_no(response):
    return response.lower() in ["y", "yes"]


def main():
    print(ASCII_ART)
    print(f"{BOLD}Welcome to the Chuck Norris Joke Machine!{RESET}\n")

    joke_count = 0
    prompt_index = 0

    while True:
        show_menu()
        try:
            choice = input(f"\n{GREEN}>>>{RESET} ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n\n{RED}Bye!{RESET}")
            return

        if choice == "4":
            print(f"{RED}Bye!{RESET}")
            return

        if choice == "2":
            try:
                term = input(f"{CYAN}Enter search term:{RESET} ").strip()
            except (EOFError, KeyboardInterrupt):
                print(f"\n\n{RED}Bye!{RESET}")
                return
            if term:
                joke = search_jokes(term)
                if joke:
                    joke_count += 1
                    print_joke(joke, joke_count)
                else:
                    print(f"{RED}No jokes found for '{term}'{RESET}\n")
            continue

        if choice == "3":
            categories = get_categories()
            show_categories(categories)
            try:
                pick = input(f"\n{GREEN}>>>{RESET} ").strip()
            except (EOFError, KeyboardInterrupt):
                print(f"\n\n{RED}Bye!{RESET}")
                return
            if pick == "0":
                category = None
            elif pick.isdigit() and 1 <= int(pick) <= len(categories):
                category = categories[int(pick) - 1]
            else:
                print(f"{RED}Invalid selection, using random{RESET}\n")
                category = None
            joke = get_random_joke(category)
            joke_count += 1
            print_joke(joke, joke_count)
            continue

        if choice == "1" or not choice:
            joke = get_random_joke()
            joke_count += 1
            print_joke(joke, joke_count)
        else:
            print(f"{RED}Invalid option{RESET}\n")
            continue

        # Ask if they want another
        prompt = JOKE_PROMPTS[prompt_index % len(JOKE_PROMPTS)]
        prompt_index += 1
        try:
            response = input(f"{prompt}").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{RED}Bye!{RESET}")
            return

        if not yes_or_no(response):
            print(f"{RED}Bye!{RESET}")
            return


if __name__ == "__main__":
    main()
