# commandgrep
custom ansible module to run a linux shell command and filter output based on an expression

Examples:

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
