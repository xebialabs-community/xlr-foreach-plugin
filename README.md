# xlr-foreach-plugin
Prototype for "for each" functionality in Release. This code is for evaluation and educational purposes only.

## Instructions

The **Control > For each** task type execute the task that is right behind it in sequence according to the values of a list. For each value in the list, a new task will be created on the fly. The looping variable will be stored in a regular release variable.

**Properties**

* **Values** - The list of values to iterate over. This can refer to a release variable.
* **Variable name** - The name of the looping variable (without `${...}` syntax) that will contain the current value while iterating. Make sure to disable 'Required' and 'Show on Create Release form' for this variable.

## As-code example

Here's a Yaml example of a template using the For each task. Use the [`xl` command line utility](https://docs.xebialabs.com/v.10.3/release)  to upload it to release.

```
apiVersion: xl-release/v1
kind: Templates
metadata:
  home: For each
spec:
- template: For each example

  variables:
  - type: xlrelease.StringVariable
    key: friend
    requiresValue: false
    showOnReleaseStart: false
    label: Friend Looping Variable

  scriptUsername: admin
  scriptUserPassword: admin

  phases:
  - phase: Simple example
    tasks:
    - name: For each friend
      type: control.ForEach
      values:
      - Alice
      - Bob
      - Carol
      variable: friend
    - name: "Hello, ${friend}!"
      type: xlrelease.ScriptTask
    - name: All done
      type: xlrelease.GateTask
```



## Build and installation

### 1. Quick setup

Copy contents of `src/main/resources` into the `ext` folder of your Release installation and restart.

Alternatively when doing development, you can also make a softlink from `ext -> src/main/resources`. Changes in the Python script will be picked up without having to restart the server.

### 2. Build a jar

Do a `gradle clean build` and upload the resulting jar in `build/libs` through the Plugin Manager UI. Then restart the Release server.
