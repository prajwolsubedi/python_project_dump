import curses
from _curses import KEY_BACKSPACE
from curses import wrapper

def start_game(stdscr):
    stdscr.addstr("Welcome to the Typing Test!")
    stdscr.addstr("Press any key to continue: ")
    user_input = stdscr.getkey()
    stdscr.clear()
    current_text = []
    target_text = "THIS IS THE TEST TYPING FOR WPM GAME."
    stdscr.addstr(0,0,target_text, curses.color_pair(3))
    stdscr.refresh()
    for i in range(len(target_text)):
        index = [0,0]
        current_letter = stdscr.getkey()
        current_text.append(current_letter)
        print("target -----",current_text)
        print("target[:i]-----",*current_text[:i+1])
        string = "".join(current_text[:i+1])
        if current_letter == target_text[i]:
            stdscr.addstr(index[0], index[1], string, curses.color_pair(1))
            index[1] = index[1] + 1
        elif current_letter == "KEY_BACKSPACE":
            stdscr.addstr(index[0], index[1], string, curses.color_pair(3))
            index[1] = index[1] - 1
        else:
            stdscr.addstr(index[0], index[1], string, curses.color_pair(2))
            index[1] = index[1] + 1



def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_game(stdscr)
    stdscr.getkey()

wrapper(main)