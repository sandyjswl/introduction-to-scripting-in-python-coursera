"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if len(line1)>len(line2):
        shorter_line = line2
        longer_line = line1
    else:
        shorter_line = line1
        longer_line = line2

    for index in range(len(shorter_line)):
        if shorter_line[index]!=longer_line[index]:
            return  index 
    if len(line1)==len(line2):
        return IDENTICAL    

    return len(shorter_line)


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if '\n' in line1 or '\n' in line2 or '\r' in line1 or '\r' in line2:
        return ""
    # if idx != singleline_diff(line1,line2):
    #   return ""
    if len(line1)>len(line2):
        shorter_line = line2
        longer_line = line1
    else:
        shorter_line = line1
        longer_line = line2
    if idx<0 or idx>len(shorter_line):
        return ""  
    res = ""  
    for index in range(len(longer_line)+1):
        if index < idx:
            res=res+"="
        if index ==idx:
            res=res+"^"  
        


    return line1+"\n"+res+"\n"+line2+"\n"


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if len(lines1)>len(lines2):
        shorter_line = lines2
        longer_line = lines1
    else:
        shorter_line = lines1
        longer_line = lines2
    for index in range(len(shorter_line)):
        if singleline_diff(shorter_line[index],longer_line[index])!=-1:
            return(index,singleline_diff(shorter_line[index],longer_line[index])) 
    if len(shorter_line)==len(longer_line):
        return (IDENTICAL, IDENTICAL)
    return (len(shorter_line),0)    
    


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines=[]
    with open(filename) as buff:
        for line in buff:
            line=line.strip()
            lines.append(line)

    return lines


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    first = get_file_lines(filename1)
    second = get_file_lines(filename2)

    diff = multiline_diff(first,second)

    if diff == (-1,-1):
        return "No differences\n"
    line = diff[0]
    ind = diff[1]

    # if len(first)>len(second):
    #     shorter_line = second
    #     longer_line = first
    # else:
    #     shorter_line = first
    #     longer_line = second
    
    res = singleline_diff_format(first[line],second[line],ind)     

    return "Line "+str(line)+":\n"+res