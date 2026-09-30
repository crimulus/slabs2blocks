import os
import json
import shutil
import zipfile

# Clean up previous generated files
if os.path.exists("data"):
    shutil.rmtree("data")

if os.path.exists("pack.mcmeta"):
    os.remove("pack.mcmeta")

# Setup the directory layout
recipe_folder = os.path.join("data", "slabs2blocks", "recipe")
os.makedirs(recipe_folder, exist_ok=True)

# Meta data
mcmeta_data = {
  "pack": {
    "description": "Slabs to Full Blocks\n\u00a77By: H4logen (shapeless by Crimulus)",
    "min_format": [121, 0],
    "max_format": [121, 0]
  }
}

with open("pack.mcmeta", "w", encoding="utf-8") as f:
    json.dump(mcmeta_data, f, indent=2)

def write_recipe(base_name):

    # Clean the prefix for slabs of _block, planks, and plurals
    slab_item = base_name.replace("_block","").replace("_planks", "").removesuffix("s");

    recipe_structure = {
        "type": "minecraft:crafting_shapeless",
        "ingredients": [
            f"minecraft:{slab_item}_slab",
            f"minecraft:{slab_item}_slab"
        ],
        "result": {
            "id": f"minecraft:{base_name}",
            "count": 1
        }
    }

    file_path = os.path.join(recipe_folder, f"slabs_to_{base_name}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(recipe_structure, f, indent=2)

block_names_list = [

    # DEDICATED SECTION: CONCRETE SLABS
    "black_concrete",
    "blue_concrete",
    "brown_concrete",
    "cyan_concrete",
    "gray_concrete",
    "green_concrete",
    "light_blue_concrete",
    "light_gray_concrete",
    "lime_concrete",
    "magenta_concrete",
    "orange_concrete",
    "pink_concrete",
    "purple_concrete",
    "red_concrete",
    "white_concrete",
    "yellow_concrete",

    # DEDICATED SECTION: WOOL SLABS
    "black_wool",
    "blue_wool",
    "brown_wool",
    "cyan_wool",
    "gray_wool",
    "green_wool",
    "light_blue_wool",
    "light_gray_wool",
    "lime_wool",
    "magenta_wool",
    "orange_wool",
    "pink_wool",
    "purple_wool",
    "red_wool",
    "white_wool",
    "yellow_wool",

    # DEDICATED SECTION: PLURALS
    "bricks",
    "cinnabar_bricks",
    "deepslate_bricks",
    "deepslate_tiles",
    "end_stone_bricks",
    "mossy_stone_bricks",
    "mud_bricks",
    "nether_bricks",
    "polished_blackstone_bricks",
    "prismarine_bricks",
    "red_nether_bricks",
    "resin_bricks",
    "stone_bricks",
    "sulfur_bricks",
    "tuff_bricks",

    # DEDICATED SECTION: PLANKS
    "acacia_planks",
    "bamboo_planks",
    "birch_planks",
    "cherry_planks",
    "crimson_planks",
    "dark_oak_planks",
    "jungle_planks",
    "mangrove_planks",
    "oak_planks",
    "pale_oak_planks",
    "poplar_planks",
    "spruce_planks",
    "warped_planks",

    # DEDICATED SECTION: _BLOCK
    "purpur_block",

    "andesite",
    "bamboo_mosaic",
    "blackstone",
    "cinnabar",
    "cobbled_deepslate",
    "cobblestone",
    "cut_copper",
    "cut_red_sandstone",
    "cut_sandstone",
    "dark_prismarine",
    "diorite",
    "exposed_cut_copper",
    "granite",
    "mossy_cobblestone",
    "oxidized_cut_copper",
    "polished_andesite",
    "polished_blackstone",
    "polished_deepslate",
    "polished_cinnabar",
    "polished_diorite",
    "polished_granite",
    "polished_sulfur",
    "prismarine",
    "polished_tuff",
    "quartz",
    "red_sandstone",
    "sandstone",
    "smooth_quartz",
    "smooth_red_sandstone",
    "smooth_sandstone",
    "smooth_stone",
    "stone",
    "sulfur",
    "tuff",
    "waxed_cut_copper",
    "waxed_exposed_cut_copper",
    "waxed_oxidized_cut_copper",
    "waxed_weathered_cut_copper",
    "weathered_cut_copper"
]

for block in block_names_list:
    write_recipe(block)


# Create ZIP file
zip_filename = "Slabs2Blocks by H4logen (shapeless by Crimulus).zip"

with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zip_file:

    # Add pack.mcmeta to the root of the ZIP
    zip_file.write("pack.mcmeta", "pack.mcmeta")

    # Add the entire data/ folder
    for root, dirs, files in os.walk("data"):
        for file in files:
            file_path = os.path.join(root, file)

            # Preserve the data/ folder structure inside the ZIP
            archive_path = os.path.relpath(file_path, ".")
            zip_file.write(file_path, archive_path)

print(
    f"🎉 Successfully generated {len(block_names_list)} recipes, "
    f"pack.mcmeta, and '{zip_filename}'!"
)
