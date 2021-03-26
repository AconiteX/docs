


Accessing Values set in Server Config Files (e.g. localOptions.cfg)
-----------------------------------------------------------------------------------

.. code-block:: java
   :caption: this.py
   
   public static int utils.getIntConfigSetting(String section, String key);
   public static int utils.getIntConfigSetting(String section, String key, int defaultValueIfNotFound);

