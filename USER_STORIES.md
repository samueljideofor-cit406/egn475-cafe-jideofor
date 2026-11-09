# Café Calle Ocho – User Stories Backlog

## Project Overview

Café Calle Ocho is a café ordering and kitchen management system designed to make ordering food easier for customers and managing orders more efficient for kitchen staff.

The system has two main personas:

1. **Customer:** A person who wants to browse the café menu, place orders, and check order progress.
2. **Kitchen Staff:** An employee who needs to receive customer orders, manage order statuses, and keep menu availability updated.

---

## 1. Customer User Stories
### Story 1: Browse the Menu
**Priority: MUST HAVE**

As a customer, I want to view the café's menu and prices, so that I can decide what I want to order.

**Acceptance Criteria**
- Given the customer opens the menu, when the page loads, then the system displays each available item's name, description, price, and category (food or drinks).
- Given the menu contains no available items, when the customer opens it, then the system displays: "No menu items are currently available."

### Story 2: Add Items to Cart
**Priority: MUST HAVE**

As a customer, I want to add food and drinks to my shopping cart, so that I can prepare my order before checking out.

**Acceptance Criteria**
- Given a menu item is available, when the customer clicks Add to Cart, then the item appears in the cart with its correct name, quantity, and price.
- Given an item is sold out, when the customer clicks Add to Cart, then the system prevents the addition and displays: "Sorry, this item is sold out."

### Story 3: Place an Order
**Priority: MUST HAVE**

As a customer, I want to submit my completed order, so that the café can prepare my food.

**Acceptance Criteria**
- Given the customer has at least one item in the cart and enters their name, when they click Place Order, then the system saves the order with a unique order number and an initial status of Received.
- Given the cart is empty or the customer name is blank, when the customer clicks Place Order, then the system prevents submission and displays: "Please add items and enter your name before placing an order."

### Story 4: Receive Order Confirmation
**Priority: MUST HAVE**

As a customer, I want to receive an order confirmation, so that I know my order was successfully submitted.

**Acceptance Criteria**
- Given an order is successfully saved, when the confirmation page loads, then it displays the order number, customer name, item names, quantities, total price, and order status.
- Given the system fails to save an order, when the customer submits it, then the system displays: "Your order could not be submitted. Please try again." and does not display a successful confirmation.

### Story 5: Track Order Status
**Priority: SHOULD HAVE**

As a customer, I want to see the current status of my order, so that I know whether my food is being prepared or is ready.

**Acceptance Criteria**
- Given a valid order number is entered, when the customer checks the order, then the system displays one of these statuses: Received, Preparing, Ready, or Cancelled.
- Given an invalid order number is entered, when the customer searches for the order, then the system displays: "Order not found. Please check your order number."

### Story 6: Cancel an Order
**Priority: COULD HAVE**

As a customer, I want to cancel my order before preparation begins, so that I can correct a mistake or change my mind.

**Acceptance Criteria**
- Given an order has a Received status, when the customer requests cancellation, then the system changes its status to Cancelled.
- Given an order has a Preparing or Ready status, when the customer requests cancellation, then the system prevents cancellation and displays: "This order can no longer be cancelled."

## 2. Kitchen Staff User Stories

### Story 7: View Incoming Orders
**Priority: MUST HAVE**

As a kitchen staff member, I want to view incoming customer orders on a kitchen order board, so that I can see which orders need to be prepared.

**Acceptance Criteria**
- Given customers have submitted orders, when kitchen staff open the order board, then the system displays each order with its order number, items, quantities, and status.
- Given there are no incoming orders, when kitchen staff open the order board, then the system displays: "There are currently no incoming orders."

### Story 8: Start Preparing an Order
**Priority: MUST HAVE**

As a kitchen staff member, I want to mark an order as Preparing, so that the kitchen knows which orders are being worked on.

**Acceptance Criteria**
- Given an order has a Received status, when staff click Start Preparing, then the system changes its status to Preparing.
- Given an order is already Ready or Cancelled, when staff attempt to start preparing it, then the system prevents the change and displays: "This order cannot be started."

### Story 9: Mark an Order Ready
**Priority: MUST HAVE**

As a kitchen staff member, I want to mark an order as Ready, so that customers know when their food is finished.

**Acceptance Criteria**
- Given an order has a Preparing status, when staff click Mark Ready, then the system changes its status to Ready.
- Given an order has a Received or Cancelled status, when staff attempt to mark it Ready, then the system prevents the change and displays: "This order cannot be marked ready."

### Story 10: Manage Sold-Out Items
**Priority: SHOULD HAVE**

As a kitchen staff member, I want to mark menu items as sold out, so that customers cannot order unavailable food.

**Acceptance Criteria**
- Given a menu item is available, when staff mark it as sold out, then the system changes its availability to Sold Out.
- Given staff try to update a menu item that does not exist, when they submit the change, then the system displays: "Menu item not found."

### Story 11: View Order Details
**Priority: SHOULD HAVE**

As a kitchen staff member, I want to view the details of each customer order, so that I can prepare the correct food and quantities.

**Acceptance Criteria**
- Given an order exists, when staff select the order, then the system displays its order number, customer name, items, quantities, and total price.
- Given staff search for an order number that does not exist, when they submit the search, then the system displays: "Order not found."

### Story 12: Access Staff Features
**Priority: MUST HAVE**

As a kitchen staff member, I want to access staff-only features securely, so that only authorized employees can manage café orders and menu availability.

**Acceptance Criteria**
- Given a user has valid staff access, when they open the kitchen order board or menu management page, then the system allows access.
- Given a customer or unauthorized user attempts to open a staff-only page, when they request access, then the system denies access and displays: "You must be staff to access this page."
---

## 3. Priority Summary

| Priority | User Stories | Total |
|---|---|---:|
| MUST HAVE | Stories 1, 2, 3, 4, 7, 8 | 6 |
| SHOULD HAVE | Stories 5, 9, 10 | 3 |
| COULD HAVE | Story 6 | 1 |

**Prototype Focus:** The six MUST HAVE stories define the main prototype. They allow customers to browse the menu, create and submit orders, receive confirmation, and allow kitchen staff to view and update orders.

---

## 4. Copilot Review

**Prompt used for Copilot Chat:**

Here are my user stories for a Flask prototype. Check each one against INVEST and tell me which are too big, vague or not testable. Do not rewrite them; list problems only.

**INVEST Review Checklist**

- Independent: Can the story be developed separately?
- Negotiable: Does it allow flexibility in implementation?
- Valuable: Does it provide value to the customer or staff?
- Estimable: Can the development effort be estimated?
- Small: Can it be completed within a reasonable development period?
- Testable: Can the acceptance criteria be tested?

After receiving Copilot's review, record its actual findings in the AI Log. Decide which suggestions to accept and which to reject.

---

## 5. Reflection Questions

### Question 1: Which story did you split into smaller stories, and why?

I split the original customer ordering story into smaller stories covering browsing the menu, adding items to the cart, placing an order, and receiving confirmation. I separated them because the original story included too many actions in one feature. Breaking it down makes each task easier to develop, test, and complete. It also makes it easier to identify problems during development.

### Question 2: Which story was hardest to write acceptance criteria for? What made it hard?

The order cancellation story was the hardest to write acceptance criteria for because there are different situations that determine whether an order can be cancelled. A customer should be able to cancel an order before the kitchen starts preparing it, but they should not be able to cancel it once preparation has started. I had to consider these situations to make sure the acceptance criteria were clear and testable.