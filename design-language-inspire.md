# INSPIRE - Design Language System (Analytical Pro)

This document serves as the source of truth for the INSPIRE application's UI/UX. All components and layouts must adhere to these specifications to maintain the "Analytical Pro" aesthetic—clean, data-dense, and financially rigorous.

## 1. Core Principles

-   **Analytical Pro**: Dense but legible. High contrast for data.
-   **Financial First**: Numbers are the UI. Always use `tabular-nums` for financial data.
-   **Visual Hierarchy**: Key metrics (LTV, DSCR) are large and bold; secondary metadata is subtle.
-   **Status Driven**: Clear, semantic color coding for deal stages and risk flags.

## 2. Color Palette (TweakCN / Tailwind)

### Base Colors
| Token | Value (HSL/Hex) | Usage |
| :--- | :--- | :--- |
| **Primary** | `#0171e2` (Blue) | Primary actions, active states, key links |
| **Secondary** | `#131a20` (Dark Slate) | Headings, strong text, sidebar navigation |
| **Background** | `#ffffff` (White) | Page background, modal background |
| **Foreground** | `#131a20` (Dark Slate) | Body text |
| **Muted** | `#ededed` (Light Gray) | Secondary backgrounds, inactive states |
| **Border** | `#e1eaef` (Blue-Gray) | Dividers, card borders, inputs |

### Component Colors
| Token | Value | Usage |
| :--- | :--- | :--- |
| **Card** | `#f9f9fb` | Cards, tiles, isolated content areas |
| **Input** | `#f7f9fa` | Form input backgrounds |
| **Accent** | `#e3ecf6` | Active selection backgrounds, hover states |

### Semantic Status Colors
| Status | Color (Tailwind) | Usage |
| :--- | :--- | :--- |
| **Success** | `bg-green-100` / `text-green-800` | Approved, Funded, On Track, Positive Delta |
| **Warning** | `bg-yellow-100` / `text-yellow-800` | Pending, Missing Info, Expiring Soon |
| **Error/Danger** | `bg-red-100` / `text-red-800` | Rejected, Overdue, Critical Flag |
| **Processing** | `bg-blue-100` / `text-blue-800` | In Progress, Underwriting, Review |
| **Neutral** | `bg-gray-100` / `text-gray-600` | Draft, Prospect, Archived |

## 3. Typography

**Font Families**
-   **Headings**: `Lato` (Clean, modern sans-serif) or optional `Playfair Display` for very high-level branding.
-   **Body**: `Lato` (sans-serif)
-   **Data/Code**: `Fragment Mono` or system mono (for IDs, raw data)

**Type Scale (Tailwind)**
-   **Page Titles**: `text-2xl font-bold text-foreground`
-   **Section Headers**: `text-lg font-bold text-foreground`
-   **Body**: `text-sm font-normal text-foreground` (Default size is 14px for density)
-   **Labels**: `text-xs font-medium text-gray-500 uppercase tracking-wider`
-   **Key Metrics**: `text-3xl` or `text-4xl` `font-bold` (e.g., LTV display)

**Financial Data Rules**
-   **Alignment**: Right-aligned for columns of numbers.
-   **Formatting**: Always use `tabular-nums` class to align digits vertically.
-   **Precision**: Display cents only when relevant (e.g., Term Sheets), otherwise round to dollars (e.g., Pipeline).

## 4. UI Components & Spacing

### Spacing System
-   **Card Padding**: `p-5` or `p-6` (20px - 24px)
-   **Grid Gaps**: `gap-6` (24px) standard for dashboard grids.
-   **Section Spacing**: `space-y-6` between vertical stacks.

### Shapes & Depth
-   **Border Radius**: `rounded-lg` (0.5rem / 8px) - Soft but professional.
-   **Shadows**: `shadow-sm` for cards, `shadow-md` for hover states/modals.
-   **Borders**: Extensive use of `border border-border` to define structure without heavy backgrounds.

### ShadCN Component Customizations
When converting to React/Shadcn, apply these overrides:

-   **Cards**: `bg-card border-border shadow-sm`
-   **Buttons**:
    -   Primary: `bg-primary hover:bg-blue-600 text-white shadow-sm`
    -   Secondary/Outline: `bg-white border-gray-300 text-gray-700 hover:bg-gray-50`
    -   Ghost: `text-gray-500 hover:text-gray-900 hover:bg-muted`
-   **Badges**: `rounded-full px-2.5 py-0.5 text-xs font-medium` (Pill shape)
-   **Tables**:
    -   Header: `bg-gray-50 text-gray-500 uppercase text-xs font-medium`
    -   Rows: `hover:bg-muted/50 border-b border-border`
    -   Density: `py-3 px-4` cells (Comfortable but dense)

## 5. Layout Patterns

### Dashboard
-   **KPI Grid**: Top row, 4-column grid. Large metrics + small trend indicators.
-   **Split View**: 2/3 Main Content (Left), 1/3 Sidebar/Tasks (Right).

### Pipeline (Kanban)
-   **Columns**: Fixed width (`w-80`), gray background header (`bg-gray-100`).
-   **Cards**: White background, `shadow-sm`, border-l-4 for status indication.

### Deal Detail
-   **Header Shell**: Sticky top bar with breadcrumbs, status badge, and primary actions.
-   **Tab Navigation**: Underline style (`border-b-2`), `text-sm font-medium`.
-   **Data Grid**: Key-value pairs using Description Lists (`dl`, `dt`, `dd`).

## 6. Iconography
-   Use **Heroicons** (Outline style for UI, Solid style for small indicators).
-   Size: `h-5 w-5` standard, `h-4 w-4` for dense areas.
-   Color: `text-gray-400` default, `text-primary` active.

