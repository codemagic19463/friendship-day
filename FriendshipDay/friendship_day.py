#!/usr/bin/env python3
# friendship_day.py
# A fun, interactive Friendship Day script with mini-games and tasks!

import random
import time
import sys

def print_with_delay(text, delay=0.02):
    """Prints text one character at a time for dramatic effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    art = r"""
  ______ _    _ _____  _      _____  _____  _____  _____ _    _ _____  
 |  ____| |  | |_   _|/ \    |_   _|/ ____|/ ____|/ ____| |  | |  __ \ 
 | |__  | |  | | | | / _ \     | | | (___ | |    | (___ | |__| | |__) |
 |  __| | |  | | | |/ ___ \    | |  \___ \| |     \___ \|  __  |  _  / 
 | |    | |__| |_| /_/   \_\  _| |_ ____) | |____ ____) | |  | | | \ \ 
 |_|     \____/|____/     \__\_____|_____/ \_____|_____/|_|  |_|_|  \_\                                                                                                        
    """
    print(art)
    print_with_delay("Happy Friendship Day to My POTTI PSYCHO! 🥳\n", 0.005)

def pause():
    input("\nPress Enter to continue...")

def emoji_puzzle():
    puzzles = [
        {"emoji": "⚽️🍟", "hint": "Sports + snack", "answer": "football fries"},
        {"emoji": "🐝📱", "hint": "Insect + device", "answer": "bee phone"},
        {"emoji": "📚🍫", "hint": "Study-time treat", "answer": "book chocolate"}
    ]
    p = random.choice(puzzles)
    print(f"🔎 Emoji Puzzle: {p['emoji']}  (Hint: {p['hint']})")
    ans = input("Your guess: ").strip().lower()
    if ans == p["answer"].lower():
        print("🎉 Correct! You're on fire!")
    else:
        print(f"❌ Nope, it was '{p['answer']}'.")

def word_scramble():
    words = ["FRIENDSHIP", "LAUGHTER", "MEMORIES", "ADVENTURE"]
    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))
    print(f"🔤 Unscramble this word: {scrambled}")
    ans = input("Your answer: ").strip().upper()
    if ans == word:
        print("👏 You got it!")
    else:
        print(f"❌ The word was '{word}'.")

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    print("🎮 Rock-Paper-Scissors — best of 3!")
    score = {"you": 0, "bot": 0}
    rounds = 1
    while max(score.values()) < 2 and rounds <= 3:
        you = input("Your move [rock/paper/scissors]: ").lower()
        bot = random.choice(choices)
        print(f"🤖 Bot plays: {bot}")
        if you == bot:
            print("Tie!")
        elif (you == "rock" and bot == "scissors") or \
             (you == "paper" and bot == "rock") or \
             (you == "scissors" and bot == "paper"):
            print("You win this round!")
            score["you"] += 1
        else:
            print("Bot wins this round!")
            score["bot"] += 1
        rounds += 1
    winner = "You" if score["you"] > score["bot"] else "Bot"
    print(f"🏆 Final Score — You: {score['you']}  Bot: {score['bot']}")
    print(f"🎊 {winner} won the match!")

def friendship_quiz():
    quiz = [
        {"q": "What's the funny name i kept you?", "a": "psycho"},
    ]
    random.shuffle(quiz)
    correct = 0
    for item in quiz:
        ans = input(f"❓ {item['q']} ").strip().lower()
        if ans == item["a"]:
            print("✅ Right!")
            correct += 1
        else:
            print(f"❌ I wish you said '{item['a'].title()}'.")
    print(f"💯 You got {correct}/{len(quiz)} correct!")

def silly_dare():
    dares = [
        "prank your best friend not me and send the proofs!",
        "Tell me your most embarrassing high-school nickname.",
        "Act like a chicken for 10 seconds infront of your parents and share me wt they did.",
        "Send me your worst selfie!"
    ]
    dare = random.choice(dares)
    print(f"🎲 Silly Dare: {dare}")

def play_all_games():
    games = [
        ("Emoji Puzzle", emoji_puzzle),
        ("Word Scramble", word_scramble),
        ("Rock-Paper-Scissors", rock_paper_scissors),
        ("Friendship Quiz", friendship_quiz),
        ("Silly Dare", silly_dare)
    ]
    random.shuffle(games)
    for name, func in games:
        print("\n" + "-" * 40)
        print_with_delay(f"Starting: {name}")
        func()
        pause()

def final_message():
    print("\n" + "=" * 40)
    print_with_delay("Thanks for playing! You’re the bestest bestie ever! ❤️", 0.01)
    print_with_delay("May our friendship stay as awesome as today. Happy Friendship Day! 🎉", 0.01)
def celebrate_friendship():
    print("\n" + "=" * 40)
    print_with_delay("💌 Friendship Day Message (Spicy Remix):", 0.01)
    message = """\
OYEE POTTI!
Happy Friendship Day ra! I just want to say—you’re not just my bestie, you’re my full-on emotional support system, comedy partner, and secret keeper.
Nuvvu naa life lo unnav ante, I feel like I won the jackpot! 😎
Your laughter is like instant mood boost, and your kindness? Next level.
I still remember our late-night chats, those random memes, and the way we vibe even without talking.
Thanks for being my rock, my ride-or-die, and the only person who understands my madness without judgment.
Today is all about celebrating *us*—our bond, our bakara, and your occasional ROBO mode 😂
Let’s keep making crazy memories, sharing deep talks, and laughing till our stomachs hurt.
Love you loads, bestie! 💖
"""
    print_with_delay(message, 0.005)
def main():
    banner()
    pause()
    play_all_games()
    final_message()
    celebrate_friendship()  # 🎉 Add this line to show your message

if __name__ == "__main__":
    main()