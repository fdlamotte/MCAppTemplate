Import ("env") # type: ignore
menv = env    # type: ignore

env_name = menv["PIOENV"]

# add variant dir from MeshCore tree in libdeps to includes
for item in menv.get("BUILD_FLAGS", []):
    if "MC_VARIANT" in item :
        variant_name = item.split("=")[1]
        menv.Append(BUILD_FLAGS=[f"-I .pio/libdeps/{env_name}/MeshCore/variants/{variant_name}"])

# add advert name from PIOENV
menv.Append(BUILD_FLAGS=[f"-D ADVERT_NAME=\'\"{env_name}\"\'"])
