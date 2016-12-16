# commandgrep
custom ansible module to run a linux shell command and filter output based on an expression

Examples:

wasantha@wasantha-ThinkPad-P50 ~/ansible-test/custom/library $ ansible-playbook ../commandgrep_test.yml
 [WARNING]: provided hosts list is empty, only localhost is available


PLAY [localhost] ***************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Test commandgrep module works] *******************************************
ok: [localhost]

TASK [Print out put] ***********************************************************
ok: [localhost] => {
    "result": {
        "changed": false, 
        "meta": [
            "wasantha  2408  2165  0 07:28 ?        00:00:00 mate-session", 
            "wasantha  2475  2408  0 07:28 ?        00:00:00 /usr/bin/ssh-agent /usr/bin/dbus-launch --exit-with-session /usr/bin/im-launch mate-session", 
            "wasantha  2478     1  0 07:28 ?        00:00:00 /usr/bin/dbus-launch --exit-with-session /usr/bin/im-launch mate-session", 
            "wasantha  2510  2408  0 07:28 ?        00:00:00 /usr/bin/mate-settings-daemon", 
            "wasantha  2519  2408  0 07:28 ?        00:00:00 mate-panel", 
            "wasantha  2551     1  0 07:28 ?        00:00:02 /usr/lib/mate-panel/wnck-applet", 
            "wasantha  2554     1  0 07:28 ?        00:00:00 /usr/lib/mate-panel/notification-area-applet", 
            "wasantha  2555     1  0 07:28 ?        00:00:00 /usr/lib/mate-panel/clock-applet", 
            "wasantha  2556  2408  0 07:28 ?        00:00:00 mate-power-manager", 
            "wasantha  2558  2408  0 07:28 ?        00:00:00 /usr/lib/x86_64-linux-gnu/polkit-mate-authentication-agent-1", 
            "wasantha  2562  2408  0 07:28 ?        00:00:00 mate-volume-control-applet", 
            "wasantha  2565  2408  0 07:28 ?        00:00:00 mate-screensaver", 
            "wasantha  3477  2519  0 07:32 ?        00:00:09 mate-terminal"
        ]
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0   

```

wasantha@wasantha-ThinkPad-P50 ~/ansible-test/custom $ ansible-playbook commandgrep_test.yml 
 [WARNING]: provided hosts list is empty, only localhost is available


PLAY [localhost] ***************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Test commandgrep module works] *******************************************
ok: [localhost]

TASK [Print out put] ***********************************************************
ok: [localhost] => {
    "result": {
        "changed": false, 
        "meta": [
            "/dev/nvme0n1p2 475232360 265090672 185978208  59% /", 
            "/dev/nvme0n1p1    523248      3604    519644   1% /boot/efi"
        ]
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0   

wasantha@wasantha-ThinkPad-P50 ~/ansible-test/custom $ vim commandgrep_test.yml 
wasantha@wasantha-ThinkPad-P50 ~/ansible-test/custom $ ansible-playbook commandgrep_test.yml 
 [WARNING]: provided hosts list is empty, only localhost is available


PLAY [localhost] ***************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Test commandgrep module works] *******************************************
ok: [localhost]

TASK [Print out put] ***********************************************************
ok: [localhost] => {
    "result": {
        "changed": false, 
        "meta": [
            "wlp4s0    Link encap:Ethernet  HWaddr 44:85:00:41:25:3a  "
        ]
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0   



```
