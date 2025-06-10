import class_segregation as cs

Abacus = cs.Item(
    desc=[],
    special=[],
    index="abacus",
    name="Abacus",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=2,
    url="/api/2014/equipment/abacus",
    contents=[],
    properties=[]
)

Acid_Vial = cs.Item(
    desc=[],
    special=[],
    index="acid-vial",
    name="Acid (vial)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(25, "gp"),
    weight=1,
    url="/api/2014/equipment/acid-vial",
    contents=[],
    properties=[]
)

Alchemists_Fire_Flask = cs.Item(
    desc=[],
    special=[],
    index="alchemists-fire-flask",
    name="Alchemist's fire (flask)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(50, "gp"),
    weight=1,
    url="/api/2014/equipment/alchemists-fire-flask",
    contents=[],
    properties=[]
)

Alchemists_Supplies = cs.Item(
    desc=[],
    special=[],
    index="alchemists-supplies",
    name="Alchemist's Supplies",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(50, "gp"),
    weight=8,
    url="/api/2014/equipment/alchemists-supplies",
    contents=[],
    properties=[]
)

Alms_box = cs.Item(
    desc=[],
    special=[],
    index="alms-box",
    name="Alms box",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(0, "cp"),
    weight=0,
    url="/api/2014/equipment/alms-box",
    contents=[],
    properties=[]
)

Amulet = cs.Item(
    desc=[],
    special=[],
    index="amulet",
    name="Amulet",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("holy-symbols", "Holy Symbols", "/api/2014/equipment-categories/holy-symbols"),
    cost=cs.Cost(5, "gp"),
    weight=1,
    url="/api/2014/equipment/amulet",
    contents=[],
    properties=[]
)

# Animal_Feed_1_day = cs.Item(
#     desc=[],
#     special=[],
#     index="animal-feed-1-day",
#     name="Animal Feed (1 day)",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(5, "cp"),
#     weight=10,
#     url="/api/2014/equipment/animal-feed-1-day",
#     contents=[],
#     properties=[]
# )

Antitoxin_vial = cs.Item(
    desc=[],
    special=[],
    index="antitoxin-vial",
    name="Antitoxin (vial)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(50, "gp"),
    weight=0,
    url="/api/2014/equipment/antitoxin-vial",
    contents=[],
    properties=[]
)

Arrow = cs.Item(
    desc=[],
    special=[],
    index="arrow",
    name="Arrow",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("ammunition", "Ammunition", "/api/2014/equipment-categories/ammunition"),
    cost=cs.Cost(1, "gp"),
    weight=1,
    url="/api/2014/equipment/arrow",
    contents=[],
    properties=[]
)

Backpack = cs.Item(
    desc=[],
    special=[],
    index="backpack",
    name="Backpack",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=5,
    url="/api/2014/equipment/backpack",
    contents=[],
    properties=[]
)

Bagpipes = cs.Item(
    desc=[],
    special=[],
    index="bagpipes",
    name="Bagpipes",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(30, "gp"),
    weight=6,
    url="/api/2014/equipment/bagpipes",
    contents=[],
    properties=[]
)

Ball_bearings_bag_of_1000 = cs.Item(
    desc=[],
    special=[],
    index="ball-bearings-bag-of-1000",
    name="Ball bearings (bag of 1,000)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=2,
    url="/api/2014/equipment/ball-bearings-bag-of-1000",
    contents=[],
    properties=[]
)

# Barding_Breastplate = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-breastplate",
#     name="Barding: Breastplate",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(1600, "gp"),
#     weight=40,
#     url="/api/2014/equipment/barding-breastplate",
#     contents=[],
#     properties=[]
# )

# Barding_Chain_mail = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-chain-mail",
#     name="Barding: Chain mail",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(300, "gp"),
#     weight=110,
#     url="/api/2014/equipment/barding-chain-mail",
#     contents=[],
#     properties=[]
# )

# Barding_Chain_shirt = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-chain-shirt",
#     name="Barding: Chain shirt",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(200, "gp"),
#     weight=40,
#     url="/api/2014/equipment/barding-chain-shirt",
#     contents=[],
#     properties=[]
# )

# Barding_Half_plate = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-half-plate",
#     name="Barding: Half plate",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(3000, "gp"),
#     weight=80,
#     url="/api/2014/equipment/barding-half-plate",
#     contents=[],
#     properties=[]
# )

# Barding_Hide = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-hide",
#     name="Barding: Hide",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(40, "gp"),
#     weight=24,
#     url="/api/2014/equipment/barding-hide",
#     contents=[],
#     properties=[]
# )

# Barding_Leather = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-leather",
#     name="Barding: Leather",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(40, "gp"),
#     weight=20,
#     url="/api/2014/equipment/barding-leather",
#     contents=[],
#     properties=[]
# )

# Barding_Padded = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-padded",
#     name="Barding: Padded",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(20, "gp"),
#     weight=16,
#     url="/api/2014/equipment/barding-padded",
#     contents=[],
#     properties=[]
# )

# Barding_Plate = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-plate",
#     name="Barding: Plate",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(6000, "gp"),
#     weight=130,
#     url="/api/2014/equipment/barding-plate",
#     contents=[],
#     properties=[]
# )

# Barding_Ring_mail = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-ring-mail",
#     name="Barding: Ring mail",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(12, "gp"),
#     weight=80,
#     url="/api/2014/equipment/barding-ring-mail",
#     contents=[],
#     properties=[]
# )

# Barding_Scale_mail = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-scale-mail",
#     name="Barding: Scale mail",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(200, "gp"),
#     weight=90,
#     url="/api/2014/equipment/barding-scale-mail",
#     contents=[],
#     properties=[]
# )

# Barding_Splint = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-splint",
#     name="Barding: Splint",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(800, "gp"),
#     weight=120,
#     url="/api/2014/equipment/barding-splint",
#     contents=[],
#     properties=[]
# )

# Barding_Studded_Leather = cs.Item(
#     desc=[],
#     special=[],
#     index="barding-studded-leather",
#     name="Barding: Studded Leather",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(180, "gp"),
#     weight=26,
#     url="/api/2014/equipment/barding-studded-leather",
#     contents=[],
#     properties=[]
# )

Barrel = cs.Item(
    desc=[],
    special=[],
    index="barrel",
    name="Barrel",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=70,
    url="/api/2014/equipment/barrel",
    contents=[],
    properties=[]
)

Basket = cs.Item(
    desc=[],
    special=[],
    index="basket",
    name="Basket",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(4, "sp"),
    weight=2,
    url="/api/2014/equipment/basket",
    contents=[],
    properties=[]
)

Battleaxe = cs.Weapon(
    desc=[],
    special=[],
    index="battleaxe",
    name="Battleaxe",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=4,
    url="/api/2014/equipment/battleaxe",
    contents=[],
    properties=[
        cs.APIObject("versatile", "Versatile", "/api/2014/weapon-properties/versatile")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d8"), cs.APIObject("slashing", "Slashing", "/api/2014/damage-types/slashing")),
    range={"normal": 5}
)

Bedroll = cs.Item(
    desc=[],
    special=[],
    index="bedroll",
    name="Bedroll",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=7,
    url="/api/2014/equipment/bedroll",
    contents=[],
    properties=[]
)

Bell = cs.Item(
    desc=[],
    special=[],
    index="bell",
    name="Bell",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=0,
    url="/api/2014/equipment/bell",
    contents=[],
    properties=[]
)

# Bit_and_bridle = cs.Item(
#     desc=[],
#     special=[],
#     index="bit-and-bridle",
#     name="Bit and bridle",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(2, "gp"),
#     weight=1,
#     url="/api/2014/equipment/bit-and-bridle",
#     contents=[],
#     properties=[]
# )

Blanket = cs.Item(
    desc=[],
    special=[],
    index="blanket",
    name="Blanket",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "sp"),
    weight=3,
    url="/api/2014/equipment/blanket",
    contents=[],
    properties=[]
)

Block_and_tackle = cs.Item(
    desc=[],
    special=[],
    index="block-and-tackle",
    name="Block and tackle",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=5,
    url="/api/2014/equipment/block-and-tackle",
    contents=[],
    properties=[]
)

Block_of_incense = cs.Item(
    desc=[],
    special=[],
    index="block-of-incense",
    name="Block of incense",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(0, "cp"),
    weight=0,
    url="/api/2014/equipment/block-of-incense",
    contents=[],
    properties=[]
)

Blowgun = cs.Weapon(
    desc=[],
    special=[],
    index="blowgun",
    name="Blowgun",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=1,
    url="/api/2014/equipment/blowgun",
    contents=[],
    properties=[
        cs.APIObject("ammunition", "Ammunition", "/api/2014/weapon-properties/ammunition"),
        cs.APIObject("loading", "Loading", "/api/2014/weapon-properties/loading")
    ],
    weapon_category="Martial",
    weapon_range="Ranged",
    category_range="Martial Ranged",
    damage=cs.Damage(cs.Dice.translate("1d6"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 25}
)

Blowgun_needle = cs.Item(
    desc=[],
    special=[],
    index="blowgun-needle",
    name="Blowgun needle",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("ammunition", "Ammunition", "/api/2014/equipment-categories/ammunition"),
    cost=cs.Cost(1, "gp"),
    weight=1,
    url="/api/2014/equipment/blowgun-needle",
    contents=[],
    properties=[]
)

Book = cs.Item(
    desc=[],
    special=[],
    index="book",
    name="Book",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(25, "gp"),
    weight=5,
    url="/api/2014/equipment/book",
    contents=[],
    properties=[]
)

Bottle_glass = cs.Item(
    desc=[],
    special=[],
    index="bottle-glass",
    name="Bottle, glass",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=2,
    url="/api/2014/equipment/bottle-glass",
    contents=[],
    properties=[]
)

Breastplate = cs.Armour(
    desc=[],
    special=[],
    index="breastplate",
    name="Breastplate",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(400, "gp"),
    weight=20,
    url="/api/2014/equipment/breastplate",
    contents=[],
    properties=[],
    armor_category="Medium",
    armor_class=cs.ArmourClass(14, True, 2),
    str_minimum=0,
    stealth_disadvantage=False
)

Brewers_Supplies = cs.Item(
    desc=[],
    special=[],
    index="brewers-supplies",
    name="Brewer's Supplies",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(20, "gp"),
    weight=9,
    url="/api/2014/equipment/brewers-supplies",
    contents=[],
    properties=[]
)

Bucket = cs.Item(
    desc=[],
    special=[],
    index="bucket",
    name="Bucket",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "cp"),
    weight=2,
    url="/api/2014/equipment/bucket",
    contents=[],
    properties=[]
)

Burglars_Pack = cs.Item(
    desc=[],
    special=[],
    index="burglars-pack",
    name="Burglar's Pack",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("equipment-packs", "Equipment Packs", "/api/2014/equipment-categories/equipment-packs"),
    cost=cs.Cost(16, "gp"),
    weight=0,
    url="/api/2014/equipment/burglars-pack",
    contents=[],
    properties=[]
)

Calligraphers_Supplies = cs.Item(
    desc=[],
    special=[],
    index="calligraphers-supplies",
    name="Calligrapher's Supplies",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=5,
    url="/api/2014/equipment/calligraphers-supplies",
    contents=[],
    properties=[]
)

Caltrops = cs.Item(
    desc=[],
    special=[],
    index="caltrops",
    name="Caltrops",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "cp"),
    weight=2,
    url="/api/2014/equipment/caltrops",
    contents=[],
    properties=[]
)

# Camel = cs.Item(
#     desc=[],
#     special=[],
#     index="camel",
#     name="Camel",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(50, "gp"),
#     weight=0,
#     url="/api/2014/equipment/camel",
#     contents=[],
#     properties=[]
# )

Candle = cs.Item(
    desc=[],
    special=[],
    index="candle",
    name="Candle",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "cp"),
    weight=0,
    url="/api/2014/equipment/candle",
    contents=[],
    properties=[]
)

Carpenters_Tools = cs.Item(
    desc=[],
    special=[],
    index="carpenters-tools",
    name="Carpenter's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(8, "gp"),
    weight=6,
    url="/api/2014/equipment/carpenters-tools",
    contents=[],
    properties=[]
)

# Carriage = cs.Item(
#     desc=[],
#     special=[],
#     index="carriage",
#     name="Carriage",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(100, "gp"),
#     weight=600,
#     url="/api/2014/equipment/carriage",
#     contents=[],
#     properties=[]
# )

# Cart = cs.Item(
#     desc=[],
#     special=[],
#     index="cart",
#     name="Cart",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(15, "gp"),
#     weight=200,
#     url="/api/2014/equipment/cart",
#     contents=[],
#     properties=[]
# )

Cartographers_Tools = cs.Item(
    desc=[],
    special=[],
    index="cartographers-tools",
    name="Cartographer's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(15, "gp"),
    weight=6,
    url="/api/2014/equipment/cartographers-tools",
    contents=[],
    properties=[]
)

Case_crossbow_bolt = cs.Item(
    desc=[],
    special=[],
    index="case-crossbow-bolt",
    name="Case, crossbow bolt",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=1,
    url="/api/2014/equipment/case-crossbow-bolt",
    contents=[],
    properties=[]
)

Case_map_or_scroll = cs.Item(
    desc=[],
    special=[],
    index="case-map-or-scroll",
    name="Case, map or scroll",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=1,
    url="/api/2014/equipment/case-map-or-scroll",
    contents=[],
    properties=[]
)

Censer = cs.Item(
    desc=[],
    special=[],
    index="censer",
    name="Censer",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(0, "cp"),
    weight=0,
    url="/api/2014/equipment/censer",
    contents=[],
    properties=[]
)

Chain_10_feet = cs.Item(
    desc=[],
    special=[],
    index="chain-10-feet",
    name="Chain (10 feet)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "gp"),
    weight=10,
    url="/api/2014/equipment/chain-10-feet",
    contents=[],
    properties=[]
)

Chain_Mail = cs.Armour(
    desc=[],
    special=[],
    index="chain-mail",
    name="Chain Mail",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(75, "gp"),
    weight=55,
    url="/api/2014/equipment/chain-mail",
    contents=[],
    properties=[],
    armor_category="Heavy",
    armor_class=cs.ArmourClass(16, False, None),
    str_minimum=13,
    stealth_disadvantage=True
)

Chain_Shirt = cs.Armour(
    desc=[],
    special=[],
    index="chain-shirt",
    name="Chain Shirt",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(50, "gp"),
    weight=20,
    url="/api/2014/equipment/chain-shirt",
    contents=[],
    properties=[],
    armor_category="Medium",
    armor_class=cs.ArmourClass(13, True, 2),
    str_minimum=0,
    stealth_disadvantage=False
)

Chalk_1_piece = cs.Item(
    desc=[],
    special=[],
    index="chalk-1-piece",
    name="Chalk (1 piece)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "cp"),
    weight=0,
    url="/api/2014/equipment/chalk-1-piece",
    contents=[],
    properties=[]
)

# Chariot = cs.Item(
#     desc=[],
#     special=[],
#     index="chariot",
#     name="Chariot",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(250, "gp"),
#     weight=100,
#     url="/api/2014/equipment/chariot",
#     contents=[],
#     properties=[]
# )

Chest = cs.Item(
    desc=[],
    special=[],
    index="chest",
    name="Chest",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "gp"),
    weight=25,
    url="/api/2014/equipment/chest",
    contents=[],
    properties=[]
)

Climbers_Kit = cs.Item(
    desc=[],
    special=[],
    index="climbers-kit",
    name="Climber's Kit",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("kits", "Kits", "/api/2014/equipment-categories/kits"),
    cost=cs.Cost(25, "gp"),
    weight=12,
    url="/api/2014/equipment/climbers-kit",
    contents=[],
    properties=[]
)

Clothes_common = cs.Item(
    desc=[],
    special=[],
    index="clothes-common",
    name="Clothes, common",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "sp"),
    weight=3,
    url="/api/2014/equipment/clothes-common",
    contents=[],
    properties=[]
)

Clothes_costume = cs.Item(
    desc=[],
    special=[],
    index="clothes-costume",
    name="Clothes, costume",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "gp"),
    weight=4,
    url="/api/2014/equipment/clothes-costume",
    contents=[],
    properties=[]
)

Clothes_fine = cs.Item(
    desc=[],
    special=[],
    index="clothes-fine",
    name="Clothes, fine",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(15, "gp"),
    weight=6,
    url="/api/2014/equipment/clothes-fine",
    contents=[],
    properties=[]
)

Clothes_travelers = cs.Item(
    desc=[],
    special=[],
    index="clothes-travelers",
    name="Clothes, traveler's",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=4,
    url="/api/2014/equipment/clothes-travelers",
    contents=[],
    properties=[]
)

Club = cs.Weapon(
    desc=[],
    special=[],
    index="club",
    name="Club",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(1, "sp"),
    weight=2,
    url="/api/2014/equipment/club",
    contents=[],
    properties=[
        cs.APIObject("light", "Light", "/api/2014/weapon-properties/light"),
        cs.APIObject("monk", "Monk", "/api/2014/weapon-properties/monk")
    ],
    weapon_category="Simple",
    weapon_range="Melee",
    category_range="Simple Melee",
    damage=cs.Damage(cs.Dice.translate("1d4"), cs.APIObject("bludgeoning", "Bludgeoning", "/api/2014/damage-types/bludgeoning")),
    range={"normal": 5}
)

Cobblers_Tools = cs.Item(
    desc=[],
    special=[],
    index="cobblers-tools",
    name="Cobbler's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(5, "gp"),
    weight=5,
    url="/api/2014/equipment/cobblers-tools",
    contents=[],
    properties=[]
)

Component_pouch = cs.Item(
    desc=[],
    special=[],
    index="component-pouch",
    name="Component pouch",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(25, "gp"),
    weight=2,
    url="/api/2014/equipment/component-pouch",
    contents=[],
    properties=[]
)

Cooks_utensils = cs.Item(
    desc=[],
    special=[],
    index="cooks-utensils",
    name="Cook's utensils",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(1, "gp"),
    weight=8,
    url="/api/2014/equipment/cooks-utensils",
    contents=[],
    properties=[]
)

Crossbow_bolt = cs.Item(
    desc=[],
    special=[],
    index="crossbow-bolt",
    name="Crossbow bolt",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("ammunition", "Ammunition", "/api/2014/equipment-categories/ammunition"),
    cost=cs.Cost(1, "gp"),
    weight=1.5,
    url="/api/2014/equipment/crossbow-bolt",
    contents=[],
    properties=[]
)

Crossbow_hand = cs.Weapon(
    desc=[],
    special=[],
    index="crossbow-hand",
    name="Crossbow, hand",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(75, "gp"),
    weight=3,
    url="/api/2014/equipment/crossbow-hand",
    contents=[],
    properties=[
        cs.APIObject("ammunition", "Ammunition", "/api/2014/weapon-properties/ammunition"),
        cs.APIObject("light", "Light", "/api/2014/weapon-properties/light"),
        cs.APIObject("loading", "Loading", "/api/2014/weapon-properties/loading")
    ],
    weapon_category="Martial",
    weapon_range="Ranged",
    category_range="Martial Ranged",
    damage=cs.Damage(cs.Dice.translate("1d6"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 30}
)

Crossbow_heavy = cs.Weapon(
    desc=[],
    special=[],
    index="crossbow-heavy",
    name="Crossbow, heavy",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(50, "gp"),
    weight=18,
    url="/api/2014/equipment/crossbow-heavy",
    contents=[],
    properties=[
        cs.APIObject("ammunition", "Ammunition", "/api/2014/weapon-properties/ammunition"),
        cs.APIObject("heavy", "Heavy", "/api/2014/weapon-properties/heavy"),
        cs.APIObject("loading", "Loading", "/api/2014/weapon-properties/loading"),
        cs.APIObject("two-handed", "Two-Handed", "/api/2014/weapon-properties/two-handed")
    ],
    weapon_category="Martial",
    weapon_range="Ranged",
    category_range="Martial Ranged",
    damage=cs.Damage(cs.Dice.translate("1d10"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 100}
)

Crossbow_light = cs.Weapon(
    desc=[],
    special=[],
    index="crossbow-light",
    name="Crossbow, light",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(25, "gp"),
    weight=5,
    url="/api/2014/equipment/crossbow-light",
    contents=[],
    properties=[
        cs.APIObject("ammunition", "Ammunition", "/api/2014/weapon-properties/ammunition"),
        cs.APIObject("loading", "Loading", "/api/2014/weapon-properties/loading"),
        cs.APIObject("two-handed", "Two-Handed", "/api/2014/weapon-properties/two-handed")
    ],
    weapon_category="Simple",
    weapon_range="Ranged",
    category_range="Simple Ranged",
    damage=cs.Damage(cs.Dice.translate("1d8"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 80}
)

Crowbar = cs.Item(
    desc=[],
    special=[],
    index="crowbar",
    name="Crowbar",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=5,
    url="/api/2014/equipment/crowbar",
    contents=[],
    properties=[]
)

Crystal = cs.Item(
    desc=[],
    special=[],
    index="crystal",
    name="Crystal",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("arcane-foci", "Arcane Foci", "/api/2014/equipment-categories/arcane-foci"),
    cost=cs.Cost(10, "gp"),
    weight=1,
    url="/api/2014/equipment/crystal",
    contents=[],
    properties=[]
)

Dagger = cs.Weapon(
    desc=[],
    special=[],
    index="dagger",
    name="Dagger",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(2, "gp"),
    weight=1,
    url="/api/2014/equipment/dagger",
    contents=[],
    properties=[
        cs.APIObject("finesse", "Finesse", "/api/2014/weapon-properties/finesse"),
        cs.APIObject("light", "Light", "/api/2014/weapon-properties/light"),
        cs.APIObject("thrown", "Thrown", "/api/2014/weapon-properties/thrown"),
        cs.APIObject("monk", "Monk", "/api/2014/weapon-properties/monk")
    ],
    weapon_category="Simple",
    weapon_range="Melee",
    category_range="Simple Melee",
    damage=cs.Damage(cs.Dice.translate("1d4"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 5}
)

Dart = cs.Weapon(
    desc=[],
    special=[],
    index="dart",
    name="Dart",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(5, "cp"),
    weight=0.25,
    url="/api/2014/equipment/dart",
    contents=[],
    properties=[
        cs.APIObject("finesse", "Finesse", "/api/2014/weapon-properties/finesse"),
        cs.APIObject("thrown", "Thrown", "/api/2014/weapon-properties/thrown")
    ],
    weapon_category="Simple",
    weapon_range="Ranged",
    category_range="Simple Ranged",
    damage=cs.Damage(cs.Dice.translate("1d4"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 20}
)

cs.Dice_Set = cs.Item(
    desc=[],
    special=[],
    index="dice-set",
    name="cs.Dice Set",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(1, "sp"),
    weight=0,
    url="/api/2014/equipment/dice-set",
    contents=[],
    properties=[]
)

Diplomats_Pack = cs.Item(
    desc=[],
    special=[],
    index="diplomats-pack",
    name="Diplomat's Pack",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("equipment-packs", "Equipment Packs", "/api/2014/equipment-categories/equipment-packs"),
    cost=cs.Cost(39, "gp"),
    weight=0,
    url="/api/2014/equipment/diplomats-pack",
    contents=[],
    properties=[]
)

Disguise_Kit = cs.Item(
    desc=[],
    special=[],
    index="disguise-kit",
    name="Disguise Kit",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("kits", "Kits", "/api/2014/equipment-categories/kits"),
    cost=cs.Cost(25, "gp"),
    weight=3,
    url="/api/2014/equipment/disguise-kit",
    contents=[],
    properties=[]
)

# Donkey = cs.Item(
#     desc=[],
#     special=[],
#     index="donkey",
#     name="Donkey",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(8, "gp"),
#     weight=0,
#     url="/api/2014/equipment/donkey",
#     contents=[],
#     properties=[]
# )

Drum = cs.Item(
    desc=[],
    special=[],
    index="drum",
    name="Drum",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(6, "gp"),
    weight=3,
    url="/api/2014/equipment/drum",
    contents=[],
    properties=[]
)

Dulcimer = cs.Item(
    desc=[],
    special=[],
    index="dulcimer",
    name="Dulcimer",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(25, "gp"),
    weight=10,
    url="/api/2014/equipment/dulcimer",
    contents=[],
    properties=[]
)

Dungeoneers_Pack = cs.Item(
    desc=[],
    special=[],
    index="dungeoneers-pack",
    name="Dungeoneer's Pack",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("equipment-packs", "Equipment Packs", "/api/2014/equipment-categories/equipment-packs"),
    cost=cs.Cost(12, "gp"),
    weight=0,
    url="/api/2014/equipment/dungeoneers-pack",
    contents=[],
    properties=[]
)

# Elephant = cs.Item(
#     desc=[],
#     special=[],
#     index="elephant",
#     name="Elephant",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(200, "gp"),
#     weight=0,
#     url="/api/2014/equipment/elephant",
#     contents=[],
#     properties=[]
# )

Emblem = cs.Item(
    desc=[],
    special=[],
    index="emblem",
    name="Emblem",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("holy-symbols", "Holy Symbols", "/api/2014/equipment-categories/holy-symbols"),
    cost=cs.Cost(5, "gp"),
    weight=0,
    url="/api/2014/equipment/emblem",
    contents=[],
    properties=[]
)

Entertainers_Pack = cs.Item(
    desc=[],
    special=[],
    index="entertainers-pack",
    name="Entertainer's Pack",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("equipment-packs", "Equipment Packs", "/api/2014/equipment-categories/equipment-packs"),
    cost=cs.Cost(40, "gp"),
    weight=0,
    url="/api/2014/equipment/entertainers-pack",
    contents=[],
    properties=[]
)

Explorers_Pack = cs.Item(
    desc=[],
    special=[],
    index="explorers-pack",
    name="Explorer's Pack",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("equipment-packs", "Equipment Packs", "/api/2014/equipment-categories/equipment-packs"),
    cost=cs.Cost(10, "gp"),
    weight=0,
    url="/api/2014/equipment/explorers-pack",
    contents=[],
    properties=[]
)

Fishing_tackle = cs.Item(
    desc=[],
    special=[],
    index="fishing-tackle",
    name="Fishing tackle",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=4,
    url="/api/2014/equipment/fishing-tackle",
    contents=[],
    properties=[]
)

Flail = cs.Weapon(
    desc=[],
    special=[],
    index="flail",
    name="Flail",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=2,
    url="/api/2014/equipment/flail",
    contents=[],
    properties=[
        
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d8"), cs.APIObject("bludgeoning", "Bludgeoning", "/api/2014/damage-types/bludgeoning")),
    range={"normal": 5}
)

Flask_or_tankard = cs.Item(
    desc=[],
    special=[],
    index="flask-or-tankard",
    name="Flask or tankard",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "cp"),
    weight=1,
    url="/api/2014/equipment/flask-or-tankard",
    contents=[],
    properties=[]
)

Flute = cs.Item(
    desc=[],
    special=[],
    index="flute",
    name="Flute",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(2, "gp"),
    weight=1,
    url="/api/2014/equipment/flute",
    contents=[],
    properties=[]
)

Forgery_Kit = cs.Item(
    desc=[],
    special=[],
    index="forgery-kit",
    name="Forgery Kit",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("kits", "Kits", "/api/2014/equipment-categories/kits"),
    cost=cs.Cost(15, "gp"),
    weight=5,
    url="/api/2014/equipment/forgery-kit",
    contents=[],
    properties=[]
)

# Galley = cs.Item(
#     desc=[],
#     special=[],
#     index="galley",
#     name="Galley",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(30000, "gp"),
#     weight=0,
#     url="/api/2014/equipment/galley",
#     contents=[],
#     properties=[]
# )

Glaive = cs.Weapon(
    desc=[],
    special=[],
    index="glaive",
    name="Glaive",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(20, "gp"),
    weight=6,
    url="/api/2014/equipment/glaive",
    contents=[],
    properties=[
        cs.APIObject("heavy", "Heavy", "/api/2014/weapon-properties/heavy"),
        cs.APIObject("reach", "Reach", "/api/2014/weapon-properties/reach"),
        cs.APIObject("two-handed", "Two-Handed", "/api/2014/weapon-properties/two-handed")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d10"), cs.APIObject("slashing", "Slashing", "/api/2014/damage-types/slashing")),
    range={"normal": 5}
)

Glassblowers_Tools = cs.Item(
    desc=[],
    special=[],
    index="glassblowers-tools",
    name="Glassblower's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(30, "gp"),
    weight=5,
    url="/api/2014/equipment/glassblowers-tools",
    contents=[],
    properties=[]
)

Grappling_hook = cs.Item(
    desc=[],
    special=[],
    index="grappling-hook",
    name="Grappling hook",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=4,
    url="/api/2014/equipment/grappling-hook",
    contents=[],
    properties=[]
)

Greataxe = cs.Weapon(
    desc=[],
    special=[],
    index="greataxe",
    name="Greataxe",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(30, "gp"),
    weight=7,
    url="/api/2014/equipment/greataxe",
    contents=[],
    properties=[
        cs.APIObject("heavy", "Heavy", "/api/2014/weapon-properties/heavy"),
        cs.APIObject("two-handed", "Two-Handed", "/api/2014/weapon-properties/two-handed")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d12"), cs.APIObject("slashing", "Slashing", "/api/2014/damage-types/slashing")),
    range={"normal": 5}
)

Greatclub = cs.Weapon(
    desc=[],
    special=[],
    index="greatclub",
    name="Greatclub",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(2, "sp"),
    weight=10,
    url="/api/2014/equipment/greatclub",
    contents=[],
    properties=[
        cs.APIObject("two-handed", "Two-Handed", "/api/2014/weapon-properties/two-handed")
    ],
    weapon_category="Simple",
    weapon_range="Melee",
    category_range="Simple Melee",
    damage=cs.Damage(cs.Dice.translate("1d8"), cs.APIObject("bludgeoning", "Bludgeoning", "/api/2014/damage-types/bludgeoning")),
    range={"normal": 5}
)

Greatsword = cs.Weapon(
    desc=[],
    special=[],
    index="greatsword",
    name="Greatsword",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(50, "gp"),
    weight=6,
    url="/api/2014/equipment/greatsword",
    contents=[],
    properties=[
        cs.APIObject("heavy", "Heavy", "/api/2014/weapon-properties/heavy"),
        cs.APIObject("two-handed", "Two-Handed", "/api/2014/weapon-properties/two-handed")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("2d6"), cs.APIObject("slashing", "Slashing", "/api/2014/damage-types/slashing")),
    range={"normal": 5}
)

Halberd = cs.Weapon(
    desc=[],
    special=[],
    index="halberd",
    name="Halberd",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(20, "gp"),
    weight=6,
    url="/api/2014/equipment/halberd",
    contents=[],
    properties=[
        cs.APIObject("heavy", "Heavy", "/api/2014/weapon-properties/heavy"),
        cs.APIObject("reach", "Reach", "/api/2014/weapon-properties/reach"),
        cs.APIObject("two-handed", "Two-Handed", "/api/2014/weapon-properties/two-handed")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d10"), cs.APIObject("slashing", "Slashing", "/api/2014/damage-types/slashing")),
    range={"normal": 5}
)

Half_Plate_Armor = cs.Armour(
    desc=[],
    special=[],
    index="half-plate-armor",
    name="Half Plate Armor",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(750, "gp"),
    weight=40,
    url="/api/2014/equipment/half-plate-armor",
    contents=[],
    properties=[],
    armor_category="Medium",
    armor_class=cs.ArmourClass(15, True, 2),
    str_minimum=0,
    stealth_disadvantage=True
)

Hammer = cs.Item(
    desc=[],
    special=[],
    index="hammer",
    name="Hammer",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=3,
    url="/api/2014/equipment/hammer",
    contents=[],
    properties=[]
)

Hammer_sledge = cs.Item(
    desc=[],
    special=[],
    index="hammer-sledge",
    name="Hammer, sledge",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=10,
    url="/api/2014/equipment/hammer-sledge",
    contents=[],
    properties=[]
)

Handaxe = cs.Weapon(
    desc=[],
    special=[],
    index="handaxe",
    name="Handaxe",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(5, "gp"),
    weight=2,
    url="/api/2014/equipment/handaxe",
    contents=[],
    properties=[
        cs.APIObject("light", "Light", "/api/2014/weapon-properties/light"),
        cs.APIObject("thrown", "Thrown", "/api/2014/weapon-properties/thrown"),
        cs.APIObject("monk", "Monk", "/api/2014/weapon-properties/monk")
    ],
    weapon_category="Simple",
    weapon_range="Melee",
    category_range="Simple Melee",
    damage=cs.Damage(cs.Dice.translate("1d6"), cs.APIObject("slashing", "Slashing", "/api/2014/damage-types/slashing")),
    range={"normal": 5}
)

Healers_Kit = cs.Item(
    desc=[],
    special=[],
    index="healers-kit",
    name="Healer's Kit",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("kits", "Kits", "/api/2014/equipment-categories/kits"),
    cost=cs.Cost(5, "gp"),
    weight=3,
    url="/api/2014/equipment/healers-kit",
    contents=[],
    properties=[]
)

Herbalism_Kit = cs.Item(
    desc=[],
    special=[],
    index="herbalism-kit",
    name="Herbalism Kit",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("kits", "Kits", "/api/2014/equipment-categories/kits"),
    cost=cs.Cost(5, "gp"),
    weight=3,
    url="/api/2014/equipment/herbalism-kit",
    contents=[],
    properties=[]
)

Hide_Armor = cs.Armour(
    desc=[],
    special=[],
    index="hide-armor",
    name="Hide Armor",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=12,
    url="/api/2014/equipment/hide-armor",
    contents=[],
    properties=[],
    armor_category="Medium",
    armor_class=cs.ArmourClass(12, True, 2),
    str_minimum=0,
    stealth_disadvantage=False
)

Holy_water_flask = cs.Item(
    desc=[],
    special=[],
    index="holy-water-flask",
    name="Holy water (flask)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(25, "gp"),
    weight=1,
    url="/api/2014/equipment/holy-water-flask",
    contents=[],
    properties=[]
)

Horn = cs.Item(
    desc=[],
    special=[],
    index="horn",
    name="Horn",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(3, "gp"),
    weight=2,
    url="/api/2014/equipment/horn",
    contents=[],
    properties=[]
)

# Horse_draft = cs.Item(
#     desc=[],
#     special=[],
#     index="horse-draft",
#     name="Horse, draft",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(50, "gp"),
#     weight=0,
#     url="/api/2014/equipment/horse-draft",
#     contents=[],
#     properties=[]
# )

# Horse_riding = cs.Item(
#     desc=[],
#     special=[],
#     index="horse-riding",
#     name="Horse, riding",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(75, "gp"),
#     weight=0,
#     url="/api/2014/equipment/horse-riding",
#     contents=[],
#     properties=[]
# )

Hourglass = cs.Item(
    desc=[],
    special=[],
    index="hourglass",
    name="Hourglass",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(25, "gp"),
    weight=1,
    url="/api/2014/equipment/hourglass",
    contents=[],
    properties=[]
)

Hunting_trap = cs.Item(
    desc=[],
    special=[],
    index="hunting-trap",
    name="Hunting trap",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "gp"),
    weight=25,
    url="/api/2014/equipment/hunting-trap",
    contents=[],
    properties=[]
)

Ink_1_ounce_bottle = cs.Item(
    desc=[],
    special=[],
    index="ink-1-ounce-bottle",
    name="Ink (1 ounce bottle)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(10, "gp"),
    weight=0,
    url="/api/2014/equipment/ink-1-ounce-bottle",
    contents=[],
    properties=[]
)

Ink_pen = cs.Item(
    desc=[],
    special=[],
    index="ink-pen",
    name="Ink pen",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "cp"),
    weight=0,
    url="/api/2014/equipment/ink-pen",
    contents=[],
    properties=[]
)

Javelin = cs.Weapon(
    desc=[],
    special=[],
    index="javelin",
    name="Javelin",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(5, "sp"),
    weight=2,
    url="/api/2014/equipment/javelin",
    contents=[],
    properties=[
        cs.APIObject("thrown", "Thrown", "/api/2014/weapon-properties/thrown"),
        cs.APIObject("monk", "Monk", "/api/2014/weapon-properties/monk")
    ],
    weapon_category="Simple",
    weapon_range="Melee",
    category_range="Simple Melee",
    damage=cs.Damage(cs.Dice.translate("1d6"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 5}
)

Jewelers_Tools = cs.Item(
    desc=[],
    special=[],
    index="jewelers-tools",
    name="Jeweler's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(25, "gp"),
    weight=2,
    url="/api/2014/equipment/jewelers-tools",
    contents=[],
    properties=[]
)

Jug_or_pitcher = cs.Item(
    desc=[],
    special=[],
    index="jug-or-pitcher",
    name="Jug or pitcher",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "cp"),
    weight=4,
    url="/api/2014/equipment/jug-or-pitcher",
    contents=[],
    properties=[]
)

# Keelboat = cs.Item(
#     desc=[],
#     special=[],
#     index="keelboat",
#     name="Keelboat",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(3000, "gp"),
#     weight=0,
#     url="/api/2014/equipment/keelboat",
#     contents=[],
#     properties=[]
# )

Ladder_10_foot = cs.Item(
    desc=[],
    special=[],
    index="ladder-10-foot",
    name="Ladder (10-foot)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "sp"),
    weight=25,
    url="/api/2014/equipment/ladder-10-foot",
    contents=[],
    properties=[]
)

Lamp = cs.Item(
    desc=[],
    special=[],
    index="lamp",
    name="Lamp",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "sp"),
    weight=1,
    url="/api/2014/equipment/lamp",
    contents=[],
    properties=[]
)

Lance = cs.Weapon(
    desc=[],
    special=[],
    index="lance",
    name="Lance",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=6,
    url="/api/2014/equipment/lance",
    contents=[],
    properties=[
        cs.APIObject("reach", "Reach", "/api/2014/weapon-properties/reach"),
        cs.APIObject("special", "Special", "/api/2014/weapon-properties/special")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d12"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 5}
)

Lantern_bullseye = cs.Item(
    desc=[],
    special=[],
    index="lantern-bullseye",
    name="Lantern, bullseye",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(10, "gp"),
    weight=2,
    url="/api/2014/equipment/lantern-bullseye",
    contents=[],
    properties=[]
)

Lantern_hooded = cs.Item(
    desc=[],
    special=[],
    index="lantern-hooded",
    name="Lantern, hooded",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "gp"),
    weight=2,
    url="/api/2014/equipment/lantern-hooded",
    contents=[],
    properties=[]
)

Leather_Armor = cs.Armour(
    desc=[],
    special=[],
    index="leather-armor",
    name="Leather Armor",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=10,
    url="/api/2014/equipment/leather-armor",
    contents=[],
    properties=[],
    armor_category="Light",
    armor_class=cs.ArmourClass(11, True, None),
    str_minimum=0,
    stealth_disadvantage=False
)

Leatherworkers_Tools = cs.Item(
    desc=[],
    special=[],
    index="leatherworkers-tools",
    name="Leatherworker's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(5, "gp"),
    weight=5,
    url="/api/2014/equipment/leatherworkers-tools",
    contents=[],
    properties=[]
)

Light_hammer = cs.Weapon(
    desc=[],
    special=[],
    index="light-hammer",
    name="Light hammer",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(2, "gp"),
    weight=2,
    url="/api/2014/equipment/light-hammer",
    contents=[],
    properties=[
        cs.APIObject("light", "Light", "/api/2014/weapon-properties/light"),
        cs.APIObject("thrown", "Thrown", "/api/2014/weapon-properties/thrown"),
        cs.APIObject("monk", "Monk", "/api/2014/weapon-properties/monk")
    ],
    weapon_category="Simple",
    weapon_range="Melee",
    category_range="Simple Melee",
    damage=cs.Damage(cs.Dice.translate("1d4"), cs.APIObject("bludgeoning", "Bludgeoning", "/api/2014/damage-types/bludgeoning")),
    range={"normal": 5}
)

Little_bag_of_sand = cs.Item(
    desc=[],
    special=[],
    index="little-bag-of-sand",
    name="Little bag of sand",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(0, "cp"),
    weight=0,
    url="/api/2014/equipment/little-bag-of-sand",
    contents=[],
    properties=[]
)

Lock = cs.Item(
    desc=[],
    special=[],
    index="lock",
    name="Lock",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(10, "gp"),
    weight=1,
    url="/api/2014/equipment/lock",
    contents=[],
    properties=[]
)

Longbow = cs.Weapon(
    desc=[],
    special=[],
    index="longbow",
    name="Longbow",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(50, "gp"),
    weight=2,
    url="/api/2014/equipment/longbow",
    contents=[],
    properties=[
        cs.APIObject("ammunition", "Ammunition", "/api/2014/weapon-properties/ammunition"),
        cs.APIObject("heavy", "Heavy", "/api/2014/weapon-properties/heavy"),
        cs.APIObject("two-handed", "Two-Handed", "/api/2014/weapon-properties/two-handed")
    ],
    weapon_category="Martial",
    weapon_range="Ranged",
    category_range="Martial Ranged",
    damage=cs.Damage(cs.Dice.translate("1d8"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 150}
)

# Longship = cs.Item(
#     desc=[],
#     special=[],
#     index="longship",
#     name="Longship",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(10000, "gp"),
#     weight=0,
#     url="/api/2014/equipment/longship",
#     contents=[],
#     properties=[]
# )

Longsword = cs.Weapon(
    desc=[],
    special=[],
    index="longsword",
    name="Longsword",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(15, "gp"),
    weight=3,
    url="/api/2014/equipment/longsword",
    contents=[],
    properties=[
        cs.APIObject("versatile", "Versatile", "/api/2014/weapon-properties/versatile")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d8"), cs.APIObject("slashing", "Slashing", "/api/2014/damage-types/slashing")),
    range={"normal": 5}
)

Lute = cs.Item(
    desc=[],
    special=[],
    index="lute",
    name="Lute",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(35, "gp"),
    weight=2,
    url="/api/2014/equipment/lute",
    contents=[],
    properties=[]
)

Lyre = cs.Item(
    desc=[],
    special=[],
    index="lyre",
    name="Lyre",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(30, "gp"),
    weight=2,
    url="/api/2014/equipment/lyre",
    contents=[],
    properties=[]
)

Mace = cs.Weapon(
    desc=[],
    special=[],
    index="mace",
    name="Mace",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(5, "gp"),
    weight=4,
    url="/api/2014/equipment/mace",
    contents=[],
    properties=[
        cs.APIObject("monk", "Monk", "/api/2014/weapon-properties/monk")
    ],
    weapon_category="Simple",
    weapon_range="Melee",
    category_range="Simple Melee",
    damage=cs.Damage(cs.Dice.translate("1d6"), cs.APIObject("bludgeoning", "Bludgeoning", "/api/2014/damage-types/bludgeoning")),
    range={"normal": 5}
)

Magnifying_glass = cs.Item(
    desc=[],
    special=[],
    index="magnifying-glass",
    name="Magnifying glass",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(100, "gp"),
    weight=0,
    url="/api/2014/equipment/magnifying-glass",
    contents=[],
    properties=[]
)

Manacles = cs.Item(
    desc=[],
    special=[],
    index="manacles",
    name="Manacles",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=6,
    url="/api/2014/equipment/manacles",
    contents=[],
    properties=[]
)

Masons_Tools = cs.Item(
    desc=[],
    special=[],
    index="masons-tools",
    name="Mason's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=8,
    url="/api/2014/equipment/masons-tools",
    contents=[],
    properties=[]
)

# Mastiff = cs.Item(
#     desc=[],
#     special=[],
#     index="mastiff",
#     name="Mastiff",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(25, "gp"),
#     weight=0,
#     url="/api/2014/equipment/mastiff",
#     contents=[],
#     properties=[]
# )

Maul = cs.Weapon(
    desc=[],
    special=[],
    index="maul",
    name="Maul",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=10,
    url="/api/2014/equipment/maul",
    contents=[],
    properties=[
        cs.APIObject("heavy", "Heavy", "/api/2014/weapon-properties/heavy"),
        cs.APIObject("two-handed", "Two-Handed", "/api/2014/weapon-properties/two-handed")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("2d6"), cs.APIObject("bludgeoning", "Bludgeoning", "/api/2014/damage-types/bludgeoning")),
    range={"normal": 5}
)

Mess_Kit = cs.Item(
    desc=[],
    special=[],
    index="mess-kit",
    name="Mess Kit",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("kits", "Kits", "/api/2014/equipment-categories/kits"),
    cost=cs.Cost(2, "sp"),
    weight=1,
    url="/api/2014/equipment/mess-kit",
    contents=[],
    properties=[]
)

Mirror_steel = cs.Item(
    desc=[],
    special=[],
    index="mirror-steel",
    name="Mirror, steel",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "gp"),
    weight=0.5,
    url="/api/2014/equipment/mirror-steel",
    contents=[],
    properties=[]
)

Morningstar = cs.Weapon(
    desc=[],
    special=[],
    index="morningstar",
    name="Morningstar",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(15, "gp"),
    weight=4,
    url="/api/2014/equipment/morningstar",
    contents=[],
    properties=[
        
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d8"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 5}
)

# Mule = cs.Item(
#     desc=[],
#     special=[],
#     index="mule",
#     name="Mule",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(8, "gp"),
#     weight=0,
#     url="/api/2014/equipment/mule",
#     contents=[],
#     properties=[]
# )

Navigators_Tools = cs.Item(
    desc=[],
    special=[],
    index="navigators-tools",
    name="Navigator's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(25, "gp"),
    weight=2,
    url="/api/2014/equipment/navigators-tools",
    contents=[],
    properties=[]
)

Oil_flask = cs.Item(
    desc=[],
    special=[],
    index="oil-flask",
    name="Oil (flask)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "sp"),
    weight=1,
    url="/api/2014/equipment/oil-flask",
    contents=[],
    properties=[]
)

Orb = cs.Item(
    desc=[],
    special=[],
    index="orb",
    name="Orb",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("arcane-foci", "Arcane Foci", "/api/2014/equipment-categories/arcane-foci"),
    cost=cs.Cost(20, "gp"),
    weight=3,
    url="/api/2014/equipment/orb",
    contents=[],
    properties=[]
)

Padded_Armor = cs.Armour(
    desc=[],
    special=[],
    index="padded-armor",
    name="Padded Armor",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(5, "gp"),
    weight=8,
    url="/api/2014/equipment/padded-armor",
    contents=[],
    properties=[],
    armor_category="Light",
    armor_class=cs.ArmourClass(11, True, None),
    str_minimum=0,
    stealth_disadvantage=True
)

Painters_Supplies = cs.Item(
    desc=[],
    special=[],
    index="painters-supplies",
    name="Painter's Supplies",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=5,
    url="/api/2014/equipment/painters-supplies",
    contents=[],
    properties=[]
)

Pan_flute = cs.Item(
    desc=[],
    special=[],
    index="pan-flute",
    name="Pan flute",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(12, "gp"),
    weight=2,
    url="/api/2014/equipment/pan-flute",
    contents=[],
    properties=[]
)

Paper_one_sheet = cs.Item(
    desc=[],
    special=[],
    index="paper-one-sheet",
    name="Paper (one sheet)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "sp"),
    weight=0,
    url="/api/2014/equipment/paper-one-sheet",
    contents=[],
    properties=[]
)

Parchment_one_sheet = cs.Item(
    desc=[],
    special=[],
    index="parchment-one-sheet",
    name="Parchment (one sheet)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "sp"),
    weight=0,
    url="/api/2014/equipment/parchment-one-sheet",
    contents=[],
    properties=[]
)

Perfume_vial = cs.Item(
    desc=[],
    special=[],
    index="perfume-vial",
    name="Perfume (vial)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "gp"),
    weight=0,
    url="/api/2014/equipment/perfume-vial",
    contents=[],
    properties=[]
)

Pick_miners = cs.Item(
    desc=[],
    special=[],
    index="pick-miners",
    name="Pick, miner's",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=10,
    url="/api/2014/equipment/pick-miners",
    contents=[],
    properties=[]
)

Pike = cs.Weapon(
    desc=[],
    special=[],
    index="pike",
    name="Pike",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(5, "gp"),
    weight=18,
    url="/api/2014/equipment/pike",
    contents=[],
    properties=[
        cs.APIObject("heavy", "Heavy", "/api/2014/weapon-properties/heavy"),
        cs.APIObject("reach", "Reach", "/api/2014/weapon-properties/reach"),
        cs.APIObject("two-handed", "Two-Handed", "/api/2014/weapon-properties/two-handed")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d10"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 5}
)

Piton = cs.Item(
    desc=[],
    special=[],
    index="piton",
    name="Piton",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "cp"),
    weight=0.25,
    url="/api/2014/equipment/piton",
    contents=[],
    properties=[]
)

Plate_Armor = cs.Armour(
    desc=[],
    special=[],
    index="plate-armor",
    name="Plate Armor",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(1500, "gp"),
    weight=65,
    url="/api/2014/equipment/plate-armor",
    contents=[],
    properties=[],
    armor_category="Heavy",
    armor_class=cs.ArmourClass(18, False, None),
    str_minimum=15,
    stealth_disadvantage=True
)

Playing_Card_Set = cs.Item(
    desc=[],
    special=[],
    index="playing-card-set",
    name="Playing Card Set",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(5, "sp"),
    weight=0,
    url="/api/2014/equipment/playing-card-set",
    contents=[],
    properties=[]
)

Poison_basic_vial = cs.Item(
    desc=[],
    special=[],
    index="poison-basic-vial",
    name="Poison, basic (vial)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(100, "gp"),
    weight=0,
    url="/api/2014/equipment/poison-basic-vial",
    contents=[],
    properties=[]
)

Poisoners_Kit = cs.Item(
    desc=[],
    special=[],
    index="poisoners-kit",
    name="Poisoner's Kit",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("kits", "Kits", "/api/2014/equipment-categories/kits"),
    cost=cs.Cost(50, "gp"),
    weight=2,
    url="/api/2014/equipment/poisoners-kit",
    contents=[],
    properties=[]
)

Pole_10_foot = cs.Item(
    desc=[],
    special=[],
    index="pole-10-foot",
    name="Pole (10-foot)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "cp"),
    weight=7,
    url="/api/2014/equipment/pole-10-foot",
    contents=[],
    properties=[]
)

# Pony = cs.Item(
#     desc=[],
#     special=[],
#     index="pony",
#     name="Pony",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(30, "gp"),
#     weight=0,
#     url="/api/2014/equipment/pony",
#     contents=[],
#     properties=[]
# )

Pot_iron = cs.Item(
    desc=[],
    special=[],
    index="pot-iron",
    name="Pot, iron",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=10,
    url="/api/2014/equipment/pot-iron",
    contents=[],
    properties=[]
)

Potters_Tools = cs.Item(
    desc=[],
    special=[],
    index="potters-tools",
    name="Potter's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=3,
    url="/api/2014/equipment/potters-tools",
    contents=[],
    properties=[]
)

Pouch = cs.Item(
    desc=[],
    special=[],
    index="pouch",
    name="Pouch",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "sp"),
    weight=1,
    url="/api/2014/equipment/pouch",
    contents=[],
    properties=[]
)

Priests_Pack = cs.Item(
    desc=[],
    special=[],
    index="priests-pack",
    name="Priest's Pack",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("equipment-packs", "Equipment Packs", "/api/2014/equipment-categories/equipment-packs"),
    cost=cs.Cost(19, "gp"),
    weight=0,
    url="/api/2014/equipment/priests-pack",
    contents=[],
    properties=[]
)

Quarterstaff = cs.Weapon(
    desc=[],
    special=[],
    index="quarterstaff",
    name="Quarterstaff",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(2, "sp"),
    weight=4,
    url="/api/2014/equipment/quarterstaff",
    contents=[],
    properties=[
        cs.APIObject("versatile", "Versatile", "/api/2014/weapon-properties/versatile"),
        cs.APIObject("monk", "Monk", "/api/2014/weapon-properties/monk")
    ],
    weapon_category="Simple",
    weapon_range="Melee",
    category_range="Simple Melee",
    damage=cs.Damage(cs.Dice.translate("1d6"), cs.APIObject("bludgeoning", "Bludgeoning", "/api/2014/damage-types/bludgeoning")),
    range={"normal": 5}
)

Quiver = cs.Item(
    desc=[],
    special=[],
    index="quiver",
    name="Quiver",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=1,
    url="/api/2014/equipment/quiver",
    contents=[],
    properties=[]
)

Ram_portable = cs.Item(
    desc=[],
    special=[],
    index="ram-portable",
    name="Ram, portable",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(4, "gp"),
    weight=35,
    url="/api/2014/equipment/ram-portable",
    contents=[],
    properties=[]
)

Rapier = cs.Weapon(
    desc=[],
    special=[],
    index="rapier",
    name="Rapier",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(25, "gp"),
    weight=2,
    url="/api/2014/equipment/rapier",
    contents=[],
    properties=[
        cs.APIObject("finesse", "Finesse", "/api/2014/weapon-properties/finesse")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d8"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 5}
)

Rations_1_day = cs.Item(
    desc=[],
    special=[],
    index="rations-1-day",
    name="Rations (1 day)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "sp"),
    weight=2,
    url="/api/2014/equipment/rations-1-day",
    contents=[],
    properties=[]
)

Reliquary = cs.Item(
    desc=[],
    special=[],
    index="reliquary",
    name="Reliquary",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("holy-symbols", "Holy Symbols", "/api/2014/equipment-categories/holy-symbols"),
    cost=cs.Cost(5, "gp"),
    weight=2,
    url="/api/2014/equipment/reliquary",
    contents=[],
    properties=[]
)

Ring_Mail = cs.Armour(
    desc=[],
    special=[],
    index="ring-mail",
    name="Ring Mail",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(30, "gp"),
    weight=40,
    url="/api/2014/equipment/ring-mail",
    contents=[],
    properties=[],
    armor_category="Heavy",
    armor_class=cs.ArmourClass(14, False, None),
    str_minimum=0,
    stealth_disadvantage=True
)

Robes = cs.Item(
    desc=[],
    special=[],
    index="robes",
    name="Robes",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=4,
    url="/api/2014/equipment/robes",
    contents=[],
    properties=[]
)

Rod = cs.Item(
    desc=[],
    special=[],
    index="rod",
    name="Rod",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("arcane-foci", "Arcane Foci", "/api/2014/equipment-categories/arcane-foci"),
    cost=cs.Cost(10, "gp"),
    weight=2,
    url="/api/2014/equipment/rod",
    contents=[],
    properties=[]
)

Rope_hempen_50_feet = cs.Item(
    desc=[],
    special=[],
    index="rope-hempen-50-feet",
    name="Rope, hempen (50 feet)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=10,
    url="/api/2014/equipment/rope-hempen-50-feet",
    contents=[],
    properties=[]
)

Rope_silk_50_feet = cs.Item(
    desc=[],
    special=[],
    index="rope-silk-50-feet",
    name="Rope, silk (50 feet)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(10, "gp"),
    weight=5,
    url="/api/2014/equipment/rope-silk-50-feet",
    contents=[],
    properties=[]
)

# Rowboat = cs.Item(
#     desc=[],
#     special=[],
#     index="rowboat",
#     name="Rowboat",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(50, "gp"),
#     weight=0,
#     url="/api/2014/equipment/rowboat",
#     contents=[],
#     properties=[]
# )

Sack = cs.Item(
    desc=[],
    special=[],
    index="sack",
    name="Sack",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "cp"),
    weight=0.5,
    url="/api/2014/equipment/sack",
    contents=[],
    properties=[]
)

# Saddle_Exotic = cs.Item(
#     desc=[],
#     special=[],
#     index="saddle-exotic",
#     name="Saddle, Exotic",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(60, "gp"),
#     weight=50,
#     url="/api/2014/equipment/saddle-exotic",
#     contents=[],
#     properties=[]
# )

# Saddle_Military = cs.Item(
#     desc=[],
#     special=[],
#     index="saddle-military",
#     name="Saddle, Military",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(20, "gp"),
#     weight=30,
#     url="/api/2014/equipment/saddle-military",
#     contents=[],
#     properties=[]
# )

# Saddle_Pack = cs.Item(
#     desc=[],
#     special=[],
#     index="saddle-pack",
#     name="Saddle, Pack",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(5, "gp"),
#     weight=15,
#     url="/api/2014/equipment/saddle-pack",
#     contents=[],
#     properties=[]
# )

# Saddle_Riding = cs.Item(
#     desc=[],
#     special=[],
#     index="saddle-riding",
#     name="Saddle, Riding",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(10, "gp"),
#     weight=25,
#     url="/api/2014/equipment/saddle-riding",
#     contents=[],
#     properties=[]
# )

# Saddlebags = cs.Item(
#     desc=[],
#     special=[],
#     index="saddlebags",
#     name="Saddlebags",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(4, "gp"),
#     weight=8,
#     url="/api/2014/equipment/saddlebags",
#     contents=[],
#     properties=[]
# )

# Sailing_ship = cs.Item(
#     desc=[],
#     special=[],
#     index="sailing-ship",
#     name="Sailing ship",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(10000, "gp"),
#     weight=0,
#     url="/api/2014/equipment/sailing-ship",
#     contents=[],
#     properties=[]
# )

Scale_Mail = cs.Armour(
    desc=[],
    special=[],
    index="scale-mail",
    name="Scale Mail",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(50, "gp"),
    weight=45,
    url="/api/2014/equipment/scale-mail",
    contents=[],
    properties=[],
    armor_category="Medium",
    armor_class=cs.ArmourClass(14, True, 2),
    str_minimum=0,
    stealth_disadvantage=True
)

Scale_merchants = cs.Item(
    desc=[],
    special=[],
    index="scale-merchants",
    name="Scale, merchant's",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "gp"),
    weight=3,
    url="/api/2014/equipment/scale-merchants",
    contents=[],
    properties=[]
)

Scholars_Pack = cs.Item(
    desc=[],
    special=[],
    index="scholars-pack",
    name="Scholar's Pack",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("equipment-packs", "Equipment Packs", "/api/2014/equipment-categories/equipment-packs"),
    cost=cs.Cost(40, "gp"),
    weight=0,
    url="/api/2014/equipment/scholars-pack",
    contents=[],
    properties=[]
)

Scimitar = cs.Weapon(
    desc=[],
    special=[],
    index="scimitar",
    name="Scimitar",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(25, "gp"),
    weight=3,
    url="/api/2014/equipment/scimitar",
    contents=[],
    properties=[
        cs.APIObject("finesse", "Finesse", "/api/2014/weapon-properties/finesse"),
        cs.APIObject("light", "Light", "/api/2014/weapon-properties/light")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d6"), cs.APIObject("slashing", "Slashing", "/api/2014/damage-types/slashing")),
    range={"normal": 5}
)

Sealing_wax = cs.Item(
    desc=[],
    special=[],
    index="sealing-wax",
    name="Sealing wax",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "sp"),
    weight=0,
    url="/api/2014/equipment/sealing-wax",
    contents=[],
    properties=[]
)

Shawm = cs.Item(
    desc=[],
    special=[],
    index="shawm",
    name="Shawm",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(2, "gp"),
    weight=1,
    url="/api/2014/equipment/shawm",
    contents=[],
    properties=[]
)

Shield = cs.Armour(
    desc=[],
    special=[],
    index="shield",
    name="Shield",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=6,
    url="/api/2014/equipment/shield",
    contents=[],
    properties=[],
    armor_category="Shield",
    armor_class=cs.ArmourClass(2, False, None),
    str_minimum=0,
    stealth_disadvantage=False
)

Shortbow = cs.Weapon(
    desc=[],
    special=[],
    index="shortbow",
    name="Shortbow",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(25, "gp"),
    weight=2,
    url="/api/2014/equipment/shortbow",
    contents=[],
    properties=[
        cs.APIObject("ammunition", "Ammunition", "/api/2014/weapon-properties/ammunition"),
        cs.APIObject("two-handed", "Two-Handed", "/api/2014/weapon-properties/two-handed")
    ],
    weapon_category="Simple",
    weapon_range="Ranged",
    category_range="Simple Ranged",
    damage=cs.Damage(cs.Dice.translate("1d6"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 80}
)

Shortsword = cs.Weapon(
    desc=[],
    special=[],
    index="shortsword",
    name="Shortsword",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(10, "gp"),
    weight=2,
    url="/api/2014/equipment/shortsword",
    contents=[],
    properties=[
        cs.APIObject("finesse", "Finesse", "/api/2014/weapon-properties/finesse"),
        cs.APIObject("light", "Light", "/api/2014/weapon-properties/light"),
        cs.APIObject("monk", "Monk", "/api/2014/weapon-properties/monk")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d6"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 5}
)

Shovel = cs.Item(
    desc=[],
    special=[],
    index="shovel",
    name="Shovel",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=5,
    url="/api/2014/equipment/shovel",
    contents=[],
    properties=[]
)

Sickle = cs.Weapon(
    desc=[],
    special=[],
    index="sickle",
    name="Sickle",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(1, "gp"),
    weight=2,
    url="/api/2014/equipment/sickle",
    contents=[],
    properties=[
        cs.APIObject("light", "Light", "/api/2014/weapon-properties/light"),
        cs.APIObject("monk", "Monk", "/api/2014/weapon-properties/monk")
    ],
    weapon_category="Simple",
    weapon_range="Melee",
    category_range="Simple Melee",
    damage=cs.Damage(cs.Dice.translate("1d4"), cs.APIObject("slashing", "Slashing", "/api/2014/damage-types/slashing")),
    range={"normal": 5}
)

Signal_whistle = cs.Item(
    desc=[],
    special=[],
    index="signal-whistle",
    name="Signal whistle",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "cp"),
    weight=0,
    url="/api/2014/equipment/signal-whistle",
    contents=[],
    properties=[]
)

Signet_ring = cs.Item(
    desc=[],
    special=[],
    index="signet-ring",
    name="Signet ring",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "gp"),
    weight=0,
    url="/api/2014/equipment/signet-ring",
    contents=[],
    properties=[]
)

# Sled = cs.Item(
#     desc=[],
#     special=[],
#     index="sled",
#     name="Sled",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(20, "gp"),
#     weight=300,
#     url="/api/2014/equipment/sled",
#     contents=[],
#     properties=[]
# )

Sling = cs.Weapon(
    desc=[],
    special=[],
    index="sling",
    name="Sling",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(1, "sp"),
    weight=0,
    url="/api/2014/equipment/sling",
    contents=[],
    properties=[
        cs.APIObject("ammunition", "Ammunition", "/api/2014/weapon-properties/ammunition")
    ],
    weapon_category="Simple",
    weapon_range="Ranged",
    category_range="Simple Ranged",
    damage=cs.Damage(cs.Dice.translate("1d4"), cs.APIObject("bludgeoning", "Bludgeoning", "/api/2014/damage-types/bludgeoning")),
    range={"normal": 30}
)

Sling_bullet = cs.Item(
    desc=[],
    special=[],
    index="sling-bullet",
    name="Sling bullet",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("ammunition", "Ammunition", "/api/2014/equipment-categories/ammunition"),
    cost=cs.Cost(4, "cp"),
    weight=1.5,
    url="/api/2014/equipment/sling-bullet",
    contents=[],
    properties=[]
)

Small_knife = cs.Item(
    desc=[],
    special=[],
    index="small-knife",
    name="Small knife",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(0, "cp"),
    weight=0,
    url="/api/2014/equipment/small-knife",
    contents=[],
    properties=[]
)

Smiths_Tools = cs.Item(
    desc=[],
    special=[],
    index="smiths-tools",
    name="Smith's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(20, "gp"),
    weight=8,
    url="/api/2014/equipment/smiths-tools",
    contents=[],
    properties=[]
)

Soap = cs.Item(
    desc=[],
    special=[],
    index="soap",
    name="Soap",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "cp"),
    weight=0,
    url="/api/2014/equipment/soap",
    contents=[],
    properties=[]
)

Spear = cs.Weapon(
    desc=[],
    special=[],
    index="spear",
    name="Spear",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(1, "gp"),
    weight=3,
    url="/api/2014/equipment/spear",
    contents=[],
    properties=[
        cs.APIObject("thrown", "Thrown", "/api/2014/weapon-properties/thrown"),
        cs.APIObject("versatile", "Versatile", "/api/2014/weapon-properties/versatile"),
        cs.APIObject("monk", "Monk", "/api/2014/weapon-properties/monk")
    ],
    weapon_category="Simple",
    weapon_range="Melee",
    category_range="Simple Melee",
    damage=cs.Damage(cs.Dice.translate("1d6"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 5}
)

Spellbook = cs.Item(
    desc=[],
    special=[],
    index="spellbook",
    name="Spellbook",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(50, "gp"),
    weight=3,
    url="/api/2014/equipment/spellbook",
    contents=[],
    properties=[]
)

Spike_iron = cs.Item(
    desc=[],
    special=[],
    index="spike-iron",
    name="Spike, iron",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "sp"),
    weight=5,
    url="/api/2014/equipment/spike-iron",
    contents=[],
    properties=[]
)

Splint_Armor = cs.Armour(
    desc=[],
    special=[],
    index="splint-armor",
    name="Splint Armor",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(200, "gp"),
    weight=60,
    url="/api/2014/equipment/splint-armor",
    contents=[],
    properties=[],
    armor_category="Heavy",
    armor_class=cs.ArmourClass(17, False, None),
    str_minimum=15,
    stealth_disadvantage=True
)

Sprig_of_mistletoe = cs.Item(
    desc=[],
    special=[],
    index="sprig-of-mistletoe",
    name="Sprig of mistletoe",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("druidic-foci", "Druidic Foci", "/api/2014/equipment-categories/druidic-foci"),
    cost=cs.Cost(1, "gp"),
    weight=0,
    url="/api/2014/equipment/sprig-of-mistletoe",
    contents=[],
    properties=[]
)

Spyglass = cs.Item(
    desc=[],
    special=[],
    index="spyglass",
    name="Spyglass",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1000, "gp"),
    weight=1,
    url="/api/2014/equipment/spyglass",
    contents=[],
    properties=[]
)

# Stabling_1_day = cs.Item(
#     desc=[],
#     special=[],
#     index="stabling-1-day",
#     name="Stabling (1 day)",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(5, "sp"),
#     weight=0,
#     url="/api/2014/equipment/stabling-1-day",
#     contents=[],
#     properties=[]
# )

Staff = cs.Item(
    desc=[],
    special=[],
    index="staff",
    name="Staff",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("arcane-foci", "Arcane Foci", "/api/2014/equipment-categories/arcane-foci"),
    cost=cs.Cost(5, "gp"),
    weight=4,
    url="/api/2014/equipment/staff",
    contents=[],
    properties=[]
)

String_10_feet = cs.Item(
    desc=[],
    special=[],
    index="string-10-feet",
    name="String (10 feet)",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(0, "cp"),
    weight=0,
    url="/api/2014/equipment/string-10-feet",
    contents=[],
    properties=[]
)

Studded_Leather_Armor = cs.Armour(
    desc=[],
    special=[],
    index="studded-leather-armor",
    name="Studded Leather Armor",
    equipment_category=cs.APIObject("armor", "Armor", "/api/2014/equipment-categories/armor"),
    gear_category=None,
    cost=cs.Cost(45, "gp"),
    weight=13,
    url="/api/2014/equipment/studded-leather-armor",
    contents=[],
    properties=[],
    armor_category="Light",
    armor_class=cs.ArmourClass(12, True, None),
    str_minimum=0,
    stealth_disadvantage=False
)

Tent_two_person = cs.Item(
    desc=[],
    special=[],
    index="tent-two-person",
    name="Tent, two-person",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "gp"),
    weight=20,
    url="/api/2014/equipment/tent-two-person",
    contents=[],
    properties=[]
)

Thieves_Tools = cs.Item(
    desc=[],
    special=[],
    index="thieves-tools",
    name="Thieves' Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(25, "gp"),
    weight=1,
    url="/api/2014/equipment/thieves-tools",
    contents=[],
    properties=[]
)

Tinderbox = cs.Item(
    desc=[],
    special=[],
    index="tinderbox",
    name="Tinderbox",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(5, "sp"),
    weight=1,
    url="/api/2014/equipment/tinderbox",
    contents=[],
    properties=[]
)

Tinkers_Tools = cs.Item(
    desc=[],
    special=[],
    index="tinkers-tools",
    name="Tinker's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(50, "gp"),
    weight=10,
    url="/api/2014/equipment/tinkers-tools",
    contents=[],
    properties=[]
)

Torch = cs.Item(
    desc=[],
    special=[],
    index="torch",
    name="Torch",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "cp"),
    weight=1,
    url="/api/2014/equipment/torch",
    contents=[],
    properties=[]
)

Totem = cs.Item(
    desc=[],
    special=[],
    index="totem",
    name="Totem",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("druidic-foci", "Druidic Foci", "/api/2014/equipment-categories/druidic-foci"),
    cost=cs.Cost(1, "gp"),
    weight=0,
    url="/api/2014/equipment/totem",
    contents=[],
    properties=[]
)

Trident = cs.Weapon(
    desc=[],
    special=[],
    index="trident",
    name="Trident",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(5, "gp"),
    weight=4,
    url="/api/2014/equipment/trident",
    contents=[],
    properties=[
        cs.APIObject("thrown", "Thrown", "/api/2014/weapon-properties/thrown"),
        cs.APIObject("versatile", "Versatile", "/api/2014/weapon-properties/versatile")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d6"), cs.APIObject("slashing", "Slashing", "/api/2014/damage-types/slashing")),
    range={"normal": 5}
)

Vestments = cs.Item(
    desc=[],
    special=[],
    index="vestments",
    name="Vestments",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(0, "cp"),
    weight=0,
    url="/api/2014/equipment/vestments",
    contents=[],
    properties=[]
)

Vial = cs.Item(
    desc=[],
    special=[],
    index="vial",
    name="Vial",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "gp"),
    weight=0,
    url="/api/2014/equipment/vial",
    contents=[],
    properties=[]
)

Viol = cs.Item(
    desc=[],
    special=[],
    index="viol",
    name="Viol",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(30, "gp"),
    weight=1,
    url="/api/2014/equipment/viol",
    contents=[],
    properties=[]
)

# Wagon = cs.Item(
#     desc=[],
#     special=[],
#     index="wagon",
#     name="Wagon",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(35, "gp"),
#     weight=400,
#     url="/api/2014/equipment/wagon",
#     contents=[],
#     properties=[]
# )

Wand = cs.Item(
    desc=[],
    special=[],
    index="wand",
    name="Wand",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("arcane-foci", "Arcane Foci", "/api/2014/equipment-categories/arcane-foci"),
    cost=cs.Cost(10, "gp"),
    weight=1,
    url="/api/2014/equipment/wand",
    contents=[],
    properties=[]
)

War_pick = cs.Weapon(
    desc=[],
    special=[],
    index="war-pick",
    name="War pick",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(5, "gp"),
    weight=2,
    url="/api/2014/equipment/war-pick",
    contents=[],
    properties=[
        
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d8"), cs.APIObject("piercing", "Piercing", "/api/2014/damage-types/piercing")),
    range={"normal": 5}
)

Warhammer = cs.Weapon(
    desc=[],
    special=[],
    index="warhammer",
    name="Warhammer",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(15, "gp"),
    weight=2,
    url="/api/2014/equipment/warhammer",
    contents=[],
    properties=[
        cs.APIObject("versatile", "Versatile", "/api/2014/weapon-properties/versatile")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d8"), cs.APIObject("bludgeoning", "Bludgeoning", "/api/2014/damage-types/bludgeoning")),
    range={"normal": 5}
)

# Warhorse = cs.Item(
#     desc=[],
#     special=[],
#     index="warhorse",
#     name="Warhorse",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(400, "gp"),
#     weight=0,
#     url="/api/2014/equipment/warhorse",
#     contents=[],
#     properties=[]
# )

# Warship = cs.Item(
#     desc=[],
#     special=[],
#     index="warship",
#     name="Warship",
#     equipment_category=cs.APIObject("mounts-and-vehicles", "Mounts and Vehicles", "/api/2014/equipment-categories/mounts-and-vehicles"),
#     gear_category=None,
#     cost=cs.Cost(25000, "gp"),
#     weight=0,
#     url="/api/2014/equipment/warship",
#     contents=[],
#     properties=[]
# )

Waterskin = cs.Item(
    desc=[],
    special=[],
    index="waterskin",
    name="Waterskin",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(2, "sp"),
    weight=5,
    url="/api/2014/equipment/waterskin",
    contents=[],
    properties=[]
)

Weavers_Tools = cs.Item(
    desc=[],
    special=[],
    index="weavers-tools",
    name="Weaver's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(1, "gp"),
    weight=5,
    url="/api/2014/equipment/weavers-tools",
    contents=[],
    properties=[]
)

Whetstone = cs.Item(
    desc=[],
    special=[],
    index="whetstone",
    name="Whetstone",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("standard-gear", "Standard Gear", "/api/2014/equipment-categories/standard-gear"),
    cost=cs.Cost(1, "cp"),
    weight=1,
    url="/api/2014/equipment/whetstone",
    contents=[],
    properties=[]
)

Whip = cs.Weapon(
    desc=[],
    special=[],
    index="whip",
    name="Whip",
    equipment_category=cs.APIObject("weapon", "Weapon", "/api/2014/equipment-categories/weapon"),
    gear_category=None,
    cost=cs.Cost(2, "gp"),
    weight=3,
    url="/api/2014/equipment/whip",
    contents=[],
    properties=[
        cs.APIObject("finesse", "Finesse", "/api/2014/weapon-properties/finesse"),
        cs.APIObject("reach", "Reach", "/api/2014/weapon-properties/reach")
    ],
    weapon_category="Martial",
    weapon_range="Melee",
    category_range="Martial Melee",
    damage=cs.Damage(cs.Dice.translate("1d4"), cs.APIObject("slashing", "Slashing", "/api/2014/damage-types/slashing")),
    range={"normal": 5}
)

Woodcarvers_Tools = cs.Item(
    desc=[],
    special=[],
    index="woodcarvers-tools",
    name="Woodcarver's Tools",
    equipment_category=cs.APIObject("tools", "Tools", "/api/2014/equipment-categories/tools"),
    gear_category=None,
    cost=cs.Cost(1, "gp"),
    weight=5,
    url="/api/2014/equipment/woodcarvers-tools",
    contents=[],
    properties=[]
)

Wooden_staff = cs.Item(
    desc=[],
    special=[],
    index="wooden-staff",
    name="Wooden staff",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("druidic-foci", "Druidic Foci", "/api/2014/equipment-categories/druidic-foci"),
    cost=cs.Cost(5, "gp"),
    weight=4,
    url="/api/2014/equipment/wooden-staff",
    contents=[],
    properties=[]
)

Yew_wand = cs.Item(
    desc=[],
    special=[],
    index="yew-wand",
    name="Yew wand",
    equipment_category=cs.APIObject("adventuring-gear", "Adventuring Gear", "/api/2014/equipment-categories/adventuring-gear"),
    gear_category=cs.APIObject("druidic-foci", "Druidic Foci", "/api/2014/equipment-categories/druidic-foci"),
    cost=cs.Cost(10, "gp"),
    weight=1,
    url="/api/2014/equipment/yew-wand",
    contents=[],
    properties=[]
)

items = [
    Abacus,
    Acid_Vial,
    Alchemists_Fire_Flask,
    Alchemists_Supplies,
    Alms_box,
    Amulet,
    Antitoxin_vial,
    Arrow,
    Backpack,
    Bagpipes,
    Ball_bearings_bag_of_1000,
    Barrel,
    Basket,
    Battleaxe,
    Bedroll,
    Bell,
    Blanket,
    Block_and_tackle,
    Block_of_incense,
    Blowgun,
    Blowgun_needle,
    Book,
    Bottle_glass,
    Breastplate,
    Brewers_Supplies,
    Bucket,
    Burglars_Pack,
    Calligraphers_Supplies,
    Caltrops,
    Candle,
    Carpenters_Tools,
    Cartographers_Tools,
    Case_crossbow_bolt,
    Case_map_or_scroll,
    Censer,
    Chain_10_feet,
    Chain_Mail,
    Chain_Shirt,
    Chalk_1_piece,
    Chest,
    Climbers_Kit,
    Clothes_common,
    Clothes_costume,
    Clothes_fine,
    Clothes_travelers,
    Club,
    Cobblers_Tools,
    Component_pouch,
    Cooks_utensils,
    Crossbow_bolt,
    Crossbow_hand,
    Crossbow_heavy,
    Crossbow_light,
    Crowbar,
    Crystal,
    Dagger,
    Dart,
    Diplomats_Pack,
    Disguise_Kit,
    Drum,
    Dulcimer,
    Dungeoneers_Pack,
    Emblem,
    Entertainers_Pack,
    Explorers_Pack,
    Fishing_tackle,
    Flail,
    Flask_or_tankard,
    Flute,
    Forgery_Kit,
    Glaive,
    Glassblowers_Tools,
    Grappling_hook,
    Greataxe,
    Greatclub,
    Greatsword,
    Halberd,
    Half_Plate_Armor,
    Hammer,
    Hammer_sledge,
    Handaxe,
    Healers_Kit,
    Herbalism_Kit,
    Hide_Armor,
    Holy_water_flask,
    Horn,
    Hourglass,
    Hunting_trap,
    Ink_1_ounce_bottle,
    Ink_pen,
    Javelin,
    Jewelers_Tools,
    Jug_or_pitcher,
    Ladder_10_foot,
    Lamp,
    Lance,
    Lantern_bullseye,
    Lantern_hooded,
    Leather_Armor,
    Leatherworkers_Tools,
    Light_hammer,
    Little_bag_of_sand,
    Lock,
    Longbow,
    Longsword,
    Lute,
    Lyre,
    Mace,
    Magnifying_glass,
    Manacles,
    Masons_Tools,
    Maul,
    Mess_Kit,
    Mirror_steel,
    Morningstar,
    Navigators_Tools,
    Oil_flask,
    Orb,
    Padded_Armor,
    Painters_Supplies,
    Pan_flute,
    Paper_one_sheet,
    Parchment_one_sheet,
    Perfume_vial,
    Pick_miners,
    Pike,
    Piton,
    Plate_Armor,
    Playing_Card_Set,
    Poison_basic_vial,
    Poisoners_Kit,
    Pole_10_foot,
    Pot_iron,
    Potters_Tools,
    Pouch,
    Priests_Pack,
    Quarterstaff,
    Quiver,
    Ram_portable,
    Rapier,
    Rations_1_day,
    Reliquary,
    Ring_Mail,
    Robes,
    Rod,
    Rope_hempen_50_feet,
    Rope_silk_50_feet,
    Sack,
    Scale_Mail,
    Scale_merchants,
    Scholars_Pack,
    Scimitar,
    Sealing_wax,
    Shawm,
    Shield,
    Shortbow,
    Shortsword,
    Shovel,
    Sickle,
    Signal_whistle,
    Signet_ring,
    Sling,
    Sling_bullet,
    Small_knife,
    Smiths_Tools,
    Soap,
    Spear,
    Spellbook,
    Spike_iron,
    Splint_Armor,
    Sprig_of_mistletoe,
    Spyglass,
    Staff,
    String_10_feet,
    Studded_Leather_Armor,
    Tent_two_person,
    Thieves_Tools,
    Tinderbox,
    Tinkers_Tools,
    Torch,
    Totem,
    Trident,
    Vestments,
    Vial,
    Viol,
    Wand,
    War_pick,
    Warhammer,
    Waterskin,
    Weavers_Tools,
    Whetstone,
    Whip,
    Woodcarvers_Tools,
    Wooden_staff,
    Yew_wand
]