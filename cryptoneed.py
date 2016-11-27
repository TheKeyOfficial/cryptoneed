# Autor: TheKey
from Crypto.Cipher import AES
import base64, random, string, sys, os
import readline
readline.parse_and_bind("tab: complete")
BLOCK_SIZE = 32
PADDING = '{'

pad = lambda s: str(s) + (BLOCK_SIZE - len(str(s)) % BLOCK_SIZE) * PADDING
Enc = lambda c, m: base64.b64encode(c.encrypt(pad(m)))
Dec = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

def randomKey(bytes):
    return ''.join(random.choice(string.ascii_letters + string.digits + "{}!@#$[]|?/&") for i in range(bytes)) 
def randomName():
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(3)) 
def randomAcii():
    return ''.join(random.choice(string.ascii_letters) for i in range(3)) 


key = randomKey(32)
iv =  randomKey(16)

cipher = AES.new(key, AES.MODE_CBC, iv)
op = 1
while op == 1:

	print '\033[31m'
	print '#############################################################################'
	print '# _________                        __                                  .___ #'
	print '# \_   ___ \_______ ___.__._______/  |_  ____   ____   ____   ____   __| _/ #'
	print '# /    \  \/\_  __ <   |  |\____ \   __\/  _ \ /    \_/ __ \_/ __ \ / __ |  #'
	print '# \     \____|  | \/\___  ||  |_> >  | (  <_> )   |  \  ___/\  ___// /_/ |  #'
	print '#  \______  /|__|   / ____||   __/|__|  \____/|___|  /\___  >\___  >____ |  #'
	print '#         \/        \/     |__|                    \/     \/     \/     \/  #'
	print '#								            #'
        print '#############################################################################'
	print '#	 							            #'
	print '#\033[32m PytonCrypter - CRYPTONEED 					            \033[31m#'
	print '#\033[32m By : TheKey		 					            \033[31m#'
	print '#\033[32m Web: https://github.com/TheKeyOfficial	 		            \033[31m#'
	print '# 								            #'
	print '#############################################################################'
	print '\033[32m'
	
	
	input = open(raw_input('Input Path: ')).readlines()
	output = open((raw_input('Output Path + Name(must include .py ending): ')), mode='w')
	
	imports = list()
	lines = list()
	
	for s in input:
		if not s.startswith('#'):
			if 'import' in s:
				imports.append(s.strip())
			else:
				lines.append(s)
	
	enced = Enc(cipher, "".join(lines))
	b64Name = randomAcii() + randomName()
	aesName = randomAcii() + randomName()
	
	
	
	
	imports.append('from base64 import b64decode as ' + b64Name)
	imports.append('from Crypto.Cipher import AES as ' + aesName)
	random.shuffle(imports)
	output.write(';'.join(imports) + "\n")
	
	cmd = "exec(%s.new(\'%s\', %s.MODE_CBC, \'%s\').decrypt(%s(\'%s\')).rstrip('{'))\n" %(aesName, key, aesName, iv, b64Name, enced)
	
	output.write('exec(%s(\'%s\'))' %(b64Name, base64.b64encode(cmd)))
	output.close
	print "Sugcesfully generatet!"
	print ''
	op2 = raw_input('EXIT (yes or no): ')
	
	if op2 == 'yes':
		op = 2
		
print 'see you soon'	



     
     
     
     
     
    
