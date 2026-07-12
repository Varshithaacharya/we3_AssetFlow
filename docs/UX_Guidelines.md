# AssetFlow UX Guidelines

This document outlines the User Experience (UX) guidelines and interaction patterns for the **AssetFlow** application. It serves as the bridge between visual design (`Design_System.md`, `UI_Components.md`) and actual user workflows.

---

## 1. UX Philosophy

AssetFlow is an enterprise application. Our primary goal is to help users manage physical assets and resources efficiently. The software must be:

- **Fast:** Interactions should feel instantaneous. Optimize for speed in data entry and retrieval.
- **Predictable:** Users should immediately know how an interaction will behave based on past experiences within the app.
- **Minimal Clicks:** Streamline workflows. Expose high-use actions directly; hide edge-case actions behind menus.
- **Accessible:** The system must be usable by everyone, supporting screen readers, keyboard navigation, and high legibility.
- **Consistent:** Reusing components and patterns reduces cognitive load. Never reinvent an interaction pattern.

---

## 2. Navigation Rules

- **Maximum Navigation Depth:** Do not exceed 3 levels of depth (e.g., `Home > Assets > Laptop-AF-001`). Deep navigation confuses users and buries data.
- **Breadcrumb Usage:** Mandatory on all detail and form pages to provide context and an easy way to move up the hierarchy.
- **Sidebar Behavior:**
  - **Desktop:** Expanded by default, collapsible via a toggle to maximize horizontal workspace.
  - **Mobile:** Hidden behind a hamburger menu toggle.
- **Page Transitions:** Instantaneous. No artificial delays or heavy animations between page loads. Use skeletons while data fetches.

---

## 3. CRUD Experience

Standardize how data is manipulated across the app (Departments, Categories, Assets, Users).

- **Create:** Primary button placed consistently top-right on list views. Usually opens a Form Modal (for simple entities) or a dedicated Create Page (for complex entities like Assets).
- **Read:** Drill down into a Detail Page by clicking the entity name or a "View" inline action.
- **Update:** Inline editing on Detail Pages for simple fields, or a dedicated "Edit" mode toggle.
- **Delete:** Hide destructive actions under a "More" (three dots) menu or a clearly marked Danger button at the bottom of a form.
- **Confirmation Dialogs:** Mandatory for all Delete actions and significant state changes (e.g., Closing an Audit Cycle).
- **Undo Strategy:** For non-destructive state changes (like archiving or transferring), provide a "Toast with Undo" option for 5 seconds before committing, reducing the need for aggressive confirmation prompts.

---

## 4. Search Experience

- **Global Search:** Always available in the top navbar. Focus via keyboard shortcut (e.g., `Ctrl+K` or `/`). Returns categorized results (Assets, Employees, Bookings).
- **Table Search:** Instant filter as the user types (debounce 300ms). Searches the current context only.
- **Filters:** Placed above tables. Apply immediately upon selection.
- **Advanced Filters:** Hidden behind a "Filter" button dropdown to keep the UI clean.
- **Saved Filters:** Allow users to save complex queries (e.g., "My Department's Missing Assets") as quickly accessible tabs or dropdown items.

---

## 5. Forms

- **Validation:** Validate on blur (when the user leaves the field) and on submit. Do not shout at the user while they are typing.
- **Autosave Policy:** For long-form data entry (e.g., Asset Registration), utilize autosave drafts. Indicate status with subtle "Saved as draft" text.
- **Required Fields:** Mark clearly with a red `*`. Disable the Submit button until all required fields are filled.
- **Error Handling:** Scroll to the first error upon failed submission. Highlight the field in red and provide a clear, actionable error message below it.
- **Success Messages:** Use a Toast notification. Automatically redirect back to the list view or detail view.
- **Cancel Behavior:** Prompt for confirmation if the user clicks "Cancel" and unsaved changes exist.

---

## 6. Tables

- **Sorting:** Click column headers to toggle Ascending/Descending/Off. Include a visual indicator (arrow) on the active sort column.
- **Filtering:** See Section 4.
- **Pagination:** Essential for performance. Default to 20 rows per page. Provide a page size selector.
- **Inline Actions:** Placed in the far-right column. Expose primary action (e.g., "View") and hide others under a "More" dropdown.
- **Bulk Actions:** Reveal a context bar at the top of the table when checkboxes are selected.

---

## 7. Dashboard

- **Information Hierarchy:** Critical actions (Pending Approvals) > High-level metrics (KPI Cards) > Actionable lists (Overdue Returns) > Analytics (Charts).
- **KPI Placement:** Top row. 4 across on desktop.
- **Chart Priority:** Keep charts simple. They should support a decision, not just look pretty. Use tooltips to reveal exact data points on hover.
- **Alert Priority:** System-wide or role-critical alerts (e.g., "3 Overdue Maintenance Requests") appear as banners above the KPI cards.

---

## 8. Workflow UX

AssetFlow handles complex workflows. Make state changes explicit.

- **Allocation Workflow:** When assigning an asset, explicitly block overlapping assignments. Present a "Transfer Request" alternative seamlessly.
- **Maintenance Workflow:** Raise -> Approve -> Repair -> Resolve. Use the Approval Timeline component to show exactly where a request is stalled.
- **Booking Workflow:** Visual calendar interaction. Click and drag on the calendar to propose a time slot. Instant visual feedback on conflicts.
- **Audit Workflow:** Step-by-step wizard. Prevent closing an audit cycle if unverified assets remain, or force the user to mark them explicitly as "Missing".
- **Approval Workflow:** Department Heads/Asset Managers should see a unified "Pending Approvals" widget on their dashboard to prevent bottlenecks.

---

## 9. Notifications

- **Success:** (Toast) "Asset AF-001 registered successfully."
- **Warning:** (Banner/Toast) "Resource Boardroom A is double-booked." (Should be blocked by system, but used as feedback).
- **Error:** (Toast/Modal) "Failed to assign asset. Please check network connection."
- **Info:** (Toast) "Audit Cycle Q3 started."
- **Reminder:** (Notification Panel) "Your booking for Projector P1 starts in 15 minutes."

---

## 10. Mobile Behaviour

- **Responsive Navigation:** Sidebar collapses to a hamburger menu. Bottom tab bar for primary views (Dashboard, Assets, Bookings, Profile) is recommended.
- **Tables:** Do not squeeze columns. Convert rows into stacked cards on mobile (e.g., Asset Name bolded on top, metadata below).
- **Cards:** Stack vertically. Ensure touch targets are large enough (`44px` minimum).
- **Buttons:** Expand primary actions to full width at the bottom of the screen to ensure easy thumb reach.

---

## 11. Accessibility

- **Keyboard Support:** Full operability without a mouse. Tab through forms, Enter/Space to activate buttons, Arrow keys for dropdowns.
- **Focus Order:** Logical top-to-bottom, left-to-right tab indexing. Active focus ring must be highly visible (e.g., 2px solid primary color).
- **Contrast:** Maintain WCAG AA standard (4.5:1 ratio) for all text against backgrounds. Avoid low-contrast gray-on-gray text.
- **Error Messaging:** Never rely on color alone to indicate an error (e.g., don't just turn the border red, include the error icon and text message).

---

## 12. Loading Behaviour

- **Skeletons:** Preferred over spinners for full-page loads. Mimic the layout of the incoming data (Table skeletons, Card skeletons) to reduce perceived wait time.
- **Progress Indicators:** Use linear progress bars at the top of the screen for routing changes or heavy API calls.
- **Optimistic UI:** For low-risk actions (like "Liking" or "Marking Read"), update the UI immediately before the server confirms, gracefully reverting on failure.

---

## 13. Empty States

- **Friendly Guidance:** Never show a blank white page. Tell the user *why* it's empty.
- **Illustration Usage:** Center a soft pastel illustration matching the context.
- **Primary CTA:** Tell the user what to do next. Example: "No departments found. [Create Department]".

---

## 14. Error States

- **Validation:** Inline, instant feedback.
- **Permission Denied (403):** Display a friendly "You don't have access to this area" page with a button to return to the Dashboard.
- **No Data (404):** "The asset you are looking for does not exist or has been deleted."
- **Server Error (500):** "Something went wrong on our end." Provide a "Retry" button.

---

## 15. Interaction Rules

- **Double-click:** Avoid relying on double-click. Use single-click to view details.
- **Hover:** Use hover for subtle discovery (tooltips, revealing inline actions on tables), but never hide critical path actions exclusively behind hover states (as they fail on touch devices).
- **Right Click:** Do not override the native browser context menu unless absolutely necessary for a highly specialized tool (e.g., Calendar view).
- **Dropdowns:** Close when clicking outside. Support typeahead filtering if the list exceeds 10 items.

---

## 16. User Journey

- **Admin:** Focus on Setup and Oversight.
  - *Flow:* Logs in -> Sets up Departments/Categories -> Invites Employees -> Assigns Roles -> Monitors organization-wide health via Reports.
- **Asset Manager:** Focus on Inventory and Maintenance.
  - *Flow:* Logs in -> Registers new assets -> Approves/Rejects Transfers and Maintenance -> Manages Audit Discrepancies.
- **Department Head:** Focus on Team Enablement.
  - *Flow:* Logs in -> Checks team allocations -> Approves intra-department transfers -> Books resources for team meetings.
- **Employee:** Focus on Daily Tasks.
  - *Flow:* Logs in -> Checks assigned assets -> Books a vehicle for an afternoon meeting -> Raises a maintenance ticket for a broken laptop -> Initiates a return request.

---

## 17. UX Consistency Rules

**CRITICAL DIRECTIVE:** Future development must adhere strictly to these Interaction Rules.

1. Do not invent new form validation patterns.
2. Do not introduce artificial delays, heavy animations, or loading screens that block the user unnecessarily.
3. Every screen generated in the future MUST be vetted against these rules to ensure predictability and speed for the end user.
4. Any deviation from these UX guidelines requires explicit approval and an update to this `UX_Guidelines.md` document.
