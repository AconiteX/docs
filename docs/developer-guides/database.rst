Game Database
======================================



Applying Database Updates
--------------------------------------
Database updates can be used to either update the structure of some item in the schema (e.g. adding a column to a table) or to update a specific item (e.g. changing an object variable to fix a galaxy-wide bug with players who already have an item in-game). For the latter, you can obviously execute a query directly on the database, but keep in mind this infrastructure was designed for 26+ galaxies running concurrently and this documentation addresses the dissemination of database updates to the source-wide community for applying updates to their respective servers.

If an update needs to be made to an existing database (such as a database running in a live server format), the update should be added as a ``.sql`` file to ``src/game/server/database/updates``.

The database uses versioning located in the table ``VERSION_NUMBER``. The column ``VERSION_NUMBER`` will reflect the number of the most recent update that has been applied to the database. For example, if the highest version number in the updates directory is ``270.sql`` then the ``VERSION_NUMBER`` will also reflect ``270``.

To add a new update, add the needed SQL to a .sql file in the updates directory and name it as the version number that is sequentially higher than the existing version number and run ``ant update_database``. ``ant update_swg`` will also run the database update script. Both of these ant commands link to the database build script located at ``src/game/server/database/build/linux/database_update.sql`` and runs the ``--delta`` command.

The final line of the SQL update file must be:
``update version_number set version_number=###, min_version_number=###;`` where ### is the new version number.

You will also need to update ```ConfigServerDatabase.cpp`` <https://github.com/SWG-Source/src/blob/master/engine/server/library/serverDatabase/src/shared/ConfigServerDatabase.cpp>`_ in the src and change the default value of ``expectedDBVersion`` to match the new highest version number to ensure that if a user acquires an src change, it also forces the DB update. Otherwise, version mismatches can cause crashes and other errors.

.. IMPORTANT::
   If you make an update that alters the schema, be sure to also make changes (or additions) to the packages, schema, or any other applicable directory so any new databases built after your update will also inherit those changes automatically.
