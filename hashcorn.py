#!/usr/bin/python3
import crypt
import sys
import os

banner = """\u001b[31m
$$\   $$\                     $$\                                               
$$ |  $$ |                    $$ |                                              
$$ |  $$ | $$$$$$\   $$$$$$$\ $$$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$$\  
$$$$$$$$ | \____$$\ $$  _____|$$  __$$\ $$  _____|$$  __$$\ $$  __$$\ $$  __$$\ 
$$  __$$ | $$$$$$$ |\$$$$$$\  $$ |  $$ |$$ /      $$ /  $$ |$$ |  \__|$$ |  $$ |
$$ |  $$ |$$  __$$ | \____$$\ $$ |  $$ |$$ |      $$ |  $$ |$$ |      $$ |  $$ |
$$ |  $$ |\$$$$$$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$  |$$ |      $$ |  $$ |
\__|  \__| \_______|\_______/ \__|  \__| \_______| \______/ \__|      \__|  \__|                                                                                                                                                                                                                                                                                   
`\\
  \\,
   \\\,^,.,,.
   ,;7~((\))`;;,,
   ,(@') ;)`))\;;',
    )  . ),((  ))\;,
   /;`,,/7),)) )) )\,,      ,,,... ,
  (& )`   (,((,((;( ))\,_,,;'`    `\\,
   `"    ` ), ))),/( (            `)\,
          '1/';/;  `               ))),
           (, (     /         )    ((/,
          / \                /     ((('
         ( 6--\%  ,>     ,,,(     /'))\'
          \,\,/ ,/`----~`\   \    >,))))'
            \/ /          `--7>' /((((('
            (,9             // /'('((\\\,
             \ \,,         (/,/   '\`\\\'\\
              `\_)1        (_)Kk    `\`\\`\\
                `\|         \Z          `\\
                  `          "            `\\\u001b[37m"""

def CheckUsage():
    if len(sys.argv)  <= 1:
        print("\u001b[33mUsage mode: python3 hashcorn wordlist.txt\u001b[37m")
        sys.exit()

def GetInputs():
    full_hash = input("Insert the hash: ")
    hash_salt = input("Insert the hash salt: ")
    return hash_salt, full_hash


def CrackHashes(hash_salt, full_hash):
    wordlist = open(sys.argv[1], "r")
    
    for password in wordlist:
        password = password.rstrip("\n")
        result_hash = crypt.crypt(password, salt=hash_salt)
        if result_hash == full_hash:
            print("Hash cracked\n")
            print("Content ->",password)
            wordlist.close()
            sys.exit()
            


if __name__ == "__main__":
    CheckUsage()
    
    print(banner)    
    hash_salt, full_hash = GetInputs()

    CrackHashes(hash_salt, full_hash)


