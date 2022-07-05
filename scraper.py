check_list=[]
    
with open("question_links.txt","r") as f:
  line=f.readline()
  while line:
      check=line.strip()
   		if check[0:30]=='https://leetcode.com/problems/':
     		  check_list.append(check)
     	line=f.readline()
    	
      print(check_list)
