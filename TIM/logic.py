from dataclasses import dataclass
import time


# Realistically i should have made a Light class that had all the shared functions
# and then have the light bar inherit from it but this seems more readable
@dataclass
class FullBeam:
    light: bool = False

    def switch_on(self):
        self.light = True
        print("\033[Full Beam switched ON")
        print(self)

    def switch_off(self):
        print("Full beam switched OFF")
        self.light = False
        print(self)


# I'm using this @dataclass decorator to autocomplete some of the boring class creation stuff.
# You can ignore it for now knowing that it writes a few basic default functions for 
# creating and displaying the class.
@dataclass
class LightBar:
    light: bool = False

    def switch_on(self):
        print("Light Bar switched ON")
        self.light = True
        print(self)

    def switch_off(self):
        print("Light Bar switched OFF")
        self.light = False
        print(self)

    def flash(self):
        print("Light Bar FLASH")
        self.light = True
        print(self)
        time.sleep(1)
        self.light = False
        print(self)


# This class is probably overkill but you get the idea hopefully of some OOP stuff with this
class LightController:
    full_beams: FullBeam
    light_bar: LightBar

    def __init__(self) -> None:
        self.full_beams = FullBeam()
        self.light_bar = LightBar()

    def __str__(self) -> str:
        beam_status = "ON" if self.full_beams.light else "OFF"
        bar_status = "ON" if self.light_bar.light else "OFF"
        return f"CAR LIGHT STATUS: Full beams are {beam_status}! - Light bar is {bar_status}!"

    def light_bar_button_pressed(self):
        if self.full_beams.light:
            self.light_bar.switch_on()
        else:
            self.light_bar.flash()

    def full_beam_toggled(self):
        if self.full_beams.light:
            self.light_bar.switch_off()
            self.full_beams.switch_off()
        else:
            self.full_beams.switch_on()


def main():
    tims_car_lights = LightController()
    print(tims_car_lights)
    tims_car_lights.light_bar_button_pressed()
    print(tims_car_lights)
    tims_car_lights.full_beam_toggled()
    print(tims_car_lights)
    tims_car_lights.light_bar_button_pressed()
    print(tims_car_lights)
    tims_car_lights.light_bar_button_pressed()
    print(tims_car_lights)
    tims_car_lights.full_beam_toggled()
    print(tims_car_lights)
    tims_car_lights.light_bar_button_pressed()
    print(tims_car_lights)
    # OUTPUT FROM PRINT STATEMENTS BELOW
    #   CAR LIGHT STATUS: Full beams are OFF! - Light bar is OFF!
    # Light Bar FLASH
    # LightBar(light=True)
    # LightBar(light=False)
    # CAR LIGHT STATUS: Full beams are OFF! - Light bar is OFF!
    # Full Beam switched ON
    # FullBeam(light=True)
    # CAR LIGHT STATUS: Full beams are ON! - Light bar is OFF!
    # Light Bar switched ON
    # LightBar(light=True)
    # CAR LIGHT STATUS: Full beams are ON! - Light bar is ON!
    # Light Bar switched ON
    # LightBar(light=True)
    # CAR LIGHT STATUS: Full beams are ON! - Light bar is ON!
    # Light Bar switched OFF
    # LightBar(light=False)
    # Full beam switched OFF
    # FullBeam(light=False)
    # CAR LIGHT STATUS: Full beams are OFF! - Light bar is OFF!
    # Light Bar FLASH
    # LightBar(light=True)
    # LightBar(light=False)
    # CAR LIGHT STATUS: Full beams are OFF! - Light bar is OFF!


if __name__ == "__main__":
    main()
