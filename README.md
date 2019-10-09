###### enigma
This an Enigma Machine emulator created using Python
Please Note this is not a gui emulator rather a commandline tool

A simple example:
'''
from enigma import Enigma

Message = 'is this working'

My_machine = Enigma()
Encrypted_message= My_machine.encrypt_str(Message)

print(Encrypted_message)

Your_machine = Enigma()
Decrypted_message = Your_machine.decrypt_str(Encrypted_message)

print(Decrypted_message)
'''
### Functions

#.plug(plugs)
This method takes input as a string.
The string should be in pairs seperated by a space and none of the letters should be repeated(cannot put 2 plugs in the same spot)
eg:
*'AB CD EF GH IJ KL MN OP QR ST UV WX YZ'*
These represent the plug settings on the enigma machine

#.set_rotors(sets, reflector, model='enigma1')
In this method the rotors and reflector is selected.
Currently only 'enigma1' model of the enigma machne is supported.

The method takes in sets which is a string of the selected from rotors available in the selected model.
eg:
*'I V III'*
This means the rotors I, V and III are selected in that order from left to right.

The method also takes in another argument ie. reflector. This is also a string containin a single letter which represents the reflector to be used.
eg:
*'B'*

The third argument is the model to be used: currently only enigma1 is supported
Enigma1 has 5 total rotors out of which 3 can be selected: **I II III IV V**
And it has 3 reflectors out of which 1 can be selected: **A B C**

#.set_windows(win)
This takes in an argument win which can either be a string containing 3 letters seperated by a single space or it can be a list of any 3 numbers from 1 to 26
This is equivalent of setting the rotors
eg:
*'Z E F'*
*[3, 18, 20]*

#.show_windows(arg=False)
This method returns the rotor positions in the windows of the machine.
If arg is True, the returned value is in form of a string containing 3 letters,
If arg is False, the returned value is a list containing 3 numbers.

#.encrypt(key)
This method takes in a key which is a string of **a single letter**, and returns the encrypted version of it.

#.encrypt_str(message)
This method takes in message which is a string eg.*'THIS IS A SECRET'* and returns the encrypted version of it as a string.

#.decrypt(key)
This method takes in the argument key which is a string of **a single letter**, and returns the decrypted version of it.

#.decrypt_str(message)
This method takes in a string and returns the decrypted version of the whole string as a string

### **NOTE**
When you create an instance the init method selects the rotors 'I V II' , reflector 'C', and sets the windows to  'Y K D' and also the model to enigma1. It does not plug anything hence the plugboard maps to itself
To initialize with your own settings replace the keywords below with your own settings:
Enigma(***rotor***,***reflector***,***plugs***,***window***,***model***)
eg:
'''
my_machine = Enigma(rotor='V II IV',reflector='B',plugs='AK GH MP TR',window='H J D')
'''
