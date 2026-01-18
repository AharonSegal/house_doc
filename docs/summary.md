# HOUSE DOCUMENTATION APP – SUMMARY

## 1. What This App Is

The House Documentation App is a **long-term documentation system for a single private house** after construction is completed.  
It is intended as the **single source of truth** for:

- Materials
- Systems
- Fixtures
- Plans
- Bureaucratic and legal documents
- Service and maintenance history
- Photos and visual evidence

The app is **for homeowners**, not professionals. It focuses on:

- Clarity
- Relevance
- Ease of finding answers in the future
- Avoiding clutter and irrelevant data

---

## 2. Core Problem

After a house is built, important information usually ends up:

- Scattered across emails, folders, messages, and paper
- Hard to find years later
- Impossible to understand without “institutional memory”
- Disconnected from real locations in the house

This makes it difficult to:

- Maintain or repair systems
- Coordinate renovations
- Prove compliance and safety
- Provide good information when selling the house

The app solves this by creating **one structured, room-driven, future-proof record** of the entire house.

---

## 3. Key Concepts

### 3.1 Room-Driven Structure

- The user defines **which room types exist** (living room, bedrooms, kitchen, bathrooms, safe room, garden, etc.).
- Only **enabled room types** are created.
- Each room has:
  - Name/label
  - Floor
  - Room type
  - Area (optional)
  - Notes

This **room system controls** what appears everywhere else (plumbing fixtures, lighting, finishes, etc.).  
If a room type is OFF:

- It is not created
- It does not appear in dropdowns or forms
- No fields are generated for it anywhere

### 3.2 Files vs Structured Data

- **Files** = plans, legal docs, photos, evidence.
- **Data** = structured information about physical elements and systems.

Files are treated as **primary documentation**, not “attachments”. They are grouped as:

- Bureaucracy & legal
- Plans & layouts
- Photos & evidence

Files can be linked to:

- Entire house
- Floor
- Room
- System

Each file has a **note for human context**.

---

## 4. Scope (What Is Included)

The app includes:

- **Base House Information**
- **People Involved** in planning and construction
- **Bureaucracy, Permits & Legal Documents** (files only)
- **Plans, Schematics & Layouts** (files + notes)
- **Room System** (room types + room instances)
- Structured data for:
  - Plumbing system + room fixtures
  - Electrical system + room outlets/switches
  - Lighting (per room)
  - Paint & wall finishes (per room)
  - Flooring (per room)
  - Wall coverings & cladding (optional)
  - Doors
  - Windows & openings
  - Kitchen
  - Bathrooms & toilets
  - HVAC & climate systems (house-level + rooms served)
  - Insulation & waterproofing
  - Safety & security (alarm, cameras, fire detection, safe room)
  - Furniture & built-ins
- **Service History & Contacts** (maintenance, repairs, pest control)
- **Photos & Evidence**
- **Future-Proofing Notes** (spare conduits, expansion, load capacity)

---

## 5. Out of Scope (What It Does NOT Do)

The app does **not**:

- Perform design or planning
- Calculate loads, quantities, or costs
- Replace professional CAD/BIM or engineering software
- Force a universal house structure
- Assume the existence of basements, roofs, gardens, balconies, etc.

It is tightly focused on **post-construction documentation for one real house**.

---

## 6. Safety Emphasis

The app gives **special emphasis** to safety:

- Alarm systems
- Fire detectors
- Cameras
- Safe room (including Israeli residential standards)

Safety information is:

- Easy to find
- Clearly labeled
- Separated from cosmetic and less critical data

---

## 7. Typical Usage Scenarios

The app should make it easy to:

- Identify paint color for repainting
- Locate plumbing shutoff valves
- Replace a lighting fixture with the correct model
- Understand which rooms an HVAC unit serves
- Share accurate information with a professional
- Verify compliance or safety documentation (e.g. safe room)
- Review past maintenance, repairs, and pest control work

---

## 8. Long-Term Vision and Success

The app is designed to:

- Stay useful for **decades**
- Outlive the original construction team
- Be understandable by someone who did not build the house
- Act as a **living house record** that grows over time

It is successful if:

- A homeowner can answer **“what is this, where is it, and what do I need to know?”** in minutes
- No irrelevant data is shown
- Information stays clear even years after entry
- The system feels **calm, ordered, and dependable**