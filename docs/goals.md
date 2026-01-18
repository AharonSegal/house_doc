
# HOUSE DOCUMENTATION APP – GOALS

## 1. Primary Product Goals

### 1.1 Single Source of Truth for the House

Build one system that becomes the **authoritative place** for all house information:

- Systems and materials
- Fixtures and finishes
- Plans and legal/bureaucratic documents
- Service history and photos

> Goal: The user does **not** need to search email, WhatsApp, random folders, and binders to understand the house.

---

### 1.2 Fast Answers to “What, Where, What to Know”

Optimize the app for these core questions:

- **What is this?**  
  Identify the component (model, manufacturer, type).

- **Where is it?**  
  Link to room, floor, and system.

- **What do I need to know?**  
  Specs, notes, safety, maintenance, warranties, service history.

> Goal: Real-world questions (paint color, shutoff valves, HVAC coverage, safe room details) are answerable **within minutes**.

---

### 1.3 Relevance and Calm UX

Ensure the app only shows what **actually exists** in the user’s house:

- Room types are toggleable
- Optional systems and sections can be disabled
- No irrelevant fields for basements, gardens, roofs, etc., if they don’t exist

> Goal: The UI feels **clean and calm**, even though the data model is rich.

---

### 1.4 Long-Term Legibility

Design for someone opening the app **5–20 years later**:

- Human-readable labels and notes
- Clear separation of files and structured data
- Stable, predictable structure (rooms, systems, documents)

> Goal: A future owner or inspector can understand the house without knowing its history.

---

## 2. Secondary Product Goals

### 2.1 Help With Professional Collaboration

- Share accurate subsets of information with:
  - Plumbers, electricians, HVAC technicians
  - Inspectors, insurance, municipal authorities
  - Renovation contractors
- Provide context: plans, photos, specs, and history in one place.

---

### 2.2 Strengthen Resale and Due Diligence

- Give potential buyers or banks a **transparent record**:
  - Documentation of systems and materials
  - Service and maintenance history
  - Safety and compliance status

---

### 2.3 Highlight Safety and Compliance

- Centralize:
  - Alarm system data
  - Fire detectors
  - Cameras
  - Safe room specs and Israeli standard compliance notes

> Goal: Safety information is **instantly accessible** and clearly separated.

---

## 3. User Goals

### 3.1 Homeowners

- Keep **all house knowledge in one place**
- Reduce stress during:
  - Emergencies (leaks, power issues)
  - Renovations
  - Insurance claims
  - Inspections or sales
- Avoid dependency on:
  - A single contractor
  - Old email accounts
  - Personal memory

### 3.2 Future Owners

- Understand what they are buying:
  - What systems exist and what shape they are in
  - What has been serviced or repaired
  - What materials and finishes were used

---

## 4. Design & Product Principles (Constraints)

1. **Relevance First**  
   - No irrelevant rooms or systems.
   - Room toggles and optional sections control visibility.

2. **Room-Driven Model**  
   - Most physical elements are linked to rooms.
   - Views can be by room or by system.

3. **Files vs Data**  
   - Files (plans, permits, photos) are stored with context.
   - Structured data (systems, fixtures, finishes) is separate and queryable.

4. **Future Use Over Initial Effort**  
   - Data entry can be slower / more detailed.
   - Long-term clarity is more important than “onboarding in 5 minutes”.

---

## 5. Non-Goals (What We Explicitly Avoid)

- Designing or planning the house
- Doing engineering or cost calculations
- Replacing professional software (CAD/BIM, load calculations, etc.)
- Forcing a global “perfect” taxonomy of houses
- Assuming every house has the same structure (basements, roofs, gardens, etc.)

The app focuses strictly on **post-construction documentation** and **homeowner comprehension**.