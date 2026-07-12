# AssetFlow Design System

This document outlines the comprehensive design system for **AssetFlow**, an enterprise Asset & Resource Management System. It establishes the visual language, components, and interaction patterns to ensure a consistent, premium, and user-friendly experience across the entire application.

---

## 1. Design Philosophy

The AssetFlow design language is rooted in **minimalism, clarity, and enterprise-grade professionalism**, drawing inspiration from modern SaaS products like Linear, Notion, and Stripe. 

- **Soft & Approachable:** We use a soft pastel color palette instead of harsh, high-contrast primary colors. This reduces cognitive load during extended use.
- **Spacious & Breathable:** Generous use of whitespace (padding and margins) ensures the interface never feels cluttered, even on data-heavy screens.
- **Premium Enterprise Feel:** Subtle shadows, rounded corners, and crisp typography create a polished, modern Odoo-friendly environment.
- **Focus on Content:** Avoid dark themes, heavy gradients, glassmorphism, and flashy UI elements. The interface should recede, bringing the user's data and workflows to the forefront.

---

## 2. Color Palette

Our color system relies on soft, accessible tones to create a clean pastel theme. Avoid using pure black (`#000000`) or pure white for backgrounds where soft grays can provide better depth.

| Role | Color Name | HEX Code | Usage |
| :--- | :--- | :--- | :--- |
| **Primary** | Soft Indigo | `#6366F1` | Primary buttons, active states, key highlights |
| **Primary Hover** | Deep Indigo | `#4F46E5` | Hover states for primary actions |
| **Secondary** | Light Ash | `#F3F4F6` | Secondary buttons, subtle backgrounds |
| **Background** | Off-White | `#F9FAFB` | Main application background |
| **Surface** | Pure White | `#FFFFFF` | Cards, dialogs, dropdowns |
| **Sidebar** | Pure White | `#FFFFFF` | Sidebar background (separated by border) |
| **Border** | Soft Gray | `#E5E7EB` | Input borders, card borders, table borders |
| **Divider** | Whisper Gray | `#F3F4F6` | Section dividers, list item separators |
| **Success** | Pastel Emerald | `#10B981` | Success states, Available status |
| **Warning** | Pastel Amber | `#F59E0B` | Warnings, Maintenance status |
| **Danger** | Pastel Red | `#EF4444` | Destructive actions, Lost status |
| **Info** | Pastel Blue | `#3B82F6` | Informational alerts, Allocated status |
| **Text Primary** | Slate Dark | `#111827` | Headings, primary body text |
| **Text Secondary**| Slate Medium | `#6B7280` | Subtitles, captions, placeholder text |
| **Disabled** | Slate Light | `#9CA3AF` | Disabled buttons, inactive text |
| **Link** | Soft Indigo | `#6366F1` | Text links |

---

## 3. Typography

**Font Family:** `Inter` (Fallback: `Roboto`, `sans-serif`). 
Inter provides excellent legibility for data-dense enterprise applications.

| Element | Size | Weight | Line Height |
| :--- | :--- | :--- | :--- |
| **H1 (Page Title)** | 24px (1.5rem) | 600 (SemiBold) | 32px |
| **H2 (Section)** | 20px (1.25rem)| 600 (SemiBold) | 28px |
| **H3 (Card Title)** | 16px (1rem) | 600 (SemiBold) | 24px |
| **Body (Base)** | 14px (0.875rem)| 400 (Regular) | 20px |
| **Button Text** | 14px (0.875rem)| 500 (Medium) | 20px |
| **Caption/Small** | 12px (0.75rem) | 400 (Regular) | 16px |

---

## 4. Spacing System

We use a strict **8-point grid system** to maintain vertical and horizontal rhythm. 

- **4px (Micro):** Inner component spacing (e.g., icon next to text in a button).
- **8px (Tiny):** Spacing between tightly related elements (e.g., label and input field).
- **12px (Small):** Padding inside small components (e.g., badges, small buttons).
- **16px (Base):** Standard padding for cards, standard gap between form fields.
- **24px (Medium):** Spacing between distinct sections within a card.
- **32px (Large):** Gap between standard layout components (e.g., between KPI cards).
- **40px (XL):** Padding around the main page content area.
- **48px (XXL):** Major section breaks on long scrollable pages.

---

## 5. Border Radius

Rounded corners soften the enterprise feel, making the software feel modern and approachable.

- **Cards:** `12px`
- **Buttons:** `8px`
- **Inputs & Selects:** `8px`
- **Dialogs/Modals:** `16px`
- **Tables (Container):** `8px`
- **Dropdown Menus:** `8px`
- **Status Chips:** `9999px` (Pill shape)

---

## 6. Shadows

Shadows should be subtle, mimicking soft ambient light rather than harsh directional light.

- **Card Shadow:** `0 1px 3px rgba(0,0,0,0.05), 0 1px 2px rgba(0,0,0,0.02)` (Very subtle lift)
- **Hover Shadow:** `0 4px 6px rgba(0,0,0,0.05), 0 2px 4px rgba(0,0,0,0.03)` (Interactive lift)
- **Dropdown Shadow:** `0 10px 15px -3px rgba(0,0,0,0.05)` (Clear separation from surface)
- **Dialog Shadow:** `0 20px 25px -5px rgba(0,0,0,0.1)` (High elevation for focus)

---

## 7. Icons

**Library:** `Lucide Icons` or `Heroicons` (Outline variants preferred).

- **Micro (14px):** Used inside badges or inline with captions.
- **Small (16px):** Used inside buttons, inputs, and dropdown items.
- **Standard (20px):** Used for sidebar navigation and standard actions.
- **Large (24px):** Used in KPI cards and empty state illustrations.
- **Stroke Width:** Consistently `1.5px` to `2px`.

---

## 8. Buttons

Buttons trigger actions. They should be easily identifiable and correctly prioritized.

| Type | Background | Text Color | Border | Hover State |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | `#6366F1` | `#FFFFFF` | None | `#4F46E5` |
| **Secondary** | `#F3F4F6` | `#111827` | None | `#E5E7EB` |
| **Outline** | Transparent | `#374151` | `1px solid #D1D5DB`| `bg-gray-50` |
| **Ghost** | Transparent | `#6B7280` | None | `bg-gray-100` |
| **Danger** | `#FEE2E2` (Pastel) | `#B91C1C` | None | `#FECACA` |

**Rules:**
- **Padding:** `8px` vertical, `16px` horizontal.
- **Radius:** `8px`.
- **Font:** `14px`, Medium (500).
- **Disabled State:** Opacity `50%`, cursor `not-allowed`, background `#F3F4F6`, text `#9CA3AF`.
- **Loading State:** Show a spinning standard icon (`16px`), disable interaction, maintain width.
- **Icon Buttons:** `8px` padding all around (square aspect ratio).

---

## 9. Form Components

Forms must be clean, spacious, and clearly validated.

- **Inputs / Dropdowns / Date Pickers / Search Bars:**
  - Background: `#FFFFFF`
  - Border: `1px solid #E5E7EB`
  - Padding: `8px 12px`
  - Height: `36px` to `40px`
  - Text: `14px`, `#111827`
  - Placeholder: `#9CA3AF`
  - Focus State: Border changes to `#6366F1`, `0 0 0 2px rgba(99,102,241,0.2)` ring.
- **Text Area:** Same as inputs, minimum height `80px`.
- **Checkbox / Radio:** `16px` by `16px`, accent color `#6366F1`.
- **Switch:** `36px` width, `20px` height pill, accent color `#6366F1`.
- **Validation Messages:** `12px` text below the input in `#EF4444` (Danger).
- **Required Fields:** Denoted by a subtle red asterisk `*`.
- **Disabled State:** Background `#F9FAFB`, text `#9CA3AF`, border `#E5E7EB`.

---

## 10. Tables

Tables are the core of AssetFlow. They must be highly legible.

- **Container:** White surface, `1px solid #E5E7EB` border, `8px` radius.
- **Table Header (TH):** Background `#F9FAFB`, Text `#6B7280`, `12px`, uppercase, medium weight.
- **Row Height:** `48px` (comfortable density).
- **Hover State:** Row background changes to `#F9FAFB` on hover.
- **Pagination:** Bottom right, outline buttons for Next/Prev.
- **Search/Filters:** Located in a toolbar directly above the table (`16px` padding).
- **Empty State:** Centered in the table container, pastel illustration, secondary text.
- **Bulk Actions:** Reveal a floating action bar at the bottom or replace the top toolbar when checkboxes are selected.

---

## 11. KPI Cards

Used on the Dashboard to provide operational snapshots.

- **Layout:** Horizontal layout. Icon on the left (or top left), Value/Label on the right (or bottom).
- **Background:** `#FFFFFF` with standard card shadow.
- **Icon:** Contained in a soft pastel circle (e.g., `bg-indigo-50`, `text-indigo-600`), `40px` by `40px`, icon size `20px`.
- **Value:** `24px`, SemiBold, `#111827`.
- **Label:** `14px`, Regular, `#6B7280`.
- **Trend Indicator:** Small badge next to the value (e.g., `+5%` in pastel green text).
- **Spacing:** `16px` internal padding.

---

## 12. Navigation

- **Sidebar Width:** `260px` (Expanded), `64px` (Collapsed).
- **Sidebar Background:** `#FFFFFF` with a `1px` right border `#E5E7EB`.
- **Top Navigation / Header:** Height `64px`. Contains Breadcrumbs on the left, Profile/Notifications on the right.
- **Page Title:** Placed below the top nav, `24px`, SemiBold.
- **Breadcrumb:** `14px`, `#6B7280`, separated by `/` or standard chevron.
- **Action Buttons:** Placed on the top right, inline with the Page Title (e.g., "Register Asset" button).

---

## 13. Dashboard Guidelines

- **Grid System:** 12-column responsive grid.
- **KPI Cards:** Top row, typically spanning 3 columns each (4 cards per row on desktop).
- **Chart Spacing:** `24px` gap between charts and tables.
- **Hierarchy:** High-level metrics at the top, actionable lists (Overdue Returns, Pending Transfers) below.

---

## 14. Status Chips

Chips denote lifecycle states. They use a pastel background with a darker, legible text color. Format: `12px`, Medium, pill shape (`px-2 py-1 rounded-full`).

| Status | Background Color | Text Color |
| :--- | :--- | :--- |
| **Available** | Pastel Green (`#D1FAE5`) | Dark Green (`#065F46`) |
| **Allocated** | Pastel Blue (`#DBEAFE`) | Dark Blue (`#1E40AF`) |
| **Reserved** | Pastel Purple (`#EDE9FE`) | Dark Purple (`#5B21B6`) |
| **Under Maintenance** | Pastel Amber (`#FEF3C7`) | Dark Amber (`#92400E`) |
| **Lost** | Pastel Red (`#FEE2E2`) | Dark Red (`#991B1B`) |
| **Retired** | Pastel Gray (`#F3F4F6`) | Dark Gray (`#374151`) |
| **Disposed** | Dark Gray (`#E5E7EB`) | Black (`#111827`) |

---

## 15. Workflow Timeline

For Approval Workflows (Transfers, Maintenance).

- **Visual:** Vertical line connecting status nodes.
- **Nodes:** `24px` circles.
- **States:**
  - **Pending:** Outline circle, gray border.
  - **Approved:** Solid pastel green circle, white check icon.
  - **Rejected:** Solid pastel red circle, white X icon.
  - **Resolved:** Solid pastel blue circle.
  - **Cancelled:** Solid gray circle.
- **Text:** Date/Time on the left, Action details on the right.

---

## 16. Calendar Design

For the Resource Booking screen.

- **Header:** Month/Week/Day toggles (Secondary buttons).
- **Grid:** Clean borders (`#E5E7EB`).
- **Time Slots:** `48px` height per hour block.
- **Events:** Pastel background cards (using the Status Chip colors to denote Booking Status: Upcoming, Ongoing).
- **Overlap:** Prevented by the system; visual overlapping is never rendered.
- **Current Time:** A subtle `#EF4444` line across the grid.

---

## 17. Dialogs (Modals)

- **Overlay:** Black with `40%` opacity, slight backdrop blur (if supported, otherwise flat).
- **Container:** Centered, `400px - 600px` max-width, `16px` radius, `#FFFFFF` background.
- **Header:** `20px` SemiBold title, close `X` icon button on the top right.
- **Body:** `14px` Regular text, `24px` padding.
- **Footer:** Right-aligned actions (Cancel as Ghost/Secondary, Action as Primary/Danger).

---

## 18. Notifications (Toasts)

Slide in from the top-right or bottom-right corner.

- **Style:** Floating card, `12px` radius, heavy shadow.
- **Success:** Green icon, bold title, standard body text.
- **Error:** Red icon, bold title.
- **Warning:** Amber icon.
- **Information:** Blue icon.
- **Duration:** Auto-dismiss after 4 seconds (unless critical).

---

## 19. Empty States

Used when a table is empty or a search yields no results.

- **Illustration:** A clean, minimalistic, monochromatic or pastel vector illustration (size `120px`).
- **Text:** `16px` SemiBold title (e.g., "No assets found"), `14px` Regular subtitle explaining what to do.
- **CTA Placement:** A primary or secondary button directly below the subtitle (e.g., "Register New Asset").

---

## 20. Responsive Rules

- **Desktop (1024px+):** Sidebar expanded, KPI cards 4-across, full tables.
- **Tablet (768px - 1023px):** Sidebar collapsed, KPI cards 2-across, tables hide non-critical columns.
- **Mobile (<768px):** Sidebar hidden (hamburger menu), KPI cards 1-across, tables convert to stacked card lists.

---

## 21. Accessibility

- **Contrast:** Ensure all text passes WCAG AA standards (minimum 4.5:1 ratio against backgrounds).
- **Keyboard Navigation:** Fully navigable via `Tab`. 
- **Focus States:** Every interactive element MUST have a visible focus ring (`2px` solid `#6366F1` with `2px` offset).
- **Touch Targets:** Minimum `44px` by `44px` for clickable elements on mobile screens.

---

## 22. Design Tokens

| Token | Value | Description |
| :--- | :--- | :--- |
| `--color-primary` | `#6366F1` | Brand primary color |
| `--color-surface` | `#FFFFFF` | Background for cards and panels |
| `--color-bg` | `#F9FAFB` | App background |
| `--color-text-main` | `#111827` | Primary text |
| `--color-text-muted`| `#6B7280` | Secondary text |
| `--color-border` | `#E5E7EB` | Standard border |
| `--font-sans` | `Inter, sans-serif` | Global font family |
| `--radius-sm` | `8px` | Buttons, Inputs |
| `--radius-md` | `12px` | Cards |
| `--radius-lg` | `16px` | Dialogs |
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Subtle lift |
| `--shadow-md` | `0 4px 6px rgba(0,0,0,0.05)` | Hover state |

---

## 23. AssetFlow Component Library

*Development Reference List for Reusable UI Components:*

- **Dashboard Cards:** Standardized wrapper for KPIs.
- **Statistics Cards:** Charts container with standardized header and legend.
- **Page Headers:** Title + Breadcrumbs + Action Buttons container.
- **Search Bars:** With integrated filtering dropdowns.
- **Tables:** Universal data grid component with pagination and row selection.
- **Status Badges:** See Section 14.
- **Timeline:** For maintenance/transfer workflows.
- **Approval Cards:** specialized card with Accept/Reject actions.
- **Activity Cards:** Log entries for audits and notifications.
- **Booking Cards:** For calendar events.
- **Maintenance/Audit/Employee/Asset Cards:** Detail view cards for entity profiles.

---

## 24. Screen Consistency Rules

**CRITICAL DIRECTIVE:** Every future screen generated for this project MUST strictly follow this design system.

1. **No Rogue Colors:** Do not introduce new colors. Use only the defined pastel palette.
2. **No Ad-Hoc Spacing:** Use only the 8-point spacing system multiples.
3. **Typography Compliance:** Stick to the defined font scale. No inline font resizing.
4. **Card Styles:** All cards must use `#FFFFFF` background, `12px` radius, and `--shadow-sm`.
5. **Updates Required:** No screen may introduce new components or styles unless this `Design_System.md` document is updated and approved first.
