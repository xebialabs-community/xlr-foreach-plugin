# xlr-foreach-plugin
Prototype for "for each" functionality in Release

## Instructions

The **Control > For each** task type execute the task that is right behind it in sequence according to the values of a list. For each value in the list, a new task will be created on the fly. The looping variable will be stored in a regular release variable.

**Properties**

* **Values** - The list of values to iterate over. This can refer to a release variable.
* **Variable name** - The name of the looping variable (without `${...}` syntax) that will contain the current value while iterating.



## Build and installation

### 1. Quick setup

Copy contents of `src/main/resources` into the `ext` folder of your Release installation and restart.

Alternatively when doing development, you can also make a softlink from `ext -> src/main/resources`. Changes in the Python script will be picked up without having to restart the server.

### 2. Build a jar

Do a `gradle clean build` and upload the resulting jar in `build/libs` through the Plugin Manager UI. Then restart the Release server.
