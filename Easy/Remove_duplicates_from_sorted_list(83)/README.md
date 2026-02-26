# [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

### **Problem Description**

Given the `head` of a **sorted** linked list, delete all duplicates such that each element appears only once. Return the linked list **sorted** as well.

---

### **Examples**

**Example 1:**

* **Input:** `head = [1, 1, 2]`
* **Output:** `[1, 2]`

**Example 2:**

* **Input:** `head = [1, 1, 2, 3, 3]`
* **Output:** `[1, 2, 3]`

---

### **Constraints**

* The number of nodes in the list is in the range `[0, 300]`.
* 
* The list is guaranteed to be **sorted** in ascending order.

---

### **Notes & Reminders**

> [!NOTE]
> Since the list is already **sorted**, any duplicate values will always be adjacent. This allows for a linear traversal without needing extra data structures (like a Set) to track seen values.

---