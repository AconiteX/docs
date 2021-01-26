Common Server Errors and How to Fix Them
============================================

"Error fetching data from remote" when logging in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The server is trying to use the JSON Web API to authenticate the account credentials provided against an external script but the server can't reach the script or the script isn't working correctly. Either disable this by commenting out or setting under ``[LoginServer]`` ``useJsonWebApi=false`` and ``useExternalAuth=false`` or you can correct the issue with the script.

