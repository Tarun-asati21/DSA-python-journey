class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # better solution 
        lst1= version1.split(".")
        lst2= version2.split(".")

        if len(lst1)<len(lst2) :
            for i in range (0, len(lst2)-len(lst1)):
                lst1.append("0")
        if len(lst1)>len(lst2) :
            for i in range (0, len(lst1)-len(lst2)):
                lst2.append("0")
        for i in range(0, len(lst1)):
            if int(lst1[i]) > int(lst2[i]) :
                return 1
            elif int(lst1[i]) < int(lst2[i]) :
                return -1
        return 0

        # # my brtue force solution -> fail in almost half test cases since question clarity not there
        # def point(str):
        #     count=0
        #     for ch in str :
        #         if ch=="." :
        #             count+=1
        #     return count
        
        # def last_rev(str) :
        #     last_rev = ""
        #     for i in range (len(str)-1, -1,-1):
        #         if str[i]==".":
        #             break
        #         last_rev = str[i] + last_rev
        #     return int(last_rev)

        # if point(version1)!=point(version2) :
        #     return 0
        # elif last_rev(version1) > last_rev(version2):
        #     return 1
        # elif last_rev(version1)<last_rev(version2) :
        #     return -1
        # else :
        #     return 0