# MCLibExample

Compiles a xiao_nrf52 repeater using meshcore as a library, can be used as a starting point for including meshcore in your own project.

By default a limited number of files from the meshcore tree are compiled (the ones that are defined in `arduino_base` + sensor helpers). By defining a `*_PLATFORM` symbol (except for ESP32 where you define the `ESP32` symbol), corresponding helpers will be added. You can also add the variant files, by defining `MC_VARIANT` to the name of the variant you are using (but you can provide your own variant files).

Some limitations:
* libraries bundled with meshcore (in `arch` and `lib` must be provided (copying the dirs is ok), same for `boards`)
* the `pre_build.py` script must be called from `platformio.ini` if you are using `variants` defined in the MeshCore tree (it will configure `INCLUDEDIRS` to point to the variants directory in `.pio/libdeps`)
* ui helpers can't be included at the moment (but you can add them to your  sources manually ...)


