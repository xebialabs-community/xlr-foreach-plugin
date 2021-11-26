#
# Copyright 2021 DIGITAL.AI
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


def getTaskPosition(task):
    """Gets the current position of the task in its container (phase or group task)"""
    index = 1
    for t in task.container.tasks:
        if task.id == t.id:
            return index
        index += 1

# Remember starting point of the task in the container
position = getTaskPosition(task)

def addTaskToChangeVariable(value):
    """Inserts a task with a little script to change the value of the looping variable"""
    scriptTask = taskApi.newTask("xlrelease.ScriptTask")
    scriptTask.script = "releaseVariables['{}'] = '{}'".format(variable, value)
    scriptTask.title = "Set {} to {}".format(variable, value)
    scriptTask = phaseApi.addTask(task.container.id, scriptTask, position)
    taskApi.lockTask(scriptTask.id)


first = True

# Create a task for each value in the list
for value in values:

    # Create a task to change the looping variable
    addTaskToChangeVariable(value)

    # Clone the first task for subsequent invocations
    if not first:
        task = getCurrentTask()
        copy = taskApi.copyTask(task.container.tasks[position - 1].id, task.container.id, position + 1)
        copy.title = task.container.tasks[position - 1].title
        taskApi.updateTask(copy)
    else:
        first = False

    position += 2
