


Accessing Values set in Server Config Files (e.g. localOptions.cfg)
-----------------------------------------------------------------------------------

.. code-block:: java
   :caption: String Values
   public static String getConfigSetting(String section, String key);

.. code-block:: java
   :caption: Boolean Values
   public static boolean utils.checkConfigFlag(String section, String key);

.. code-block:: java
   :caption: Float Values
   public static float utils.getFloatConfigSetting(String section, String key);
   public static float utils.getFloatConfigSetting(String section, String key, float defaultValueIfNotFound);

.. code-block:: java
   :caption: Integer Values
   public static int utils.getIntConfigSetting(String section, String key);
   public static int utils.getIntConfigSetting(String section, String key, int defaultValueIfNotFound);

