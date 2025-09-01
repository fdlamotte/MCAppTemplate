# MAppTemplate

Template to creating your own app using MeshCore as a lib

Populate `src` with your own source files (you can start from `simple_sensor`

By default a limited number of files from the meshcore tree are compiled (the ones that are defined in `arduino_base` + sensor helpers). By defining a `*_PLATFORM` symbol (except for ESP32 where you define the `ESP32` symbol), corresponding helpers will be added. You can also add the variant files, by defining `MC_VARIANT` to the name of the variant you are using (but you can provide your own variant files).

Some limitations:
* `boards` files from MC must be copied to the repository (if not provided by platform)
* the `pre_build.py` script must be called from `platformio.ini` if you are using `variants` defined in the MeshCore tree (it will configure `INCLUDEDIRS` to point to the variants directory in `.pio/libdeps`) and copy MC libs in `libdeps`
* UI helpers are included according to `DISPLAY_CLASS`, you'll have to provide the display support libraries (Adafruit GFX for instance)
