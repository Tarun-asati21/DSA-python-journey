SELECT *
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$'
    AND mail LIKE BINARY "%@leetcode.com" ;
    # binary represents that jaisa lhika hai condition me, vaisa hi match karo exact, case sensitive!!