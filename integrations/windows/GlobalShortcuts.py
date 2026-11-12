from pynput import keyboard


class GlobalShortcuts:

    def __init__(
        self,
        on_text_input,
        on_voice_press=None,
        on_voice_release=None
    ):

        self.on_text_input = on_text_input
        self.on_voice_press = on_voice_press
        self.on_voice_release = on_voice_release

        self.listener = None

        self.ctrl_pressed = False
        self.alt_pressed = False
        self.b_pressed = False
        self.f_pressed = False

        self.voice_active = False

    def start(self):

        if self.listener is not None:
            return

        self.listener = keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release
        )

        self.listener.start()

    def stop(self):

        if self.listener is not None:
            self.listener.stop()
            self.listener.join()
            self.listener = None

    def _on_press(self, key):

        if key in (
            keyboard.Key.ctrl,
            keyboard.Key.ctrl_l,
            keyboard.Key.ctrl_r
        ):
            self.ctrl_pressed = True

        elif key in (
            keyboard.Key.alt,
            keyboard.Key.alt_l,
            keyboard.Key.alt_r
        ):
            self.alt_pressed = True

        elif self._is_char(key, 'b'):

            if not self.b_pressed:
                self.b_pressed = True

                if self.ctrl_pressed and self.alt_pressed:
                    if self.on_text_input is not None:
                        self.on_text_input()

        elif self._is_char(key, 'f'):
            self.f_pressed = True

        if (
            self.ctrl_pressed
            and self.alt_pressed
            and self.f_pressed
            and not self.voice_active
        ):

            self.voice_active = True

            if self.on_voice_press is not None:
                self.on_voice_press()

    def _on_release(self, key):

        if self._is_char(key, 'f'):
            self.f_pressed = False
            self._stop_voice()

        elif key in (
            keyboard.Key.ctrl,
            keyboard.Key.ctrl_l,
            keyboard.Key.ctrl_r
        ):
            self.ctrl_pressed = False
            self._stop_voice()

        elif key in (
            keyboard.Key.alt,
            keyboard.Key.alt_l,
            keyboard.Key.alt_r
        ):
            self.alt_pressed = False
            self._stop_voice()

        elif self._is_char(key, 'b'):
            self.b_pressed = False

    def _stop_voice(self):

        if self.voice_active:
            self.voice_active = False

            if self.on_voice_release is not None:
                self.on_voice_release()

    def _is_char(self, key, char):

        virtual_keys = {
            'b': 66,
            'f': 70
        }

        return getattr(key, 'vk', None) == virtual_keys[char.lower()]