sublime-nekoml
------

Note: This is the first time I tried to write syntax definition, so it probably has some Bug

### features

* Syntax highlighting for `*.nml` file

* Auto Completion(only core lib), _afasdfsa_

  - Entirely by hand typing, Is very hard work, so there will be some typos

  - May need setting: `"auto_complete_triggers": [ {"characters": ".", "selector": "source.nml"} ]`

* Goto Definition: `F12`,Jump Back: `Alt + -`

  - Need add `/neko-master/src/core` Folder to current project. 

     > `Menu -> Project -> Add Folder to Project...`

### requirement

* Sublime text 3 build 3103(2016-02-09) or newer. since a [new Syntax Definition file format](https://www.sublimetext.com/docs/3/syntax.html)

### misc

* [hello nekml](https://github.com/R32/haxe-proj-template/tree/master/nml)

* [CMake compile c/c++ as NDLL](https://github.com/R32/haxe-proj-template/tree/master/gcc) - `/ndll/CMakeLists.txt` - Only Test in MSVC 2013
