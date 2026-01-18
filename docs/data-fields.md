# HOUSE DOCUMENTATION APP – DATA FIELDS

> This document lists the **main data entities and fields**, covering your full domain (sections 1–22).  
> Types are indicative only (string, integer, boolean, date, enum, text, etc.).

---

## 1. Base House Information (Section 1)

### 1.1 House

- `id`
- `address` (string)
- `year_of_construction` (integer)
- `total_built_area_sqm` (float, optional)
- `number_of_floors` (integer)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 2. People Involved (Section 2)

### 2.1 Person

- `id`
- `house_id` (FK → House)
- `name` (string)
- `role` (enum/string: contractor_builder, architect, structural_engineer, plumbing_engineer, electrical_engineer, interior_designer, project_manager, other)
- `custom_role_label` (string, optional, for “other”)
- `company` (string, optional)
- `phone` (string, optional)
- `email` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 3. Bureaucracy, Permits & Legal Documents (Section 3)

### 3.1 BureaucraticDocument (File Metadata)

- `id`
- `house_id` (FK → House)
- `file_url_or_path` (string)
- `file_type` (enum/string: building_permit, municipality_approval, occupancy_approval, compliance_certificate, insurance_document, general_warranty, contract_agreement, other)
- `description` (string, optional)
- `date` (date, optional)
- `related_authority` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 4. Plans, Schematics & Layouts (Section 4)

### 4.1 PlanDocument

- `id`
- `house_id` (FK → House)
- `file_url_or_path` (string)
- `plan_type` (enum/string: architectural_as_built, structural, plumbing_layout, electrical_layout, hvac_plan, safe_room_plan, low_voltage_plan, other)
- `scope_level` (enum: house, floor, room)
- `floor` (integer, optional)
- `room_id` (FK → Room, optional)
- `version` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 5. Room System (Section 5)

### 5.1 RoomType

- `id`
- `house_id` (FK → House)
- `type_key` (enum/string: living_room, bedroom, kitchen, bathroom, toilet, laundry_room, safe_room, storage, basement, balcony, garden, roof, hallway, office, other)
- `enabled` (boolean)
- `custom_label` (string, optional, used if type_key = other)
- `created_at` (datetime)
- `updated_at` (datetime)

### 5.2 Room

- `id`
- `house_id` (FK → House)
- `room_type_id` (FK → RoomType)
- `name` (string, e.g. “Bedroom 1”)
- `floor` (integer, optional)
- `area_sqm` (float, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 6. Plumbing System (Section 6)

### 6.1 PlumbingSystem (House-Level)

- `id`
- `house_id` (FK → House)
- `main_water_inlet_location` (string, optional)
- `shutoff_valves_locations` (text, optional)
- `pipe_material_types` (text or JSON array, optional)
- `drainage_system_description` (text, optional)
- `water_heater_type` (enum/string: electric, gas, solar, heat_pump, other, optional)
- `water_heater_model` (string, optional)
- `water_heater_serial` (string, optional)
- `solar_or_heat_pump_details` (text, optional)
- `water_filtration_system_details` (text, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

### 6.2 PlumbingFixture (Room-Linked)

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room)
- `fixture_type` (enum: sink, toilet, shower, bathtub, washing_machine_connection, other)
- `model` (string, optional)
- `manufacturer` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 7. Electrical System (Section 7)

### 7.1 ElectricalSystem (House-Level)

- `id`
- `house_id` (FK → House)
- `main_panel_location` (string, optional)
- `circuits_list` (text or JSON, optional)
- `breaker_ratings` (text or JSON, optional)
- `grounding_system_notes` (text, optional)
- `has_smart_systems` (boolean)
- `smart_systems_notes` (text, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

### 7.2 ElectricalPoint (Room-Linked)

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room)
- `point_type` (enum: outlet, switch, special_power_point, other)
- `description` (string, optional)  // e.g. “oven 220V”, “data + power”
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 8. Lighting (Section 8)

### 8.1 LightingFixture (Room-Linked)

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room)
- `light_type` (enum: ceiling, wall, spot, outdoor, other)
- `fixture_model` (string, optional)
- `manufacturer` (string, optional)
- `wattage` (float, optional)
- `color_temperature` (string, optional, e.g. “3000K”)
- `dimmable` (boolean)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 9. Paint & Wall Finishes (Section 9)

### 9.1 PaintSpec (Per Room & Surface)

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room)
- `surface` (enum: walls, ceiling, feature_wall, other)
- `paint_brand` (string, optional)
- `series` (string, optional)
- `color_name` (string, optional)
- `color_code` (string, optional)
- `finish_type` (string, optional, e.g. “matte”, “satin”)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 10. Flooring (Section 10)

### 10.1 FlooringSpec (Per Room)

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room)
- `flooring_type` (string/enum, e.g. tile, parquet, vinyl, carpet)
- `material` (string, optional)
- `model_series` (string, optional)
- `size` (string, optional, e.g. “60x60 cm”)
- `finish` (string, optional, e.g. “matte”, “polished”)
- `grout_color` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 11. Wall Coverings & Cladding (Section 11)

### 11.1 WallCovering (Per Room)

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room)
- `covering_type` (enum: tile, decorative_panel, stone, wood, other)
- `material` (string, optional)
- `model` (string, optional)
- `finish` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 12. Doors (Section 12)

### 12.1 Door

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room, optional)
- `door_type` (enum: interior, exterior, other)
- `manufacturer` (string, optional)
- `model` (string, optional)
- `finish` (string, optional)
- `lock_type` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 13. Windows & Openings (Section 13)

### 13.1 WindowOpening

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room)
- `window_type` (string/enum, e.g. sliding, tilt_and_turn, fixed)
- `frame_material` (string, optional, e.g. aluminum, PVC, wood)
- `glass_type` (string, optional, e.g. double_glazed, laminated)
- `manufacturer` (string, optional)
- `insulation_notes` (text, optional)
- `has_shutters` (boolean)
- `has_nets` (boolean)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 14. Kitchen (Section 14)

### 14.1 Kitchen

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room, optional – kitchen room)
- `cabinets_description` (text, optional)
- `countertop_material` (string, optional)
- `countertop_model` (string, optional)
- `sink_model` (string, optional)
- `faucet_model` (string, optional)
- `vent_hood_model` (string, optional)
- `appliances_list` (text/JSON – oven, cooktop, fridge, dishwasher, etc. with models)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 15. Bathrooms & Toilets (Section 15)

### 15.1 BathroomToilet (Per Room)

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room)
- `toilet_model` (string, optional)
- `sink_model` (string, optional)
- `faucet_model` (string, optional)
- `shower_or_bathtub_model` (string, optional)
- `waterproofing_notes` (text, optional)
- `has_washing_machine` (boolean)
- `washing_machine_model` (string, optional)
- `has_dryer` (boolean)
- `dryer_model` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 16. HVAC & Climate (Section 16)

### 16.1 HVACSystem

- `id`
- `house_id` (FK → House)
- `system_type` (enum: central, individual_units)
- `model` (string, optional)
- `capacity` (string/float, optional)
- `manufacturer` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

### 16.2 HVACSystemRoomLink

- `id`
- `hvac_system_id` (FK → HVACSystem)
- `room_id` (FK → Room)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 17. Insulation & Waterproofing (Section 17)

### 17.1 InsulationWaterproofingElement

- `id`
- `house_id` (FK → House)
- `scope_level` (enum: house, floor, room, exterior_area)
- `floor` (integer, optional)
- `room_id` (FK → Room, optional)
- `element_type` (enum: thermal_insulation, acoustic_insulation, bathroom_waterproofing, exterior_waterproofing, other)
- `description` (text, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 18. Safety & Security (Section 18)

### 18.1 SafetySecuritySystem

- `id`
- `house_id` (FK → House)
- `system_type` (enum: alarm_system, cameras, fire_detectors, other)
- `model` (string, optional)
- `manufacturer` (string, optional)
- `description` (text, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

### 18.2 SafeRoom

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room, optional – if safe room is a room)
- `door_type` (string, optional)
- `window_type` (string, optional)
- `standard_compliance_notes` (text, optional, including Israeli residential standards)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 19. Furniture & Built-ins (Section 19)

### 19.1 FurnitureBuiltIn

- `id`
- `house_id` (FK → House)
- `room_id` (FK → Room)
- `item_type` (enum: closet, built_in_shelving, custom_carpentry, other)
- `material` (string, optional)
- `finish` (string, optional)
- `manufacturer` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 20. Service History & Contacts (Section 20)

### 20.1 ServiceProvider

- `id`
- `house_id` (FK → House)
- `provider_type` (enum: plumber, electrician, hvac, general_maintenance, pest_control, other)
- `name` (string)
- `company` (string, optional)
- `phone` (string, optional)
- `email` (string, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

### 20.2 ServiceRecord

- `id`
- `house_id` (FK → House)
- `service_provider_id` (FK → ServiceProvider, optional)
- `date` (date)
- `service_type` (enum: maintenance, repair, pest_control, inspection, other)
- `system_type` (enum/string: plumbing, electrical, hvac, safety, finishes, structure, other, optional)
- `room_id` (FK → Room, optional)
- `description` (text)
- `attached_file_id` (FK → generic File/Document entity, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 21. Photos & Evidence (Section 21)

### 21.1 Photo (or Photo Metadata)

- `id`
- `house_id` (FK → House)
- `file_url_or_path` (string)
- `scope_level` (enum: house, floor, room, system)
- `floor` (integer, optional)
- `room_id` (FK → Room, optional)
- `system_type` (enum/string, optional)
- `photo_type` (enum: pre_closure, plumbing_stage, electrical_stage, waterproofing_stage, final, other)
- `description` (string, optional)
- `date` (date, optional)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## 22. Future-Proofing (Section 22)

### 22.1 FutureProvision

- `id`
- `house_id` (FK → House)
- `scope_level` (enum: house, floor, room, system)
- `floor` (integer, optional)
- `room_id` (FK → Room, optional)
- `system_type` (enum/string, optional)
- `provision_type` (enum: spare_conduit, spare_plumbing_point, expansion_option, load_capacity_limit, other)
- `description` (text)
- `notes` (text, optional)
- `created_at` (datetime)
- `updated_at` (datetime)