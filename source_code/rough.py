import curses
import datetime
import time


def display_time(stdscr, row, col):
    # Get current time
    current_time = datetime.datetime.now()

    # Format current time
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Clear the specific line
    stdscr.move(row, col)
    stdscr.clrtoeol()

    # Print the current time at the specified position
    stdscr.addstr(row, col, time_str)

    # Refresh the screen to display the changes
    stdscr.refresh()


def main(stdscr):
    # Don't show cursor
    curses.curs_set(0)

    # Update the time every second
    while True:
        # Display time on specific line
        display_time(stdscr, 5, 0)

        # Wait for 1 second before updating the time
        time.sleep(1)


# Run the main function
curses.wrapper(main)
