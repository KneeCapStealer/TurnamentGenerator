import tkinter as tk


class UIManager:
    bgColor = '#121426'
    fgColor = '#89afb3'
    activeColor = '#464d91'

    def __init__(self):
        # TkInter Window setup:
        self.__window = tk.Tk()
        self.__window.geometry('960x540+0+0')
        self.__window.config(bg=UIManager.bgColor)
        self.__init_enter_player_field()

        # input list from Entry Field
        self.__input: list[str] = []

        # StartProgram:
        self.__window.mainloop()

    def __init_enter_player_field(self):
        self.__enterPlayerText = tk.Label(self.__window, text='Enter player names here',
                                          fg=UIManager.fgColor, bg=UIManager.bgColor)
        self.__enterPlayerText.place(x=7, y=20)

        self.__enterPlayerField = tk.Entry(self.__window)
        self.__enterPlayerField.place(x=10, y=50)

        self.__enterPlayerButton = tk.Button(self.__window, text='ADD', fg=UIManager.fgColor, bg=UIManager.bgColor,
                                             activebackground=UIManager.activeColor, borderwidth=0,
                                             command=self.add_player)
        self.__enterPlayerButton.place(x=150, y=47)

    def add_player(self):
        self.__input.append(self.__enterPlayerField.get())
        self.__enterPlayerField.delete(0, tk.END)
