# enigma
This an Enigma Machine emulator created using Python\n
Please Note this is not a gui emulator rather a commandline tool

A simple example:

from enigma import Enigma

Message = 'is this working'

My_machine = Enigma()

Encrypted_message= My_machine.encrypt_str(Message)

print(Encrypted_message)

Your_machine = Enigma()

Decrypted_message = Your_machine.decrypt_str(Encrypted_message)

print(Decrypted_message)




