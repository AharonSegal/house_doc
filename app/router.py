from fastapi import APIRouter

router = APIRouter()

# =========================
# 1. Main info
# =========================

from app.modules.house.router import router as house_router  # House basic info
from app.modules.people.router import router as people_router  # People involved / contacts
from app.modules.files.router import router as files_router  # Files & permits / schematics

router.include_router(
    house_router,
    prefix="/house",
    tags=["house"]
)  # House basic info: address, size, year, etc.

router.include_router(
    people_router,
    prefix="/people",
    tags=["people"]
)  # People: contractor, architect, interior designer, etc.

router.include_router(
    files_router,
    prefix="/files",
    tags=["files"]
)  # Files: permits, legal docs, schematics, etc.


# =========================
# 2. Advanced / Future (not yet)
# =========================

# from app.modules.plumbing.router import router as plumbing_router  # Plumbing system details
# from app.modules.electrical.router import router as electrical_router  # Electrical system details
# from app.modules.lighting.router import router as lighting_router  # Lighting details per room

# router.include_router(plumbing_router, prefix="/plumbing", tags=["plumbing"])
# router.include_router(electrical_router, prefix="/electrical", tags=["electrical"])
# router.include_router(lighting_router, prefix="/lighting", tags=["lighting"])


# =========================
# 3. House items / materials
# =========================

from app.modules.paint.router import router as paint_router          # Paint & wall finishes
from app.modules.flooring.router import router as flooring_router    # Flooring & tiles
from app.modules.doors_windows.router import router as doors_windows_router  # Doors & windows
from app.modules.appliances.router import router as appliances_router        # Appliances & built-ins

router.include_router(
    paint_router,
    prefix="/paint",
    tags=["paint"]
)  # Paint: interior/exterior, color codes, brand, room mapping

router.include_router(
    flooring_router,
    prefix="/flooring",
    tags=["flooring"]
)  # Flooring: tile name, serial, material, room mapping

router.include_router(
    doors_windows_router,
    prefix="/doors-windows",
    tags=["doors-windows"]
)  # Doors & Windows: models, measurements, hardware, room mapping

router.include_router(
    appliances_router,
    prefix="/appliances",
    tags=["appliances"]
)  # Appliances: washer, dryer, fridge, oven, dishwasher, etc.

# =========================
# 4. Photos & Evidence
# =========================

from app.modules.photos.router import router as photos_router  # Photos & evidence

router.include_router(
    photos_router,
    prefix="/photos",
    tags=["photos"]
)  # Photos: before/after, defects, proof, warranty evidence



# =========================
# 5. Future-proofing (not yet)
# =========================

# from app.modules.future.router import router as future_router  # Future-proofing / upgrades / smart home

# router.include_router(future_router, prefix="/future", tags=["future"])
