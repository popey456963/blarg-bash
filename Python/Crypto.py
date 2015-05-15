
""" 
Bricolager.py - Bricolage Brute-forcer 
Author: Zach Banks (therethinker) 
Licensed under Creative Commons Attribution 
""" 
USERNAME = "popey456963" 
PASSWORD = "plmnko456963" 

class Bricolager: 

    def __init__(self, username, password): 
        self.user = username 
        self.passw = password 
        
        #if using web.py: 
        #import web 
        #self.web = web 
        #if using webPy class: 
        self.web = webPy() 
        
    def __str__(self): 
        return self.getBoardString(self.board) 
        
    def printOut(self, board): 
        print self.getBoardString(board) 
    
    def copy(self, board): 
        #creates a copy of the board 
        out = [] 
        for row in board: 
            out.append(row[:]) 
        return out 
    
    def makeHex(self, n): 
        #makes hex from int 
        return hex(n)[2:].zfill(2) 
    
    def getBoardString(self, board): 
        output = "" 
        for x in board[::-1]: 
            for y in x: 
                output += y 
            output += "\n" 
        return output 
    
    def createBoard(self): 
        if len(self.boardstr) != (self.xlen * self.ylen): 
            print "[ERR] -- BAD BOARDSTR LENGTH. GOT %s EXPECTED %s" % (len(self.boardstr), (self.xlen * self.ylen)) 
            return 
        
        self.blank = "." 
        self.directions = [(1,0), (-1, 0), (0, 1), (0, -1)] 
        self.len = (self.xlen * self.ylen) - self.boardstr.count(self.blank) 
        
        #generate board 
        self.board = [] 
        for x in range(self.xlen): 
            self.board.append([]) 
            for y in range(self.ylen)[::1]: 
                index = y + x * self.ylen 
                self.board[x].append(self.boardstr[index]) 
    
    def getBoard(self): 
        import re 
        rawdata = self.web.get("http://www.hacker.org/brick/index.php?password=%s&name=%s" % (self.passw, self.user)) 
        data = re.search(r'param name="FlashVars" value="x=([0-9]*)&y=([0-9]*)&board=([.a-z]*)"', rawdata) 
        self.ylen = int(data.group(1)) 
        self.xlen = int(data.group(2)) 
        self.boardstr = data.group(3) 
        print self.xlen, self.ylen 
        self.createBoard() 
        print b 
        print " " 
        #self.bruteForce() 
        
    
    def submit(self, answer): 
        url = "http://www.hacker.org/brick/index.php?name=%s&password=%s&path=%s" % (self.user, self.passw, answer) 
        if self.web.get(url).count("your solution sucked") > 0: 
            print "[!!!] ERROR: %s" % answer 
        else: 
            print "SOLVED! \n " 
            #self.getBoard() 
    
    def remove(self, board, x, y): 
        #removes piece, decrements counter -DNC! 
        piece = board[x][y] 
        board[x][y] = self.blank 
        return piece 
    
    def removeColor(self, board, x, y, count): 
        #removes surrounding pieces -DNC! 
        piece = self.remove(board, x, y) 
        count = count + 1 
        if piece == self.blank: 
            return count 
        for dx, dy in self.directions: 
            if self.isPiece(board, x+dx, y+dy, piece): 
                count = self.removeColor(board, x+dx, y+dy, count) 
        return count 
    
    def isPiece(self, board, x, y, piece): 
        #does a piece actually exist there? 
        if 0 <= x < self.xlen and 0 <= y < self.ylen: 
            return board[x][y] == piece 
        else: 
            return False 
    
    def shift(self, board):    
        #moves pieces around according to blank spots 
        startBoard = self.copy(board) 
        def areBlank(x, y): 
            return x == y == self.blank    
        #x-shift 
        for x in range(self.xlen): 
            for y in range(1, self.ylen): 
                if not board[x][y] == self.blank: 
                    continue 
                for nx in range(x, self.xlen-1): 
                    #for row in board: 
                    board[nx][y] = board[nx+1][y]        
        #y-shift 
        hitNonBlankRow = False 
        for y in range(0, self.ylen): 
            for row in board: 
                if not row[y] == self.blank: 
                    hitNonBlankRow = True 
                    break 
            else: 
                if hitNonBlankRow: 
                    for ny in range(y, self.ylen-1): 
                        for row in board: 
                            row[ny] = row[ny+1] 
        if startBoard != board: 
            del startBoard 
            return self.shift(board) 
        else: 
            del startBoard 
            return board 
    
    def click(self, board, x, y, answer=None): 
        #call this, it removes the piece, appends to answer 
        count = self.removeColor(board, x, y, 0) 
        if count < 3: 
            return (False, answer) 
        self.shift(board) 
        if not answer == None: 
            answer = "%s%s%s" % (answer, self.makeHex(y), self.makeHex(x)) 
            return (count, answer) 
        else: 
            self.answer = "%s%s%s" % (self.answer, self.makeHex(y), self.makeHex(x)) 
            return (count, self.answer) 
                      
    def bruteForce(self): 
        #self.test() 
        print self.len 
        answer = self.iterate(self.board, "", 0) 
        if answer: 
            self.submit(answer) 
        else: 
            return "[!!!] NO SOLUTION!" 

    def iterate(self, board, answer, count): 
        tmpboard = self.copy(board) 
        for x in range(self.xlen): 
            for y in range(self.ylen): 
                if self.isPiece(tmpboard, x, y, "."): 
                    continue 
                else: 
                    tmpboard = self.copy(board) 
                    tmpcount, tmpanswer = self.click(tmpboard, x, y, answer) 
                    #print (tmpcount + count) 
                    if tmpcount < 3: #click returned an error: less than 3 blocks 
                        tmpboard = self.copy(board) 
                        continue 
                    if (tmpcount + count) >= self.len: 
                        return tmpanswer 
                    #print tmpcount + count, tmpanswer 
                    #self.printOut(tmpboard) 
                    finalAnswer = self.iterate(tmpboard, tmpanswer, (tmpcount + count)) 
                    if finalAnswer: 
                        return finalAnswer 
                    else: 
                        continue 

        return False 
    
    def test(self): 
        #used for debugging purposes 
        pass 

""" 
web.py - Web Facilities 
Author: Sean B. Palmer, inamidst.com 
About: http://inamidst.com/phenny/ 
--- 
Repackaged into webPy class by Zach Banks 
""" 
import urllib 
class webPy: 
    class Grab(urllib.URLopener): 
       def __init__(self, *args): 
          #feel free to edit "therethinker" 
          self.version = 'webPy/bricolager/therethinker/0.2)' 
          urllib.URLopener.__init__(self, *args) 
       def http_error_default(self, url, fp, errcode, errmsg, headers): 
          return urllib.addinfourl(fp, [headers, errcode], "http:" + url) 
    urllib._urlopener = Grab() 

    def get(self, uri): 
       u = urllib.urlopen(uri) 
       bytes = u.read() 
       u.close() 
       return bytes 

    def head(self, uri): 
       u = urllib.urlopen(uri) 
       info = u.info() 
       u.close() 
       return info 

    def post(self, uri, query): 
       data = urllib.urlencode(query) 
       u = urllib.urlopen(uri, data) 
       bytes = u.read() 
       u.close() 
       return bytes    

if __name__ == "__main__": 
    b = Bricolager(USERNAME, PASSWORD) 
    while True: 
        b.getBoard() 
        b.bruteForce() 
