from pynput import keyboard

class GlobalShortcuts:

    def __init__(self, on_text_input, on_voice_toggle=None):

        self.on_text_input = on_text_input
        self.on_voice_toggle = on_voice_toggle

        self.listener = None

    def start(self):

        if self.listener is not None:
            return

        if self.on_voice_toggle is not None:
            self.listener = keyboard.GlobalHotKeys({
                '<ctrl>+<alt>+b': self.on_text_input,
                '<ctrl>+<alt>+f': self.on_voice_toggle
            })
        else:
            self.listener = keyboard.GlobalHotKeys({
                '<ctrl>+<alt>+b': self.on_text_input
            })

        self.listener.start()

    def stop(self):

        if self.listener is not None:
            self.listener.stop()
            self.listener = None

        