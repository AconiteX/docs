Trigger Functions
======================================

Script functions are used in the SWG Code Base as a trigger to send information from the `src` (engine) to the `dsrc` (scripts) when specific actions occur. All script functions are defined in `ScriptFunctionTable.cpp <https://github.com/SWG-Source/src/blob/master/engine/server/library/serverScript/src/shared/ScriptFunctionTable.cpp>`_. We won't cover every script function here (there's more than 300) as some were developed for a singular use-case, however, most commonly used functions are explained to get you started.

Note: This page covers script trigger functions only, which (excluding the return enumerator) are one-way ``[src > dsrc]``. It is not documentation for all of the JNI calls that the `dsrc` can execute to send commands back to the engine.
  
Important Considerations
--------------------------------------
.. NOTE::
  Consistent with working on a code base whose development began in 1999 and ended in 2011, there are a number of "modern day" priniples you will be counciled against and some logic of these systems may not make sense. While several amazing contributors have helped modernize many components of this code base, archaic ideology and usage remains at its core. Thus, **be sure to read this section beacuse there are a number of nuances that can leave you with broken code and hours of debugging for simple mistakes.**

* All script functions are implemented in the dsrc as `public int` and must `throws InterruptedException`.
* The `src` listens for the a return code (int) inside each script function which use constants defined [base_class.java](https://github.com/SWG-Source/dsrc/blob/master/sku.0/sys.server/compiled/game/script/base_class.java) that tell the engine how to proceed. **Do not exit a script function with any other return statement.**
    * `return SCRIPT_CONTINUE;` exits the method and continues (this is the method you will see and use 90% of the time).
    * `return SCRIPT_OVERRIDE;` exits the method and *blocks* the contemplated action (only applicable in certain scenarios). For example, if you return with SCRIPT_OVERRIDE in the `OnAboutToBeTransferred` script function, it will block the transfer of the item, whereas SCRIPT_CONTINUE would allow it to move forward. Either one will exit the method.
    * `return SCRIPT_DEFAULT;` is deprecated and will generally only be found in conversation scripts.
* Different triggers pass different information, but the one constant will always be that the first parameter of any script function will be `obj_id self` so you have the network ID of the object the script is running on. *And importantly, if you add a new script function, note that you do NOT need to include this as one of the parameters passed, it is included automatically.*
* Script functions are *NOT* static and shouldn't be declared as static (they won't work). If you have a block of code in a script function that you may need to execute or reach more than once, you should put it in a separate method and send a `messageTo` that method whenever you need to access it. `messageTo` requires specific formatting and there are other considerations, see: **LINK** Methods for Object Communication, Time/Synchronization, and Loops (DSRC). 
* Remember that any script function will be run regardless of what script the function is in if that function is in a script attached to an object and that object receives the trigger. As noted in the overview of scripts, when a trigger is sent by the src, in almost all cases the script function is executed as a `trigAllScripts` on *every* script attached to that object. This makes sense, for instance, because if a player has the `OnLogin` script function enumerated in two scripts attached to the player that handle separate things, like veteran rewards and PvP, both would need to update when the player logs in. In some rare circumstances, this can be problematic based on the use-case, in which case you may need to add a new script function that uses the `trigOneScript` approach instead.
* A lot of script functions contain a parameter `dictionary params` (see class contructors) or other unused parameters which are routinely null (but may pass certain information as well, depending on the method or application). *Importantly, though, script functions will not get executed if they are missing parameters, even if they won't be used.* **Always use the exact template and parameters as prescribed in ScriptFunctionTable.cpp, even if they aren't used.**  

Script Engine Triggers
--------------------------------------
.. code-block:: java
  public int OnAttach(obj_id self) throws InterruptedException { }

OnAttach is triggered when the script is attached to an object (see [GameScriptEngine.cpp#229](https://github.com/SWG-Source/src/blob/e0aceec9cb59afb2d139b043c8f3244f7c828179/engine/server/library/serverScript/src/shared/GameScriptObject.cpp#L229)). This includes the following scenarios:
* `GameScriptObject::attachScript` is executed in the src
* `attachScript(obj_id object, String script)` is executed in the dsrc
* `/script attach <oid> <script>` is executed in-game

**Tip:** A general practice across the source is to replicate the code in `OnAttach` also in `OnInitialize` due to the variability in how/if these functions may be triggered based on how the world object is generated (buildouts, scripts, spawners, etc.).
