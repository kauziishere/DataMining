import itertools
def Init_item():
	init_itm = []
	df = open("dataset.csv","r")
	string = df.read()
	tmp = string.split("\n")
	tmp = tmp[:-1]
	for each in tmp:
		init_itm.append(each.split(","))
	return init_itm
	
def Frequent_Set(sup_cnt):
	dictionary = {}
	df = open("dataset.csv","r")
	string = df.read()
	string1 = string.replace("\n",",");
	string2 = string1.split(",")
	string3 = string2[:-1]
	print string3
	SET =  set(string3)
	F_SET = set()
	print SET
	for each in SET:
		cnt = string3.count(each)
		print each +"	"+str(cnt)
	
		if(cnt >= sup_cnt):
			F_SET.add(each)
	return F_SET
		
def Combinations(f):
	comb = list()
	for each in itertools.combinations(list(f), 2):
		comb.append(each)
	return comb	

def Combination1(old_comb_list):
	f_list = list()
	comb = Combinations(old_comb_list)
	print comb
	tmp = list(comb)
	lst = list()
	for i in range(len(tmp)):
		lst.append(list(set().union(*list(tmp[i]))))
	for each in lst:
		if(len(each) == 3):
			f_list.append(each)	
	return f_list

def Freq_list(f_list,sup_cnt):
	new_freq = []
	for i in range(len(f_list)):
		cnt = 0
		for j in range(len(Init_item())):
			if(set(f_list[i]).issubset(set(Init_item()[j]))):
				cnt = cnt + 1
		if(cnt >= sup_cnt):
			print f_list[i],cnt
			new_freq.append(f_list[i])
	return new_freq

def Rule_Gen(FI,conf):
	LHS_cnt = 0
	item_cnt = 0
	for each in FI:
		for i in set(each):
			LHS = set(i)
			RHS = set(each) - LHS
			for item in Init_item():
				if(LHS.issubset(set(item))):
					LHS_cnt = LHS_cnt + 1
				if(set(each).issubset(set(item))):
					item_cnt = item_cnt + 1
			print (float(item_cnt) / LHS_cnt)
			if((float(item_cnt) / LHS_cnt) >= conf):
				print LHS,"-->", RHS,(float(item_cnt) / LHS_cnt)


sup_cnt = input("Enter the sup_cnt: ")
conf_pcnt = input("Enter the cnf_pcnt: ")
print Init_item()
FI1 = Frequent_Set(sup_cnt)
print FI1 
CL2 =  Combinations(FI1)
print CL2
CL2 = [list(item) for item in set(tuple(row) for row in CL2)]

FI2 = Freq_list(CL2,sup_cnt)
CL3 =  Combination1(FI2)
print CL3
	
CL3 = [list(item) for item in set(tuple(row) for row in CL3)]
CL3 = Freq_list(CL3,sup_cnt)
FI3 = Freq_list(CL3,conf_pcnt)
print "freq_set"
print FI3		
print  Rule_Gen(FI3,conf_pcnt)
