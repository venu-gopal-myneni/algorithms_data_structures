
def no_comms(s1,s2):
    no_comms =True
    for i in s1:
        if i in s2:
            no_comms = False
            break
    return no_comms
def case3(s1,s2):
    ''' some pos matches and no coms'''
    s11=list(s1)
    s22=list(s2)
    out=[]
    pos_list=[]
    for pos,val in enumerate(s1):
    
        if s2[pos] == val:
            pos_list.append(pos)
            out.append(val)
    for index in sorted(pos_list, reverse=True):
        del s11[index]
        del s22[index]
    no_coms =no_comms("".join(s11),"".join(s22))
    if no_coms:
        return len(out)
    else:
        return len(out)+case4("".join(s11),"".join(s22))

def case4(s1,s2):
    s11=list(s1)
    s22=list(s2)
    for pos,val in enumerate(s1):
        if val not in s2:
            s11.remove(val)
        if s2[pos] not in s1:
            s22.remove(s2[pos])
    s11 = "".join(s11)
    s22 ="".join(s22)
    print(s11,s22)
    if len(s11) > len(s22):
        if s22 in s11:
            return len(s22)
        else:
            return 0
    elif len(s11) == len(s22):
        return "to be coded"
    else:
        if s11 in s22:
            return len(s11)
        else:
            return 0

# def commonChild(s1,s2):
#     if s1==s2:
#         return len(s1)
#     if no_comms(s1,s2):
#         return 0
#     return case3(s1,s2)

com_dict={}
def commonChild(s1,s2):
    global com_dict
    if s1==s2:
        com_dict[s1+s2]=len(s1)
        return len(s1)
    elif no_comms(s1,s2):
        com_dict[s1+s2]=0
        return 0
    else:
        if s1+s2 in com_dict:
            return com_dict[s1+s2]
        if s1[-1] == s2[-1]:
            A=commonChild(s1[0:-1],s2[0:-1])
            com_dict[s1[0:-1]+s2[0:-1]] = A
            return 1+A
        else:
            A=commonChild(s1,s2[0:-1])
            com_dict[s1+s2[0:-1]] = A
            B=commonChild(s1[0:-1],s2)
            com_dict[s1[0:-1]+s2] = B
            return max(A,B )

if __name__=="__main__":
    s1='OUDFRMYMAW'
    s2='AWHYFCCMQX' # 2
    print(commonChild(s1,s2))
    

    
    
