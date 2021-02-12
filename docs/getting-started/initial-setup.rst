Initial Setup of the Server
======================================

This guide is intended to get you from obtaining the software through to logging into the game which is running on your own server.

Environment Overview
--------------------------------------
The SWG Source Server is distributed as a pre-configured environment image (the "Quick Start Server") which is covered in this guide. Alternatively, you can create a custom environment, which is unsupported, however, support and information is available in the Custom Environment Information Guide.

The Quick Start Server (also referred to as the "VM" for "Virtual Machine") is a pre-setup and self-contained Linux-based server image created by SWG Source. The Virtual Machine operates like a computer inside your computer and is used to run the server so you can connect and play SWG. Using the Virtual Machine allows you to very quickly set up and run a server with just a few simple steps and avoids many of the complicated environmental configuration complexities.

Oracle VirtualBox
--------------------------------------
To run the Virtual Machine, you'll need to download and install Oracle VirtualBox. To download, visit the `Oracle VirtualBox Website <https://www.virtualbox.org/wiki/Downloads>`_ and select the "Windows Hosts" link to download the installer. Proceed through and complete the installation.

Download the Virtual Machine Image
--------------------------------------
Next, you'll need to download the actual Virtual Machine Image file which contains the pre-configured server environment (a ``.ova`` file). `Click here to acquire the latest version of the Virtual Machine <https://drive.google.com/file/d/18e07y-Hry2boaOTy8vROezISGekDluji/view?usp=sharing>`_ *(Version 3.0 "Irish" last updated November 1, 2020)*.

.. IMPORTANT::
   You should join the `SWG Source Discord <https://discord.gg/Va8e6n8>`_ if you haven't already. You can use the command **!vm** in any channel to make sure you have the latest version of the Virtual Machine Image as this guide may be outdated.
   
Local Information Gathering
--------------------------------------
Before we can setup the Virtual Machine, we must learn more about your computer and network. This section will help you determine the following (but if you already know them you can skip this section):

* A local static IP address you can assign the VM that won't collide with your DHCP range or subnet mask
* The technical specifications of your computer, including its RAM, Hard Disk Space, and Cores.

**Network Information:** We will need to determine a local static IP address we can assign to the VM. First, we need to determine what your router's DHCP (Dynamic Host Configuration Protocol) range is. This range is used to assign a local IP address to each device that connects to your network. We need to avoid this range so the VM does not collide with another device on your network.

To determine your DHCP range, we first need to determine the local address (called the "Default Gateway") of your router. You can do this by opening Command Prompt with: ``Start (Windows Key) > Command Prompt`` or ``Windows Key + R > cmd``. In the prompt window that pops up, type ``ipconfig`` and press enter. A lot of information will show up in the console. Look for the line that says ``Default Gateway``. You can also directly search the internet to find the default gateway address of your router if you know the brand and model.

Once you know the default gateway, you can login to the router by pasting the default gateway into your web browser just like a website. You may be asked to login, in which case you'll need to search the web for the default username and password for your router. Once you've logged in, you'll need to look for your DHCP range and select a static IP address that is HIGHER than this range. For example, if your DHCP Range is ``192.168.1.1 to 192.168.1.200`` you may want to pick a number like ``192.168.1.204``. You should only change the digits after the very last period and should not exceed 250. Remember, different routers use different formats. Your range may be ``192.168.1.XXX`` or ``192.168.254.XXX`` or even another combination. Once you've picked a number that is higher than the range, write it down and remember it as we'll use it as the static IP address for the server.

**Computer Information:** Most of the information we need about your computer can be found in Task Manager. Press ``Ctrl + Shift + Esc`` and select the ``Performance`` tab. In the side pane, click on ``CPU`` and make note of the number of ``Cores`` you have, which is listed under the utilization graph. Next look at the side pane for the ``Memory`` section and you should see ``XX / XX GB (XX%)``. The larger number will represent the total amount of RAM you have. Finally, open Windows Explorer (``Windows Key + E``) and select ``This PC`` in the side menu. Under ``Devices and Drives`` you should see your main hard disk (likely "Local Disk (C:)). Make note of how much space you have available.

**Port Forwarding (Optional):** If other people will be playing on your server and they won't be on your home network, you'll need to also enable port forwarding for ports ``44452 to 44463`` in ``both UDP and TCP``. Port forwarding is outside the scope of this guide, but you can easily search the web for instructions on how to do this for your specific router.

Importing the Virtual Machine
--------------------------------------
Once you've gathered the necessary information, we're ready to import the Virtual Machine ``.ova`` file. First, open Oracle VirtualBox.

1. Go to ``File > Import Appliance``
2. In the Import Wizard, the Appliance to Import prompt will appear first. Click the folder icon and select the path to the ``.ova`` file you downloaded. Then click ``Next``.
3. On the Appliance Settings prompt, you may wish to change the ``CPU`` and ``RAM`` sections with the information we learned from our information gathering. Be sure you configure the Virtual Machine to meet the :doc: `Minimum System Requirements <getting-started/minimum-system-requirements>`_. Then click ``Import``.
4. When the wizard has finished, you should see ``SWG Source 3.0`` in the side bar. Right click and select ``Settings``.
5. This step is optional but for convenience we recommend setting ``General > Advanced > Shared Clipboard`` and ``Drag'n'Drop`` to ``Bidirectional``.
6. In settings, select ``Network > Adapter 1`` make sure ``Attached to`` is set to ``Bridged Adapter`` and ``Name`` is the name of your network card.
7. Once you've saved the changes, we're ready to go back to the main window of Oracle VirtualBox, select ``SWG Source 3.0`` and click ``Start``. Any future time you want to start the server, you'll just need to open Oracle VirtualBox and click start.

Connection Setup Inside the VM
--------------------------------------
Once the VM has started and you can see the desktop, you'll need to setup the networking (one-time setup required):

1. Click the ``Menu`` button. It's where the Start button would be if you were on Windows and type ``YaST`` then select the application.
2. You will be asked for a password. The password is ``swg``. By default, any time you are asked for a password anywhere inside the VM, the password is ``swg``.
3. Once inside YaST, select ``System > Network Settings``.
4. From the ``Overview`` tab, select the ``Device Name`` with ``eth0`` then click the ``Edit`` button.
5. In the window that pops up, click the ``Address`` tab. Then select the radial button next to ``Statically Assigned IP Address``. Below the button, in the field labeled ``IP Address`` type the static IP you selected earlier. In the nearby field labeled ``Subnet Mask`` enter ``255.255.255.0``. Then click the ``Next`` button.
6. On the ``Hostname/DNS`` tab, in the ``Name Server 1`` field, enter the ``Default Gateway`` of your router we used earlier to login to your router. In ``Name Server 2`` enter ``8.8.8.8``.
7. On the ``Routing`` tab, in the field labeled ``Default IPv4 Gateway`` enter the ``Default Gateway`` of your router. Then click ``OK``. A loading window will appear.
8. Back on your Desktop, click the ``Terminal`` application and type ``su root`` then enter ``swg`` as the password. Then type ``nano /etc/hosts``.
9. Use the arrow keys to navigate down the hosts file. You should already see an entry that contains your static IP address and the word ``swg``. If you do not, add it. It should look like this: ``XXX.XXX.XXX.XXX swg``. If it is already there, no change is required.
10. Now hit ``Ctrl + O`` and press ``Enter`` to save then press ``Ctrl + X`` to exit nano.
11. Now we will test network connectivity. Type ``ping localhost`` and press ``Enter``. You should get data back by a message that says ``XX bytes from localhost``. Press ``Ctrl + C`` to stop pinging. Repeat this process with ``ping <your static ip>`` (like ``ping 192.168.1.204``). Then try ``ping <default gateway>`` and finally try pinging ``ping 8.8.8.8``. If all of these return that ``XX bytes from (whatever)`` then you have successfully setup your network. Close the terminal window.

Installing the Server and Snapshotting
-------------------------------------------
1. Back on the desktop, find the file called ``Run this then ./install.sh`` and double click. When the window opens, type ``./install.sh``. This will begin the installation process. No further action is required. **The installation will take about 30 to 40 minutes.**
2. The process will complete when there is no longer anything moving in the terminal window and you see the prompt to enter another command that looks like this ``swg@swg:~>`` again.
3. Back in Oracle VirtualBox, let's take a snapshot, which is a frozen-in-time record of the VM state. Click ``SWG Source 3.0`` then click the ``Take`` button. Give it a name like ``Initial Setup Complete`` and click ``OK``. It will take a minute to complete. Now if you ever break your server, you can click the ``Restore`` button to revert back to this point.
4. You've successfully setup your server, now let's get it running!

Starting and Stopping the Server
-------------------------------------------
1. Inside the server, open ``Terminator`` (the red icon in the taskbar).
2. In the ``bottom left`` window, type ``ant start`` and then press ``Enter``. This will start your server. This is called an ``ant command``. There are several for your server that you may want to use. You can learn more about all of the available ant commands here. (LINK!!!)
3. In the ``bottom right`` window, type ``./stationchat`` and press ``Enter``. This will start the Chat Server.
4. Your server is ready when you see the message ``[exec] Cluster swg is ready for players`` in the bottom left. The bottom left window will be referred to as the ``Console``. Any warnings, errors, or crashes will dump here. If you encounter an issue, we may ask for your console output, which is whatever appears in this window.
5. When you are done playing and want to turn the server off, use the ``top right`` window and type ``cd swg-main`` and press ``Enter`` then ``ant stop`` and press ``Enter``.

Logging Into The Game
-------------------------------------------
1. Acquire the latest SWG Source Client by using the ``!client`` command in Discord for the latest download link. Once you've downloaded and extracted the client to a safe place on your computer, run the ``UpdateSwgClient.bat`` file to get the latest changes.
2. In your extracted client, find the ``login.cfg`` file and open it in ``Notepad``. Find the line that says ``loginServerAddress0=XXX.XXX.XXX.XXX`` and edit the part after the ``=`` by typing in your static IP address. Save the changes.
3. Now you're ready to start the client. Double click and run ``SwgClient_r.exe`` to start the game.
4. When you get to the login screen, enter any username you want. You do not need to enter a password. Anyone else connecting to your server can enter whatever username they like to have their own account. Once you have logged in, you're ready to create your characters and play.

Next Steps
-------------------------------------------
* Make sure you get the latest patches from SWG Source to keep in sync and have the latest features by following the Update Guide (LINK!!).
* Learn how to use admin commands to grant yourself items, quests, credits, or whatever else you like (LINK!!).
* Explore configuration options to enable/disable features or toggle things like double XP in the server configuration and client configuration guides (LINK!!).
* Check out the FACs (Frequently Asked Customizations) to learn how to make commonly requested changes, like combat levels, playing structures in city limits, etc. 
