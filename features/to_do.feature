Feature: To-Do List Management

    Scenario: Add a task to the to-do list
        Given the user starts the to-do list application
        When the user chooses to add a new task "Buy groceries" with priority "High"
        Then the to-do list should contain "Buy groceries" with priority "High" and status "Pending"

    Scenario: List all tasks in the to-do list
        Given the user starts the to-do list application
        When the user chooses to list all tasks
        Then the output should contain:
        | Task          | Status   | Priority |
        | Buy groceries | Pending  | High     |

    Scenario: Mark a task as completed
        Given the user starts the to-do list application
        And the to-do list contains tasks:
        | Task          | Status   | Priority |
        | Buy groceries | Pending  | High     |
        When the user marks task "Buy groceries" as completed
        Then the to-do list should show task "Buy groceries" as completed

    Scenario: Clear the entire to-do list
        Given the user starts the to-do list application
        And the to-do list contains tasks:
        | Task          | Status   | Priority |
        | Buy groceries | Pending  | High     |
        When the user chooses to clear all tasks
        Then the to-do list should be empty

    Scenario: List tasks by priority
        Given the user starts the to-do list application
        And the to-do list contains tasks:
        | Task          | Status   | Priority |
        | Buy groceries | Pending  | High     |
        | Pay bills     | Pending  | Low      |
        When the user chooses to list tasks with priority "High"
        Then the output should contain:
        | Task          | Status   | Priority |
        | Buy groceries | Pending  | High     |
