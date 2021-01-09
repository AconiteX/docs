Initial Setup of the Server
======================================

This guide is intended to get you from obtaining the software through to logging into the game which is running on your own server.

Environment Overview
--------------------------------------
The SWG Source Server is available in two formats. A pre-configured environment image (the "Quick Start Server") which is covered in this guide. Alternatively, you can create a custom environment, which is covered separately in the Custom Environment Information Guide.

The Quick Start Server (also referred to as the "VM" for "Virtual Machine") is a pre-setup and self-contained Linux-based server image created by SWG Source. The Virtual Machine operates like a computer inside your computer and is used to run the server so you can connect and play SWG. Using the Virtual Machine allows you to very quickly setup and run a server with just a few simple steps and avoids many of the complicated environmental configuration complexities.

Before continuing, make sure the computer you will host the 

Oracle VirtualBox
--------------------------------------
To run the Virtual Machine, you'll need to download and install Oracle VirtualBox. To download, visit the `Oracle VirtualBox Website <https://www.virtualbox.org/wiki/Downloads>`_ and select the "Windows Hosts" link to download the installer. Proceed through and complete the installation.

Download the Virtual Machine Image
--------------------------------------
Next you'll need to download the actual Virtual Machine Image file which contains the pre-configured server environment (a ``.ova`` file). `Click here to acquire the latest version of the Virtual Machine <https://drive.google.com/file/d/18e07y-Hry2boaOTy8vROezISGekDluji/view?usp=sharing>`_ *(Version 3.0 "Irish" last updated November 1, 2020)*.

.. IMPORTANT::
   You should join the `SWG Source Discord <https://discord.gg/Va8e6n8>`_ if you haven't already. You can use the command **!vm** in any channel to make sure you have the latest version of the Virtual Machine Image as this guide may be outdated.
   
Local Information Gathering
--------------------------------------
Before we can setup the Virtual Machine, we must learn more about your computer and network. This section will help you determine the following (but if you already know them you can skip this section):

* A local static IP address you can assign the VM that won't collide with your DHCP range or subnet mask
* The technical specifications of your computer, including its RAM, Hard Disk Space, and Cores.

**Network Information:** We will need to determine a local static IP address we can assign to the VM. First, we need to determine what your router's DHCP (Dynamic Host Configuration Protocol) range is. This range is used to assign a local IP address to each device that connects to your network. We need to avoid this range so the VM does not collide with another device on your network.

To determine your DHCP range, we first need to determine the local address (called the "Default Gateway") of your router. You can do this by opening Command Prompt with: ``Start (Windows Key) > Command Prompt`` or ``Windows Key + R > cmd``. In the prompt window that pops up, type ``ipconfig`` and press enter. A lot of information will show up in the console. Look for the line that says ``Default Gateway``. You can also directly search the internet to find the default gateway address of your router if you know the brand and model.

Once you know the default gateway, you can login to the router by pasting the default gateway into your web browser just like a website. You may be asked to login, in which case you'll need to search the web for the default username and password for your router. You may also find this information on 

**Port Forwarding (Optional):** If other people will be playing on your server and they won't be on your home network, you'll need to also enable port forwarding for ports ``44452 to 44463`` in ``both UDP and TCP``. Port forwarding is outside the scope of this guide, but you can easily search the web for instructions on how to do this for your specific router.

Importing the Virtual Machine
--------------------------------------
Once you've gathered the necessary information, we're ready to import the Virtual Machine ``.ova`` file. First, open Oracle VirtualBox.

1. Go to ``File > Import Appliance``
2. In the Import Wizard, the Appliance to Import prompt will appear first. Click the folder icon and select the path to the ``.ova`` file you downloaded. Then click ``Next``.
3. On the Appliance Settings prompt, you may wish to change the ``CPU`` and ``RAM`` sections with the information we learned from our information gathering. Be sure you configure the Virtual Machine to meet the :doc: `Minimum System Requirements <getting-started/minimum-system-requirements>`_.




