import tkinter as tk
import random

class WindowSpammer:
    def __init__(self, root):
        self.root = root
        self.root.title("Master Control")
        self.root.geometry("350x150+100+100")
        
        # Track active windows and enforce the new limit
        self.spawned_windows = []
        self.max_windows = 25 
        
        # Main Window UI
        label = tk.Label(root, text="Multi-Window Simulator\n(Safety limit: 25 windows)", font=("Arial", 11))
        label.pack(pady=10)
        
        self.spawn_btn = tk.Button(root, text="Release the Chaos", command=self.spawn_loop, bg="lightcoral")
        self.spawn_btn.pack(pady=5)
        
        close_btn = tk.Button(root, text="Close All Safely", command=self.close_everything)
        close_btn.pack(pady=5)
        
        # Safe Exit: Closing the master window kills everything instantly
        self.root.protocol("WM_DELETE_WINDOW", self.close_everything)

    def spawn_loop(self):
        # Keep spawning as long as we are under the 25-window ceiling
        if len(self.spawned_windows) < self.max_windows:
            self.create_sub_window()
            # Spawns the next window every 200 milliseconds for a faster effect
            self.root.after(200, self.spawn_loop)

    def create_sub_window(self):
        sub_win = tk.Toplevel(self.root)
        sub_win.title("⚠️ Pop-up!")
        
        # Randomize screen placement
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = random.randint(50, screen_width - 300)
        y = random.randint(50, screen_height - 200)
        sub_win.geometry(f"250x100+{x}+{y}")
        
        lbl = tk.Label(sub_win, text="Harmless chaotic window.", font=("Arial", 10))
        lbl.pack(pady=20)
        
        self.spawned_windows.append(sub_win)
        
        # If a single window is closed, free up the slot so the loop can run again
        sub_win.protocol("WM_DELETE_WINDOW", lambda: self.remove_window(sub_win))

    def remove_window(self, win):
        if win in self.spawned_windows:
            self.spawned_windows.remove(win)
        win.destroy()

    def close_everything(self):
        # Erases the main root process, instantly wiping all children from memory
        self.root.quit()

if __name__ == "__main__":
    window = tk.Tk()
    app = WindowSpammer(window)
    window.mainloop()