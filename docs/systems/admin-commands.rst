


Faction and Galactic Civil War
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the Faction of a Player or NPC
""""""""""""""""""""""""""""""""""""""""""
Use /setFaction to change the faction of a player or NPC. You must specify ``-target``. Use ``declared`` for Special Forces, ``covert`` for Active Duty, and ``onleave`` for on leave (note: NPCs cannot be on leave). Then specify either ``rebel`` or ``imperial``. You can remove a faction (back to neutral) by just specifying ``clear``.
.. code-block:: c

  /setFaction -target <declared | covert | onleave> <rebel | imperial>
  /setFaction -target <clear>

Set the Faction Rank of a Player
""""""""""""""""""""""""""""""""""""""""""
Use /setRank to change the rank of a player. You must specify ``-target``. The ranks are numerical from 1 as "Private" to 12 as "General."
.. code-block:: c

  /setRank -target <0 to 12>
  
