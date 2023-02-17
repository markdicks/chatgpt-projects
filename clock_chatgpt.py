import tkinter as tk
from datetime import datetime

class DigitalClock(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._time_str = tk.StringVar()
        self._time_str.set(datetime.now().strftime('%H:%M:%S'))

        # create label to display the time
        self._time_label = tk.Label(self, textvariable=self._time_str, font=('Courier', 50), fg='white', bg='black')
        self._time_label.pack(fill='x', padx=20, pady=20)

        # add features to the clock
        self._show_seconds = True
        self._show_milliseconds = False
        self._toggle_seconds_button = tk.Button(self, text='Hide Seconds', command=self.toggle_seconds)
        self._toggle_milliseconds_button = tk.Button(self, text='Show Milliseconds', command=self.toggle_milliseconds)
        self._toggle_seconds_button.pack(side='left', padx=20, pady=10)
        self._toggle_milliseconds_button.pack(side='left', padx=20, pady=10)

        # start the clock
        self.update_time()

    def toggle_seconds(self):
        self._show_seconds = not self._show_seconds
        if self._show_seconds:
            self._toggle_seconds_button.config(text='Hide Seconds')
        else:
            self._toggle_seconds_button.config(text='Show Seconds')
        self.update_time()

    def toggle_milliseconds(self):
        self._show_milliseconds = not self._show_milliseconds
        if self._show_milliseconds:
            self._toggle_milliseconds_button.config(text='Hide Milliseconds')
        else:
            self._toggle_milliseconds_button.config(text='Show Milliseconds')
        self.update_time()

    def update_time(self):
        now = datetime.now()
        time_str = now.strftime('%H:%M')
        if self._show_seconds:
            time_str += now.strftime(':%S')
        if self._show_milliseconds:
            time_str += now.strftime('.%f')[:4]
        self._time_str.set(time_str)
        self.after(100, self.update_time)

if __name__ == '__main__':
    root = tk.Tk()
    root.configure(bg='black')
    root.title('Digital Clock')
    DigitalClock(root).pack(fill='both', expand=True)
    root.mainloop()
