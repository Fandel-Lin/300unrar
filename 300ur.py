import subprocess

pw=["28388","29323"]

for r in range(299):
	p1 = subprocess.Popen(['ls'], stdout=subprocess.PIPE)
	output0 = p1.communicate()[0]
	
	pwn = '-p'+str(int(pw[0])+int(pw[1]))
	fn = str(pw[0])+'+'+str(pw[1])+'.rar'
	p1 = subprocess.Popen(['unrar','x','-y',pwn,fn], stdout=subprocess.PIPE)
	p1.communicate()[0]
	
	p1 = subprocess.Popen(['ls'], stdout=subprocess.PIPE)
	output1 = p1.communicate()[0]
	
	x0 = (str(output0)[2:-1]).split('\\n')
	x1 = (str(output1)[2:-1]).split('\\n')
	
	target=''
	for i in x1:
		if i not in x0:
			target=i
			break
	pw=(target[:-4]).split('+')

fn = pw[0]+'.rar'
p1 = subprocess.Popen(['unrar','x','-y','-p'+pw[0],fn], stdout=subprocess.PIPE)
p1.communicate()[0]
