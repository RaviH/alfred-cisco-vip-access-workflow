# cisco_vip_access_alfred_workflow
Connect to VPN via Cisco AnyConnect Secure Mobility Client and VIP Access

How to use:
---

#### Download and Install the workflow
1. Download the workflow file from https://github.com/RaviH/cisco_vip_access_alfred_workflow/blob/master/VPN.alfredworkflow
2. Open the workflow file in Alfred

#### Software 

#### Setup the network password config

You have two choices for storing your network password:

##### 1: Use Alfred to store it in a config file in your workflow data directory

1. Open Alfred and enter `vpn create password`
2. Enter your password. 
3. Your password should be stored (in base 64 encoded format) in the config.json directory of your workflow data file.

![](http://i.giphy.com/AQ8oqGT2sd6cE.gif)

##### 2: Store it in keychain access

1. Open Keychain Access.
2. Click on `login` 
3. Click on `+` on the bottom left
4. Keychain Item Name: http://vpn.yourcompany.com *(doesn't matter what you enter here as long as it is a web url)*
5. Account Name: spiderman *(Doesn't matter what you provide for accont name)*
6. Password: `your network password`
7. Click Add.
8. Reopen the keychain item.
9. Add this to your comments section: `org.javawithravi.alfred.workflow.cisco.anytimeconnect.vip`

#### Connect to VPN

Enter `VPN connect` and enter. If you have setup your password correctly, you should be connected.

![](http://i.giphy.com/P3osvJ3wI1wPK.gif)