class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def swap(s, i,j ) :
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return "".join(s)

        possibilities =set()

        possibilities.add(s1)
        a=swap(s1, 0,2)
        possibilities.add(a)
        possibilities.add(swap(s1,1,3))
        possibilities.add(swap(a,1,3))

        return s2 in possibilities

        

