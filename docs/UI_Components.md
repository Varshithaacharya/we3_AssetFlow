# AssetFlow UI Components

This document defines the complete library of reusable UI components for the **AssetFlow** application. It builds directly upon the foundational `Design_System.md` document.

**Theme Constraints:** Soft pastel, minimal, professional, clean, high whitespace, rounded corners, and absolute consistency.

---

## 1. Page Layout

Every major screen in AssetFlow follows a consistent page layout structure.

- **Page Header:** The topmost container within the main view, below the top navbar. Uses `--color-surface` or transparent background with `24px` bottom margin.
- **Breadcrumb:** Placed at the top left of the Page Header. Uses `--color-text-muted`, `14px`, separated by `/`.
- **Page Title:** Directly below breadcrumbs. Size `24px`, SemiBold, `--color-text-main`.
- **Page Description:** (Optional) Below the Page Title. Size `14px`, Regular, `--color-text-muted`.
- **Primary Action Button:** Top right of the Page Header. Uses `--color-primary` background, white text. E.g., "New Asset".
- **Secondary Action Button:** To the left of the Primary Action. Ghost or Outline style. E.g., "Export".
- **Toolbar:** Placed above Data Tables or content grids. Contains Search, Filter Bar, and View Toggles.
- **Content Area:** The main grid or table container. Padding `24px` to `40px` depending on screen size. Background is `--color-bg`.
- **Footer:** Minimal, centered text (`12px`, `--color-text-muted`), containing version info or copyright.

---

## 2. Navigation Components

- **Sidebar:** Width `260px`. White background, `1px` right border. Contains navigation links with `20px` icons and `14px` Medium text. Active state uses `bg-indigo-50` with `--color-primary` text.
- **Collapsed Sidebar:** Width `64px`. Displays only icons centered horizontally. Tooltips appear on hover.
- **Top Navbar:** Height `64px`, fixed at the top of the content area. White background, subtle bottom border.
- **Profile Menu:** Located top right. Avatar (`32px` circle), opens an `8px` rounded dropdown with options (Profile, Settings, Logout).
- **Notification Panel:** Triggered by a bell icon in the Top Navbar. Slide-out panel or wide dropdown (`320px`) showing an Activity Feed.
- **Quick Actions:** A "plus" icon button in the Top Navbar or Sidebar triggering a global "Create New..." dropdown menu.

---

## 3. Search Components

- **Global Search:** Located in the Top Navbar. Input width `240px` (expands on focus), prefix search icon. Searches all assets, employees, and bookings.
- **Page Search:** Located in the Toolbar above tables. Input width `320px`, prefix search icon, placeholder "Search in [Current Context]...".
- **Search Suggestions:** Dropdown appearing below Global Search containing "Recent Searches" and matched categories.
- **Recent Searches:** List items inside Search Suggestions. Subtle clock icon prefix.
- **Filter Chips:** Removable pills (pastel background, `12px` text) appearing below the Page Search to denote active filters (e.g., `Status: Available [X]`).
- **Saved Filters:** Dropdown next to Page Search allowing users to save and quickly select complex filter chip combinations.

---

## 4. Filter Bar

A horizontal bar or dropdown-driven toolbar containing specific filters.

- **Date Filter:** Date Range Picker input.
- **Department Filter:** Single or multi-select dropdown listing departments.
- **Status Filter:** Multi-select dropdown mapping to Status Chips (Available, Allocated, etc.).
- **Category Filter:** Dropdown for Asset Categories.
- **Employee Filter:** Searchable dropdown (typeahead) for Assignees/Auditors.
- **Location Filter:** Dropdown for physical locations.
- **Clear Filters:** Ghost button (`text-red-500` or `--color-text-muted`) appearing when at least one filter is active.

---

## 5. Data Tables

- **Standard Table:** White container, `12px` radius, subtle shadow. `48px` row height.
- **Compact Table:** `36px` row height, smaller font (`13px`). Used for modals or dense data like Audit lines.
- **Expandable Table:** Rows feature a chevron prefix. Clicking expands the row to reveal inner details or sub-tables (e.g., Audit discrepancies).
- **Grouped Table:** Rows grouped by Category or Department with a light gray header row spanning all columns.
- **Sortable Columns:** Column headers are clickable, showing an up/down arrow icon on hover or active sort.
- **Pagination:** Bottom right of the table container. "Showing 1-10 of 50" text on the left, Prev/Next buttons on the right.
- **Bulk Actions:** A floating bar that overlays the Toolbar when 1+ checkboxes are selected, offering actions like "Delete Selected" or "Assign".
- **Empty Table:** Table body is replaced by an Empty State (Illustration + Description).
- **Loading Table:** Replaced by Skeleton Table rows.

---

## 6. Cards

All cards share a `--color-surface` (white) background, `12px` radius, and `--shadow-sm`. Spacing is consistently `16px` or `24px` padding.

- **Dashboard KPI Card:**
  - **Purpose:** High-level metric display.
  - **Layout:** Horizontal. Icon Left, Data Right.
  - **Typography:** Value `24px` SemiBold, Label `14px` Regular.
  - **Icon:** `40px` circle with pastel background.
  - **Badge Placement:** Top right corner (Trend Indicator, e.g., "+5%").
- **Statistics Card:**
  - **Purpose:** Chart container.
  - **Layout:** Header (Title + Filter) above the Chart area.
- **Asset Card:**
  - **Purpose:** Grid view display for Assets.
  - **Layout:** Image placeholder top, Title and Category below, Status Chip bottom left.
  - **Actions:** View Details button (Ghost) on bottom right.
- **Employee Card:**
  - **Purpose:** Directory display.
  - **Layout:** Avatar left, Name/Role right, Department badge below.
- **Booking Card:**
  - **Purpose:** Calendar event or list item.
  - **Layout:** Time range left, Resource name and Booker right. Pastel background matching status.
- **Maintenance Card:**
  - **Purpose:** Kanban or list view for repairs.
  - **Layout:** Asset Name, Issue snippet, Priority badge (High/Med/Low).
- **Audit Card:**
  - **Purpose:** Audit cycle summary.
  - **Layout:** Cycle Name, Date Range, Progress Pill showing completion %.
- **Department Card:**
  - **Purpose:** Org setup overview.
  - **Layout:** Department Name, Head name, Headcount.
- **Activity Card:**
  - **Purpose:** Log entry display.
  - **Layout:** Small avatar/icon left, "User did Action" text right, relative timestamp (`12px` muted text).
- **Notification Card:**
  - **Purpose:** Unread alert display.
  - **Layout:** Icon left, Title/Body right, Action buttons (Mark Read, View) bottom right.

---

## 7. Forms

- **Standard Form:** Single column, stacked inputs. Label (`14px` Medium), `8px` gap, Input. `24px` gap between fields.
- **Two Column Form:** Side-by-side inputs for wide screens, wrapping to single column on mobile.
- **Wizard Form:** Multi-step form with a horizontal progress indicator at the top. Next/Back buttons in the footer.
- **Tabbed Form:** Top horizontal tabs to switch between form sections (e.g., General, Specifications, Financial).
- **Attachment Upload:** Dashed border box (`#E5E7EB`), centered upload icon, "Drag and drop or click to upload" text. Pastel gray hover state.
- **Image Upload:** Circular or square avatar/image preview with an edit overlay on hover.
- **Validation Messages:** `12px` red text appearing instantly below the field on blur/submit. Field border turns red.
- **Required Fields:** Label suffixed with a subtle red `*`.

---

## 8. Detail Pages

Every Detail Page (Asset Details, Employee Details, Booking Details, Audit Details, Maintenance Details) follows a strict layout:

1. **Header Area:** Breadcrumbs, Large Title (Entity Name/ID), Primary Status Chip next to title. Action buttons on the far right (Edit, Delete, Transfer).
2. **Two-Pane Layout (Desktop):**
   - **Main Content (Left, 70%):** Tabbed navigation (e.g., Overview, History, Documents). Displaying core attributes in a 2-column key-value grid.
   - **Sidebar (Right, 30%):** Contextual widgets. (e.g., Assigned To Employee Card, Current Location, Quick Actions).

---

## 9. Timeline Components

- **Approval Timeline:** Vertical nodes. Pending (Gray Outline) -> Approved (Green Solid) -> Resolved (Blue Solid).
- **Activity Timeline:** Vertical line on the left. Small gray dots. Displays full history of an asset or employee.
- **Maintenance Timeline:** Shows transitions: Raised -> Approved -> In Progress -> Resolved.
- **Allocation Timeline:** History of who held an asset (Check-out date to Check-in date).
- **Audit Timeline:** Cycle creation -> Auditor Assignment -> Verification -> Cycle Closure.

---

## 10. Status Components

- **Badges:** Small square/rounded tags used for counts or priorities (e.g., `Priority: High` in pastel red).
- **Chips:** Pill-shaped (`rounded-full`) used exclusively for Entity Lifecycle Status (Available, Allocated, Maintenance, etc.).
- **Indicators:** Small `8px` colored dots next to text (e.g., Online/Offline status).
- **Progress Pills:** Horizontal bar with percentage text inside or next to it (e.g., Audit progress 75%).
- **Workflow Labels:** Rectangular tags denoting approval stages (Pending, Approved, Rejected).

---

## 11. Dashboard Components

- **KPI Cards:** Top row grid.
- **Charts:** Used for Utilization Trends (Line) and Allocation Summaries (Bar).
- **Recent Activities:** A specialized table or list using Activity Cards.
- **Quick Actions:** 3-4 Primary/Secondary large buttons (Register Asset, Book Resource) horizontally aligned.
- **Alerts:** Banner format at the top of the dashboard for system-wide notices.
- **Upcoming Returns:** A dedicated compact table showing Asset, Assignee, and Expected Return Date.
- **Maintenance Summary:** Donut chart or list showing active repair priorities.
- **Booking Calendar:** Mini-calendar widget showing today's resource usage.

---

## 12. Empty States

Used when data is absent.
- **Illustration:** Monochromatic pastel SVG `120x120px` centered.
- **Headline:** `18px` SemiBold, Dark Slate. (e.g., "No assets allocated yet")
- **Description:** `14px` Regular, Muted Slate. (e.g., "When assets are assigned to you, they will appear here.")
- **CTA:** Primary Button directly below the description.

---

## 13. Modals

Standard dialog structure (`16px` radius, heavy shadow).
- **Confirmation:** Title, Message, Cancel (Secondary), Confirm (Primary).
- **Delete:** Title, Warning message in bold, Cancel (Secondary), Delete (Danger Button).
- **Approve:** Action modal with an optional "Notes" text area. Approve (Primary) / Cancel.
- **Reject:** Requires "Reason" text area. Reject (Danger) / Cancel.
- **Assign:** Form modal with Employee/Department dropdowns and Date Pickers.
- **Transfer:** Form modal showing current assignee vs. new assignee.

---

## 14. Notifications

- **Toast:** Floating bottom-right. Dismisses in 4s. Used for success/error feedback on form submissions.
- **Alert Banner:** Full-width strip below the Page Header. Pastel background (blue/amber/red). Used for Overdue Returns or pending approvals.
- **Activity Feed:** List of Notification Cards inside the Notification Panel.
- **Unread Badge:** Small red dot `8px` positioned top-right of the bell icon.

---

## 15. Calendar Components

- **Booking Calendar:** The main view for resource booking.
- **Weekly Calendar:** 7-day horizontal grid with vertical time slots.
- **Monthly Calendar:** Standard grid view.
- **Timeline View:** Horizontal timeline showing resources as rows and time as columns (Gantt chart style).

---

## 16. Charts

- **Bar Chart:** Use pastel colors matching the dataset. Subdued grid lines.
- **Line Chart:** Smooth curves. Soft shadow below the line.
- **Pie / Donut Chart:** Used for Category breakdown or Status breakdown.
- **Heat Map:** Used for Resource Booking peak usage (lighter pastel = low usage, darker pastel = high usage).
- **Trend Cards:** Mini sparkline charts inside KPI Cards.

---

## 17. Loading States

- **Skeleton Cards:** Gray pulse animation (`bg-gray-200`) shaped like KPI cards or Asset Cards.
- **Skeleton Tables:** Rows of gray pulse rectangles mimicking text layout.
- **Skeleton Forms:** Gray rectangles mimicking inputs.

---

## 18. Component Naming Convention

All components built must adhere to PascalCase naming for reusability. Examples:

- `AppHeader`
- `SidebarNav`
- `KpiCard`
- `FilterBar`
- `DataTable`
- `StatusChip`
- `ApprovalTimeline`
- `ActivityCard`
- `AssetCard`
- `BookingCalendar`
- `WizardForm`
- `EmptyState`
- `ConfirmModal`

---

## 19. Component Reuse Rules

Consistency is enforced by composing screens exclusively from these components.

- **Dashboard:** Uses `AppHeader`, `KpiCard` (x4), `TrendCard`, `DataTable` (Upcoming Returns), `ActivityFeed`.
- **Asset Registration Screen:** Uses `AppHeader`, `WizardForm` or `TabbedForm`, `ImageUpload`.
- **Asset Directory:** Uses `AppHeader`, `FilterBar`, `DataTable` or `AssetCard` grid, `StatusChip`, `Pagination`.
- **Asset Detail View:** Uses `AppHeader`, `StatusChip`, `ActivityTimeline`, `DetailPane`, `ConfirmModal`.
- **Booking Screen:** Uses `AppHeader`, `FilterBar`, `BookingCalendar`, `QuickAction` (New Booking).
- **Maintenance Screen:** Uses `AppHeader`, `DataTable`, `StatusChip`, `ApprovalTimeline`.
- **Audit Screen:** Uses `AppHeader`, `FilterBar`, `AuditCard`, `ProgressPill`, `DataTable`.

---

## 20. Future Development Rules

**Strict Enforcement:**
1. **No New Components:** Developers MUST reuse components from this document. If a design requirement cannot be met, existing components must be extended.
2. **Naming Consistency:** Code structures (React/Vue/OWL) must match the Component Naming Convention (e.g., `<StatusChip />`).
3. **Property Passthrough:** Components must support standardized properties (e.g., `variant="primary"`, `size="md"`).
4. **Document Updates:** If an entirely new component paradigm is absolutely necessary, this `UI_Components.md` document MUST be updated and approved by the Design System Architect before development begins.
