def getTaskPosition(task):
    index = 1
    for t in task.container.tasks:
        if task.id == t.id:
            return index
        index += 1

position = getTaskPosition(task)

def addTaskToChangeVariable(value):
    scriptTask = taskApi.newTask("xlrelease.ScriptTask")
    scriptTask.script = "releaseVariables['{}'] = '{}'".format(variable, value)
    scriptTask.title = "Set {} to {}".format(variable, value)
    scriptTask = phaseApi.addTask(task.container.id, scriptTask, position)
    taskApi.lockTask(scriptTask.id)

first = True
for value in values:
    addTaskToChangeVariable(value)

    if not first:
        task = getCurrentTask()
        copy = taskApi.copyTask(task.container.tasks[position - 1].id, task.container.id, position + 1)
        copy.title = task.container.tasks[position - 1].title
        taskApi.updateTask(copy)
    else:
        first = False
    position += 2
