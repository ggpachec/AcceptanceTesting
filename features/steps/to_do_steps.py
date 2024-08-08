from behave import given, when, then
from to_do import main, to_do_list, add_task, list_tasks, mark_task_completed, clear_tasks, list_tasks_by_priority


@given('the user starts the to-do list application')
def step_impl(context):
    context.to_do_list = []
    # This simulates starting the application and clearing any existing tasks
    clear_tasks()


@when('the user chooses to add a new task "{task}" with priority "{priority}"')
def step_impl(context, task, priority):
    add_task(task, priority)
    context.to_do_list = list_tasks()

@then('the to-do list should contain "{task}" with priority "{priority}" and status "{status}"') def step_impl(context, task): 
    # Check if the task is in the to-do list 
    assert task in to_do_list, f'Task "{task}" not found in the to-do list' 


@when('the user chooses to list all tasks')
def step_impl(context):
    context.to_do_list = list_tasks()


@then('the output should contain:')
def step_impl(context):
    expected_tasks = [dict(row) for row in context.table]
    for expected_task in expected_tasks:
        found = False
        for task in context.to_do_list:
            if task["task"] == expected_task["Task"] and task["status"] == expected_task["Status"] and task["priority"] == expected_task["Priority"]:
                found = True
        assert found, f'Task "{expected_task["Task"]}" with status "{expected_task["Status"]}" and priority "{expected_task["Priority"]}" not found in the list.'


@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    mark_task_completed(task)
    context.to_do_list = list_tasks()


@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for t in context.to_do_list:
        if t["task"] == task:
            assert t["status"] == "Completed", f'Task "{task}" is not marked as completed.'


@when('the user chooses to clear all tasks')
def step_impl(context):
    clear_tasks()


@then('the to-do list should be empty')
def step_impl(context):
    assert len(list_tasks()) == 0, 'The to-do list is not empty.'


@when('the user chooses to list tasks with priority "{priority}"')
def step_impl(context, priority):
    context.to_do_list = list_tasks_by_priority(priority)
