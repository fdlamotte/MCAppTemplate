import shutil, os

Import ("env") # type: ignore
menv = env    # type: ignore

env_name = menv["PIOENV"]
variant_name = None

stm32_platform = False
esp32_platform = False
nrf52_platform = False
rp2040_platform = False

add_exampledir_to_incs = False
example_name = ""

# Parse BUILD_FLAGS to customize build
for item in menv.get("BUILD_FLAGS", []):
    # add variant dir from MeshCore tree in libdeps to includes
    if "MC_VARIANT" in item :
        variant_name = item.split("=")[1]
        variant_dir = f".pio/libdeps/{env_name}/MeshCore/variants/{variant_name}"
        menv.Append(BUILD_FLAGS=[f"-I {variant_dir}"])

    elif "ADD_BUILD_FLAGS" in item :
        build_flags_file = f"build_flags/{item.split("=",1)[1]}"
        with open(build_flags_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    menv.Append(BUILD_FLAGS=[line])
        menv["BUILD_FLAGS"].remove(item)

    elif "STM32_PLATFORM" in item :
        stm32_platform = True

    elif "BUILD_EXAMPLE" in item :
        example_name = item.split("=")[1]

    elif "EXCLUDE_FROM_EXAMPLE" in item :
        add_exampledir_to_incs = True

    elif "MC_UI_FLAVOR" in item :
        ui_name = item.split("=")[1]
        ui_dir = f".pio/libdeps/{env_name}/MeshCore/examples/{example_name}/{ui_name}"
        menv.Append(BUILD_FLAGS=[f"-I {ui_dir}"])

# add advert name from PIOENV
menv.Append(BUILD_FLAGS=[f"-D ADVERT_NAME=\'\"{env_name}\"\'"])

# copy libs from MC
libdeps  =f".pio/libdeps/{env_name}/"
mc_dir = libdeps+"MeshCore/"

# copy ed25519 in .pio/libdeps
ed_dir = libdeps+"ed25519/"
if not os.path.exists(ed_dir):
    shutil.copytree(mc_dir+"lib/ed25519", ed_dir)

# if STM32_PLATFORM, then get LFS wrapper
lfs_dir = libdeps+"Adafruit_LittleFS_stm32/"
if stm32_platform and not os.path.exists(lfs_dir):
    shutil.copytree(mc_dir+"arch/stm32/Adafruit_LittleFS_stm32", lfs_dir)

if add_exampledir_to_incs:
    example_dir = f".pio/libdeps/{env_name}/MeshCore/examples/{example_name}"
    print(f"adding {example_dir} to includes")
    menv.Append(BUILD_FLAGS=[f"-I {example_dir}"])